[TOC]



# vagrant

## Install

Fedora

```shell
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf -y install vagrant
```



Ubuntu

```bash
curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
sudo apt install ./vagrant_2.2.9_x86_64.deb
vagrant --version
```



### status

```shell
vagrant status
vagrant up
vagrant halt
vagrant reload
vagrant destroy
```



## Initialize a Project Directory

### Create a directory

```shell
mkdir vagrant_getting_started
cd vagrant_getting_started
```

### Initialize the project

```shell
vagrant init hashicorp/bionic64
vagrant init -m hashicorp/bionic64
```



## Install and Specify a Box

### Install a Box (Optional)

```shell
vagrant box add hashicorp/bionic64
```



## Boot an Environment

### Bring up a virtual machine

```shell
vagrant up
```



### SSH into the machine

```shell
vagrant ssh
```



### Destroy the machine

```shell
vagrant destroy
```



### Remove the box

```shell
vagrant box list
vagrant box remove hashicorp/bionic64
```



## Synchronize Local and Guest Files

```shell
vagrant up
vagrant ssh
```



### Explore the synced folder

```shell
vagrant@vagrant:~$ ls /vagrant/
Vagrantfile

vagrant@vagrant:~$ touch /vagrant/foo

vagrant@vagrant:~$ exit
logout
Connection to 127.0.0.1 closed.
❯ ls
      foo       Vagrantfile 
```



## Provision a Virtual Machine

### Create an HTML directory

```shell
 mkdir html
```



```html
vim index.html
<!DOCTYPE html>
<html>
  <body>
    <h1>Getting started with Vagrant!</h1>
  </body>
</html>
```



```shell
vim bootstrap.sh
apt-get update
apt-get install -y apache2
if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
```



### Configure Vagrant

```shell
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision :shell, path: "bootstrap.sh"
end
```



### Provision the webserver

```shell
vagrant up # If your machine were not already up
vagrant reload --provision # the guest machine is already running

vagrant ssh
wget -qO- 127.0.0.1
```



## Configure the Network

### Configure port forwarding

```shell
vim Vagrantfile
config.vm.network :forwarded_port, guest: 80, host: 4567

vagrant reload
```



### Bridge interface

```shell
vim Vagrantfile
config.vm.network "public_network"

vim Vagrantfile
```



## Share an Environment

## Prerequisites

### Install the plugin

```shell
vagrant plugin install vagrant-share
```



### Share the environment

```shell
vagrant share
```



## Teardown an Environment

### Suspend the machine

```shell
vagrant suspend
```



### Halt the machine

```shell
vagrant halt
```



### Destroy the machine

```shell
vagrant destroy
```



## Rebuild an Environment

### Vagrant Up

```shell
 vagrant up
```



## Multi-Machine

Create machine

```bash
Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7"
  
  config.vm.provider "virtualbox" do |vb|
    end
    
 config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.hostname = "web"
  end

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    config.vm.hostname = "db"
  end
end

```



private network

```bash
class VagrantPlugins::ProviderVirtualBox::Action::Network
  def dhcp_server_matches_config?(dhcp_server, config)
    true
  end
end


Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7"
  
  config.vm.provider "virtualbox" do |vb|
    end
    
 config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.network "private_network", type: "dhcp",
      name: "vboxnet0"
    web.vm.hostname = "web"
  end

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    db.vm.network "private_network", ip:"192.168.56.101",
      name: "vboxnet0"
    config.vm.hostname = "db"
  end
end

```



Install apache

```bash
Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7"
  
  config.vm.provider "virtualbox" do |vb|
    end
    
 config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.hostname = "web"
    web.vm.provision "allow_guest_host_resolution",
    type: "shell",
      inline: <<-SHELL
        yum update
        yum install -y httpd
       SHELL
  end

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    config.vm.hostname = "db"
  end
end

```



Diffrent Cpu and memory

```bash
Vagrant.configure("2") do |config|
config.vm.box = "bento/centos-7"

 config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
     vb.cpus = 3
   end


config.vm.define "web" do |web|
    web.vm.box = "bento/centos-7"
    web.vm.network "private_network", type: "dhcp",
      name: "vboxnet0"
    web.vm.hostname = "web"
    web.vm.provision "allow_guest_host_resolution",
      type: "shell",
      inline: <<-SHELL
        yum update
        yum install -y httpd
       SHELL
    web.vm.provider :virtualbox do |vv|
      vv.customize ["modifyvm", :id, "--memory", "2048"]
      vv.customize ["modifyvm", :id, "--cpus", "2"]
    end
  end

  config.vm.define "db" do |db|
    db.vm.box = "bento/centos-7"
    db.vm.network "private_network", ip:"192.168.56.101",
      name: "vboxnet0"
    db.vm.hostname = "db"
    db.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--memory", "1024"]
      v.customize ["modifyvm", :id, "--cpus", "1"]
    end
  end
end

```



## Source

> https://learn.hashicorp.com/tutorials/vagrant/getting-started-share?in=vagrant/getting-started 
