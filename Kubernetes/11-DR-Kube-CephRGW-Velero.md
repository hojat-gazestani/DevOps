# Architecture: Velero + Ceph RGW Multisite

**two synchronized Ceph multisite RGW clusters** for Velero adds **geo-redundancy** and ensures **cross-site DR resilience** without relying on a single storage endpoint.

```pgsql
    +-------------------+           +-------------------+
    |  Active Cluster   |           |  Passive Cluster  |
    |  Region A (K8s)   |           |  Region B (K8s)   |
    +-------------------+           +-------------------+
              |                             |
       Velero (backup)              Velero (restore only)
              |                             |
         RGW-A  (Ceph Site A) <-->  RGW-B  (Ceph Site B)
               [Ceph RGW Multisite Replication]
```


## Setup Steps Overview
1. Ceph RGW Multisite Configuration
2. Shared S3 Credentials (Global User)
3. Velero Install in Both Clusters

Bounes
4. failover scrip
5. restore runbook
6. Prometheus/Grafana alert rules


## Implimentation

1. Ceph Ceph Multi-Site RGW Sync

Ceph's multisite configuration to replicate objects between two RGW zones:
+ ZoneGroup: e.g. `global`
+ Zone A: handles writes (Velero in active cluster)
+ Zone B: read-only mirror (used by passive cluster)

On both Ceph clusters, enable zone synchronization:

```sh
# On PRIMARY cluster
radosgw-admin zonegroup create --rgw-zonegroup=global ...
radosgw-admin zone create --rgw-zone=zone-a ...
radosgw-admin zone modify --rgw-zone=zone-a --master --default
radosgw-admin period update --commit

# On SECONDARY cluster
radosgw-admin zonegroup modify --rgw-zonegroup=default --add-zone=zone-b
radosgw-admin zone create --rgw-zone=zone-b --endpoints=http://<SECONDARY_RGW_HOST>:80
radosgw-admin period update --commit



# Set up multisite sync
radosgw-admin sync group create --group-id=velero-sync-group --status=enabled
radosgw-admin sync group modify --group-id=velero-sync-group --source-zone=zone-a --dest-zone=zone-b
radosgw-admin period update --commit

# Verify Sync Status
radosgw-admin sync status
#  Expected Output:
> data sync status:
>   zonegroup=default
>   zone=primary-zone
>   source: 5/5 shards
>   destination: 5/5 shards
```

> Make sure the replication policy for the `velero-backups` bucket is set to full (metadata and objects).

2. Shared S3 Credentials (Global User)

Create a user in RGW that exists in both zones:

```sh
radosgw-admin user create --uid=velero --display-name="Velero" \
  --access-key=VELERO_ACCESS_KEY \
  --secret-key=VELERO_SECRET_KEY
```

3. Velero Install in Both Clusters

Install Velero in **both clusters** using **identical credentials and bucket name**, but different RGW endpoints:

**Active Cluster (writes to Zone A):**

```sh
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.8.0 \
  --bucket velero-backups \
  --secret-file ./velero-credentials \
  --backup-location-config region=global,s3ForcePathStyle=true,s3Url=http://rgw-a.example.com \
  --use-volume-snapshots=false
```

**Passive Cluster (reads from Zone B):**

```sh
velero install \
  --provider aws \
  --plugins velero/velero-plugin-for-aws:v1.8.0 \
  --bucket velero-backups \
  --secret-file ./ceph-rgw-credentials \
  --backup-location-config region=global,s3ForcePathStyle=true,s3Url=http://rgw-b.example.com \
  --use-volume-snapshots=false
  --use-restic
```

> Do not schedule backups on the passive cluster.

###  Test Backup
```sh
velero backup create test-backup --include-namespaces=default
```

### Verify Sync to Secondary RGW
```sh
aws --endpoint-url=http://<SECONDARY_RGW_HOST>:80 s3 ls s3://velero-backups/backups/
```

### Velero Backup Health:

```sh
velero backup describe <BACKUP_NAME>
```



## Disaster Recovery Workflow
1. Ensure latest backup exists in Ceph (check replication status).
2. On passive cluster, run:

    ```sh
    velero backup get
    velero restore create --from-backup <latest-backup-name>
    ```
3. Reconfigure DNS / ingress / external IPs as needed.
4. (Optional) Resume backups in Region B, stop in Region A.

+ Update Velero to Use Secondary RGW
```sh
velero backup-location set default \
  --provider aws \
  --bucket velero-backups \
  --config region=default,s3ForcePathStyle="true",s3Url=http://<SECONDARY_RGW_HOST>:80
```

+ Restore from Secondary
```sh
velero restore create --from-backup test-backup
```