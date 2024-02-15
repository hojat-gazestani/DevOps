# Namespace
* Set of symbols (names) that are used to identify and refer to objects of various kinds.
* Ensures that all of a given set of objects (kernel resource) have unique names so that they can be easily identified.
* Consists of one or more processes + a set of resources
* Namespaces
  * Control Group
  * Interprocess Communication (IPC)
  * Mount (mnt)
  * Network (net)
  * Process ID (PID)
  * Time (time)
  * User
  * NNIX time sharing (UTS)
  * syslog

# Cgroup Namespace
* Used by containers to isolate a set of processes into a virtual system at OS level
* chroot is used to isolate only the file paths
* Cgroup limit, isolate and measures resource usage of a group of processes.
* Cgroup can hav their own set of resource quotas for memory, CPU, Network and I/O.