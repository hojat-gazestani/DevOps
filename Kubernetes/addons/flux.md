

```bash
export GITLAB_TOKEN=<Your-Token>
```





My Gitlab container is running on docker container bind 2222 host port to 22 container:

```bash
flux bootstrap git \
  --url=http://git.zaraamad.ir/zaraavand/fluxcd.git \
  --branch=rahtal \
  --path=clusters/ \
  --username=git \
  --password=$GITLAB_TOKEN \
  --allow-insecure-http=true \
  --ssh-hostname=172.27.103.113:2222 

 
  ✔ public key: ecdsa-sha2-nistp384 AAAAE2VjZHNhLXNoYTItbmlz
```



Flux will provide a SSH public key add this key to Gitlab



1. **Go to your GitLab project**: `http://git.gitlab.ir/test/argocd`
2. **Navigate to Settings → Repository**
3. **Expand "Deploy keys"**
4. **Click "Add deploy key"**
5. **Paste the public key** and give it a title (e.g., "Flux CD")
6. **Check "Grant write permissions to this key"** (Flux needs write access to manage manifests)
7. **Click "Add key"**



### check everything 

```bash
flux check
flux get sources git

kubectl get pods -n flux-system
kubectl get gitrepositories -n flux-system

kubectl get kustomizations -n flux-system
flux get kustomizations

```





### Uninstall Flux completely



```bsah
flux uninstall --namespace=flux-system
```





```bash
kubectl delete gitrepository flux-system -n flux-system
kubectl get gitrepositories -n flux-system
flux get sources git --watch
```





# Helm Installation



```bash
kubectl create secret docker-registry gitlab-registry-secret-flux-system \
  --docker-server=registry.gitlab.ir:5005 \
  --docker-username="hojat-kube" \
  --docker-password="yourpassword" \
  --docker-email=hojat-kube@example.com \
  -n flux-system \
  --dry-run=client -o yaml > gitlab-registry-secret-flux-system.yaml
  
```





```bash
helm repo add fluxcd [https://charts.fluxcd.io](https://charts.fluxcd.io/) 
helm repo update

#Installing the HelmRelease CRD
kubectl apply -f https://raw.githubusercontent.com/fluxcd/helm-operator/master/deploy/crds.yaml 



kubectl create namespace flux 

#This would create the kubernetes secret for flux to communicate with GitHub
kubectl create secret generic flux-git-deploy --from-file=identity=./id_rsa -n flux --dry-run=client -o yaml | kubectl apply -f - 

# Flux install
helm install flux fluxcd/flux \
	--set git.url=git@github.com:pavan-kumar-99/medium-manifests.git \
	--set git.branch=fluxcd \
	--set git.secretName="flux-git-deploy" \
	--set git.user=flux-user \
	--set git.path=helm-releases \
	--namespace flux
	
#Install fluxcd deployment 
helm upgrade -i helm-operator fluxcd/helm-operator --set git.ssh.secretName=flux-git-deploy --namespace flux

#Install helm-operator deployment
helm upgrade -i helm-operator fluxcd/helm-operator --wait \
--namespace fluxcd \
--set git.ssh.secretName=flux-git-deploy \
--set helm.versions=v3
```



​	
