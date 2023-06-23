# [Pod](https://kubernetes.io/docs/concepts/workloads/pods/) 

+ Pods are the smallest deployable units in Kubernetes

- pod of whales
![whales](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/02-kube-components/01-wahles.jpg)

+ pea pod
![pea](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/02-kube-components/02-Peas.jpg)

- is a **group** of one or more **containers**, with **shared storage** and **network resources**, and  models an application-specific **logical host**

## Using Pods
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f https://github.com/hojat-gazestani/kubernetes/blob/main/Kubeadm/manifest/01-pod.yml
```

## Use Cases for Multi-Container Pods




## anti-patterns:

1. Deploying **pods without** specifying a **memory** or **CPU limit**.and Request more resources than the limit when setting the memory and CPU resources for a container
2. Pulling the **latest tag** in containers in production
3. running Pods **without controllers** like **Deployment** or **Job** are big mistakes.
4. **Lack of Health Checks**, not using Liveness and Readiness probes for pods


## Pods command

+ To list the running containers within a pod,
```bash
kubectl get pods my-pod -o jsonpath='{range .status.containerStatuses[*]}{.name}{"\t"}{.state.running.startedAt}{"\n"}{end}'
my-centos	2023-06-12T05:15:40Z
my-nginx	2023-06-12T05:14:57Z
```