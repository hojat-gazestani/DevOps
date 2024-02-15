[TOC]



# KVM

## Getting start

### Install  packages

#### Check whether Virtualization is enabled

```shell
egrep -c '(vmx|svm)' /proc/cpuinfo
kvm-ok
sudo apt install -y cpu-checker
```



```shell
sudo apt-get update -y
sudo apt-get install -y qemu qemu-kvm libvirt-daemon libvirt-daemon-system bridge-utils virt-manager

dpkg --list | grep qemu
lsmod | grep kvm

sudo systemctl status libvirtd.service
```



### Managing disk images with qemu-img

```shell
qemu-img -h | grep Supported

qemu-img create -f raw debian.img 10G
ls -lah debian.img
file -s debian.img
qemu-img info debian.img
```



### Preparing images for OS installation with qemu-nbd

* outlined to partition and create a filesystem on the blank image:

* associate the blank image file
```shell
modprobe nbd
qemu-nbd --format=raw --connect=/dev/nbd0 debian.img 
```

* Create two partitions on the block device. swap,root partition
```shell
sfdisk /dev/nbd0 << EOF 
,1024,82; 
EOF 

ls -la /dev/nbd0*
mkswap /dev/nbd0p1
mkfs.ext4 /dev/nbd0p2
modinfo nbd

file -s /dev/nbd0
file -s debian.img
```



### Installing a custom OS on the image with debootstrap

```shell

sudo apt install -y debootstrap

sudo mount /dev/nbd0p2 /mnt/kvm-os
mount | grep mnt

sudo debootstrap --arch=amd64 --include="openssh-server vim" stable /mnt/kvm-os http://httpredir.debian.org/debian/
 ls -lah /mnt/kvm-os
 
 mount --bind /dev/ /mnt/kvm-os/dev
 ls -la /mnt/kvm-os/dev/ | grep nbd0 
 sudo chroot /mnt/
 pwd
 cat /etc/debian_version
 mount -t proc none /proc
 mount -t sysfs none /sys
 apt-get install -y --force-yes linux-image-amd64 grub2
 grub-install /dev/nbd0 --force
 update-grub2
 passwd
 echo "pts/0" >> /etc/securetty
 systemctl set-default multi-user.target
 echo "/dev/sda2 / ext4 defaults,discard 0 0" > /etc/fstab
 umount /proc/ /sys/ /dev/
 exit
 
 grub-install /dev/nbd0 --root-directory=/mnt/kvm-os/ --modules="biosdisk part_msdos" --force
 sed -i 's/nbd0p2/sda2/g' /mnt/kvm-os/boot/grub/grub.cfg 
 umount /mnt/kvm-os/
 qemu-nbd --disconnect /dev/nbd0 
```



### Resizing an image

```sh
apt install kpartx

qemu-img info debian.img
qemu-img resize -f raw debian.img +10GB
qemu-img info debian.img
```



print the name of the first unused loop device:

```shell
losetup -f
```

> /dev/loop0

```she
losetup /dev/loop1 debian.img
```



Read the partition information from the associated loop device and create device mappings:

```shell
# Read the partition information from the associated loop device
kpartx -av /dev/loop1

# Representing the partitions on the raw image:
ls -la /dev/mapper

# Obtain some information from the root partition mapping:
tune2fs -l /dev/mapper/loop1p2

# Check the filesystem on the root partition of the mapped device:
e2fsck /dev/mapper/loop1p2 

# Remove the journal from the root partition device:
tune2fs -O ^has_journal /dev/mapper/loop1p2

# Ensure that the journaling has been removed:
tune2fs -l /dev/mapper/loop1p2 | grep "features"

# Remove the partition mapping:
kpartx -dv /dev/loop1

# Detach the loop device from the image:
losetup -d /dev/loop1

# Associate the raw image with the network block device:
qemu-nbd --format=raw --connect=/dev/nbd0 debian.img

# List the available partitions
fdisk /dev/nbd0
p
d
n
p
2
w

# Associate the first unused loop device with the raw image file
losetup /dev/loop1 debian.img

# Read the partition information from the associated loop device and create the device mappings
kpartx -av /dev/loop1

# perform a filesystem check
e2fsck -f /dev/mapper/loop1p2
 
# Resize the filesystem on the root partition of the mapped device:
resize2fs /dev/nbd0p2

# Create the filesystem journal because we removed it earlier
tune2fs -j /dev/mapper/loop1p2

# Remove the device mappings
kpartx -dv /dev/loop1
losetup -d /dev/loop1
```



### Using pre-existing images

```shell
 wget https://people.debian.org/~aurel32/qemu/amd64/debian_wheezy_amd64_standard.qcow2
 wget https://cdimage.debian.org/cdimage/openstack/archive/9.3.0/debian-9.3.0-openstack-amd64.qcow2
 
 qemu-img info debian-9.3.0-openstack-amd64.qcow2
```



### Running virtual machine with qemu-system-*

```shell
# list binaries file you have
ls -la /usr/bin/qemu-system-*

# what CPU architectures QEMU supports on the host system: 
qemu-system-x86_64 --cpu help

# Start a new QEMU virtual machine using the x86_64 CPU architecture
qemu-system-x86_64 \
-name debian \
-vnc 146.20.141.254:0 \
-cpu Nehalem \
-m 1024 \
-drive format=raw,index=2,file=debian.img \
-daemonize

# Ensure that the instance is running
pgrep -lfa qemu

# Terminate the Debian QEMU instance
sudo pkill qemu

```



### Starting the QEMU VM with KVM support

````shell
cat /proc/cpuinfo | egrep "vmx|svm" | uniq

modprobe kvm

# Start a QEMU instance with KVM support
sudo qemu-system-x86_64 -name debian -vnc 192.168.122.1:0 -m 1024 -drive format=raw,index=2,file=debian.img -enable-kvm -daemonize

# Ensure that the instance is running: 
pgrep -lfa qemu

# Terminate the instance
pkill qemu
````



### Connecting to a running instance with VNC

```shell
# Start a new KVM-accelerated qemu instance:
sudo qemu-system-x86_64 \
-name debian \
-vnc 192.168.122.1:0 \
-m 1024 \
-drive format=raw,index=2,file=debian.img \
-enable-kvm \
-daemonize

# Ensure that the instance is running: 
pgrep -lfa qemu

# Start the VNC client and connect to the VNC server on the IP address and display
port you specified in step 1
```



## Install and configuring libvirt

````shell
# install the package
sudo apt update && apt install libvirt-bin

# Ensure that the libvirt daemon is running
pgrep -lfa libvirtd

# Examine the default configuration: 
cat /etc/libvirt/libvirtd.conf | grep -vi "#" | sed '/^$/d'

# Disable the security driver in QEMU 
vim /etc/libvirt/qemu.conf
security_driver = "none"

# Restart the libvirt daemon: 
sudo /etc/init.d/libvirt-bin restart

# Examine all configuration files in the libvirt directory:
ls -la /etc/libvirt/
````



### Create KVM instances by XML file

```shell
# List all virtual machines
 virsh list --all
```



```xml
 vim kvm1.xml
<domain type='kvm' id='1'>
	<name>kvm1</name>
    <memory unit='KiB'>1048576</memory>
    <vcpu placement='static'>1</vcpu>
    <os>
        <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
        <boot dev='hd'/>
    </os>
    <on_poweroff>destroy</on_poweroff>
    <on_reboot>restart</on_reboot>
    <on_crash>restart</on_crash>
    <devices>
        <emulator>/usr/bin/qemu-system-x86_64</emulator>
        <disk type='file' device='disk'>
        	<driver name='qemu' type='raw'/>
        	<source file='./debian.img'/>
        	<target dev='hda' bus='ide'/>
        	<alias name='ide0-0-0'/>
        	<address type='drive' controller='0' bus='0' target='0' unit='0'/>
        </disk>
        <interface type='network'>
            <source network='default'/>
            <target dev='vnet0'/>
            <model type='rtl8139'/>
            <alias name='net0'/>
            <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
        </interface>
        <graphics type='vnc' port='5900' autoport='yes' listen='192.168.122.1'>
            <listen type='address' address='192.168.122.1'/>
        </graphics>        
    </devices>
    <seclabel type='none'/>
</domain>
```



```shell
# Define the virtual machine
virsh define kvm1.xml
```



#### Dump xml

````shell
virsh dumpxml VM_NAME
virsh dumpxml --domain VM_NAME

virsh dumpxml --domain openbsd | grep 'source file'
````



#### List VM guests

```shell
virsh list
virsh list --all
```



### Create KVM instances by virt-inst

```shell
# installing the package:
sudo apt install virtinst

virt-install --name <VM-NAME> --memory <GUEST-RAM> \
# Guest storage
	--disk 
	--filesystem
# Installation method
	--location
	--cdrom
	--pxe
	--import
	--boot


```



#### Create a virtual machine from an ISO image

```shell
virt-install \
--name UbuS16-1 \
--memory 1024 \
--vcpus 2 \
--disk size=10 \
--cdrom ~/Downloads/ISO/ubuntu-16.04.7-server-amd64.iso \
--os-variant ubuntu16.04
```



#### VMware

```
virt-install --virt-type=kvm --name=esxi1 \                       ─╯
--cpu host-passthrough \
--ram 4096 --vcpus=4 \
--virt-type=kvm --hvm \
--cdrom VMware-VMvisor-Installer-7.0U3d-19482537.x86_64.iso \
--network default,model=e1000 \
--graphics vnc --video qxl \
--disk pool=default,size=80,sparse=true,bus=ide,format=qcow2 \
--boot cdrom,hd --noautoconsole --force
```



#### Create KVM instance by invoking the virt-install

```shell
virt-install \
--name kvm2 \
--ram 1024 \
--disk path=debian.img,format=raw \
--graphics vnc,listen=192.168.122.1 \
--extra-args='console=tty0' \
-v --hvm \
--import
 
# virtual machine definition file that was automatically generated
cat /etc/libvirt/qemu/kvm1.xml
```



#### Create KVM instances with virt-install and using the console	

```shell
# Installing a virtual machine from the network
virt-install \ 
  --name guest1-rhel7 \ 
  --memory 2048 \ 
  --vcpus 2 \ 
  --disk size=8 \ 
  --location http://example.com/path/to/os \ 
  --os-variant rhel7 

# Install KMV instances with virt-install and define console
virt-install \
--name kvm22 \
--ram 1024 \
--disk path=kvm22.img,size=8 \
--extra args="text console=tty0 utf8 console=ttyS0,115200" \
--graphics vnc,listen=192.168.122.1 \
--hvm \
--location=http://ftp.ir.debian.org/debian/dists/stable/main/installer-amd64/ 

# Attach to the console
virsh console kvm3

# Start the newly provisioned VM
virsh start kvm1

# Using your favorite VNC client, connect to the instance
systemctl enable serial-getty@ttyS0.service
systemctl start serial-getty@ttyS0.service

# Close the VNC session and connect to the virtual instance from the host OS
virsh console kvm1
	free -m
	
Disconnect from the console using the Ctrl + ] key 

# Examine the image file created after the installation: 
qemu-img info /tmp/kvm1.img
```



#### Create KVM Virtual Machine Using Qcow2 Image

```shell
# Importing a virtual machine image

virt-install \
--name DebS9-1 \
--memory 1024 \
--vcpus 2 \
--disk ~/Documents/ww/kvm/images/debian-9.qcow2 \
--import \
--os-variant debian9

virt-customize -a debian-9.qcow2 --root-password password:123

virt-install \
--name debian9 \
--memory 2048 \
--vcpus 1 \
--disk ./debian-9.qcow2,bus=sata \
--import \
--os-variant debian9 \
--network default \
--vnc --noautoconsole 


# List OS Variants
osinfo-query os

# To launch the same VM next time, run:
virsh --connect qemu:///system start centos8
```



#### KVM Import an OVA Template

```
tar xvf xenial-server-cloudimg-amd64.ova

qemu-img convert -O qcow2 ubuntu-xenial-16.04-cloudimg.vmdk ubuntu-xenial-16.04-cloudimg.qcow2
virt-customize   -a ubuntu-xenial-16.04-cloudimg.qcow2 --root-password password:123

virt-install \
> --name UbuS16 \
> --memory 4096 \
> --vcpus 4 \
> --disk ubuntu-xenial-16.04-cloudimg.qcow2,bus=sata \
> --import \
> --os-variant ubuntu16.04
```



####  Create a virtual machine using PXE

```shell
virt-install \ 
  --name guest1-rhel7 \ 
  --memory 2048 \ 
  --vcpus 2 \ 
  --disk size=8 \ 
  --network=bridge:br0 \ 
  --pxe \ 
  --os-variant rhel7 
```



####  Create a virtual machine with Kickstart

```shell
virt-install \ 
  --name guest1-rhel7 \ 
  --memory 2048 \ 
  --vcpus 2 \ 
  --disk size=8 \ 
  --location http://example.com/path/to/os \ 
  --os-variant rhel7 \
  --initrd-inject /path/to/ks.cfg \ 
  --extra-args="ks=file:/ks.cfg console=tty0 console=ttyS0,115200n8" 
```



#### Create a virtual machine and scpcify networks

```shell
virt-install \
--name testmachine \
--ram=128 \
--vcpus=1 \
--disk path=/var/lib/libvirt/images/testmachine.img,size=0.2 \
--nographics \
--location /tmp/Core-current.iso \
--extra-args "console=ttyS0" \
--network bridge:br0 \

osinfo-query os
```



#### Create Ubuntu 22.04 KVM Guest From Cloud Image

```shell
sudo mkdir /var/lib/libvirt/images/templates
wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

sudo mv -i jammy-server-cloudimg-amd64.img \
  /var/lib/libvirt/images/templates/ubuntu-22-server.qcow2
  
  
sudo apt update \
  && sudo apt install cloud-utils whois -y
  
VM_NAME="UbuS22-nextCloud-1"
USERNAME="ubuntu"
PASSWORD="Password"

sudo mkdir /var/lib/libvirt/images/$VM_NAME \
  && sudo qemu-img convert \
  -f qcow2 \
  -O qcow2 \
  /var/lib/libvirt/images/templates/ubuntu-22-server.qcow2 \
  /var/lib/libvirt/images/$VM_NAME/root-disk.qcow2
  
sudo qemu-img resize \
  /var/lib/libvirt/images/$VM_NAME/root-disk.qcow2 \
  100G
  
  
sudo echo "#cloud-config
system_info:
  default_user:
    name: $USERNAME
    home: /home/$USERNAME

password: $PASSWORD
chpasswd: { expire: False }
hostname: $VM_NAME

# configure sshd to allow users logging in using password 
# rather than just keys
ssh_pwauth: True
" | sudo tee /var/lib/libvirt/images/$VM_NAME/cloud-init.cfg


sudo cloud-localds \
  /var/lib/libvirt/images/$VM_NAME/cloud-init.iso \
  /var/lib/libvirt/images/$VM_NAME/cloud-init.cfg
  
  
sudo virt-install \
  --name $VM_NAME \
  --memory 8192 \
  --disk /var/lib/libvirt/images/$VM_NAME/root-disk.qcow2,device=disk,bus=virtio \
  --disk /var/lib/libvirt/images/$VM_NAME/cloud-init.iso,device=cdrom \
  --os-type linux \
  --os-variant ubuntu16.04 \
  --virt-type kvm \
  --graphics none \
  --network network=my-net,model=virtio \
  --import
  
# Cleanup

sudo rm /var/lib/libvirt/images/$VM_NAME/cloud-init.iso \
  && sudo rm /var/lib/libvirt/images/$VM_NAME/cloud-init.cfg
  
sudo virsh edit $VM_NAME


# Then remove this section:
<disk type='file' device='cdrom'>
  <driver name='qemu' type='raw'/>
  <source file='/var/lib/libvirt/images/template-ubuntu-22/cloud-init.iso'/>
  <target dev='sda' bus='sata'/>
  <readonly/>
  <address type='drive' controller='0' bus='0' target='0' unit='0'/>
</disk>

# A Note About Cloning
# Delete match and mac address lines
vim /etc/netplan/50-cloud-init.yaml
network:
    ethernets:
        enp1s0:
            dhcp4: true
            match:
                macaddress: 52:54:00:c2:9e:bc
            set-name: enp1s0
    version: 2
    
# add lines
network:
    ethernets:
        enp1s0:
            dhcp4: true
    version: 2

```





### Starting, stopping, and removing KVM instances

```shell
# List all instances in all states
virsh list --all

virsh start kvm1

# Examine the running process for the virtual machine: 
pgrep -lfa qemu

# Terminate the VM and ensure its status changed from running to shut off: 
virsh destroy kvm1
virsh list --all

# Shutdown the guest
virsh shutdown VM_NAME
virsh shutdown --domain VM_NAME

# Force a guest to stop
virsh destroy VM_NAME
virsh destroy --domain VM_NAME

# Deleting a guest
virsh undefine kvm1
virsh undefine --domain kvm1

rm -rf /nfswheel/kvm/openbsd.qcow2
virsh list --all

# error: Refusing to undefine while domain managed save image exists
virsh managedsave-remove kvm1
```



* A note about error: “cannot delete inactive domain with snapshots”

```shell
virsh snapshot-list UbuS16-1
virsh snapshot-list --domain VM_NAME
virsh snapshot-delete --domain VM_NAME --snapshotname

virsh snapshot-create UbuS16-1
virsh snapshot-revert --snapshotname 1651481979 UbuS16-1
```

* Remove associated VM storage volumes and snapshots while undefineing a domain/VM

```shell
virsh undefine --domain {VM_NAME_HERE} --storage

virsh domblklist --domain {VM_NAME_HERE}
virsh snapshot-list --domain {VM_NAME_HERE}

virsh undefine --domain {VM_NAME_HERE} --remove-all-storage

virsh undefine --domain {VM_NAME_HERE} --delete-snapshots

virsh undefine --domain mysql-server --remove-all-storage

virsh undefine --domain mysql-server --remove-all-storage 
```





### Inspecting and editing KVM config

```shell
# Ensure that you have a running
virsh list

# Dump the instance configuration file to standard output (stdout).
virsh dumpxml kvm1

# Save the configuration to a new file, as follows: 
virsh dumpxml kvm1 > kvm1.xml

# Edit the configuration in place and change the available memory for the VM:
virsh edit kvm1
```



### Managing CPU and memory resources in KVM

```shell
# Get memory statistics for the running instance:
virsh dommemstat kvm1

# To increase the maximum amount of memory that can be allocated to the VM
virsh setmaxmem kvm1 4G --config
virsh setmaxmem kvm1 512M --config

# Update the available memory for the VM to 2 GB
virsh setmem kvm1 --size 512M

virsh dumpxml kvm1 | grep memory

####
# CPUs:
####

# Get information about the guest CPUs: 
virsh vcpuinfo kvm1

# List the number of virtual CPUs used by the guest OS: 
virsh vcpucount kvm1

# Change the number of allocated CPUs to 4 for the VM
virsh edit kvm1
 
# Ensure that the CPU count update took effect: 
virsh vcpucount kvm1
virsh dumpxml kvm1 | grep -i cpu
```



### Attaching block devices to virtual machines

```shell
# Create a new 1 GB image file:
dd if=/dev/zero of=/tmp/new_disk.img bs=1M count=1024

# Attach the file as a new disk to the KVM instance: 
virsh attach-disk kvm1 /tmp/new_disk.img vda --live

# Connect to the KVM instance via the console: 
virsh console kvm1
	# Print the kernel ring buffer and check for the new block device: 
	dmesg | grep vda

	# Examine the new block device: 
	fdisk -l /dev/vda

# Dump the instance configuration from the host OS: 
virsh dumpxml kvm1

# Get information about the new disk: 
virsh domblkstat kvm1 vda

# Detach the disk: 
virsh detach-disk kvm1 vda --live

# Copy or create a new raw image: 
cp /tmp/new_disk.img /tmp/other_disk.img

# Write the following config file: 
cat other_disk.xml

# Attach the new device: 
virsh attach-device kvm1 --live other_disk.xml

# Detach the block device: 
 virsh detach-device kvm1 other_disk.xml --live
```



### Sharing dirctory between a running VM and host OS

```shell
mkdir /tmp/shared
touch /tmp/shared/file

virsh edit kvm1
<devices>
    ...
    <filesystem type='mount' accessmode='passthrough'>
    <source dir='/home/hoji/Documents/ww/kvm/shared'/>
    <target dir='tmp_shared'/>
    </filesystem>
    ...fie
</devices>

# Selinux configuration
sudo semanage fcontext -a -t svirt_image_t "/home/hoji/Documents/ww/kvm/shared(/.*)?"
sudo restorecon -vR /home/hoji/Documents/ww/kvm/shared

virsh start kvm1

virsh console kvm1
	lsmod | grep 9p
	mount -t 9p -o trans=virtio tmp_shared /mnt
	mount | grep tmp_shared
	ls -la /mnt/
```



### Autostarting KVM instances

```shell
# Enable the VM autostart: 
virsh autostart kvm1

# Obtain information for the instance: 
virsh dominfo kvm1

# Stop the running instance and ensure that it is in the shut off state: 
virsh destroy kvm1
virsh list --all

# Stop the libvirt daemon and ensure that it is not running: 
/etc/init.d/libvirt-bin stop
pgrep -lfa libvirtd

# Start back the libvirt daemon:
/etc/init.d/libvirt-bin start

# List all running instances: 
virsh list --all

# Disable the autostart option: 
virsh autostart kvm1 --disable

# Verify the change: 
virsh dominfo kvm1 | grep -i autostart
 
```



### Working with storage pools

```shell
# Copy the raw Debian image file 
cp /tmp/kvm1.img /var/lib/libvirt/images/

# Create the following storage pool definition: 
cat file_storage_pool.xml
<pool type="dir">
  <name>file_virtimages</name>
  <target>
    <path>/var/lib/libvirt/images</path>
  </target>
</pool>

# Cannot access storage file, Permission denied Error in KVM Libvirt
sudo vim /etc/libvirt/qemu.conf
	user = "hoji"
	group = "libvirt"

sudo systemctl restart libvirtd
sudo usermod -a -G libvirt $(whoami)
sudo chown hoji:libvirt /var/lib/libvirt/images

# Define the new storage pool
virsh pool-define file_storage_pool.xml

# List all storage pools: 
virsh pool-list --all

# Start the new storage pool and ensure that it's active: 
virsh pool-start file_virtimages
virsh pool-list --all

# Enable the autostart feature on the storage pool: 
virsh pool-autostart file_virtimages
virsh pool-list --all
 
# Obtain more information about the storage pool: 
virsh pool-info file_virtimages

# List all volumes that are a part of the storage pool: 
virsh vol-list file_virtimages

# Obtain information on the volume:
virsh vol-info /var/lib/libvirt/images/kvm1.img

# Start new KVM instance using the storage pool and volume
virt-install --name kvm1 --ram 1024 --graphics vnc,listen=146.20.141.158 --hvm --disk vol=file_virtimages/kvm1.img --import

virsh list --all
```



### Managing volumes

```shell
# List the available storage pools: 
virsh pool-list --all

# List the available volumes, that are a part of the storage pool:
virsh vol-list file_virtimages

# Create a new volume with the specified size:
virsh vol-create-as file_virtimages new_volume.img 9G

# List the volumes on the filesystem: 
ls -lah /var/lib/libvirt/images/
 
# Obtain information about the new volume: 
qemu-img info /var/lib/libvirt/images/new_volume.img
 
# Use the virsh command to get even more information:
virsh vol-info new_volume.img --pool file_virtimages

# Dump the volume configuration: 
virsh vol-dumpxml new_volume.img --pool file_virtimages
 
# Resize the volume and display the new size: 
virsh vol-resize new_volume.img 10G --pool file_virtimages
virsh vol-info new_volume.img --pool file_virtimages

# Delete the volume and list all available volumes in the storage pool: 
virsh vol-delete new_volume.img --pool file_virtimages
virsh vol-list file_virtimages

# Clone the existing volume: 
virsh vol-clone kvm1.img kvm2.img --pool file_virtimages
virsh vol-list file_virtimages


```



### Managing secrets

```shell
# List all available secrets:
virsh secret-list
```



```html
# Create the following secrets definition:
vim volume_secret.xml
<secret ephemeral='no'>
  <description>Passphrase for the iSCSI iscsi-target.linux-admins.net target server</description> 	   <usage type='iscsi'>
    <target>iscsi_secret</target>
  </usage>
</secret>
```



```shell
# Create the secret and ensure that it has been successfully created:
virsh secret-define volume_secret.xml
virsh secret-list

# Set a value for the secret:
virsh secret-set-value 7ad1c208c2c5-4723-8dc5-e2f4f576101a $(echo "some_password" | base64)
```



```html
# Create a new iSCSI pool definition file:
vim iscsi.xml
<pool type='iscsi'>
  <name>iscsi_virtimages</name>
  <source>
    <host name='iscsi-target.linux-admins.net'/>
    <device path='iqn2004-04.ubuntu:ubuntu16:iscsi.libvirtkvm'/>
    <auth type='chap' username='iscsi_user'>
      <secret usage='iscsi_secret'/>
    </auth>
  </source>
  <target>
    <path>/dev/disk/by-path</path>
  </target>
</pool>

```



## KVM Networking with libvirt



### The Linux bridge 

#### Book 



##### Load module

```shell
# check whether 802.1d Ethernet bridging options is enabled
cat /boot/config-`uname -r` | grep -i bridg

# verify that the module is loaded 
lsmod | grep bridge

# obtain more information about its version and features
modinfo bridge
```



##### Install linux bridge, Delete and Create new Virtual bridge, Add Vnet to bridge

```shell
sudo apt install bridge-utils
 
# Build a new KVM instance
virt-install --name kvm1 --ram 1024 --disk path=debian.img,format=raw --graphics vnc,listen=192.168.122.1 --noautoconsole --hvm --import
  
# List all the available bridge devices: 
brctl show

# Bring the virtual bridge down, delete it, and ensure that it's been deleted:
ifconfig virbr0 down
brctl delbr virbr0
brctl show

# Create a new bridge and bring it up: 
brctl addbr virbr0
brctl show
ifconfig virbr0 up

# Assign an IP address to bridge:
ip addr add 192.168.122.1 dev virbr0
ip addr show virbr0

# List the virtual interfaces on the host OS: 
ip a s | grep vnet

# Add the virtual interface vnet0 to the bridge:
sudo ip link add vnet0 type dummy
brctl addif virbr0 vnet0
brctl show virbr0

# Enable the Spanning Tree Protocol (STP) on bridge and obtain more information:
brctl stp virbr0 on
brctl showstp virbr0
```



* From inside the KVM instance,

  ```shell
  ssh KVM-instance
  
  # bring the interface up
  ifconfig eth0 up
  
  # request an IP address
  dhclient eth0
  
  # test connectivity to the host OS: 
  ip a s eth0
  ping 192.168.122.1 -c 3
  ```



##### Configuration file, manage service

```shell
# Linux bridge name and IP address defined in:
sudo cat /etc/libvirt/qemu/networks/default.xml

# dnsmasq service configuration specified:
sudo cat /var/lib/libvirt/dnsmasq/default.conf 

# See DHCP server is running on the host OS and it configuration
pgrep -lfa dnsmasq
virsh net-edit default
```



```shell
# examine the table of MAC addresses the bridge knows about
brctl showmacs virbr0
virsh console kvm1
ip a s eth0
```



When the bridge sees a frame on one of its ports, it records the time then after a set amount of time not seeing the same MAC address again, it will remove the record from the its CAM table,  We can set the time limit in seconds before the bridge will expire the MAC address entry by executing the following command: 

```shell
brctl setageing virbr0 600
```



##### Build the brctl from source

```shell
cd /usr/src/
apt-get update && apt-get install build-essential automake pkg-config git
git clone git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/bridge-utils.git
cd bridge-utils/
autoconf
./configure && make && make install
brctl --version

```



#### Site 

##### Method 1: Creating Bridge Network using Virtual Machine Manager (NATed)

Open Virtual Machine Manager, and go to **Edit > Connection Details > Virtual Networks**



[![virtual machine manager virtual networks](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-virtual-networks.png?ezimgfmt=rs:696x270/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)


Configure a new network interface by clicking the **+** at the bottom of the window. Give the virtual network a name.

[![virtual machine manager network name](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-network-name.png?ezimgfmt=rs:696x593/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

Click the Forward button, on next window, provide virtual network information.

[![virtual machine manager network information](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-network-information.png?ezimgfmt=rs:696x593/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

Click forward and choose if to enable IPv6.

[![virtual machine manager ipv6](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-ipv6.png?ezimgfmt=rs:696x593/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

Select the network type and forwarding policy.



[![virtual machine manager choose route](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-choose-route.png?ezimgfmt=rs:696x593/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

Finish the setting and save your configurations. The new Virtual network should show on the overview page.

[![virtual machine manager network created](https://computingforgeeks.com/wp-content/uploads/2019/04/virtual-machine-manager-network-created.png?ezimgfmt=rs:696x389/rscb23/ng:webp/ngcb23)](data:image/svg+xml,)

A bridge on the host system is automatically created for the network.

```
$ brctl show virbr4      
bridge name	bridge id		STP enabled	interfaces
virbr4		8000.525400c2410a	yes		virbr4-nic
```



##### Method 2: Create KVM bridge with virsh command.

Create a new bridge XML file.

```
vim br10.xml
```

Add bridge details to the file.

```
<network>
  <name>br10</name>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <bridge name='br10' stp='on' delay='0'/>
  <ip address='192.168.30.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.30.50' end='192.168.30.200'/>
    </dhcp>
  </ip>
</network>
```

To define a network from an XML file without starting it, use:



```
$ sudo virsh net-define  br10.xml
Network br1 defined from br10.xml
```

To start a (previously defined) inactive network, use:

```
$ sudo virsh net-start br10
Network br10 started
```

To set network to autostart at service start:

```
$ sudo virsh net-autostart br10
Network br10 marked as autostarted
```

Check to Confirm if autostart flag is turned to `yes` – Persistent should read yes as well.

```
$ sudo virsh net-list --all
 Name              State    Autostart   Persistent
----------------------------------------------------
 br10              active   yes         yes
 default           active   yes         yes
 docker-machines   active   yes         yes
 fed290            active   no          yes
 vagrant-libvirt   active   no          yes
```

Confirm bridge creation and IP address.

```
$ ip addr show dev br10
28: br10: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:94:00:f5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.30.1/24 brd 192.168.30.255 scope global br10
       valid_lft forever preferred_lft forever
```



##### Method 3: Create a bridge by editing network scripts (CentOS / RHEL / Fedora):

Below script will create a bridge called br10.

```
sudo vim /etc/sysconfig/network-scripts/ifcfg-br10
```

With:

```
DEVICE=br10
STP=no
TYPE=Bridge
BOOTPROTO=none
DEFROUTE=yes
NAME=br10
ONBOOT=yes
DNS1=8.8.8.8
DNS2=192.168.30.1
IPADDR=192.168.30.3
PREFIX=24
GATEWAY=192.168.30.1
```



The configuration of *eth0* interface that I’m bridging to will be:

```
$ cat /etc/sysconfig/network-scripts/ifcfg-eno1 
DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
BRIDGE=br10
```

Restart your network daemon.

```shell
sudo systemctl disable NetworkManager && sudo systemctl stop NetworkManager
sudo systemctl restart network.service
```



```
$ ip addr show dev br10
28: br10: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:94:00:f5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.30.1/24 brd 192.168.30.255 scope global br10
       valid_lft forever preferred_lft forever
```



##### Method 4: Create a bridge by editing network scripts (Debian / Ubuntu):

Configure Bridging interface:

```
$ sudo vim  /etc/network/interfaces
auto br10 
iface br10 inet static
address 192.168.1.10
network 192.168.1.1
netmask 255.255.255.0
broadcast 192.168.1.255
gateway 192.168.1.1
dns-nameservers 192.168.1.1
bridge_ports eth0
bridge_stp off
```

Disable all lines on eth0 interface section to look something like below:

```
auto eth0
iface eth0 inet manual
```

Restart your networking service.

```
 sudo systemctl restart networking.service
```



##### Method 5: Using Nmcli tool

Use the `nmcli` network management command line tool to  create a Linux bridge on the desired interface. Let’s first list all  available connections.

```
$ sudo nmcli connection show 
NAME                UUID                                  TYPE      DEVICE 
enp1s0              498869bb-0d88-4a4c-a83a-c491d1040b0b  ethernet  enp1s0 
Wired connection 1  0977f29f-fa2e-3d7f-831c-6f41f8782be3  ethernet  enp7s0 
```

Since my bridge will be created on the second device `enp7s0`, I’ll delete the existing connection then create a bridge with this device.

```
$ sudo nmcli connection delete 0977f29f-fa2e-3d7f-831c-6f41f8782be3
Connection 'Wired connection 1' (0977f29f-fa2e-3d7f-831c-6f41f8782be3) successfully deleted.
```

`1.` Save bridge related information to variables.

```
BR_NAME="br10"
BR_INT="enp7s0"
SUBNET_IP="192.168.30.10/24"
GW="192.168.30.1"
DNS1="8.8.8.8"
DNS2="8.8.4.4"
```

Where:

- **BR_NAME**: The name of the bridge to be created.
- **BR_INT**: the physical network device to be used as bridge slave.
- **SUBNET_IP**: IP address and subnet assigned to the bridge created.
- **GW**: The IP address of the default gateway
- **DNS1** and **DNS2**: IP addresses of DNS servers to be used.

`2.` Define new bridge connection.

```
sudo nmcli connection add type bridge autoconnect yes con-name ${BR_NAME} ifname ${BR_NAME}
```

Output:

```
Connection 'br0' (be6d4520-0257-49c6-97c2-f515d6554980) successfully added.
```

`3.` Modify bridge to add IP address, Gateway and DNS

```
sudo nmcli connection modify ${BR_NAME} ipv4.addresses ${SUBNET_IP} ipv4.method manual
sudo nmcli connection modify ${BR_NAME} ipv4.gateway ${GW}
sudo nmcli connection modify ${BR_NAME} ipv4.dns ${DNS1} +ipv4.dns ${DNS2}
```

`4.` Add the network device as bridge slave.

```
sudo nmcli connection delete ${BR_INT}
sudo nmcli connection add type bridge-slave autoconnect yes con-name ${BR_INT} ifname ${BR_INT} master ${BR_NAME}
```

Sample output.

```
Connection 'enp7s0' (f033dbc9-a90e-4d4c-83a9-63fd7ec1cdc1) successfully added.
```

Check connections.

```
$ sudo nmcli connection show 
NAME    UUID                                  TYPE      DEVICE 
br0     be6d4520-0257-49c6-97c2-f515d6554980  bridge    br0    
enp1s0  498869bb-0d88-4a4c-a83a-c491d1040b0b  ethernet  enp1s0 
enp7s0  f033dbc9-a90e-4d4c-83a9-63fd7ec1cdc1  ethernet  enp7s0 
```

#### Step 2: Bring up network bridge

Once the network bridge connection has been created, bring it up.

```
$ sudo nmcli connection up br10
Connection successfully activated (master waiting for slaves) (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)
```

View bridge details by running.

```
sudo nmcli connection show br10
```

The `ip addr` command should give output similar to below.

```
$ ip ad
3: enp7s0:  mtu 1500 qdisc fq_codel master br10 state UP group default qlen 1000
     link/ether 52:54:00:a2:f6:a8 brd ff:ff:ff:ff:ff:ff
 4: br10:  mtu 1500 qdisc noqueue state UP group default qlen 1000
     link/ether 52:54:00:a2:f6:a8 brd ff:ff:ff:ff:ff:ff
     inet 192.168.122.10/24 brd 192.168.122.255 scope global noprefixroute br10
        valid_lft forever preferred_lft forever
     inet6 fe80::4f2f:ce6d:dc6b:2101/64 scope link noprefixroute 
        valid_lft forever preferred_lft forever
```

Congratulations!!. You have successfully created and configured Bridge Networking for KVM  on a Linux system. Check KVM related articles below.





### The Open vSwitch	

#### Remove Linux bridge, Install OVS, Add Vnet to OVS

```shell
# Remove the existing Linux bridge
brctl show
ifconfig virbr0 down
brctl delbr virbr0
brctl show

# unload the kernel module for the Linux bridge before using OVS
root@kvm:/usr/src# sudo modprobe -r bridge

# Install the OVS package on Ubuntu: 
sudo apt-get install openvswitch-switch -y
 
# Ensure that the OVS processes are running: 
pgrep -lfa switch

# Ensure that the OVS kernel module has been loaded: 
lsmod | grep switch

# List the available OVS switches: 
sudo ovs-vsctl show

# Create a new OVS switch: 
sudo ovs-vsctl add-br virbr1
sudo ovs-vsctl show

# Add the interface of the running KVM instance to the OVS switch:
sudo ovs-vsctl add-port virbr1 vnet0
sudo ovs-vsctl show

# Configure an IP address on the OVS switch: 
sudo ip addr add 192.168.122.1/24 dev virbr1
ip addr show virbr1
 
# Configure an IP address inside the KVM guest
virsh console kvm1
ifconfig eth0 up && ip addr add 192.168.122.210/24 dev eth0
ip addr show eth0
ping 192.168.122.1

# query to database engine
sudo ovsdb-client list-dbs
sudo ovsdb-client list-tables
```



#### Remove OVS Vnet, Delete OVS switch

```shell
# To remove the KVM virtual interface from the OVS switch
ovs-vsctl del-port virbr1 vnet0

# To completely delete the OVS switch
ovs-vsctl del-br virbr1 && ovs-vsctl show e5164e3e-7897-4717-b766-eae1918077b0
```



### Configuring NAT forwarding network



#### How to do it

```shell
# List all available networks: 
virsh net-list --all

# Dump the configuration of the default network:
virsh net-dumpxml default

# Compare that with the XML definition file for the default network: 
cat /etc/libvirt/qemu/networks/default.xml

# List all running instances on the host: 
virsh list --all

# Ensure that the KVM instances are connected to the default Linux bridge: 
brctl show
```



```html
# Create a new NAT network definition:
vim nat_net.xml
<network>
  <name>nat_net</name>
  <bridge name="virbr1"/>
  <forward/>
  <ip address="10.10.10.1" netmask="255.255.255.0">
    <dhcp>
      <range start="10.10.10.2" end="10.10.10.254"/>
    </dhcp>
  </ip>
</network>
```



```shell
# Define the new network:
virsh net-define nat_net.xml
virsh net-list --all

# Start the new network and enable autostarting
virsh net-start nat_net
virsh net-autostart nat_net
virsh net-list

# Obtain more information about the new network: 
virsh net-info nat_net

# Edit the XML definition of the kvm1 instance and change the name of the source network:  
virsh edit kvm1
  ...
  <interface type='network'>
    ...
    <source network='nat_net'/>
    ...
  </interface>
...

# Restart the KVM guest:
virsh destroy kvm1
virsh start kvm1

# List all software bridges on the host: 
brctl show
```



```shell
# Connect to the KVM instances and check the IP address of the eth0 interface
virsh console kvm1
ip a s eth0 | grep inet
ifconfig eth0 up && dhclient eth0
ping 10.10.10.1 -c 3
```



```shell
# On the host OS, examine which DHCP services are running: 
pgrep -lfa dnsmasq

# Check the IP of the new bridge interface: 
ip a s virbr1

# List the iptables rules for the NAT table: 
iptables -L -n -t nat
```



### Configuring bridged network

```shell
ifdown eth1

# Edit the network configuration file - Debian/Ubuntu: 
vim /etc/network/interfaces
autovirbr2
iface virbr2 inet static
	address 192.168.1.2
	netmask 255.255.255.0
	network 192.168.1.0
	broadcast 192.168.1.255
	gateway 192.168.1.1
	bridge_ports eth1
	
# Edit the network configuration file -  RedHat/CentOS
vim /etc/sysconfig/ifcfg-eth1
DEVICE=eth1
NAME=eth1
NM_CONTROLLED=yes
ONBOOT=yes
TYPE=Ethernet
BRIDGE=virbr2

vim /etc/sysconfig/ifcfg-bridge_net
DEVICE=virbr2
NAME=virbr2
NM_CONTROLLED=yes
ONBOOT=yes
TYPE=Bridge
STP=on
IPADDR=192.168.1.2
NETMASK=255.255.255.0
GATEWAY=192.168.1.1

# Start the new interface up:
ifup virbr2

# Disable sending packets to iptables that originate from the guest VMs: 
sysctl -w net.bridge.bridge-nf-call-iptables=0  # net.bridge.bridge-nf-call-iptables = 0
sysctl -w net.bridge.bridge-nf-call-iptables=0  # net.bridge.bridge-nf-call-iptables = 0
sysctl -w net.bridge.bridge-nf-call-arptables=0 # net.bridge.bridge-nf-call-arptables = 0

# List all bridges on the host: 
brctl show

# Edit the XML definition for the KVM instance:
virsh edit kvm1
...
	<interface type='bridge'>
		<source bridge='virbr2'/>
	</interface>
...

# Restart the KVM instance: 
virsh destroy kvm1
virsh start kvm1
```



### Configuring PCI passthrough network

```shell
# Enumerate all devices on the host OS: 
virsh nodedev-list --tree

# List all PCI Ethernet adapters:
lspci | grep Ethernet

# Obtain more information about NIC that the eth1 device is using:
virsh nodedev-dumpxml pci_0000_03_00_1

# Convert the domain, bus, slot, and function values to hexadecimal:
printf %x 0
printf %x 3
printf %x 0
printf %x 1

# Create a new libvirt network definition file: 
vim passthrough_net.xml
<network>
	<name>passthrough_net</name>
	<forward mode='hostdev' managed='yes'>
		<pf dev='eth1'/>
	</forward>
</network>

# Define, start, and enable autostarting on the new libvirt network: 
virsh net-define passthrough_net.xml
virsh net-start passthrough_net
virsh net-autostart passthrough_net
virsh net-list

# Edit the XML definition for the KVM guest:
 virsh edit kvm1
 ...
<devices>
	...
	<interface type='hostdev' managed='yes'>
		<source>
			<address type='pci' domain='0x0' bus='0x00'slot='0x07' function='0x0'/>
		</source>
		<virtualport type='802.1Qbh' />
	</interface>
	<interface type='network'>
		<source network='passthrough_net'>
	</interface>
	...
</devices>
...

# Restart the KVM instance:
virsh destroy kvm1
virsh start kvm1

# List the Virtual Functions (VFs) provided by SR-IOV NIC: 
virsh net-dumpxml passthrough_net
```



### Manipulating network interfaces

```xml
# Create a new bridge interface configuration file: 
vim test_bridge.xml
<interface type='bridge' name='test_bridge'>
	<start mode="onboot"/>
	<protocol family='ipv4'>
		<ip address='192.168.1.100' prefix='24'/>
	</protocol>
	<bridge>
		<interface type='ethernet' name='vnet0'>
		<mac address='fe:54:00:55:9b:d6'/>
</interface>
</bridge>
</interface>
```



```shell
# Define the new interface: 
virsh iface-define test_bridge.xml
virsh iface-list --all

# Start the new bridge interface: 
virsh iface-start test_bridge
virsh iface-list --all | grep test_bridge

# List all bridge devices on the host:
brctl show

# Check the active network configuration of the new bridge: 
ip a s test_bridge

# Obtain the MAC address of bridge: 
virsh iface-mac test_bridge

# Obtain the name of the bridge based by providing its MAC address:
 virsh iface-name 4a:1e:48:e1:e7:de
 
# Destroy the interface, as follows: 
virsh iface-destroy test_bridge
virsh iface-list --all | grep test_bridge
virsh iface-undefine test_bridge
virsh iface-list --all | grep test_bridge
```



## KVM Libvirt Storage Pools

### Types of storage pools

1. **Directory pool**: format types such as raw, qcow, qcow2, dmg, vmdk, vpc or ISO images.
2. **Filesystem pool**: Use a block device (E.g. partition or LVM group) .
3. **Network filesystem pool** - Use a network filesystem (E.g. `cifs`, `glusterfs`, `nfs` etc.) 
4. **Logical volume pool** - Use an LVM volume group as a pool for storing volumes.
5. **Disk pool** - Use a physical disk as a pool. The volumes can be created by adding partitions to the disk.
6. **iSCSI pool** - Use an iSCSI target to store volumes. All volumes should be pre-allocated on the iSCSI server.
7. iSCSI direct pool - This is a variant of the iSCSI pool. Instead of using iscsiadm, it uses `libiscsi`. It requires a host, a path which is the target IQN, and an initiator IQN.
8. SCSI pool - Use an SCSI host bus adapter in almost the same way as an iSCSI target.
9. RBD pool - This storage driver provides a pool which contains all RBD  images in a RADOS pool. RBD (RADOS Block Device) is part of the Ceph  distributed storage project.
10. Sheepdog pool - Use Sheepdog Cluster as a pool to store volumes.
11. Gluster pool - Use Gluster distributed file system as a pool.
12. ZFS pool - Use ZFS filesystem as a pool.
13. Vstorage pool - Use Virtuozzo distributed software-defined storage as a pool.



### Change KVM Libvirt Default Storage Pool Location

Default location is `/var/lib/libvirt/images/` for images.

* Tools to change default location
  1. `virsh` command line program.
  2. graphical `Virt-manager` 
  3. **Cockpit** web console.

#### Change KVM Libvirt default storage pool location using virsh program

*  power off all running guests.

```shell
virsh list --all
virsh shutdown <vm-name>
```



* List all the configured storage pools in your KVM host machine:

```she
virsh pool-list 
```



* view the details of the default storage

```shell
virsh pool-info default
```



* display the path of the default storage pool

```shell
virsh pool-dumpxml default | grep -i path
```



* Stop and undefine the default storage pool 

```shell
virsh pool-destroy default
virsh pool-undefine default
```



* If there is no default Storage pool exists for any reason, you can create one

```shell
virsh pool-define-as --name default --type dir --target /NEW/PATH/FOR/images
```



* Edit the default storage pool
* create it and assign sufficient permission to the new path directory

```shell
virsh pool-edit default 
	...
	<path>/NEW/PATH/FOR/images</path>
	...

```



* Finally, start the default storage pool:

```shell
virsh pool-start default
```



* Set storage pool to start automatically on system boot:

```shell
virsh pool-autostart default
```



* Verify if the libvirt storage pool path has been changed or not with command:

```shell
virsh pool-dumpxml default | grep -i path
```



* Check the storage pool state:

```shell
virsh pool-list 
```



* Restart libvirtd service:

```shell
sudo systemctl restart libvirtd
```



*  We need to do one last thing. Copy all VM images from old storage path to the new one:

```shell
sudo mv /var/lib/libvirt/images/archlinux.qcow2 /NEW/PATH/FOR/images
```



#### Change KVM Libvirt default storage pool location using Virt-manager

* Open Virt-manager application. Right click on QEMU/KVM and click **Details** option.
* View KVM connection details

[![View KVM connection details](https://ostechnix.com/wp-content/uploads/2021/06/View-KVM-connection-details.png)](https://ostechnix.com/wp-content/uploads/2021/06/View-KVM-connection-details.png)   



You can also click **Edit-> Connection details** from the Virt-manager interface. 

* Under the **Storage** section, you will see the default storage pool location.

[![KVM Libvirt default storage pool location](https://ostechnix.com/wp-content/uploads/2021/06/KVM-Libvirt-default-storage-pool-location.png)](https://ostechnix.com/wp-content/uploads/2021/06/KVM-Libvirt-default-storage-pool-location.png)KVM Libvirt default storage pool location

* Click **Stop Pool** and then **Delete Pool** options in the bottom left pane.

[![Stop and delete KVM Libvirt default storage pool](https://ostechnix.com/wp-content/uploads/2021/06/Stop-and-delete-KVM-Libvirt-default-storage-pool.png)](https://ostechnix.com/wp-content/uploads/2021/06/Stop-and-delete-KVM-Libvirt-default-storage-pool.png)Stop and delete KVM Libvirt default storage pool



* Click the **plus (+)** sign on the bottom left pane to create a new storage pool for use by the virtual machines.

Enter the name for the storage pool (E.g. `default` in my case). Choose the type of the pool. In our case, I have selected **Filesystem Directory**. Specify the target location and click Finish.

[![Create new KVM Libvirt storage pool](https://ostechnix.com/wp-content/uploads/2021/06/Create-new-KVM-Libvirt-storage-pool.png)](https://ostechnix.com/wp-content/uploads/2021/06/Create-new-KVM-Libvirt-storage-pool.png)Create new KVM Libvirt storage pool

* Now the new Storage is active. Check the **Autostart** box to automatically start the new storage pool at system boot.

[![New KVM Libvirt storage pool location](https://ostechnix.com/wp-content/uploads/2021/06/New-KVM-Libvirt-storage-pool-location.png)](https://ostechnix.com/wp-content/uploads/2021/06/New-KVM-Libvirt-storage-pool-location.png)New KVM Libvirt storage pool location

* Move all the VM images from the old storage directory to the new one.

```
$ sudo mv /var/lib/libvirt/images/archlinux.qcow2 /home/sk/.local/share/libvirt/images/
```

**1.2.7.** Finally, restart libvirtd service:

```
$ sudo systemctl restart libvirtd
```



#### Troubleshooting

`Cannot access storage file, Permission denied Error in KVM Libvirt`



Today, I started my Arch Linux virtual machine using `virsh start` command and ended up with this error - `Failed to start domain 'Archlinux_default' error: Cannot access storage file  '/home/sk/.local/share/libvirt/images/Archlinux_default.img' (as  uid:107, gid:107): Permission denied`. It is actually a [Vagrant](https://ostechnix.com/vagrant-tutorial-getting-started-with-vagrant/) machine created with KVM Libvirt provider.

Then, I tried again to start the VM using `vagrant up` command. It also displayed the same error.

  

```
 Bringing machine 'default' up with 'libvirt' provider…
 ==> default: Checking if box 'archlinux/archlinux' version '20210601.24453' is up to date…
 ==> default: Starting domain.
 There was an error talking to Libvirt. The error message is shown
 below:
 Call to virDomainCreateWithFlags failed: Cannot access storage file '/home/sk/.local/share/libvirt/images/Archlinux_default.img' (as uid:107, gid:107): Permission denied
```

[![Failed to start domain, cannot access storage file, permission denied error in vagrant, virsh command](https://ostechnix.com/wp-content/uploads/2021/06/Failed-to-start-domain-cannot-access-storage-file-permission-denied-error-in-vagrant-virsh-command.png)](https://ostechnix.com/wp-content/uploads/2021/06/Failed-to-start-domain-cannot-access-storage-file-permission-denied-error-in-vagrant-virsh-command.png)Failed to start domain, cannot access storage file, permission denied error

Just to be sure, I tried one more time to start the VM from [Virt-manager](https://ostechnix.com/how-to-manage-kvm-virtual-machines-with-virt-manager/) GUI application. This time also it did return the same error.

[![Failed to start domain, cannot access storage file, permission denied error in virt-manager](https://ostechnix.com/wp-content/uploads/2021/06/Failed-to-start-domain-cannot-access-storage-file-permission-denied-error-in-virt-manager.png)](https://ostechnix.com/wp-content/uploads/2021/06/Failed-to-start-domain-cannot-access-storage-file-permission-denied-error-in-virt-manager.png)Failed to start domain, cannot access storage file, permission denied error in virt-manager

All the error messages explicitly says that the the `qemu` user does not have read permission to the Libvirt storage directory.

In this brief tutorial, allow me to show you how to fix "error: Failed to  start domain ... error: Cannot access storage file .... (as uid:107,  gid:107): Permission denied" in KVM Libvirt.

##### Fix "Cannot access storage file, Permission denied Error" in KVM Libvirt

This is one of the common KVM Libvirt error. This error will usually occur after **[changing path of the Libvirt's default storage directory](https://ostechnix.com/how-to-change-kvm-libvirt-default-storage-pool-location/)**. 

##### Method 1:

**Step 1:** Edit `/etc/libvirt/qemu.conf` file:

```
$ sudo nano /etc/libvirt/qemu.conf
```

**Step 2:** Find the `user` and `group` directives. By default, both are set to `"root"`.

```
 [...] 
 Some examples of valid values are:
 #
 user = "qemu"   # A user named "qemu"
 user = "+0"     # Super user (uid=0)
 user = "100"    # A user named "100" or a user with uid=100
 #
 #user = "root"
 The group for QEMU processes run by the system instance. It can be
 specified in a similar way to user.
 #group = "root"
 [...]
```

Uncomment both lines and replace `root` with your username and group with `libvirt` as shown below:

```
 [...] 
 Some examples of valid values are:
 #
 user = "qemu"   # A user named "qemu"
 user = "+0"     # Super user (uid=0)
 user = "100"    # A user named "100" or a user with uid=100
 #
 user = "sk"
 The group for QEMU processes run by the system instance. It can be
 specified in a similar way to user.
 group = "libvirt"
 [...]
```

[![Configure user and group for kvm libvirt](https://ostechnix.com/wp-content/uploads/2021/06/Configure-user-and-group-for-kvm-libvirt.png)](https://ostechnix.com/wp-content/uploads/2021/06/Configure-user-and-group-for-kvm-libvirt.png)Configure user and group for kvm libvirt

Press `CTRL+O` and press `ENTER` to save the changes and press `CTRL+X` to exit the file.

**Step 3:** Restart `libvirtd` service:

```
$ sudo systemctl restart libvirtd
```

**Step 4:** Please make sure the user is a member of the `libvirt` group. If not, add the user to `libvirt` group using command:

```
$ sudo usermod -a -G libvirt $(whoami)
```

**Step 5:** Finally start the VM:

```
$ virsh start
```

If you prefer to use vagrant, run this instead:

```
$ vagrant up
```

This time the Virtual machine should start.

**Step 6:** Check the VM status:

```
$ virsh list
```

Or,

```
$ vagrant status
```

[![Check kvm libvirt virtual machine status](https://ostechnix.com/wp-content/uploads/2021/06/Check-kvm-libvirt-virtual-machine-status.png)](https://ostechnix.com/wp-content/uploads/2021/06/Check-kvm-libvirt-virtual-machine-status.png)Check kvm libvirt virtual machine status

##### Method 2:

The another to way to fix KVM Libvirt permission issue is by setting proper ACL permission to the Libvirt storage pool directory. In my case, my  storage pool directory is located in `$HOME` directory.

**Step 1:** Let us get the current ACL permissions to the `$HOME` directory.

```
$ sudo getfacl -e /home/sk/
```

**Sample output:**

```
 getfacl: Removing leading '/' from absolute path names
 file: home/sk/
 owner: sk
 group: sk
 user::rwx
 user:qemu:--x            #effective:--x
 group::---            #effective:---
 mask::--x
 other::---
```

As you see in the above output, the `qemu` user doesn't has **read** permission to the storage pool location. In some distributions, the user name might be `libvirt-qemu`.

**Step 2:** Set the read and executable permission for the user `qemu` using command:

```
$ sudo setfacl -m u:qemu:rx /home/sk/
```

Replace `qemu` and `/home/sk/` with your own.

Now, the qemu user has read and executable permission over the storage pool directory. You can verify it using command:

```
$ sudo getfacl -e /home/sk/
```

**Sample output:**

```
 getfacl: Removing leading '/' from absolute path names
 file: home/sk/
 owner: sk
 group: sk
 user::rwx
 user:qemu:r-x            #effective:--x
 group::---            #effective:---
 mask::--x
 other::---
```

**Step 3:** Restart libvirtd service:

```
$ sudo systemctl restart libvirtd
```

Now the Libvirt guest machines will start without any issue.



## Provision VMs on KVM with Terraform

### Install Terraform

```
# Debian / Ubuntu systems
sudo apt update
sudo apt install wget curl unzip

# RHEL based systems
sudo yum install curl wget unzip
```



Download terraform

```
TER_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest | grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_amd64.zip
```



extract and move *terraform* binary file to the **/usr/local/bin** directory.

```
unzip terraform_${TER_VER}_linux_amd64.zip
sudo mv terraform /usr/local/bin/

which terraform
terraform --version
```



### Install Terraform KVM provider

```shell
vim main.tf
terraform {
  required_providers {
    libvirt = {
      source = "dmacvicar/libvirt"
    }
  }
}

provider "libvirt" {
  # Configuration options
}
```



```shell
terraform init
cd ~/.terraform.d
mkdir plugins
```



### Install Terraform KVM provider on Linux

*Linux 64-bit system:*

```
curl -s https://api.github.com/repos/dmacvicar/terraform-provider-libvirt/releases/latest \
  | grep browser_download_url \
  | grep linux_amd64.zip \
  | cut -d '"' -f 4 \
  | wget -i -
```



Extract the file downloaded:

```
# 64-bit Linux
unzip terraform-provider-libvirt_*_linux_amd64.zip
rm -f terraform-provider-libvirt_*_linux_amd64.zip
```



Move `terraform-provider-libvirt` binary file to the `~/.terraform.d/plugins `directory.

```
mkdir -p ~/.terraform.d/plugins/
mv terraform-provider-libvirt_* ~/.terraform.d/plugins/terraform-provider-libvirt
```



### Using Terraform To Provision VMs on KVM

```
mkdir -p ~/projects/terraform
cd ~/projects/terraform
```



For automatic installation of KVM Provider, define like below:



```
$ vim main.tf
terraform {
  required_providers {
    libvirt = {
      source = "dmacvicar/libvirt"
    }
  }
}

provider "libvirt" {
  ## Configuration options
  uri = "qemu:///system"
  #alias = "server2"
  #uri   = "qemu+ssh://root@192.168.100.10/system"
}
```



Thereafter, run terraform init command to initialize the environment:

```
$ terraform init
```



We can now create `libvirt.tf` file for your VM deployment on KVM.



```shell
vim libvirt.tf
# Defining VM Volume
resource "libvirt_volume" "centos7-qcow2" {
  name = "centos7.qcow2"
  pool = "default" # List storage pools using virsh pool-list
  source = "https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2"
  #source = "./CentOS-7-x86_64-GenericCloud.qcow2"
  format = "qcow2"
}

# Define KVM domain to create
resource "libvirt_domain" "centos7" {
  name   = "centos7"
  memory = "2048"
  vcpu   = 2

  network_interface {
    network_name = "default" # List networks with virsh net-list
  }

  disk {
    volume_id = "${libvirt_volume.centos7-qcow2.id}"
  }

  console {
    type = "pty"
    target_type = "serial"
    target_port = "0"
  }

  graphics {
    type = "spice"
    listen_type = "address"
    autoport = true
  }
}

# Output Server IP
output "ip" {
  value = "${libvirt_domain.centos7.network_interface.0.addresses.0}"
}
```



Generate and show Terraform execution plan



```
terraform plan
```



Then build your Terraform infrastructure if desired state is confirmed to be correct.



```
 terraform apply
 ...
 Enter a value: yes
```



Press “**yes**” to confirm execution. Below is my terraform execution output.

Confirm VM creation with `virsh` command.

```
$ sudo virsh  list
 Id   Name       State
--------------------------
 7    centos7    running
```



et Instance IP address.

```
$ sudo virsh net-dhcp-leases default 
 Expiry Time           MAC address         Protocol   IP address           Hostname   Client ID or DUID
------------------------------------------------------------------------------------------------------------------------------------------------
 2019-03-24 16:11:18   52:54:00:3e:15:9e   ipv4       192.168.122.61/24    -          -
 2019-03-24 15:30:18   52:54:00:8f:8c:86   ipv4       192.168.122.198/24   rhel8      ff:61:69:21:bd:00:02:00:00:ab:11:0e:9c:c6:63:ee:7d:c8:d1
```

My instance IP is `192.168.122.61`. I can ping the instance.

```
$  ping -c 1 192.168.122.61 
PING 192.168.122.61 (192.168.122.61) 56(84) bytes of data.
64 bytes from 192.168.122.61: icmp_seq=1 ttl=64 time=0.517 ms

--- 192.168.122.61 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.517/0.517/0.517/0.000 ms
```

To destroy your infrastructure, run:



```
$ terraform destroy
...
Enter a value: yes
```



### Using cloud-init with Terraform Libvirt provider

we can use [libvirt_cloudinit_disk](https://github.com/dmacvicar/terraform-provider-libvirt/blob/master/website/docs/r/cloudinit.html.markdown) resource to pass user data to the instance.

Create Cloud init configuration file.



```
$ vim cloud_init.cfg
#cloud-config
# vim: syntax=yaml
#
# ***********************
# 	---- for more examples look at: ------
# ---> https://cloudinit.readthedocs.io/en/latest/topics/examples.html
# ******************************
#
# This is the configuration syntax that the write_files module
# will know how to understand. encoding can be given b64 or gzip or (gz+b64).
# The content will be decoded accordingly and then written to the path that is
# provided.
#
# Note: Content strings here are truncated for example purposes.
ssh_pwauth: True
chpasswd:
  list: |
     root: StrongRootPassword
  expire: False

users:
  - name: jmutai # Change me
    ssh_authorized_keys:
      - ssh-rsa AAAAXX #Chageme
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    shell: /bin/bash
    groups: wheel
```

- This will set root password to `StrongRootPassword`
- Add user named `jmutai` with specified Public SSH keys
- The user will be added to wheel group and be allowed to run sudo commands without password.

Edit `libvirt.tf` to use Cloud init configuration file.



```
# Defining VM Volume
resource "libvirt_volume" "centos7-qcow2" {
  name = "centos7.qcow2"
  pool = "default"
  source = "https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2"
  #source = "./CentOS-7-x86_64-GenericCloud.qcow2"
  format = "qcow2"
}

# get user data info
data "template_file" "user_data" {
  template = "${file("${path.module}/cloud_init.cfg")}"
}

# Use CloudInit to add the instance
resource "libvirt_cloudinit_disk" "commoninit" {
  name = "commoninit.iso"
  pool = "default" # List storage pools using virsh pool-list
  user_data      = "${data.template_file.user_data.rendered}"
}

# Define KVM domain to create
resource "libvirt_domain" "centos7" {
  name   = "centos7"
  memory = "2048"
  vcpu   = 2

  network_interface {
    network_name = "default"
  }

  disk {
    volume_id = "${libvirt_volume.centos7-qcow2.id}"
  }

  cloudinit = "${libvirt_cloudinit_disk.commoninit.id}"

  console {
    type = "pty"
    target_type = "serial"
    target_port = "0"
  }

  graphics {
    type = "spice"
    listen_type = "address"
    autoport = true
  }
}

# Output Server IP
output "ip" {
  value = "${libvirt_domain.centos7.network_interface.0.addresses.0}"
}
```

Re-initialize Terraform working directory.



```
$ terraform init
```



Then create the Virtual Machine and its resources using apply command:



```
terraform plan
terraform apply
```



Or use `virsh` command to get the server IP address.

```
$ sudo virsh net-dhcp-leases default
 Expiry Time           MAC address         Protocol   IP address           Hostname   Client ID or DUID
---------------------------------------------------------------------------------------------------------
 2019-03-24 16:41:32   52:54:00:22:45:57   ipv4       192.168.122.219/24   -          -
```

Try login to the instance as root user and password set.



Check if ssh user created can login with SSH key and run sudo without password.



```
$ ssh jmutai@192.168.122.219
```



## Migrating KVM Instances



## Using Python to Build and Manage KVM Instances 

```shell
# see that the virsh command uses various libvirt shared libraries
ldd /usr/bin/virsh | grep libvirt

# list of functions, classes, and methods that the Python libvirt module provides,
pydoc libvirt
```



### Installing and using the Python libvirt library

```shell
# Install the Python development packages pip and virtualenv : 
apt-get install python-pip python-dev pkg-config build-essential autoconf libvirt-dev
pip install virtualenv

# Create a new Python virtual environment and activate it: 
mkdir kvm_python
virtualenv kvm_python/
source kvm_python/bin/activate

# Install the libvirt module: 
pip install libvirt-python
pip freeze
python --version

# Install iPython and start it:
apt-get install ipython
ipython
```



### Defining KVM instances with Python

```python
import libvirt
```



```xml
 xmlconfig = """

<domain type='kvm' id='1'>
	<name>kvm_python</name>
	<memory unit='KiB'>1048576</memory>
	<currentMemory unit='KiB'>1048576</currentMemory>
	<vcpu placement='static'>1</vcpu>
	<resource>
		<partition>/machine</partition>
	</resource>
	<os>
		<type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		<boot dev='hd'/>
	</os>
	<features>
		<acpi/>
		<apic/>
		<pae/>
	</features>
	<clock offset='utc'/>
	<on_poweroff>destroy</on_poweroff>
	<on_reboot>restart</on_reboot>
	<on_crash>restart</on_crash>
	<devices>
		<emulator>/usr/bin/qemu-system-x86_64</emulator>
		<disk type='file' device='disk'>
			<driver name='qemu' type='raw'/>
			<source file='/tmp/debian.img'/>
			<backingStore/>
			<target dev='hda' bus='ide'/>
			<alias name='ide0-0-0'/>
			<address type='drive' controller='0' bus='0' target='0'
unit='0'/>
		</disk>
		<controller type='usb' index='0'>
			<alias name='usb'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x01'
function='0x2'/>
		</controller>
		<controller type='pci' index='0' model='pci-root'>
			<alias name='pci.0'/>
		</controller>
		<controller type='ide' index='0'>
			<alias name='ide'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x01'
function='0x1'/>
		</controller>
		<interface type='network'>
			<mac address='52:54:00:da:02:01'/>
			<source network='default' bridge='virbr0'/>
			<target dev='vnet0'/>
			<model type='rtl8139'/>
			<alias name='net0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x03'
function='0x0'/>
		</interface>
		<serial type='pty'>
			<source path='/dev/pts/5'/>
			<target port='0'/>
			<alias name='serial0'/>
		</serial>
		<console type='pty' tty='/dev/pts/5'>
			<source path='/dev/pts/5'/>
			<target type='serial' port='0'/>
			<alias name='serial0'/>
		</console>
		<input type='mouse' bus='ps2'/>
		<input type='keyboard' bus='ps2'/>
		<graphics type='vnc' port='5900' autoport='yes'
listen='0.0.0.0'>
			<listen type='address' address='0.0.0.0'/>
		</graphics>
		<video>
			<model type='cirrus' vram='16384' heads='1'/>
			<alias name='video0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x02'
function='0x0'/>
		</video>
		<memballoon model='virtio'>
			<alias name='balloon0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x04'
function='0x0'/>
		</memballoon>
	</devices>
</domain>
"""

 xmlconfig = """
<domain type='kvm'>
  <name>UbuS16-2</name>
  <uuid>8dc4e848-24d7-4f03-97cc-795e7d61ac50</uuid>
  <metadata>
    <libosinfo:libosinfo xmlns:libosinfo="http://libosinfo.org/xmlns/libvirt/domain/1.0">
      <libosinfo:os id="http://ubuntu.com/ubuntu/16.04"/>
    </libosinfo:libosinfo>
  </metadata>
  <memory unit='KiB'>1048576</memory>
  <currentMemory unit='KiB'>1048576</currentMemory>
  <vcpu placement='static'>2</vcpu>
  <os>
    <type arch='x86_64' machine='pc-i440fx-5.2'>hvm</type>
    <boot dev='hd'/>
  </os>
  <features>
    <acpi/>
    <apic/>
    <vmport state='off'/>
  </features>
  <cpu mode='host-model' check='partial'/>
  <clock offset='utc'>
    <timer name='rtc' tickpolicy='catchup'/>
    <timer name='pit' tickpolicy='delay'/>
    <timer name='hpet' present='no'/>
  </clock>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <pm>
    <suspend-to-mem enabled='no'/>
    <suspend-to-disk enabled='no'/>
  </pm>
  <devices>
    <emulator>/usr/bin/qemu-system-x86_64</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/home/hoji/.local/share/libvirt/images/UbuS16-1.qcow2'/>
      <target dev='vda' bus='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </disk>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <target dev='hda' bus='ide'/>
      <readonly/>
      <address type='drive' controller='0' bus='0' target='0' unit='0'/>
    </disk>
    <controller type='usb' index='0' model='ich9-ehci1'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x7'/>
    </controller>
    <controller type='usb' index='0' model='ich9-uhci1'>
      <master startport='0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0' multifunction='on'/>
    </controller>
    <controller type='usb' index='0' model='ich9-uhci2'>
      <master startport='2'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x1'/>
    </controller>
    <controller type='usb' index='0' model='ich9-uhci3'>
      <master startport='4'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x2'/>
    </controller>
    <controller type='pci' index='0' model='pci-root'/>
    <controller type='ide' index='0'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
    </controller>
    <controller type='virtio-serial' index='0'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
    </controller>
    <interface type='user'>
      <mac address='52:54:00:5f:5c:28'/>
      <model type='virtio'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </interface>
    <serial type='pty'>
      <target type='isa-serial' port='0'>
        <model name='isa-serial'/>
      </target>
    </serial>
    <console type='pty'>
      <target type='serial' port='0'/>
    </console>
    <channel type='spicevmc'>
      <target type='virtio' name='com.redhat.spice.0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>
    <input type='tablet' bus='usb'>
      <address type='usb' bus='0' port='1'/>
    </input>
    <input type='mouse' bus='ps2'/>
    <input type='keyboard' bus='ps2'/>
    <graphics type='spice' autoport='yes'>
      <listen type='address'/>
      <image compression='off'/>
    </graphics>
    <sound model='ich6'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
    </sound>
    <video>
      <model type='qxl' ram='65536' vram='65536' vgamem='16384' heads='1' primary='yes'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
    </video>
    <redirdev bus='usb' type='spicevmc'>
      <address type='usb' bus='0' port='2'/>
    </redirdev>
    <redirdev bus='usb' type='spicevmc'>
      <address type='usb' bus='0' port='3'/>
    </redirdev>
    <memballoon model='virtio'>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>
    </memballoon>
  </devices>
</domain>
"""
```



```python
# Obtain a connection to the hypervisor:
conn = libvirt.open('qemu:///system')

# Define the new instance without starting it: 
instance = conn.defineXML(xmlconfig)

# List the defined instances on the host: 
instances = conn.listDefinedDomains()

print 'Defined instances: {}'.format(instances) Defined instances: ['kvm_python']
```



```bash
# Ensure the instance has been defined, using the virsh command:
virsh list --all
```



```python
vim kvm.py
import libvirt
xmlconfig = """

<domain type='kvm' id='1'>
	<name>kvm_python</name>
	<memory unit='KiB'>1048576</memory>
	<currentMemory unit='KiB'>1048576</currentMemory>
	<vcpu placement='static'>1</vcpu>
	<resource>
		<partition>/machine</partition>
	</resource>
	<os>
		<type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
		<boot dev='hd'/>
	</os>
	<features>
		<acpi/>
		<apic/>
		<pae/>
	</features>
	<clock offset='utc'/>
	<on_poweroff>destroy</on_poweroff>
	<on_reboot>restart</on_reboot>
	<on_crash>restart</on_crash>
	<devices>
		<emulator>/usr/bin/qemu-system-x86_64</emulator>
		<disk type='file' device='disk'>
			<driver name='qemu' type='raw'/>
			<source file='/tmp/debian.img'/>
			<backingStore/>
			<target dev='hda' bus='ide'/>
			<alias name='ide0-0-0'/>
			<address type='drive' controller='0' bus='0' target='0'
unit='0'/>
		</disk>
		<controller type='usb' index='0'>
			<alias name='usb'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x2'/>
		</controller>
		<controller type='pci' index='0' model='pci-root'>
			<alias name='pci.0'/>
		</controller>
		<controller type='ide' index='0'>
			<alias name='ide'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x01'
function='0x1'/>
		</controller>
		<interface type='network'>
			<mac address='52:54:00:da:02:01'/>
			<source network='default' bridge='virbr0'/>
			<target dev='vnet0'/>
			<model type='rtl8139'/>
			<alias name='net0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x03'
function='0x0'/>
		</interface>
		<serial type='pty'>
			<source path='/dev/pts/5'/>
			<target port='0'/>
			<alias name='serial0'/>
		</serial>
		<console type='pty' tty='/dev/pts/5'>
			<source path='/dev/pts/5'/>
			<target type='serial' port='0'/>
			<alias name='serial0'/>
		</console>
		<input type='mouse' bus='ps2'/>
		<input type='keyboard' bus='ps2'/>
		<graphics type='vnc' port='5900' autoport='yes'
listen='0.0.0.0'>
			<listen type='address' address='0.0.0.0'/>
		</graphics>
		<video>
			<model type='cirrus' vram='16384' heads='1'/>
			<alias name='video0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x02'
function='0x0'/>
		</video>
		<memballoon model='virtio'>
			<alias name='balloon0'/>
			<address type='pci' domain='0x0000' bus='0x00' slot='0x04'
function='0x0'/>
		</memballoon>
	</devices>
</domain>
"""

conn = libvirt.open('qemu:///system')
if conn == None:
	print('Failed to connecto to the hypervizor')
	exit(1)

instance = conn.defineXML(xmlconfig)
if instance == None:
	print('Failed to define the instance')
	exit(1)

instances = conn.listDefinedDomains()
print('Defined instances: {}'.format(instances))

conn.close()
```



```bash
python kvm.py
```



Starting, stopping, and deleting KVM instances with Python 



```
```

