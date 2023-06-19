# [Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)

```bash
# Pull container images:
    sudo kubeadm config images pull

# initialize cluster
sudo kubeadm init  --apiserver-advertise-address=192.168.56.50 --pod-network-cidr 192.169.0.0/16

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl get nodes

# OR
export KUBECONFIG=/etc/kubernetes/admin.conf

kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.25.0/manifests/calico.yaml 
kubectl apply -f calico.yaml 
sudo systemctl status kubelet -l
```

```bash
kubeadm token create --print-join-command
kubeadm join 192.168.56.50:6443 --token hsgmo9.ogxzyianiogtxceq \
	--discovery-token-ca-cert-hash sha256:c53f1aaa3035bb4f122aa6792b607bcc4bf4764c3fd98d3e903d9ab318b110dd

kubectl get pods -n kube-system
```
