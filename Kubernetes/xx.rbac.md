
```shell
mkdir /home/$USER/kube-certs && cd /home/$USER/kube-certs
openssl genrsa -out arman.key 2048
openssl req -new -key arman.key -out arman.csr -subj "/CN=arman/O=finance"
sudo cp /etc/kubernetes/pki/ca.{crt,key} .
openssl x509 -req -in arman.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out arman.crt -days 365
```

```shell
kubectl --kubeconfig arman.kubeconfig config set-cluster kubernetes --server https://192.168.56.71:6443 --certificate-authority=ca.crt
kubectl --kubeconfig arman.kubeconfig config set-credentials arman --client-certificate /home/$USER/kube-certs/arman.crt --client-key /home/$USER/kube-certs/arman.key
kubectl --kubeconfig arman.kubeconfig config set-context arman-kubernetes --cluster kubernetes --namespace finance --user arman
#kubectl --kubeconfig arman.kubeconfig config current-context arman-kubernetes --cluster kubernetes --namespace finance --user arman
cat arman-kubeconfig
```

```shell

kubectl --kubeconfig arman.kubeconfig get pods
cp ~/.kube/config arman.kubeconfig && vim arman-kubeconfig


user: arman
namespace: finance
name: arman-kubernetes
current-context: arman-kubernetes
user:
  - name: arman
    user:
      client-certificate-data: cat arman.crt | base64 -w0
      client-key-data: cat arman.key | base64 -w0
```

```shell
kubectl create role arman-finance --verb=get,list --resource=pods --namespace finance
kubectl -n finance get role arman-finance -o yaml
kubectl create rolebinding arman-finance-rolebinding --role=arman-finance --user=arman --namespace finance
kubectl -n finance get rolebinding arman-finance-rolebinding -o yaml
kubectl --kubeconfig arman.kubeconfig get pods
```

```shell
kubectl -n finance edit role arman-finance
rule:
- apiGroup:
  - "*"
  resource:
  - "*"
  verbs:
  - "*"
kubectl --kubeconfig arman.kubeconfig get pods
```

## hojat

```shell
openssl genrsa -out hojat.key 2048
openssl req -new -key hojat.key -out hojat.csr -subj "/CN=hojat/O=finance"
openssl x509 -req -in hojat.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out hojat.crt -days 365
```

```shell
kubectl --kubeconfig arman.kubeconfig config set-cluster kubernetes --server https://master:6443 --certificate-authority=ca.crt
kubectl --kubeconfig hojat.kubeconfig config set-credentials hojat --client-certificate /home/$USER/kube-certs/hojat.crt --client-key /home/$USER/kube-certs/hojat.key
kubectl --kubeconfig hojat.kubeconfig config set-context hojat-kubernetes --cluster kubernetes --namespace finance --user hojat
#kubectl --kubeconfig hojat.kubeconfig config current-context hojat-kubernetes --cluster kubernetes --namespace finance --user hojat
vim hojat-kubeconfig
current-context: hojat.kubernetes 
```

```shell
kubectl -n finance delete rolebinding arman-finance-rolebinding
kubectl create rolebinding finance-rolebinding --role=arman-finance --group=finance --namespace finance
```