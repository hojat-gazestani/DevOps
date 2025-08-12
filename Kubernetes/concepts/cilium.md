# Cilium

## Kube-proxy

+ Handles traffic routing within a cluster to the appropriate backend pods.
+ Run on each node

### Kube-proxy mode

+ `iptables`:
  + Kernel level.
  + Session affinity, external traffic 

+ `ipvs`:
  + Uses Linux IP Virtual Server (IPVS)
  + Better performance and more sophisticated LB 
  + Reqires kernel module (`ip_vs`, `ip_vs_rr`, `ip_vs_wrr`, `ip_vs_sh`)
  + Larget and high-scale cluster 


How to chcke the current



```sh
kubectl -n kube-system get ds kube-proxy -o jsonpath='{.spec.template.spec.containers[0].command}'

```





### Strict ARP

+ Especially relevant when running in **IPVS mode**

+ `kube_proxy_strict_arp: true` tells the Linux kernel to only response to ARP request **if the target IP is actually configured on the node**
+ This prevents **ARP flux** - a problem where multiple nodes incorrectly respond to ARP requests for the same service IP, which can cause:
  + Unstable connections
  + Packet loss
  + Load balancing issues

**When it matters**

+ **IPVS mode: Required** for certain setup like **MetalLB in ARP mode**.
+ **iptables mode**: Has no effect (safe to leave default)
+ **LoadBalancer on bare metal**: Strongly recommended if you rely on ARP for service advertisement.



**Kubespray setting**

```sh
kube_proxy_mode: ipvs
kube_proxy_strict_arp: true
```



**Checking if it's enabled**

```sh
kubectl -n kube-system get cm kube-proxy -o yaml | grep strictARP -A2

```



**And on node**

```sh
sysctl net.ipv4.conf.all.arp_ignore
sysctl net.ipv4.conf.all.arp_announce

```



Resullt

```sh
net.ipv4.conf.all.arp_ignore = 1
net.ipv4.conf.all.arp_announce = 2

```



Meaning:

- Ignore ARP requests for IPs not on this node
- Only announce ARP from the correct interface





NOTE:

If you’re using **MetalLB in layer2 mode** with Kubespray, `kube_proxy_strict_arp: true` is basically **mandatory**.



