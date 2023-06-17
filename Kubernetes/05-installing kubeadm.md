# [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

## Before you begin

+ 2 GB or more of RAM
+ 2 CPUs 
+ Full network connectivity between all machines
+ Unique hostname, MAC address, and product_uuid for every node
+ Certain ports are open `nc 127.0.0.1 6443`
+ Swap disabled.

## Installing kubeadm, kubelet and kubectl

+ install these packages on all of your machines:

+ `kubeadm`: bootstrap the cluster.

+ `kubelet`: runs on all of the machines in your cluster and does things like **starting pods** and containers.

+ `kubectl`: the command line util to talk to your cluster.

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```