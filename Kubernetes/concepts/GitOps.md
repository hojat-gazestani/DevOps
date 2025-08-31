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



