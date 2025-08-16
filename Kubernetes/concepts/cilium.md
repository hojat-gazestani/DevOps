# Cilium



## Cilium + MetalLB layer 2 + without kube-proxy



In `inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml`:



```sh
kube_network_plugin: cilium

kube_proxy_mode: none
kube_proxy_strict_arp: false  # irrelevant with kube-proxy disabled

metallb_enabled: true
metallb_ip_ranges:
  - "172.23.2.40-172.23.2.50"
  
metallb_layer2_advertise_ip: true
metallb_layer2_announce_ip: true
```







in `inventory/arc/group_vars/k8s_cluster/k8s-net-cilium.yml`

```sh
cni_provider: cilium

cilium_kube_proxy_replacement: strict

cilium_load_balancer_mode: dsr

cilium_enable_host_firewall: false

cilium_policy_enforcement: default
```



In ` inventory/arc/group_vars/k8s_cluster/addons.yml`

```sh
metallb_enabled: true
metallb_speaker_enabled: "{{ metallb_enabled }}"
metallb_namespace: "metallb-system"
metallb_protocol: "layer2"
metallb_port: "7472"
metallb_memberlist_port: "7946"
metallb_config:
  speaker:
    nodeselector:
      kubernetes.io/os: "linux"
    tolerations:
      - key: "node-role.kubernetes.io/control-plane"
        operator: "Equal"
        value: ""
        effect: "NoSchedule"
  controller:
    nodeselector:
      kubernetes.io/os: "linux"
    tolerations:
      - key: "node-role.kubernetes.io/control-plane"
        operator: "Equal"
        value: ""
        effect: "NoSchedule"
  address_pools:
    primary:
      ip_range:
        - 172.23.2.40-172.23.2.50
```



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
# Temporarily set the values (will reset on reboot)
sudo sysctl -w net.ipv4.conf.all.arp_ignore=0
sudo sysctl -w net.ipv4.conf.all.arp_announce=0


# Make permanent by adding to /etc/sysctl.conf
echo "net.ipv4.conf.all.arp_ignore = 0" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.conf.all.arp_announce = 0" | sudo tee -a /etc/sysctl.conf

# Apply changes
sudo sysctl -p

```


The default values (0) allow:

- The system to respond to ARP requests regardless of which interface they arrive on

- The system to announce ARP replies for any local IP address





NOTE:

If you’re using **MetalLB in layer2 mode** with Kubespray, `kube_proxy_strict_arp: true` is basically **mandatory**.



## Cilium with kube-proxy

+ Kube-proxy in **IPVS mode** and Cilium just provide CNI
  + `kube_proxy_strict_arp: true`is required for **MetalLB Layer 2**

### 

### Cilium without Kube-proxy

+ `kubeProxyReplacement: true` in Cilium
+ The `strictARP` setting in `kube-proxy` has no effect because kube-proxy isn't even running 
+ You instead control ARP handling through Cilium's own logic via `externalIPs` / `loadBalancer`handling



### Cilium with MetalLB Layer 2 mode

+ With kube-proxy  `kube_proxy_strict_arp: true` is recommended for kube-proxy **IPVS mode**
+ Wouthut kube-proxy: you must configure MetalLB `avoid-buggy-ips` and ensure Cilium's eBPF service LB doesn't respond to IPs it doesn't own. (Cilium 1.11+ automatically handle ARP correctly)



###  Kubespray specifics

In `inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml`:

```sh
kube_proxy_mode: ipvs
kube_proxy_strict_arp: true

```



This will:

+ Deploy kube-proxy in IPVS mode

+ Apply ARP sysctl tweaks

+ Work fine with Cilium as CNI

If you plan full kube-proxy replacement with Cilium:

```sh
kube_proxy_mode: none
kube_proxy_strict_arp: false  # no effect without kube-proxy

```



And in Cilium’s Helm values:



```sh
kubeProxyReplacement: strict
loadBalancer:
  mode: dsr

```

