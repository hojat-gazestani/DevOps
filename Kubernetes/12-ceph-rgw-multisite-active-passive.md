# Ceph RGW (RADOS Gateway) multisite

> **highly available, disaster-resilient**, and **geo-redundant object** storage system across multiple regions or datacenters.

## Ceph RGW Multisite

+ **Asynchronous replication** of S3/Swift buckets and objects across independent Ceph clusters (regions).
+ **Read/write access in active-active or active-passive** modes.
+ **Failover** to another site for disaster recovery.
+ **Versioned and consistent bucket synchronization** (via bucket sync policies).
+ **ZoneGroup + Zone architecture** to separate and manage regions and zones.


## Core Concepts

****



| Term               | Description                                                  |
| ------------------ | ------------------------------------------------------------ |
| Realm              | The top-level container across all regions ( unique multisite namespace) |
| ZoneGroup          | A grouping of zones typically represnting a geographic region |
| Zone               | A single Ceph TGW zone(usually  a Ceph cluster with RGW endpoints) |
| Master Zone        | One zone that manages metadata and controls updates across the realm |
| Backup Sync Policy | Controls how specific buckets sync across zones              |



### Typical Topology (Active-Passive DR Example)



```bash
              +-------------------------+
              |     Realm: orca-realm  |
              +-------------------------+
                  |            |
        +---------+            +---------+
        |                               |
 +-------------+                 +-------------+
 | ZoneGroup A |                 | ZoneGroup B |
 +-------------+                 +-------------+
      |                               |
 +---------+                     +---------+
 | Zone A1 | <-- Master          | Zone B1 | <-- Passive (DR)
 +---------+                     +---------+

```





## Synchronization Mechanism
+ Uses **metadata sync** and **data sync** via `radosgw-admin sync` processes.
+ Each RGW instance runs **sync moduls** to ensure updates are eventually consisntent
+ Support **incremental** object sync, versioning, and **resync on demand**.



## High Availability and Disaster Recovery 

| Feature                 | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| Geo-redundancy          | Store and access objects from geographically distant sites   |
| DR failover             | Switch S3 endpoints to a passive zone in case the master site fails |
| Consistency controls    | Backet sync policies ensure consistency of data and metadata |
| Multi-site health check | Use `radosgw-admin sync status` to monitor replication across sites |





## Configuration



1. Create the Realm and ZoneGroups (on Active Zone A)

```bash
# Create a realm
radosgw-admin realm create --rgw-realm=orca-realm --default

# Create zonegroup
radosgw-admin zonegroup create --rgw-zonegroup=zonegroup-a \
    --master --default \
    --endpoints=http://rgw-a.example.com:80

# Create zone
radosgw-admin zone create --rgw-zonegroup=zonegroup-a \
    --rgw-zone=zone-a --master --default \
    --endpoints=http://rgw-a.example.com:80 \
    --access-key=ACCESS_KEY --secret=SECRET_KEY

```



2. Pull Realm to Passive Zone (Zone B)

```sh
# Pull realm from Zone A
radosgw-admin realm pull --url=http://rgw-a.example.com:80 --rgw-realm=orca-realm --access-key=ACCESS_KEY --secret=SECRET_KEY

# Pull period
radosgw-admin period pull --url=http://rgw-a.example.com:80 --access-key=ACCESS_KEY --secret=SECRET_KEY

```



3. Create ZoneGroup and Zone on Passive Zone B

```sh
# Create zonegroup with same name
radosgw-admin zonegroup set --rgw-zonegroup=zonegroup-a \
    --endpoints=http://rgw-b.example.com:80

# Create new zone
radosgw-admin zone create --rgw-zonegroup=zonegroup-a \
    --rgw-zone=zone-b \
    --endpoints=http://rgw-b.example.com:80 \
    --access-key=ACCESS_KEY_B --secret=SECRET_KEY_B

# Update zonegroup to include the new zone
radosgw-admin zonegroup modify --rgw-zonegroup=zonegroup-a --add-zone=zone-b

# Commit changes
radosgw-admin period update --commit

```



4. Start Metadata and Data Sync

```sh
# Start `radosgw` on both sides (or restart):
systemctl restart ceph-radosgw@rgw.`hostname`

# monitor:
radosgw-admin sync status
```



5. Configure Buckets (Optional)

```sh
radosgw-admin bucket sync enable --bucket=mybucket
```



> If not configured, all buckets will sync by default (from master zone).



6. Failover Steps (If Zone A Fails)

On Zone B:

1. Promote to master:

```sh
radosgw-admin zone modify --rgw-zone=zone-b --master
radosgw-admin period update --commit

```

2. Redirect your S3/Swift clients to Zone B RGW endpoint (`rgw-b.example.com`).
3. After recovery, optionally revert back by pulling latest realm again from Zone B to Zone A.



7. Monitoring and Validation

```sh
radosgw-admin sync status
radosgw-admin bucket stats --bucket=mybucket

/var/log/ceph/ceph-client.radosgw.*.log

```





# **Ceph RGW Multisite Setup (Active-Passive)** script using **Python + PyYAML** 



1. Install Requirements

```sh
python -m venv .venv
source ...
pip install pyyaml
```



2.  `config.yaml` Example



```yml
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

```



3. Python Ceph multisite

```pyt
import subprocess
import yaml
import sys

def run(cmd):
    print(f">>> {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        sys.exit(1)

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
        # Master setup
        print("🟢 Setting up Master Zone...")
        run(f"radosgw-admin realm create --rgw-realm={realm} --default")
        run(f"radosgw-admin zonegroup create --rgw-zonegroup={zonegroup} "
            f"--master --default --endpoints={endpoint}")
        run(f"radosgw-admin zone create --rgw-zonegroup={zonegroup} "
            f"--rgw-zone={zone_name} --master --default --endpoints={endpoint} "
            f"--access-key={access_key} --secret={secret_key}")
        run("radosgw-admin period update --commit")
    else:
        # Passive setup
        print("🟡 Setting up Passive Zone...")
        # Find master zone info
        master_zone = next((z for z in zones if zones[z].get("master")), None)
        if not master_zone:
            print("❌ Master zone not found in config.")
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



4. How to Run

```sh
# For active (zone-a)
python setup_ceph_multisite.py config.yaml zone-a

# For passive (zone-b)
python setup_ceph_multisite.py config.yaml zone-b

```

