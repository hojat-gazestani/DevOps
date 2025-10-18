## Etcd for Ubuntu

### controller 
```shell
sudo apt install etcd -y

sudo vim /etc/default/etcd
ETCD_NAME="controller01"
ETCD_DATA_DIR="/var/lib/etcd"
ETCD_INITIAL_CLUSTER_STATE="new"
ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-01"
ETCD_INITIAL_CLUSTER="controller01=http://172.25.23.2:2380"
ETCD_INITIAL_ADVERTISE_PEER_URLS="http://172.25.23.2:2380"
ETCD_ADVERTISE_CLIENT_URLS="http://172.25.23.2:2379"
ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380"
ETCD_LISTEN_CLIENT_URLS="http://172.25.23.2:2379"
```
### Finalize installation
```shell
sudo systemctl enable etcd
sudo systemctl restart etcd
```