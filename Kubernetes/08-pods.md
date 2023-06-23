# Pod 

+ Pods are the smallest deployable units in Kubernetes

- pod of whales
![whales](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/02-kube-components/01-wahles.jpg)

+ pea pod
![pea](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/02-kube-components/02-Peas.jpg)


# Pods command

+ To list the running containers within a pod,
```bash
kubectl get pods my-pod -o jsonpath='{range .status.containerStatuses[*]}{.name}{"\t"}{.state.running.startedAt}{"\n"}{end}'
my-centos	2023-06-12T05:15:40Z
my-nginx	2023-06-12T05:14:57Z
```