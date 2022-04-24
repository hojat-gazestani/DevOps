[TOC]



# vagrant

## Install

```shell
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
sudo dnf -y install vagrant
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



## Source

> https://learn.hashicorp.com/tutorials/vagrant/getting-started-share?in=vagrant/getting-started