# Python script that **automates both Ceph RGW Multisite setup** and **Velero S3 backup integration**



## Run Minio in docker container



```sh
docker pull minio/minio

docker run --name minio \
-p 9000:9000 \
-p 41411:41411 \
-v data:/data \
-e "MINIO_SERVER_URL=http://0.0.0.0:9000" \
-e "MINIO_BROWSER_REDIRECT_URL=http://172.27.103.53:9000" \
minio/minio server /data --console-address ":41411"

```



## Verlero setup



```sh
wget https://github.com/vmware-tanzu/velero/releases/download/v1.16.1/velero-v1.16.1-linux-amd64.tar.gz
tar xzvf velero-v1.16.1-linux-amd64.tar.gz

sudo mv velero-v1.16.1-linux-amd64/velero /usr/local/bin
which velero
rm -rf velero-v1.16.1-linux-amd64*

cat <<EOF>> ceph.cred
[default]
aws_access_key_id=<access_key>
aws_secret_access_key=<secret_key>
EOF

velero install \
--provider aws \
--plugins velero/velero-plugin-for-aws:v1.9.2 \
--bucket backup \
--secret-file ./ceph.cred \
--backup-location-config region=minio,s3ForcePathStyle=true,s3Url=http://172.27.103.53:80

velero backup-location get

```



## Features

+ Multisite RGW zone creation (`zone-a`, `zone-b`)

+ Velero `credentials-velero` file generation

+ Velero install command output (ready to paste or run)



##  Config file



```yaml
realm: orca-realm
zonegroup: zonegroup-a

zones:
  zone-a:
    master: true
    endpoint: http://rgw-a.example.com:80
    access_key: RGW_ZONE_A_KEY
    secret_key: RGW_ZONE_A_SECRET

  zone-b:
    master: false
    endpoint: http://rgw-b.example.com:80
    access_key: RGW_ZONE_B_KEY
    secret_key: RGW_ZONE_B_SECRET

user:
  uid: velero
  display_name: Velero User

velero:
  bucket: velero-backups
  region: us-east-1
  output_secret_file: ./credentials-velero
  plugin_image: velero/velero-plugin-for-aws:v1.8.0
  namespace: velero

```





## Script



```python
import subprocess
import yaml
import sys
import os

def run(cmd):
    print(f">>> {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        sys.exit(1)

def generate_velero_creds(config, zone_name):
    creds_path = config['velero'].get('output_secret_file', './credentials-velero')
    zone = config['zones'][zone_name]
    with open(creds_path, 'w') as f:
        f.write("[default]\n")
        f.write(f"aws_access_key_id={zone['access_key']}\n")
        f.write(f"aws_secret_access_key={zone['secret_key']}\n")
    os.chmod(creds_path, 0o600)
    print(f"🧾 Velero credentials written to {creds_path}")
    return creds_path

def output_velero_install(config, zone_name, creds_path):
    endpoint = config['zones'][zone_name]['endpoint']
    bucket = config['velero']['bucket']
    region = config['velero']['region']
    plugin = config['velero']['plugin_image']
    ns = config['velero']['namespace']

    print("\n🚀 Velero install command:")
    print("------------------------------------------------")
    print(f"""velero install \\
  --provider aws \\
  --plugins {plugin} \\
  --bucket {bucket} \\
  --backup-location-config region={region},s3ForcePathStyle=true,s3Url={endpoint} \\
  --snapshot-location-config region={region} \\
  --secret-file {creds_path} \\
  --namespace {ns}
""")
    print("------------------------------------------------\n")

def setup_zone(config, zone_name):
    realm = config['realm']
    zonegroup = config['zonegroup']
    zones = config['zones']
    zone = zones[zone_name]
    user = config.get('user', {})

    is_master = zone.get('master', False)
    endpoint = zone['endpoint']
    access_key = zone['access_key']
    secret_key = zone['secret_key']

    if is_master:
        print("🟢 Setting up Master Zone...")
        run(f"radosgw-admin realm create --rgw-realm={realm} --default")
        run(f"radosgw-admin zonegroup create --rgw-zonegroup={zonegroup} "
            f"--master --default --endpoints={endpoint}")
        run(f"radosgw-admin zone create --rgw-zonegroup={zonegroup} "
            f"--rgw-zone={zone_name} --master --default --endpoints={endpoint} "
            f"--access-key={access_key} --secret={secret_key}")
        run("radosgw-admin period update --commit")
    else:
        print("🟡 Setting up Passive Zone...")
        master_zone = next((z for z in zones if zones[z].get("master")), None)
        if not master_zone:
            print("❌ Master zone not found.")
            sys.exit(1)
        master = zones[master_zone]
        master_endpoint = master['endpoint']
        master_access_key = master['access_key']
        master_secret_key = master['secret_key']

        run(f"radosgw-admin realm pull --url={master_endpoint} "
            f"--access-key={master_access_key} --secret={master_secret_key} "
            f"--rgw-realm={realm}")
        run(f"radosgw-admin period pull --url={master_endpoint} "
            f"--access-key={master_access_key} --secret={master_secret_key}")
        run(f"radosgw-admin zone create --rgw-zonegroup={zonegroup} "
            f"--rgw-zone={zone_name} --endpoints={endpoint} "
            f"--access-key={access_key} --secret={secret_key}")
        run(f"radosgw-admin zonegroup modify --rgw-zonegroup={zonegroup} "
            f"--add-zone={zone_name}")
        run("radosgw-admin period update --commit")

    if user:
        run(f"radosgw-admin user create --uid={user['uid']} "
            f"--display-name='{user['display_name']}' "
            f"--access-key={access_key} --secret={secret_key}")

    print(f"✅ Setup complete for zone: {zone_name}")

    creds_path = generate_velero_creds(config, zone_name)
    output_velero_install(config, zone_name, creds_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python setup_ceph_multisite.py config.yaml zone-a|zone-b")
        sys.exit(1)

    config_path = sys.argv[1]
    zone_to_setup = sys.argv[2]

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    setup_zone(config, zone_to_setup)

```



##  Run



```sh
python setup_ceph_multisite.py config.yaml zone-a

```



# support **automated failover detection** and **dynamic Velero S3 endpoint switching**.



## 🧰 Solution Overview

### Tools:

- Python with `requests`, `pyyaml`
- `kubectl` (to patch Velero)
- Optional: systemd or Cron for periodic runs



## Config 

```yml
failover:
  check_interval: 30           # seconds
  rgw_check_path: /            # path to check for health
  failover_threshold: 3        # number of failed checks before triggering
  active_zone: zone-a
  passive_zone: zone-b

```



## Script `failover_monitor.py`

```python
import requests
import yaml
import time
import subprocess

def is_rgw_healthy(endpoint, path="/", timeout=3):
    try:
        resp = requests.get(f"{endpoint}{path}", timeout=timeout)
        return resp.status_code < 500
    except requests.RequestException:
        return False

def switch_velero_endpoint(config, zone_name):
    endpoint = config['zones'][zone_name]['endpoint']
    region = config['velero']['region']
    bucket = config['velero']['bucket']

    print(f"🔁 Switching Velero to {zone_name} ({endpoint})...")
    patch = {
        "spec": {
            "provider": "aws",
            "objectStorage": {
                "bucket": bucket
            },
            "config": {
                "region": region,
                "s3ForcePathStyle": "true",
                "s3Url": endpoint
            }
        }
    }

    subprocess.run([
        "kubectl", "patch", "backupstoragelocation", "default",
        "-n", config['velero'].get('namespace', 'velero'),
        "--type=merge",
        "-p", yaml.dump(patch)
    ], check=True)

    print(f"✅ Velero now points to {zone_name}.")

def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    failover = config['failover']
    check_interval = failover.get('check_interval', 30)
    threshold = failover.get('failover_threshold', 3)
    check_path = failover.get('rgw_check_path', '/')

    active = failover['active_zone']
    passive = failover['passive_zone']
    active_endpoint = config['zones'][active]['endpoint']

    failures = 0

    while True:
        print(f"🔍 Checking RGW health at {active_endpoint}{check_path}")
        if is_rgw_healthy(active_endpoint, check_path):
            print("✅ RGW is healthy.")
            failures = 0
        else:
            failures += 1
            print(f"⚠️ RGW failed {failures}/{threshold} checks")

        if failures >= threshold:
            print("🚨 Triggering failover to passive zone...")
            switch_velero_endpoint(config, passive)
            break  # Exit after failover or continue for auto-recovery
        time.sleep(check_interval)

if __name__ == "__main__":
    main()

```





## Run as a Systemd Service or Cronjob



### Systemd file `/etc/systemd/system/ceph-failover.service`



```sh
[Unit]
Description=Ceph RGW Failover Monitor

[Service]
ExecStart=/usr/bin/python3 /opt/ceph/failover_monitor.py
Restart=always

```



```sh
sudo systemctl enable --now ceph-failover.service
```



