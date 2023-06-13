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
* first method
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

* second method

```bash
$ sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates

$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/docker.gpg
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"


$ sudo apt update
$ sudo apt install -y containerd.io

$ containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
$ sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml

$ sudo systemctl restart containerd
$ sudo systemctl enable containerd
```

* third method

```bash
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt remove containerd 
sudo apt update
sudo apt install containerd.io -y
sudo rm /etc/containerd/config.toml

sudo systemctl restart containerd
```