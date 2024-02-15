# CentOS


## ovs bridge
```sh
# "external bridge"
ovs-vsctl add-br br0 &&  ovs-vsctl add-port br0 eth0 && ifconfig eth0 0.0.0.0 && dhclient br0

# internal bridge
ovs-vsctl add-br br-int

# gre tunnel 
ovs-vsctl add-port br-int gre0 -- set interface gre0 type=gre options:remote_ip=<remote ip>

```


## Setup required directories and config files
image link: https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2
            https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2
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

# Ubuntu

## create an Ubuntu 22.04
```sh
sudo virt-install --name=ubuntu-base \
--description "Test Server" \
--os-variant=ubuntu22.04 \
--vcpus=2 \
--ram=4096 \
--disk path=/var/lib/libvirt/images/ubuntu-server.qcow2,format=qcow2,bus=virtio,size=15 \
--vnc \
--cdrom="/var/lib/libvirt/images/ubuntu-22.04.3-live-server-amd64.iso" \
--network bridge:br0
```

```sh
virsh dumpxml ubuntu-test > ubuntu-test.xml
```

# method 2 xml

```sh
# get the iso
wget http://releases.ubuntu.com/14.04.3/ubuntu-14.04.3-server-amd64.iso

# create the image disk 
qemu-img create -f qcow2 disk.qcow2 10G


vim ubuntu.xml
<domain type='kvm'>
  <name>ubuntu</name>
  <memory unit='GB'>2</memory>
  <vcpu>1</vcpu>
   <os>
 <type arch='x86_64' machine='pc-0.12'>hvm</type>
    <boot dev='cdrom'/>
  </os>
 <features>
    <pae/>
    <acpi/>
    <apic/>
  </features>
  <clock sync="localtime"/>
  <devices>
    <emulator>/usr/bin/kvm</emulator>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='/tmp/ubuntu-14.04.3-server-amd64.iso'/>
      <target dev='hdc' bus='ide'/>
      <readonly/>
    </disk>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2' cache='none'/>
      <source file='/tmp/disk.qcow2'/>
      <target dev='hda'/>
    </disk>
    <interface type='bridge'>
        <source bridge='br0'/>
        <virtualport type='openvswitch'/>
        <model type='virtio' />
    </interface>
    <graphics type='vnc' port='-1' autoport='yes' keymap='fr' listen='0.0.0.0' passwd='password'/>
  </devices>
</domain>


# launch the creation
virsh create ubuntu.xml
 
# you can connect to using vnc.

```

# Snapshots

## one
```sh
virsh snapshot-create-as ubuntu-test --name initial-install
virsh snapshot-list ubuntu-test
virsh snapshot-revert ubuntu-test initial-install
virsh snapshot-delete ubuntu-test added-neofetch
```


# delete

## one
```sh
virsh undefine ubuntu-test --remove-all-storage
```

# clone existing virtual machine

## base
```sh
virt-clone --original {Domain-Vm-Name-Here} --auto-clone
virt-clone --original {Domain-Vm-Name-Here} --name {New-Domain-Vm-Name-Here} --auto-clone
virt-clone --original {Domain-Vm-Name-Here} \
--name {New-Domain-Vm-Name-Here} --file {/var/lib/libvirt/images/File.Name.here}
```

## example
```sh
sudo virsh shutdown ubuntu-box1
sudo virsh suspend  ubuntu-box1
virsh list
sudo virt-clone --original ubuntu-box1 --auto-clone
sudo virsh start ubuntu-box1
sudo virsh start ubuntu-box1-clone
virsh list
```

# KVM forward ports to guests VM with UFW on Linux

## Find out information about your KVM network

```sh
virsh net-list
virsh net-info default
virsh net-dumpxml default
```

## Understanding KVM networking and default iptables/ufw rules
```sh
iptables -A FORWARD -d 192.168.122.0/24 -o virbr0 -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -s 192.168.2.0/24 -d 192.168.122.0/24 -o virbr0 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

```

## Step 1 – Configure kvm firewall hook
```sh
cd /etc/libvirt/hooks/
vi qemu
#!/bin/bash
# Hook to insert NEW rule to allow connection for VMs
# 192.168.122.0/24 is NATed subnet 
# virbr0 is networking interface for VM and host
# -----------------------------------------------------------------
# Written by Vivek Gite under GPL v3.x {https://www.cyberciti.biz}
# -----------------------------------------------------------------
# get count
#################################################################
## NOTE replace 192.168.2.0/24 with your public IPv4 sub/net   ##
#################################################################
v=$(/sbin/iptables -L FORWARD -n -v | /usr/bin/grep 192.168.122.0/24 | /usr/bin/wc -l)
# avoid duplicate as this hook get called for each VM
[ $v -le 2 ] && /sbin/iptables -I FORWARD 1 -o virbr0 -m state -s 192.168.2.0/24 -d 192.168.122.0/24 --state NEW,RELATED,ESTABLISHED -j ACCEPT
```

```sh
chmod -v +x /etc/libvirt/hooks/qemu

```

## Configuring the UFW (Iptables firewall) to port forward
```sh
vim /etc/ufw/before.rules
# KVM/libvirt Forward Ports to guests with Iptables (UFW) #
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -d 202.54.1.4 -p tcp --dport 1:65535 -j DNAT --to-destination 192.168.122.253:1-65535 -m comment --comment "VM1/CentOS 7 ALL ports forwarding"
-A PREROUTING -d 202.54.1.5 -p tcp --dport 22 -j DNAT --to-destination 192.168.122.125:22 -m comment --comment "VM2/OpenBSD SSH port forwarding"
-A PREROUTING -d 202.54.1.6 -p tcp --dport 443 -j DNAT --to-destination 192.168.122.231:443 -m comment --comment "VM3/FreeBSD 443 port forwarding"
-A PREROUTING -d 202.54.1.7 -p tcp --dport 80 -j DNAT --to-destination 192.168.122.229:80 -m comment --comment "VM4/CentOS 80 port forwarding"
COMMIT
```

```sh
bash /etc/libvirt/hooks/qemu
ufw reload
reboot
```

## Verify that forwarding ports to guests in libvirt/KVM working

```sh
iptables -L FORWARD -nv --line-number
iptables -t nat -L PREROUTING -n -v --line-number
iptables -t nat -L -n -v
```


## Linux forwarding ports to guests in libvirt / KVM iptables rules
```sh
iptables-save -t nat
iptables-save -t filter | grep FORWARD
```

# reset password

```sh
virsh dumpxml debian9-vm1 | grep 'source file'
<source file='/var/lib/libvirt/images/debian9-vm1.qcow2'/>

openssl passwd -1
mySecretRootAccountPasswordHere
$1$M1bf5Y3T$p2CYEz8vlUD2R.fXydTLt.

guestfish --rw -a /var/lib/libvirt/images/debian9-vm1.qcow2

launch
list-filesystems
mount /dev/sda1 /
vi /etc/shadow
root:$1$M1bf5Y3T$p2CYEz8vlUD2R.fXydTLt.:17572:0:99999:7:::
flush
quit


virsh start debian9-vm1

virsh list
virsh console debian9-vm1
```




