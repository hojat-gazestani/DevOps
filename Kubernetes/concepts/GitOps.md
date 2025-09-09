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











