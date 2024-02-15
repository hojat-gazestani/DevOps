Google Cloud Fundamentals: Core Infrastructure - Note
=====================================================
- [intro](#intro)
  - [GCP services](#GCP-services)
  - [cloud computing](#cloud-computing)
  - [fundamental characteristic of devices](#fundamental-characteristic-of-devices )
  - [PaaS](#PaaS)
  - [IaaS](#IaaS)
  - [qus](#qus)
- [resource hairarchy](#resource-hairarchy)
  - [todo](#todo)
- [Networking Fundamentals](#Networking-Fundamentals)
  - [compnents](#compnents)
  - [resources](#resources)
  - [Regions and Zones](#Regions-and-Zones)
  - [Virtual Private Cloud (VPC)](#Virtual-Private-Cloud-(VPC))
  - [GCP Projects ](#GCP-Projects)
  - [IP Addresses](#IP-Addresses)
  - [Routes](#Routes)
  - [Firewalls ](#Firewalls)
  - [DNS Resolution](#DNS-Resolution)
  - [Network Billing](#Network-Billing)
- [Google Compute engine and networking](#Google-Compute-engine-and-networking )
- [Cloud storage integration](#Cloud-storage-integration)
  - [Google Cloud Bigtable](#Google-Cloud-Bigtable)
  - [Google Cloud SQL and Google Cloud Spanner](#Google-Cloud-SQL-and-Google-Cloud-Spanner)
  - [Cloud Spanner](#Cloud-Spanner)
  - [Comparing Storage Options](#Comparing-Storage-Options)
  - [Course Labs](#Course-Labs)
  - [questions](#questions)
-[Containers, Kubernetes, and Kubernetes Engine](#Containers,-Kubernetes,-and-Kubernetes-Engine)
  - [Container](#Container)
  - [question](#question)
  - [Introduction to Kubernetes and GKE](#Introduction-to-Kubernetes-and-GKE)
  - [Course Labs](#Course-Labs)
  - [questions](#questions)
- [introduction to App Engine](#introduction-to-App-Engine)
  - [Google App Engine Standard Environment](#Google-App-Engine-Standard-Environment)
  - [Google App Engine Flexible Environment](#Google-App-Engine-Flexible-Environment)
  - [questions](#questions)
  - [Google Cloud Endpoints and Apigee Edge](#Google-Cloud-Endpoints-and-Apigee-Edge)
  - [Demonstration Getting Started with App Engine](#Demonstration-Getting-Started-with-App-Engine)
  - [questions](#questions)
- [Development in the cloud](#Development-in-the-cloud)
  - [Deployment Infrastructure as code](#Deployment-Infrastructure-as-code)
- [Monitoring Proactive instrumentation](#Monitoring-Proactive-instrumentation)
- [Big Data](#Big-Data)
  - [Introduction to Big Data and Machine Learning](#Introduction-to-Big-Data-and-Machine-Learning)


### GCP services
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/1-%20GCP%20resource%20hairearchy/1-services.png)

* Compute
  * Cupute engine
  * Kubernetes engine
  * App engine 
  * App engine 
  * Cloud foundation

* Storage 
  * Bigtable 
  * Cloud Storage 
  * Cloud SQL 
  * Cloud Spanner 
  * Cloud Datastore 

* Big Data 
  * Big Query 
  * Pub/Sub 
  * Data flow 
  * Data proc
  * Data lab

* Machine Learning 
  * Natural Language API 
  * Machine Learning 
  * Speech API 
  * Translate API 

### cloud computing
- Customers can scale their resource use up and down 
- Computing resources available on-demand and self-service 
- Customers pay only for what they use or reserve 
- Resources are available from anywhere over the network 

- Providers are NOT dedicating physical resources to each customer 

### fundamental characteristic of devices 
* Choose a fundamental characteristic of devices in a virtualized data center. 
* They are manageable separately from the underlying hardware. 

### PaaS
* Platform as a Service 
* let you bind your application code to libraries that give access to the infrastructure your application needs 

### IaaS
* Infrastructure as a Service
* provides raw compute, storage, and network, organized in ways that are familiar from physical data centers 

### qus
* qus1
  * What kind of customer benefits most from billing by the second for cloud resources such as virtual machines?
    * Customers who create and run many virtual machines 

* qus2
  * Services and APIs are enabled on a per project basis.

* qus3
  * Choose a fundamental characteristic of devices in a virtualized data center.
    * They are manageable separately from the underlying hardware. 
    * They use less resources than devices in a physical data center. 
    * They are more secure. 
    * They are available from anywhere on the Internet.

## resource hairarchy
### todo
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/1-%20GCP%20resource%20hairearchy/2-%20hierarchy.png)

* When would you choose to have an organization node?
  * When you want to apply organization-wide policies centrally. 
  * When you want to create folders 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/1-%20GCP%20resource%20hairearchy/3-%20project%20attributes.png)

* Order these IAM role types from broadest to finest-grained.* 
  * Primitive roles, predefined roles, custom roles 

* Can NOT IAM policies that are implemented higher in the resource hierarchy take away access that is granted by lower-level policies

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/1-%20GCP%20resource%20hairearchy/4-%20folder.png)


![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/1-%20GCP%20resource%20hairearchy/5-iam%20hairarchy.png)


* When would you choose to have an organization node?  
  * 
  * When you want to apply organization-wide policies centrally. 
  * When you want to organize resources into projects. 

* Order these IAM role types from broadest to finest-grained. 
  * Primitive roles, predefined roles, custom roles 

* Can NOT IAM policies that are implemented higher in the resource hierarchy take away access that is granted by lower-level policies 

## Networking Fundamentals
### compnents
 
* Network components
  * VPCs 
  * Projects 
  * Networks 
  * Regions 
  * Zones 
  * Subnets 
  * Switching 
  * Routing 
  * Firewalls
  
* Essentially, we’ll be going over this diagram: 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/1-diagram.png)

* GCP has 11 regions, 33 zones and over 100 points of presence throughout the globe. 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/2-regions-zones.png)

### Regions and Zones
* When building an application for high availability and fault tolerance, it’s crucial to distribute your resources across multiple zones and regions. 


* Zones are independent of each other, with completely separate physical infrastructure, networking, and isolated control planes that ensure typical failure events only affect that zone. 


* Another design consideration is speed and latency.  Zones have high-bandwidth, low-latency connections to other zones in the same region. 


* A region is a specific geographical location that is sub-divided into zones. 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/2-regions-zones.png)

* regions: 
  * To bring their applications closer to users around the world, and for improved fault tolerance


### resources
* Global Resources: 
  * 
  * Images 
  * Snapshots 
  * VPC Network 
  * Firewalls 
  * Routes 

* Regional Resources:
  * Static external IP addresses
  * Subnets 

* Zonal Resources:
  * Instances (VMs)
  * Persistent Disks

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/4-disks-images.png)

### Virtual Private Cloud (VPC) 
* global private isolated virtual network partition that provides managed networking functionality for your GCP resources. 

* global, spanning all regions. 

* The instances within the VPC have internal IP addresses and can communicate privately with each other across the globe. 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/5-routing-vpc.png)

### GCP Projects 
* an organizational construct used for billing and permissions. 
* Used for apps or various environments like Prod/Test/Dev. 
* Finance/HR/Marketing. 
* some use it to provide billing to customers based on their usage within a cloud-hosted environment. 

* it’s simply a way to organize resources from a billing and permissions perspective, and each project has its own VPC network(s) isolated from other projects in GCP. 


![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/12-projects.png)

* VPC Networks and Subnets
  * VPC network is like VRF 

 

* GCP Project
  *VPC Network
    * Subnets 
    * Routes
    * Firewall
    * Internal DNS

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/6-gcp-networks.png)

* VPC network called default is global, while each of the subnets within it is regional. 

* Even though subnets are regional, instances can communicate with other instances in the same VPC network using their private IP addresses. 

* Of course, you can isolate these subnets within the network if you wish using firewall policies. 
 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/7-gcp-subnet-zones.png)

* If you want complete isolation between various applications, customers, etc., you could create multiple networks.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/8-multiple-networks.png)

* You can have up to five networks per project, including the default network. Multiple networks within a single project can provide multi-tenancy, IP overlap, or isolation within the project itself. Just another option instead of having multiple projects. 

### IP Addresses
Each VM instance in GCP will have an internal IP address and typically an external IP address.  The internal IP address is used to communicate between instances in the same VPC network, while the external IP address is used to communicate with instances in other networks or the Internet. These IP addresses are ephemeral by default but can be statically assigned. 

### Routes
* All networks have routes in order to communicate with each other

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/9-gcp-routes.png)

* Routes are considered a “network resource” and cannot be shared between projects or networks. 

* If an instance tag is used, the route applies to that instance, and if an instance tag is not used, then the route applies to all instances in that network. 

* Even though there are no “routers” in the software-defined network, you can still think of each VM instance as connected to some core router, with all traffic passing through it based on the perspective of each node’s individual route table.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/10-gcp-route-tables.png)

### Firewalls 

* Each VPC network has its own distributed firewall, 

* If you have a concept in your mind that all this traffic is flowing through some single firewall chokepoint device somewhere, you’re mistaken. GCP is a full SDN, with firewall policies applied at the instance-level, no matter where it resides. These checks are performed immediately without having to funnel traffic through dedicated security appliances.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/3-network-components/11-gcp-firewalls.png)

* Firewall rules can match IP addresses or ranges, but can also match tags.  Tags are user-defined strings that help organize firewall policies for standards-based policy approach. For example, you could have a tag called web-server, and have a firewall policy that says any VM with the tag web-server should have ports HTTP, HTTPS, and SSH opened. 

* Firewall rules are at the network resource level and are not shared between projects are other networks. 

### DNS Resolution 

* DNS entries are automatically created resolving to a formatted hostname. 

* FQDN = <pre>[hostname].c.[project-id].internal</pre> 

* So, if I had an instance named “porcupine” in my project called “tree”, my DNS FQDN would be: 

* porcupine.c.tree.internal 

* Resolution of this name is handled by an internal metadata server that acts as a DNS resolver (169.254.169.254), provided as a part of Google Compute Engine (GCE). This resolver will answer both internal queries and external DNS queries using Google’s public DNS servers. 

* If an instance or service needs to be accessed publicly by FQDN, a public-facing DNS record will need to exist pointing to the external IP address of the instance or service. This can be done by publishing public DNS records. You have the option of using some external DNS service outside of GCP or using Google Cloud DNS. 

### Network Billing 

* GCP bills clients for egress traffic only.  Egress traffic is considered as traffic to the Internet, or from one region to another (in the same network), or between zones within a region. 

* You are not billed for ingress traffic. Ingress traffic includes VM-to-VM traffic in a single zone (same region, network), and traffic to most GCP services. 

* Some notes on caveats/limitations 
  * VPC networks only support IPv4 unicast traffic (No IPv6, or broadcast/multicast) 
  * Maximum of 7000 VM instances per VPC network 

## Google Compute engine and networking 

* For which of these interconnect options is a Service Level Agreement available 

* Google Cloud Load Balancing allows you to balance HTTP-based traffic across multiple Compute Engine regions. 

* Networks are global; subnets are regional 

* Local SSD is used for an application running in a Compute Engine virtual machine needs high-performance scratch space.  

* Choose an application that would be suitable for running in a Preemptible VM. 

* A batch job that can be checkpointed and restarted 

* Use big VMs for in-memory databases and CPU-intensive analytics; use many VMs for fault tolerance and elasticity 

* VPC routers and firewalls, They are managed by Google as a built-in feature. 

* A GCP customer wants to load-balance traffic among the back-end VMs that form part of a multi-tier application. Which load-balancing option should this customer choose? 

* The regional internal load balancer 

* For which of these interconnect options is a Service Level Agreement available? 

* Dedicated Interconnect 

## Cloud storage integration  

Ways to getting data into your cloud: 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/5-%20Cloud%20storage/0-cloud-storage.png)

### Google Cloud Bigtable
* Is a big data database service

* relational database schema:
  * tables in which every row has the same set of columns,
  * and the database engine enforces that rule and other rules you specify for each table
  * 
* NoSQL
  * not all the rows might need to have the same columns
  * the database might be designed to take advantage of that by sparsely populating the rows.
  * Which brings us to Bigtable
  * It's ideal for data that has a single lookup key
  * persistent hash table.
  * Cloud Bigtable is ideal for storing large amounts of data with very low latency.
  * It supports high throughput, both read and write, so it's a great for operational, analytical(IoT,user analytics and financial data analysis.)
* Bigtable
  * scalability
  * administration tasks like upgrades and restarts transparently
  * encrypted data in both in-flight and at rest.
  * major application including  search, analytics, maps and Gmail

* Can interact with other GCP services

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/5-%20Cloud%20storage/7-access-pattern.png)

### Google Cloud SQL and Google Cloud Spanner
* CloudSQL
  * Is managed RDBMS
  * Offers MySQL and PostgresSQLBeta database as service
  * use data base schema for data consistent
  * transactions, changes as all or nothing. Either they all get made, or none do.

* benefits of using the Cloud SQL
  * Automation replication (read, failover, and external replicas)
  * backup your data with either on-demand or scheduled backups
  * vertically by changing the machine type(read and write)
  * horizontally replicas(read)
  * data is encrypted(google security)

  * CloudSQL connections
  ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/5-%20Cloud%20storage/8-cloudSQl-connections.png)

* horizontal scaleability, consider using Cloud Spanner. It offers transactional consistency at a global scale, schemas, SQL, and automatic synchronous replication for high availability.
  * outgrown any relational database,
  * sharding your databases for throughput high performance
  * transactional consistency
  * global data and strong consistency,
  * financial applications, and inventory applications.

* Questions

### Google Cloud Datastore
* Is a horizontally scalable NoSQL DB
* Designed for application backend
* store structured data from App Engine apps
* automatically handles sharding and replication
* Unlike Cloud Bigtable, it also offers transactions that affect multiple database rows, and it lets you do SQL-like queries. 
* free daily quota that provides storage, reads, writes, deletes and small operations at no charge

* Questions



* Cloud Datastore databases CAN span App Engine and Compute Engine applications. 

### Comparing Storage Options
* Technical detail 1
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/5-%20Cloud%20storage/9-compare1.png)
* Cloud Datastore actually stores structured objects.
* Technical detail 2
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/5-%20Cloud%20storage/10-compare2.png)

### Course Labs
---------------

### Deploy a web server VM instance
```commandline
Compute Engine > VM instances.
Create Instance.
Create an Instance Name: 	bloghost
Region and Zone:            ${Zone}
Machine type: 				default
Boot disk:  				Debian GNU/Linux 9 (stretch).
Identity and API access : 	defaults
Firewall: 					Allow HTTP traffic.

Networking, disks, security, management, sole tenancy -> Management
Startup script: 
apt-get update
apt-get install apache2 php php-mysql -y
service apache2 restart

Create.
 
Copy: bloghost VM instance's internal and external IP
```
### Create a Cloud Storage bucket using the gsutil command line
```commandline
Google Cloud Platform -> Activate Cloud Shell ->  Continue.
gcloud config set project qwiklabs-gcp-03-ca3c8283cc51
export LOCATION=ASIA
gsutil mb -l $LOCATION gs://$DEVSHELL_PROJECT_ID
gsutil cp gs://cloud-training/gcpfci/my-excellent-blog.png my-excellent-blog.png
gsutil cp my-excellent-blog.png gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/my-excellent-blog.png
```

### Create the Cloud SQL instance
````commandline
Navigation menu -> SQL -> Create instance.
Choose a database engine: 			MySQL.
Instance ID,						blog-db
Root password						simplesimple
Single zone							region and zone assigned by Qwiklabs.

Create Instance.

click on blog-db
Copy  Public IP address 
Users -> ADD USER ACCOUNT
User name : blogdbuser
Password	: simplesimple
ADD

Connections -> Add network.
choose Public IP
Name: web front end
Network: external IP address of your bloghost /32 , 35.192.208.2/32
Done 
Save 
````

### Configure an application in a Compute Engine instance to use Cloud SQL
```commandline
 Navigation menu -> Compute Engine > VM instances.
 SSH: bloghost.
 cd /var/www/html
 sudo vim index.php
 <html>
<head><title>Welcome to my excellent blog</title></head>
<body>
<h1>Welcome to my excellent blog</h1>
<?php
 $dbserver = "CLOUDSQLIP";
$dbuser = "blogdbuser";
$dbpassword = "DBPASSWORD";
// In a production blog, we would not store the MySQL
// password in the document root. Instead, we would store it in a
// configuration file elsewhere on the web server VM instance.
$conn = new mysqli($dbserver, $dbuser, $dbpassword);
if (mysqli_connect_error()) {
        echo ("Database connection failed: " . mysqli_connect_error());
} else {
        echo ("Database connection succeeded.");
}
?>
</body></html>

sudo service apache2 restart

35.192.208.2/index.php
Database connection failed: ...

sudo vim index.php
replace CLOUDSQLIP: Cloud SQL instance Public IP
DBPASSWORD with the Cloud SQL database password

sudo service apache2 restart

Database connection succeeded.
```

### Configure an application in a Compute Engine instance to use a Cloud Storage object
```commandline
Cloud Storage: Browser.
bucket that is named after your GCP project.
my-excellent-blog.png opy the URL behind
Public access
 
 Return to your ssh session on your bloghost
cd /var/www/html
sudo vim index.php
<img src='https://storage.googleapis.com/qwiklabs-gcp-0005e186fa559a09/my-excellent-blog.png'>

sudo service apache2 restart
```

### questions

  
## Containers, Kubernetes, and Kubernetes Engine
------------------------------------------------

* IaaS
  * Offering let you share compute resources with others by virtualizing the hardware.
  * Each Virtual Machine has its own instance of an operating system, your choice, and you can build and run applications on it with access to memory, file systems, networking interfaces, and the other attributes that physical computers also have

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/1-IaaS.png)

* PaaS (App Engine)
  * Instead of getting a blank Virtual Machine, you get access to a family of services that applications need. 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/3-services.png)

* So all you do is write your code and self-contained workloads that use these services and include any dependent libraries. 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/4-self-contained-workloads.png)

* As demand for your application increases, the platform scales your applications seamlessly and independently by workload and infrastructure.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/5-scales.png)

###  Container

* give you the independent scalability of workloads like you get in a PaaS environment, and an abstraction layer of the operating system and hardware, like you get in an Infrastructure as a Service environment.
* What do you get as an invisible box around your code and its dependencies with limited access to its own partition of the file system and hardware?

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/6-container.png)

* You can treat the operating system and hardware as a black box. So you can move your code from development, to staging, to production, or from your laptop to the Cloud without changing or rebuilding anything. 

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/7-os.png)

* Kubernetes
  * In microservice infrastructure, you can make applications modular. They deploy it easily and scale independently across a group of hosts. The host can scale up and down, and start and stop Containers as demand for your application changes, or even as hosts fail and are replaced.
 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/8-microservice.png)

* A tool that helps you do this well is Kubernetes. Kubernetes makes it easy to orchestrate many Containers on many hosts. Scale them, roll out new versions of them, and even roll back to the old version if things go wrong.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/6-kubernetes/9-kubernetes.png)

* Cloud Build
  * a managed service for building Containers. 

### question

### Introduction to Kubernetes and GKE


* kubernetes
  * Kubernetes offers an API that lets people, that is authorized people, not just anybody, control its operation through several utilities. 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/1-kubernetes.png)

* cluster
  * It's a set of master components that control the system as a whole and a set of nodes that run containers.
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/2-cluster.png)

* Google cloud kubernetes
  * Google Cloud provides Kubernetes Engine, which is Kubernetes as a managed service in the cloud. 
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/3-gcp-kubernetes.png)

* pod
  * A pod is the smallest deployable unit in Kubernetes. Think of a pod as if it were a running process on your cluster. It could be one component of your application or even an entire application.
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/4-pod.png)

  * One way to run a container in a pod in Kubernetes is to use the kubectl run command.
  ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/5-run-pod.png)

```commandline
kubectl run nginx --image=nginx:1.15.7
```

To see the running nginx pods, run the command 
```commandline
kubectl get pods
```

To make the pods in your deployment publicly available, you can connect a load balancer to it by running the kubectl expose command.
```commandline
kubectl expose deployments nginx --port=80 --type=LoadBalancer
```

* Kubernetes then creates a service with a fixed IP address for your pods.

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/6-services.png)

* A service is the fundamental way Kubernetes represents load balancing. To be specific, you requested Kubernetes to attach an external load balancer with a public IP address to your service so that others outside the cluster can access it.

* Any client that hits that IP address will be routed to a pod behind the service.
![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/7-client.png)

* The kubectl get services command shows you your service's public IP address

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/8-get.png)
* To scale a deployment, run the kubectl scale command.
```commandline
kubectl scale nginx --replica=3
```

* You could also use auto scaling with all kinds of useful parameters. For example, here's how to auto scale a deployment based on CPU usage
*  Kubernetes will scale up the number of pods when CPU usage hits 80% of capacity. 
```commandline
kubectl autoscale nginx --min=10 --max=15 --cpu=80
```

* Instead of issuing commands, you provide a configuration file that tells Kubernetes what you want your desired state to look like and Kubernetes figures out how to do it.  
  * ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/7-kubernetes/9-file.png)

* After change, run the kubectl apply command to use the updated config file. 
```
kubectl apply -f nginx-deployment.yml
```

use the kubectl get replicasets command to view your replicas and see their updated state. 
```commandline
kubectl get replicasets
```

to watch the pods come online
```commandline
kubectl get pods
```

let's check the deployments to make sure the proper number of replicas are running 
```commandline
kubectl get deployments
```

The kubectl get services command confirms that the external IP of the service is unaffected.
```commandline
kubectl get services
```

### Introduction to Hybrid and Multi-Cloud Computing (Anthos)

* Anthos is a hybrid and multi-cloud solution powered by the latest innovations in distributed systems, and service management software from Google. The Anthos framework rests on Kubernetes and Google Kubernetes engine deployed on-prem. 
* Anthos also provides a rich set of tools for 
  * monitoring and 
  * maintaining the consistency of your applications across all of your network, 
  * whether on-premises, in the Cloud, or in multiple clouds. 

##  Course Labs

Confirm that needed APIs are enabled
------------------------------------
* Navigation menu -> APIs & Services
* Kubernetes Engine API
* Container Registry API

Start a Kubernetes Engine cluster
----------------------------------
```commandline
gcloud container clusters create webfrontend --zone us-central1-a --num-nodes 2
kubectl version

```
Compute Engine > VM Instances.

Run and deploy a container
--------------------------
```commandline
kubectl create deploy nginx --image=nginx:1.17.10
kubectl get pods

kubectl expose deployment nginx --port 80 --type LoadBalancer
kubectl get services
Open a new web browser tab and paste your cluster external IP

kubectl scale deployment nginx --replicas 3
kubectl get pods
kubectl get services
```

### questions


## introduction to App Engine

* App Engine (PaaS)
* Don't  focus on the infrastructure at all, Only focus on your code. 
* App engine will scale your application automatically in response to the amount of traffic it receives. 

* App Engine offers two environments:
  * standard
  * flexible

* built-in services
  * NoSQL databases, 
  * in-memory caching, 
  * load balancing, 
  * health checks, 
  * logging, 
  * authenticate users. 

### Google App Engine Standard Environment

* It offers a simpler deployment experience than the Flexible environment and fine-grained auto-scale.
* low utilization applications might be able to run at no charge.
  * ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/9-AppEngine/1-app-engin.png)

### Google App Engine Flexible Environment
* Build and deploy containerized apps with a click
* No sandbox constaints
* Can access App Engine resource

* Your application runs inside Docker containers on Google Compute Engine Virtual Machines, VMs.

* health checked, 
* healed as necessary, 
* choose which geographical region they run in,
* and critical backward-compatible updates 

* App Engine services
  * data store, 
  * memcached, 
  * task queues, 
  * and so on

* comparing 
* ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/9-AppEngine/2comparing.png)

* compair kubernetes with app engine
* ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/9-AppEngine/3-compare.png)

### questions

### Google Cloud Endpoints and Apigee Edge

* API
  * A clean, well-defined interface that abstracts away needless details and then they document that interface
  * ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/9-1-api/4-api.png)

* Google Cloud platform provides two API management tools
  * Cloud Endpoints supports applications running in GCP's compute platforms in your choice of languages and your choice of client technologies. 
  * Apigee Edge is also a platform for developing and managing API proxies. Focus onbusiness problems like rate limiting, quotas, and analytics.  business problems like rate limiting, quotas, and analytics. 
    * need not be in GCP, engineers often use it when they are "taking apart" a legacy application
    * Instead of replacing a monolithic application in one risky move, they can instead use Apigee Edge to peel off its services one by one, standing up microservices to implement each in turn, until the legacy application can be finally retired.

### Demonstration Getting Started with App Engine

### Activate Google Cloud Shell
```commandline
gcloud auth list
gcloud config list project
```

### Initialize App Engine
```commandline
gcloud app create --project=qwiklabs-gcp-04-3a06c7b0a06b
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
cd python-docs-samples/appengine/standard_python3/hello_world
```

### Run Hello World application locally
```commandline
sudo apt-get update
sudo apt-get install virtualenv

virtualenv -p python3 venv

source venv/bin/activate
pip install  -r requirements.txt
python main.py

Cloud Shell: Web preview: Preview on port 8080
Ctrl-C
 
Navigation menu: App Engine: Dashboard.
Notice that no resources are deployed.
```
 
 
### Deploy and run Hello World on App Engine
```commandline
cd ~/python-docs-samples/appengine/standard_python3/hello_world
gcloud app deploy

http://YOUR_PROJECT_ID.appspot.com
gcloud app browse
```

### Disable the application
```commandline
Navigation menu: App Engine: Settings.
Disable application.
```

### questions


## Development in the cloud

* Cloud Source Repositories
  * keep code private to a GCP project and use IAM permissions to protect it, but not have to maintain the Git instance yourself.
  * It provides Git version control to support your team's development of any application or 
  * service, including:
    * those that run on App Engine,
    * Compute Engine,
    * and Kubernetes Engine.
    * With Cloud Source Repositories, 

* source viewer 
  * you can browse and view repository files from within the GCP console.

* Cloud Functions
  * provide compute resources, no matter whether it happens once a day or once a millisecond.
  * write a single purpose function that did the necessary image manipulations and then arrange for it to automatically run whenever a new image gets uploaded. 
  * Cloud Functions can trigger on events in Cloud Storage, Cloud Pub/Sub, or in HTTP call. 

### Deployment Infrastructure as code
* provide repeatable deployments
* Create a yaml template describing your environment and use deplyement Manger to create resources

What is the advantage of putting event-driven components of your application into Cloud Functions?

### question

## Monitoring Proactive instrumentation
* Stackdriver is GCP's tool for monitoring, logging and diagnostics.

* core components
* ![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/10-monitoring/1-core-component.png)

##  Course Labs

### Confirm that needed APIs are enabled
```commandline
Navigation menu click APIs and services:  confirm that these APIs are enabled:
Cloud Deployment Manager v2 API
Cloud Runtime Configuration API
Stackdriver monitoring API
```

### Create a Deployment Manager deployment

* Cloud Shell button -> 
```
export MY_ZONE=
export MY_ZONE=us-central1-a
```

```
gsutil cp gs://cloud-training/gcpfcoreinfra/mydeploy.yaml mydeploy.yaml
sed -i -e "s/PROJECT_ID/$DEVSHELL_PROJECT_ID/" mydeploy.yaml
sed -i -e "s/ZONE/$MY_ZONE/" mydeploy.yaml

cat mydeploy.yaml
  resources:
  - name: my-vm
    type: compute.v1.instance
    properties:
      zone: us-central1-a
      machineType: zones/us-central1-a/machineTypes/n1-standard-1
      metadata:
        items:
        - key: startup-script
          value: "apt-get update"
      disks:
      - deviceName: boot
        type: PERSISTENT
        boot: true
        autoDelete: true
        initializeParams:
          sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-9-stretch-v20180806
      networkInterfaces:
      - network: https://www.googleapis.com/compute/v1/projects/qwiklabs-gcp-dcdf854d278b50cd/global/networks/default
        accessConfigs:
        - name: External NAT
          type: ONE_TO_ONE_NAT


gcloud deployment-manager deployments create my-first-depl --config mydeploy.yaml
gcloud deployment-manager deployments list

Navigation menu (￼), click Compute Engine > VM instances
Click on the VM instance
Custom metadata
```

### Update a Deployment Manager deployment
```
nano mydeploy.yaml
      value: "apt-get update; apt-get install nginx-light -y"
Ctrl+O, Enter
Ctrl+X

gcloud deployment-manager deployments update my-first-depl --config mydeploy.yaml

 Navigation menu (￼), click Compute Engine > VM instances.
 
my-vm VM instance's -> VM instance details -> Custom metadata 
```

### View the Load on a VM using Cloud Monitoring
```
Navigation menu (￼), click Compute Engine > VM instances.

my-vm -> STOP
EDIT (pencil icon
Compute Engine default service account
Allow full access to all Cloud APIs
Save
Start
START

Navigation menu (￼), click Compute Engine > VM instances.

my-vm instance, click SSH in its row in the VM instances list.
dd if=/dev/urandom | gzip -9 >> /dev/null &
```

### Create a Monitoring workspace
```
Navigation menu > Monitoring.
Settings -> GCP Projects 

curl -sSO https://dl.google.com/cloudagents/install-monitoring-agent.sh
sudo bash install-monitoring-agent.sh

curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh
sudo bash install-logging-agent.sh

Metrics Explorer
n the Metric pane of Metrics Explorer, select the resource type VM instance and the metric CPU usage.

Return to your ssh session on my-vm
 
kill %1
```

### question

## Big Data

### Introduction to Big Data and Machine Learning
* Google's technologies for getting the most out of data fastest. Whether it's real time analytics or machine learning. These tools are intended to be simple and practical for you to embed in your applications so that you can put data into the hands of your domain experts and get insights faster.

### Google Cloud Big Data Platform

* Google Cloud Big Data Solutions are designed to help you transform your business and user experiences with meaningful data insights

* Integrated Serverless Platform:
  * Serverless means you don't have to worry about provisioning Compute Instances to run your jobs. The services are fully managed, and you pay only for the resources you consume.
  * The platform is integrated, so that GCP data services work together to help you create custom solutions

![alt text](https://github.com/hojat-gazestani/Cloud/blob/main/GCP/Corsera/11-ML/1.png)
 
* Apache Hadoop:
  * An open source framework for big data. 
  * It is based on the MapReduce programming model which Google invented and published. 
  * The MapReduce model is, at its simplest, means that one function, traditionally called the "Map function," runs in parallel with a massive dataset to produce intermediate results. And another function, traditionally called the "Reduce function," builds a final result set based on all those intermediate results. 
  * The term "Hadoop" is often used informally to encompass Apache Hadoop itself, and related projects such as Apache Spark, Apache Pig, and Apache Hive.
  
* Cloud Dataproc
  * is a fast, easy, managed way to run Hadoop, Spark, Hive, and Pig on Google Cloud Platform.

  * Once your data is in a cluster, you can use Spark and Spark SQL to do data mining. 
  * And you can use MLib, which is Apache Spark's machine learning libraries to discover patterns through machine learning.

* Cloud Dataflow
  * Cloud Dataproc is great when you have a data set of known size or when you want to manage your cluster size yourself
  * But what if your data shows up in real time or it's of unpredictable size or rate
  * It's both a unified programming model and a managed service and it lets you develop and execute a big range of data processing patterns: extract, transform, and load batch computation and continuous computation. 
  * Dataflow fully automates the management of whatever processing resources are required
  * Dataflow frees you from operational tasks like resource management and performance optimization. 

  * use cases
    * general purpose ETL tool
    * data analysis engine
    * fraud detection
    * financial services
    * IoT analytics and manufacturing
    * healthcare and logistics and click stream
    * point of sale and segmentation analysis in retail.
    * It can be used in real time applications such as personalizing gaming user experiences.

* BigQuery
  * instead of a dynamic pipeline, your data needs to run more in the way of exploring a vast sea of data
  * You want to do ad-hoc SQL queries on a massive data set.
  * you can run super-fast SQL queries against multiple terabytes of data in seconds using the processing power of Google's infrastructure

* Cloud Pub/Sub
  * Whenever you're working with events in real time, it helps to have a messaging service. That's what Cloud Pub/Sub is. It's meant to serve as a simple, reliable, scalable foundation for stream analytics. You can use it to let independent applications you build send and receive messages. That way they're decoupled, so they scale independently.
  * Pub: publishers
  * Sub: subscribers

* Cloud Datalab
  * takes the management work out of this natural technique. It runs in a Compute Engine virtual machine.
  * It's integrated with BigQuery, Compute Engine, and Cloud Storage, so accessing your data doesn't run into authentication hassles.

### Google Cloud Machine Learning Platform

* Machine learning APIs
  * Gain insight form images
  * Detect inappropriate content
  * Analyze sentiment
  * Extract text

* Cloud Natural Language API
  * Can return text in real time
  * Highly accurate, even in noisy environments
  * Access from any device
  * Uses ML models to revel structure and meaning of text
  * Extract info about items mentioned in text documents, news, article, and blog post.

* Cloud translation API

* Cloud Video intelligence API

## Review

* Which compute service lets customers run virtual machines that run on Google's infrastructure?
  * Compute Engine
  
* Which compute service lets customers deploy their applications in containers that run in clusters on Google's infrastructure?
  * Kubernetes Engine
  
*Which compute service lets customers focus on their applications, leaving most infrastructure and provisioning to Google, while still offering various choices of runtime?
  * App Engine
  
  * Which compute service lets customers supply chunks of code, which get run on-demand in response to events, on infrastructure wholly managed by Google?
      * Cloud Functions

For what kind of traffic would the regional load balancer be the first choice? Choose all that are correct (2 answers).
* UDP traffic
* TCP traffic on arbitrary port numbers

* Choose a simple way to let a VPN into your Google VPC continue to work in spite of routing changes,
  * Cloud Router

* Which of these storage needs is best addressed by Cloud Datastore?
  * Structured objects, with transactions and SQL-like queries

* Which of these storage needs is best addressed by Cloud Spanner?
  * A relational database with SQL queries and horizontal scalability

* Which of these storage needs is best addressed by Cloud Bigtable?
  * Structured objects, with lookups based on a single key


* Which of these storage needs is best addressed by Cloud Storage?
  * Immutable binary objects