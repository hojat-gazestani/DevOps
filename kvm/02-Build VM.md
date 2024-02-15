
## Setup required directories and config files
image link: https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2

```sh
D=/var/lib/libvirt/images
VM=CentOS-7-SSH
mkdir -vp $D/$VM
```

## meta-data file for KVM VM
```sh
cd $D/$VM
vim meta-data
instance-id: CentOS-7-SSH
local-hostname: CentOS-7-SSH
```

## user-data file for KVM VM
```sh
cd $D/$VM
vim user-data
#cloud-config
# Customize as per your need. At least change username (orcadmin) and ssh-ed22519 
# key with your actual public key
 
# Hostname management
preserve_hostname: False
hostname: CentOS-7-SSH
fqdn: CentOS-7-SSH.orca.local
 
# Setup Users with ssh keys so that I can log in into new machine
users:
    - default
    - name: orcadmin
      groups: ['wheel']
      shell: /bin/bash
      sudo: ALL=(ALL) NOPASSWD:ALL
      password: "123"
      ssh-authorized-keys:
		    - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCOi8bgbt/Vvhzq033Q5CecZbV2GM7P3TDEReXFjBYJQMGNX2Jf02k1fvSsaDtdEDblvFyry3oQBrrbQG22RxPfhk5ztt52ggm+dPsorIcBxsyjjykPYqSE1xhKXyScoRqNL44suzM7JBiZvH91yOcMknN+AZ+lluZuBuICL+kAOEnqSFs1WQVXwpp26qW4KDAqdq62CNolR8fijVaLs6DFNBqZoj11dOxuNZBeKfBQBLfcBijngG5zEKapa06SjaY0mW44+WN18EcQZPNvwRZIk8T17UJPzNeql+lJ1H6YRgYoD0G9HFhmEP1EYV1iD9eGMkoulNh7fwKfmT83N8hrJFODtqNNpXz/7UYixQ755k57/1Kws1mI0Fzrwp7NTJRkq017NVWrAWeFYdgNDWPPbFCnzjuZlyLSG3igbmXs/9fhLcj/KTUlv7BS17RMFWGpJKE2HAimKFK1A9AZH6UwlOPVLraE7it9Vk7ZgaabbacnUcFIjr/REnmTkRRMO6s= user@cp
      	- ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxv3N93X7TFJFllDjdcg3ieSL7nB0VlTbFxgWDzweCLcCaH2Wi0EJqzkoF5LX/UOlMIUTUrQlamC2Gxplb0AwxUQM1crn9edYy/r3ctT2imDSIUKnLk74pIj1p8NG+wKYRa9290ojdJSDEXhXxrM6Iev0v2VrNDBTO29P8l9LyhCgmHIPLEiznnt28avjSqvWBdb8zgGx6HImspq4VEUb5hCRRJiAZ26zTBOBSPnYQPMnzoF4vEwOZols9rzCDeHxIZnpaZJBH9mF++y4iztYKJmaUE6oATVSpJGUmVH+t6DMpoGGKAbddbxwOA1ogMwhtsGq2jg5bdYCh7wsxMsxAMx6rRVgCapl/NbEFw825H9KrOQgc4FSRjSKzkX+teNACWVRt6tscMvkoWw/L3yLPB5n65SeMWrQ3AHUgFyLnn0mfw/bHNNxWcF9AIWT/qK0B7JdKkETOM2RGaJB+wyxtmN5tVy32MlbS/TUEH0w3Mib6JEgqPsRkz/yEVHXmAhk= root@Sword
 
# Configure where output will go
output:
  all: ">> /var/log/cloud-init.log"
 
# configure interaction with ssh server
ssh_genkeytypes: ['ed25519', 'rsa']
 
# Install your public ssh key to the first user-defined user configured
# in cloud.cfg in the template (optional since I created orcadmin)
ssh_authorized_keys:
  - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCOi8bgbt/Vvhzq033Q5CecZbV2GM7P3TDEReXFjBYJQMGNX2Jf02k1fvSsaDtdEDblvFyry3oQBrrbQG22RxPfhk5ztt52ggm+dPsorIcBxsyjjykPYqSE1xhKXyScoRqNL44suzM7JBiZvH91yOcMknN+AZ+lluZuBuICL+kAOEnqSFs1WQVXwpp26qW4KDAqdq62CNolR8fijVaLs6DFNBqZoj11dOxuNZBeKfBQBLfcBijngG5zEKapa06SjaY0mW44+WN18EcQZPNvwRZIk8T17UJPzNeql+lJ1H6YRgYoD0G9HFhmEP1EYV1iD9eGMkoulNh7fwKfmT83N8hrJFODtqNNpXz/7UYixQ755k57/1Kws1mI0Fzrwp7NTJRkq017NVWrAWeFYdgNDWPPbFCnzjuZlyLSG3igbmXs/9fhLcj/KTUlv7BS17RMFWGpJKE2HAimKFK1A9AZH6UwlOPVLraE7it9Vk7ZgaabbacnUcFIjr/REnmTkRRMO6s= user@cp
  - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCxv3N93X7TFJFllDjdcg3ieSL7nB0VlTbFxgWDzweCLcCaH2Wi0EJqzkoF5LX/UOlMIUTUrQlamC2Gxplb0AwxUQM1crn9edYy/r3ctT2imDSIUKnLk74pIj1p8NG+wKYRa9290ojdJSDEXhXxrM6Iev0v2VrNDBTO29P8l9LyhCgmHIPLEiznnt28avjSqvWBdb8zgGx6HImspq4VEUb5hCRRJiAZ26zTBOBSPnYQPMnzoF4vEwOZols9rzCDeHxIZnpaZJBH9mF++y4iztYKJmaUE6oATVSpJGUmVH+t6DMpoGGKAbddbxwOA1ogMwhtsGq2jg5bdYCh7wsxMsxAMx6rRVgCapl/NbEFw825H9KrOQgc4FSRjSKzkX+teNACWVRt6tscMvkoWw/L3yLPB5n65SeMWrQ3AHUgFyLnn0mfw/bHNNxWcF9AIWT/qK0B7JdKkETOM2RGaJB+wyxtmN5tVy32MlbS/TUEH0w3Mib6JEgqPsRkz/yEVHXmAhk= root@Sword
 
# set timezone for VM
timezone: Asia/Tehran
 
# Remove cloud-init 
runcmd:
  - systemctl stop network && systemctl start network
  - yum -y remove cloud-init
 ```

## Copy cloud image
```sh
cd $D/$VM
cp -v /var/lib/libvirt/boot/CentOS-7-x86_64-GenericCloud.qcow2 $VM.qcow2
```

## Create 60GB disk image for new KVM VM
```sh
cd $D/$VM
export LIBGUESTFS_BACKEND=direct
qemu-img create -f qcow2 -o preallocation=metadata $VM.new.image 60G
virt-resize --quiet --expand /dev/sda1 $VM.qcow2 $VM.new.image
mv -v $VM.new.image $VM.qcow2
ls -l
```

## Creating a cloud-init ISO and a pool for our RHEL 8 (beta) VM
```sh
cd $D/$VM
mkisofs -o $VM-cidata.iso -V cidata -J -r user-data meta-data
virsh pool-create-as --name $VM --type dir --target $D/$VM
```

## install the CentOS-7-x86_64-GenericCloud.qcow2 image provided in the RHEL 8 downloads
```sh
cd $D/$VM
virt-install --import --name $VM \
--memory 2048 --vcpus 2 --cpu host \
--disk $VM.qcow2,format=qcow2,bus=virtio \
--disk $VM-cidata.iso,device=cdrom \
--network bridge=virbr0,model=virtio \
--os-type=linux \
--os-variant=rhel7.5 \
--graphics spice \
--noautoconsole
```

## Delete unwanted files:
```sh
cd $D/$VM
virsh change-media $VM hda --eject --config
rm -vi meta-data user-data *.iso
```

## How to find out IP address of KVM VM provided by DHCP
```sh
virsh net-dhcp-leases default
virsh net-dhcp-leases default | grep $VM | awk '{ print $5}'
```

## Log in to your RHEL 8 (beta) VM
```sh
ssh orcadmin@192.168.122.229
```