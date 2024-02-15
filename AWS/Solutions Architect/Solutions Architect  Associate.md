AWS Certified Solutions Architect  Associate -  Notes
======================================================
- [VPC](#vpc)
	- [What is a vpc?](#What-is-a-vpc)

Availibity zone Regon
session2 part1

## VPC
### What is a vpc?
* VPC : Virtual Private Cloud - Isolated cloud resource Atuoscaling Load balancing
  * test
  *
  ![vpv](https://github.com/hojat-gazestani/Cloud/blob/main/AWS/Solutions%20Architect/pic/1-vpc.jpeg)


* EC2 : Elastic computing cloud

* beanstalk: Run quickly web application - Not high available- Frondend web developer Lambda : load code into Amazon - High availibility zones - Backend web developer

* AMI : Amazon Machin image

* Direct connect: on-primises Tunnel to AWS

* Route53: DNS

* EBS : Elastic block storage
* Session2 Part3

* Storage Gateway : on-promises , software appliaence , cloud storage low latency connection caching

* Cloud front : Content Delivery Network, Edge location

* Database services: SQL : Amazon RDS (Relational database service) Open source NoSQL : Dynamo DB (high-performance, low latency, ) online gaming data warehouse : Amazon redshift (Use SQL to Analyzing structure data) Cach : Amazon Elasticach (In-momeory caching) Gaming real-time, sub-milisecond responce, real-time transaction, BI, Gaming leader board

* Management tools: monitoring : Cloudwatch Infrastucture as code: Cloud formation (Crete Amazon resource using json files) Log activity : Clouad trail (Track user activity and API usage - Capture, Store, Act, Review) Audit, assess : AWS config ( resource inventory, configuration history, Configuration change, send notification

* Security and identity: IAM : AWS identity and access management kms : key management service (Create encryption key e.g: key for IAM) Directory servicee : Microsoft active direcotry Certification manager : Create and manage CA server (SSL/TLS) Web Application firewall :

* Application service: API gateway : Developer use to create, secure, publish and monitor simple notification service : send push message (like UDP - just send) simple queue service : send push message when consumer asked (like TCP - wait for ack) Simple email service : transaction email, marketing message, content simple wordflow service : create and run workflow Elastic transconding : media transcoding inside cloud.


## Session 3

* Amazon simple storage service (S3), Gleciers

* S3: secure, durable, high scalble accesable with web service

* Bucket (directory): object container
	* unique user - specified key
	* file name
	* unlimited number of object
	
	* target storage
		* kinees 
		* elastic mapreduce
		* emr
		
	* ebs, aws rds _. snapshot
	* data stage -> aws redshit, dynomoDB
	* backup, archive
		* on-promises
	* content media, software storage
	* big data analytics
	* static website hosting
	* cloud native mibile/ internet app hosting
	* disaster recovery

* Glaciers Data archving, long term backup, low cost, cold data, 5 hours

## Session 4

* S3 Classes

* 5 TB,

* S3 standard (General purpose: frequenty access, High avaiable, low latency, shor and long term )

* Intelligent tiering: decrease cost by auto teiring (frequent and archive)

* infrequent standard: less frequenty but rapid access

* one zone-infrequent:
* Archive (S3 Glacier)

* Data archiving, online backup, 3-5 hours, 40 TB

*  Vault: container using for archive, 100 vault per account IAM policy, vault access policy virtual lock: lock change restore 5% data per month instance retrieval: lowest cost for long-live data retrive in milisecond

* flexible retrive : lowest cost for long-live data - access one/two time per years

* Deep archive : 7-10 years or longer to meet regulatory, ca be restored with 12 hours
* object Life cycle policy

* After 30 days, transition -> statnard After 90 days, transition -> Glacier After 1000 days, Delete

* Encrypt inflight SSL api extend data at rest : server side encryption (AWS kms) AES256 Client side encryption

* Versioning protect dat accidental deletion

* Suspend

* MFA delete : multi factor authentication

* Pre-sign URL : limited access time

* Coress-regoin Replication rule: Async new object source bucket to target bucket
* EC2

* C4 : Compute optimal R3 : Memeory i2 : storage g2 : GPU based

* AMI: Amazon Machine Image Public by AWS AWS market place Generating from existing instance uploaded virtual server
* pricing

* on-demand
* reserve instance
	* all upfront (63% saving per years)
	* partial upfront
	* no upfront
* spot instance (not critical server)

* Elastic Block store

* EBS volume automaticaly replicate

* Magnetc volume :
	* clold data work load
	* lowest performance
	* 1gb - 1tb
	* 100 iops
	* data is accessed infrequently
	sequential read
	low-cost storage space
				 
General peropse ssd
	system boot , virtual desktop, development, development test environmet
	volume size: 1gb -16 tb
	10000 ipos
	1tb - 3000 ipbs
	5tb - 15000
	heavy traffic credit - brust -> 3000 iops
	system boot volume
	small to medium sized database
	
				
provisioned iops ssd
	critiqal busines, large database, 
	i/o intansive workload
	volume size 4GB-16TB
	20000 - 320 mb

## Sesion 5

VPC (Virtual Private Cloud)

Virtual network in our cloud

Region

VPC1
	Mandetory
	---------
	subnet
		one subnet -> one availibility zone
		
		public
		private 
		vpn only
	route table
		Defaul route -> local route
	
	Internet Gateway
	DHCP option set
		
	Network gatewawy
	ACL - Network access list
	
	Optional component:
	------------------
	security setting
	Elastic IP (EIP) - Public IP address
	Elastic network interface (ENI) - virtual network interface
	Endpoint : private connecton
		AWS VPC <-> AWS service <-> internet
	perring
		used for VPC interconnection
	nat instance / nat gateeway
	VPG/ CGW / VPN
	
	Availibilty zone1
	Availibilty zone2
VPC2
VPC3

IP address space
