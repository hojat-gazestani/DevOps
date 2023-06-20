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
vboxmanage clonevm "UbuS20-Base" --name "Kube-UbuS20-Master-56.80" --register --mode machine

vboxmanage clonevm "UbuS20-Base" --name "Kube-UbuS20-Worker1-56.81" --register --mode machine

vboxmanage clonevm "UbuS20-Base" --name "Kube-UbuS20-Worker2-56.82" --register --mode machine
```

```bash
sudo hostnamectl set-hostname master

echo "alias ipa='ip -c -br a'
alias ipr='ip -c -br r'
" >> ~/.bashrc

sudo sed -i 's/192.168.56.70/192.168.56.51/g' /etc/netplan/00-installer-config.yaml
sudo netplan apply
```
