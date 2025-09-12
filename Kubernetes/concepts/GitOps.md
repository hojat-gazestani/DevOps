**GitOps**

​	 set of procedures that uses the power of Git to provide both **revision and change control** 

With the deployment of **declarative kubernetes manifest** files being controlled by common Git operation.



**Core GitOps**

1. Infrastructure configuration	

   Computing resources (servers, storage, load balancer) that enable software applications to operate correctly

2. Software deployment: 

   Process of taking a particular version of a software application and making it ready to run on the computing infrastructure.



**code review**

​	Is a software development practice in which **code changes are proactively examined f**or error or omissions  by a second pair of eyes, leading to fewer prevetable outage.

​	When GitOps is used with kubernetes, the "code" being reviewed may be primarily Kuberentes YAML manifestss or other declarative configuration files.

+ Teching and sharing knowledge 
+ Consistency in design and implementation 
+ Team cohesion



**GitOps benefits**

+ Declarative
  + Describe *what* you want to achieve as opposed to *how* to get there.
  + Idempotency: Operation can be performed any number of time and produce the same result.
+ Imperative:
  + Descrive a sequence of instruction for manipulating the system to reach your desired state.



![Screenshot 1404-06-09 at 10.17.27 AM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-09 at 10.17.27 AM.png)



**Observability**

​	Ability to examine and describe a system's current running state and be alerted when unexpected conditions occur.

**GitOps**: storing a copy of your application configuration in source control and using it as a

source of truth for the desired state of your application. 

![](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-12 at 1.03.28 PM.png)



**Compliance**: organization’s information system meets a particular set of industry standards, typically focused on customer data security and adherence 



**Auditability**: is a system’s capability to be verified as being compliant with a set of standards. If a system can’t be shown to an internal or external auditor to be compliant, no statement about the system’s compliance can be made



**Disaster recovery:** toring declarative specifications of the environment under source control as a source of truth. Having a complete definition of what the environment should be facilitates the re-creation of the environment in the event of a disaster.



## Kubernetes





![Screenshot 1404-06-12 at 1.37.08 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-12 at 1.37.08 PM.png)

### Control plane

monitors the cluster state, makes changes, schedules work, and responds to events.

**kube-apiserver:** An entry point to the cluster providing a REST API to evaluate and update the desired cluster state

**kube-controller-manager:** Daemon continuously monitoring the shared state of the cluster through the API server to make changes attempting to move the *current state toward the desired state*

**kube-scheduler:** A component that is responsible for scheduling the workloads across the available nodes in the cluster

**etcd**: A highly available key-value database typically used as Kubernetes’ backing store for all cluster configuration data



## worker machine

**kubelet**: The primary “node agent” that manages the actual containers on the node.

**kube-proxy:** A network proxy that reflects Services as defined in the Kubernetes API on each node and can do simple TCP, UDP, and SCTP stream forwarding



### How declarative configuration works

*kubectl apply* merges the manifest from the specified file and the live resource manifest. (the command updates only fields specified in the file, keeping everything else untouched.)

Every time the kubectl apply command updates a resource, it saves the input manifest in the *kubectl.kubernetes.io/last-applied-configuration* 

This allows kubectl to execute a three-way diff/merge that automatically analyzes differences between two files while also considering the origin or the common ancestor of both files.

 This is so the next kubectl apply does not override the replicas value set by the Horizontal Pod Autoscaler. However, don’t forget that the replicas field might also be stored in the last-applied-configuration annotation. 

If that is the case, the missing replicas field in the manifest file will be treated as a field deletion, so whenever kubectl apply is run, the replicas value set imperatively by the Horizontal Pod Autoscaler will be removed from the live Deployment. The Deployment will scale down to the default of one replica.



### Controller architecture

**Controllers** are brains that understand what a particular kind of resource manifest means 

make the system’s **actual state** match the **desired state** as described by the manifest



**Controller delegation**

The Pod provides the ability to run one or more containers that have requested resources on a node in the cluster. 

The ReplicaSet controller run multiple instances of the same application which Pod.

Deployment controller leverages functionality provided by ReplicaSets to implement various deployment strategies such as rolling updates.

![Screenshot 1404-06-19 at 9.05.50 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 9.05.50 PM.png)



**Controller pattern**

Each controller runs an infinite loop, and every iteration reconciles the desired and the actual state of the cluster resources it is responsible for.

![Screenshot 1404-06-19 at 9.08.09 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 9.08.09 PM.png)



### NGINX operator

**ConfigMap:**  an API object used to store non-confidential data in key-value pairs. , configure the list of servers and customized static content. 

+ environment variables
+ command-line arguments
+ config files in a Volume. 



![Screenshot 1404-06-19 at 9.15.14 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 9.15.14 PM.png)



ConfigMap change is using the Kubernetes watch API. The watch feature is provided by the Kubernetes API for most resource types and allows the caller to be notified when a resource is created, modified, or deleted. 



### Getting started with CI/CD

![Screenshot 1404-06-19 at 9.46.58 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 9.46.58 PM.png)



With CronJob

```bash
❯ cat gitops-cronjob-mine.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: gitops-cron
  namespace: test
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 0
      template:
        spec:
          restartPolicy: Never
          serviceAccountName: gitops-serviceaccount
          containers:
          - name: gitops-operator
            image: gitopsbook/example-operator:v1.0
            command: [sh, -e, -c]
            args:
            - git clone https://github.com/gitopsbook/sample-app-deployment.git /tmp/example &&
              find /tmp/example -name '*.yaml' -exec kubectl apply -f {} \;
```



Supporting resources 

```bash
❯ cat gitops-resources-mine.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: gitops-serviceaccount
  namespace: test
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: gitops-operator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: admin
subjects:
- kind: ServiceAccount
  name: gitops-serviceaccount
  namespace: test
```





### Continuous integration pipeline

The CI pipeline does not communicate directly to the Kubernetes API server, instead it commits the desired change into Git and trust sometime later, the new change will be detected by the GitOps operator and applied.

![Screenshot 1404-06-20 at 1.02.12 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 1.02.12 PM.png)



GitOps CI pipeline goal:

+ Build and test
+ Publish a new container image to container registery
+ Update the Kubernetes manifests in Git to reflect the new image



```bash
❯ cat gitops-ci.sh
export VERSION=$(git rev-parse HEAD | cut -c1-7)
make build
make test

export NEW_IMAGE="gitopsbook/sample-app:${VERSION}"
docker build -t ${NEW_IMAGE} .
docker push ${NEW_IMAGE}

git clone http://github.com/gitopsbook/sample-app-deployment.git
cd sample-app-deployment

kubectl patch \
  --local \
  -o yaml \
  -f deployment.yaml \
  -p "spec:
        template:
          spec:
            containers:
            - name: sample-app
              image: ${NEW_IMAGE}" \
  > /tmp/newdeployment.yaml
mv /tmp/newdeployment.yaml deployment.yaml

git commit deployment.yaml -m "Update sample-app image to ${NEW_IMAGE}"
git push
```



**IMAGE TAGS AND THE TRAP OF THE LATEST TAG**

Use Git commit-SHA as part of the container's image tag.

reuse `latest` tag is a common mistake from build to build.

Kubernetes will not deploy the new version to the cluster at the second apply because not finding any change in the manifest, then `kubectl apply` will have zero effect.

The Deployment specs are the same from the prespective of Kubernetes.



Pro

Git commit SHA as unique version into the image tag enable traceability

rollback to the older version becomes impossible.

+ Semantic version
+ Build number
+ Date/time string





# 3. Environment management



## Introduction to environment management

QA, E2E, stage, Prod

![Screenshot 1404-06-20 at 1.42.59 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 1.42.59 PM.png)





Environment components:

+ Code
+ Run-time prerequisites
+ Configuration

![Screenshot 1404-06-20 at 1.48.45 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 1.48.45 PM.png)



Configuration of environment-specific application properties 

Each environment could contain DB storage, distributed cache, or messaging (such as data) for isolation. 



![Screenshot 1404-06-20 at 1.51.36 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 1.51.36 PM.png)



For example, ingress and egress can be configured to block traffic between preprod and prod environments for security.



PICKING THE RIGHT GRANULARITY

+ **Release independent:** your code must be deployed without dependencies on other teams/code.
+ **Test boundary:** Testing of the new code should be independent of other code release.
+ **Access control:** 
  + Seperate access control for preprod and prod
  + each environment can limit access control to only the team actively working on the codebase
+ **Isolation**: Each environment is a logical work unit and should be isolated from other environments.



### Namespace management



Namespaces provide a scope for unique resource naming, resource quotas, RBAC, hardware isolation,

and network configuration:

Kubernetes Namespace ~= Environment



![Screenshot 1404-06-20 at 3.59.59 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 3.59.59 PM.png)

**RBAC** is a method of regulating access to computer or network resources based on the roles of individual users within an enterprise. 

**role** contains rules that represent a set of permissions.

**ClusterRole:** A role can be defined within a Namespace with a role or clusterwide



Namespace:

+ CPU intensive application  - dedicated multicore hardware.
+  service requiring heavy disk I/O - high-speed SSD
+ networking policy (ingress/egress) to limit cross-Namespace traffic



**DEPLOY AN APP IN TWO DIFFERENT ENVIRONMENTS**

guestbook-qa and a preprod 

calledguestbook-e2e end-to-end 



![Screenshot 1404-06-20 at 4.10.30 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.10.30 PM.png)



````bash
kubectl create namespace guestbook-qa
kubectl create namespace guestbook-e2e

export K8S_GUESTBOOK_URL=https://k8s.io/examples/application/guestbook
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/redis-master-deployment.yaml
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/redis-master-service.yaml
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/redis-slave-deployment.yaml
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/redis-slave-service.yaml
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/frontend-deployment.yaml
kubectl apply -n guestbook-qa -f ${K8S_GUESTBOOK_URL}/frontend-service.yaml
````



test that the guestbook-qa environment

![Screenshot 1404-06-20 at 4.15.08 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.15.08 PM.png)



let’s promote guestbook-qa to the guestbook-e2e environment. 

use exactly the same YAML as was used in the guestbook-qa environment. This is similar to how your automated CD pipeline would work:



```bash
export K8S_GUESTBOOK_URL=https://k8s.io/examples/application/guestbook
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/redis-master-deployment.yaml
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/redis-master-service.yaml
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/redis-slave-deployment.yaml
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/redis-slave-service.yaml
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/frontend-deployment.yaml
kubectl apply -n guestbook-e2e -f ${K8S_GUESTBOOK_URL}/frontend-service.yaml
```



![Screenshot 1404-06-20 at 4.17.58 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.17.58 PM.png)



### Network isolation

only the intended clients can access the specific environment.

*Namespace network policy t*hat restricts network communication between Namespaces.



**EGRESS**: inside to outside

**INGRESS**: Outside to inside



![Screenshot 1404-06-20 at 4.24.52 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.24.52 PM.png)

```bash
kubectl create namespace qa
kubectl create namespace prod

kubectl -n qa apply -f curlpod.yaml
kubectl -n prod apply -f curlpod.yaml
```



```bash
❯ cat curlpod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: curl-pod
spec:
  containers:
  - name: curlpod
    image: radial/busyboxplus:curl
    command:
    - sh
    - -c
    - while true; do sleep 1; done
```





```bash
kubectl -n prod apply -f web.yaml

❯ cat web.yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
```



By default, Pods running in a Namespace can send network traffic to other Pods running in different Namespaces.



```bsh
kubectl describe pod web -n prod | grep IP
kubectl -n qa exec curl-pod -- curl -I http://<web pod ip>
kubectl -n prod exec curl-pod -- curl -I http://<web pod ip>
```



Let’s add a NetworkPolicy to our Pods in each Namespace:



```bash
kubectl apply -f block-other-namespace.yaml

❯ cat block-other-namespace.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  namespace: prod                         # Applies to Namespace prod
  name: block-other-namespace
spec:
  podSelector: {}                              # Selects all Pods in Namespace prod
  ingress:
  - from:
    - podSelector: {}                 # Specifies ingress to allow requests coming from prod Namespace only. Requests from other Namespaces will be blocked.
```



This NetworkPolicy is applied to the prod Namespace and allows only ingress

(incoming network traffic) from the prod Namespace



```bash
$ kubectl -n qa exec curl-pod -- curl -I http://<web pod ip> # Curl from namespace qa is blocked!
$ kubectl -n prod exec curl-pod -- curl -I http://<web pod ip> # Gets back Http 200
```



### Preprod and prod clusters



## Git strategies

Use a separate Git repository to hold your Kubernetes manifests

+ It provides a clean separation of application code and application config.
+ There will be times when you wish to modify the manifests without triggering an entire CI build



### Single branch (multiple directories)

the main branch will always contain the exact config used in each environment.

tools such as Kustomize 

![Screenshot 1404-06-20 at 4.45.14 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.45.14 PM.png)



### Multiple branches

each branch is equivalent to an environment.

The advantage here is that each branch will have the exact manifest for the environ ment without using any tool such as Kustomize. 



### Multirepo vs. monorepo

+ startup environment: monorepo
+ enterprise environment: Multireop



![Screenshot 1404-06-20 at 4.50.16 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-20 at 4.50.16 PM.png)



## Configuration management

having a directory for each environment 

kubectl apply -f <directory>.

To create new environment  need to make sure you add that resource to the YAML in each of your environments. 



factors when choosing this tools:

+ Declarative
+ Readable
+ Flexible
+ Maintainable





### Helm

 self-described package manager 

 maintaining several values.yaml, one for each environment (such as values-base.yaml, values-prod.yaml, and values-dev.yaml)









## 9 ArgoCD

![What is Argo CD? Features, Architecture, and Benefits](https://www.opsmx.com/wp-content/uploads/2022/07/Argo-1-e1630327305635-1.png)





### Core concepts

### Application

![Screenshot 1404-06-19 at 3.56.56 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 3.56.56 PM.png)



The **Application source** includes the repository URL and the directory inside of the repository.



 ![Screenshot 1404-06-19 at 3.57.54 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 3.57.54 PM.png)



The **Application destination** defines where resources must be deployed and includes the API server URL of the target Kubernetes cluster, along with the cluster Namespace name.



### Sync and health statuses

**Sync status** answers whether the observed application resources state deviates from the resources state stored in the Git repository. 

kubectl diff command - status are in-sync and out-of-sync. 



The **in-sync status** means that each application resource is found and fully matching to the expected resource state. 

he **out-of-sync** status means that at least one resource status is not matching to the expected state or not found in the target cluster.



 **health status**

+ **Healthy**: required number of Pods is running and each Pod successfully passes both readiness and liveness probes
+ **Progressing**: Represents a resource that is not healthy yet but is still expected to reach a healthy state. 
  + progressingDeadlineSeconds
+ **Degraded**:  The antipode of a healthy status. The example is a Deployment that could not reach a healthy status within an expected timeout
+ **Missing**: Represents the resource that is stored in Git but not deployed to the target cluster.



### PROJECT

A Project provides a logical grouping of Applications, isolates teams from each other, and allows for fine-tuning access control in each Project.

![Screenshot 1404-06-19 at 4.15.24 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 4.15.24 PM.png)



+ Restricts which Kubernetes clusters and Git repositories might be used by Project Applications
+ Restricts which Kubernetes resources can be deployed by each Application within a Project



### Architecture

GitOps operator

+ Retrieve resource manifests.
+ Detect and fix the deviations.
+ Present the results to end users.



![Screenshot 1404-06-19 at 4.19.00 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 4.19.00 PM.png)





### RETRIEVE RESOURCE MANIFESTS

The manifest generation in Argo CD is implemented by the *argocd-repo-server* component. 

+ too time consuming to download the whole repository

  + Argo CD solves this by caching the repository content on local disk and using the git

    fetch command 

+ memory usage, Helm or Kustomize

  + Argo CD allows the user to limit the number of parallel manifest generations and scale up

    

![Screenshot 1404-06-19 at 5.57.13 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 5.57.13 PM.png)



DETECT AND FIX THE DEVIATIONS

**argocd-application-controller:** reconciliation phase 

1. The controller loads the live Kubernetes cluster state, 
2. compares it with the expected manifests provided by the argocd-repo-server, and patches deviated resources. 



![Screenshot 1404-06-19 at 5.59.55 PM](/Users/hojat/Library/Application Support/typora-user-images/Screenshot 1404-06-19 at 5.59.55 PM.png)



**PRESENT THE RESULTS TO END USERS**

This task is performed by the argocd-server component. 

The argocd-server is a stateless web application that loads the information about reconciliation results and powers the web user interface.





