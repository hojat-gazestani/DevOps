# Create VMs on Virtual Box

* Vagrant install Ubuntu 22.04

```bash
sudo apt install vagrant -y
```

* Vagrant initialize with dummy box

```bash
vim metadata.json
{
  "name": "dummy",
  "versions": [{
    "version": "0",
    "providers": [{
      "name": "virtualbox",
      "url": "/home/arman/Documents/ww/Vagrant/empty.box"
    }]
  }]
}
```

```bash
touch empty.box
```

```bash
zip dummy-virtualbox.zip metadata.json empty.box
```

```bash
vagrant init dummy
```


# Virtual Box
![LAB](https://github.com/hojat-gazestani/DevOps/blob/main/Kubernetes/Pic/01-environment/02-LAB.png)
```bash
vboxmanage clonevm "UbuS22-base" --name "Kube-UbuS22-Master-56.50" --register --mode machine

vboxmanage clonevm "UbuS22-base" --name "Kube-UbuS22-Master-56.51" --register --mode machine

vboxmanage clonevm "UbuS22-base" --name "Kube-UbuS22-Master-56.52" --register --mode machine
```

```bash
sudo hostnamectl set-hostname master

echo "alias ipa='ip -c -br a'
alias ipr='ip -c -br r'
" >> ~/.bashrc

sudo sed -i 's/192.168.56.50/192.168.56.51/g' /etc/netplan/00-installer-config.yaml
sudo netplan apply
```
