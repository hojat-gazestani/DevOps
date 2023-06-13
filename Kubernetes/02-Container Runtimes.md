# Container Runtimes

## [About cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/)

+ **cgroups** used for **resource management** for pods and containers which includes **cpu/memory** requests and limits for containerized workloads.
+ use a Linux distribution that enables and uses cgroup v2 by default.
  + Linux Kernel version is 5.8 or later
  + Container runtime supports cgroup v2. For example:
    + containerd v1.4 and later
    + cri-o v1.20 and later
  + Ubuntu (since 21.10, 22.04+ recommended)
  + Debian GNU/Linux (since Debian 11 bullseye)
  + RHEL and RHEL-like distributions (since 9)

## [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

[affect](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)

![Containerd](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/01-environment/01-containerd.png)

## Disable swap & add kernel settings
```bash
sudo sed -ri '/\sswap\s/s/^#?/#/' /etc/fstab
sudo swapoff -a
```

## Install and configure prerequisites

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

* Verify 

```bash
lsmod | grep br_netfilter
lsmod | grep overlay
```

## Installing Containerd

```bash
# Install required packages
sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates

# Add Docker repo
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Install containerd
sudo apt update
sudo apt install -y containerd.io

# Configure containerd and start service
sudo su -
mkdir -p /etc/containerd
containerd config default>/etc/containerd/config.toml

# restart containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
systemctl status containerd
```

## Debugging Kubernetes nodes with crictl

[Mapping from dockercli to crictl](https://kubernetes.io/docs/reference/tools/map-crictl-dockercli/)

[crictl](https://kubernetes.io/docs/tasks/debug/debug-cluster/crictl/)

[download crictl](https://github.com/kubernetes-sigs/cri-tools/releases)

```bash
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.27.0/crictl-v1.27.0-darwin-amd64.tar.gz
sudo tar -xzf crictl-v1.27.0-darwin-amd64.tar.gz -C /usr/local/bin/
```
# OR
```bash
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.27.0/crictl-v1.27.0-linux-amd64.tar.gz
tar -xzvf crictl-v1.27.0-linux-amd64.tar.gz
sudo mv crictl /usr/local/bin
sudo crictl ps
```

```bash
#List all pods:
crictl pods

# List pods by name
crictl pods --name nginx-65899c769f-wv2gp

# List pods by label:
crictl pods --label run=nginx

# List all images:
crictl images

# List images by repository:
crictl images nginx

# Only list image IDs:
crictl images -q

# List containers
crictl ps -a

# List running containers:
crictl ps
```

* Execute a command in a running container
```bash
crictl exec -i -t 1f73f2d81bf98 ls
```

```bash
# Get all container logs:
crictl logs 87d3992f84f74

# Get only the latest N lines of logs:
crictl logs --tail=1 87d3992f84f74
```

### Run a pod sandbox 

```bash
vim pod-config.json
{
  "metadata": {
    "name": "nginx-sandbox",
    "namespace": "default",
    "attempt": 1,
    "uid": "hdishd83djaidwnduwk28bcsb"
  },
  "log_directory": "/tmp",
  "linux": {
  }
}
```

```bash
crictl runp pod-config.json
```

### Create a container
```bash
# Pull a busybox image
crictl pull busybox

```

* Create configs for the pod and the container

```bash
vim pod-config.json
{
  "metadata": {
    "name": "busybox-sandbox",
    "namespace": "default",
    "attempt": 1,
    "uid": "aewi4aeThua7ooShohbo1phoj"
  },
  "log_directory": "/tmp",
  "linux": {
  }
}
```

```bash
vim container-config.json
{
  "metadata": {
    "name": "busybox"
  },
  "image":{
    "image": "busybox"
  },
  "command": [
    "top"
  ],
  "log_path":"busybox.log",
  "linux": {
  }
}

```

* Create the container, passing the ID of the previously-created pod, the container config file, and the pod config file. The ID of the container is returned

```bash
crictl create f84dd361f8dc51518ed291fbadd6db537b0496536c1d2d6c05ff943ce8c9a54f container-config.json pod-config.json
```

```bash
crictl ps -a

crictl start 3e025dd50a72d956c4f14881fbb5b1080c9275674e95fb67f965f6478a957d60

crictl ps
```





