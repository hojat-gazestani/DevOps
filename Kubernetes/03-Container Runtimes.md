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

## Installing Containerd

```bash
# Install required packages
sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates lsb-release
```
* first method
```bash
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
```

```bash
# restart containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
systemctl status containerd
```