## Private Virtual Bridge

- must be installed
```sh
ip
brctl (deprecated). Use ip link instead
tunctl (deprecated). Use ip tuntap and ip link instead
```

##  create a bridge
```sh
ip link add br0 type bridge ; ifconfig br0 up
brctl addbr br0 (deprecated)
```

- qemu-ifup script containing the following (run as root):

```sh
#!/bin/sh
set -x

switch=br0

if [ -n "$1" ];then
        # tunctl -u `whoami` -t $1 (use ip tuntap instead!)
        ip tuntap add $1 mode tap user `whoami`
        ip link set $1 up
        sleep 0.5s
        # brctl addif $switch $1 (use ip link instead!)
        ip link set $1 master $switch
        exit 0
else
        echo "Error: no interface specified"
        exit 1
fi
```

- Generate a MAC address, either manually or using:
```sh
#!/bin/bash
# generate a random mac address for the qemu nic
printf 'DE:AD:BE:EF:%02X:%02X\n' $((RANDOM%256)) $((RANDOM%256))
```

- Run each guest with the following, replacing $macaddress with the value from the previous step
```sh
qemu-system-x86_64 -hda /path/to/hda.img -device e1000,netdev=net0,mac=$macaddress -netdev tap,id=net0

```

- or You can either create a system-wide qemu-ifup in /etc/qemu-ifup or use another one. In the latter case, run

```sh
qemu-system-x86_64 -hda /path/to/hda.img -device e1000,netdev=net0,mac=$macaddress -netdev tap,id=net0,script=/path/to/qemu-ifup

```

## Create a bridge
```sh
uuidgen
336758DD-3A31-4E36-9353-537976D53CE0

sudo cp /etc/libvirt/qemu/networks/default.xml /etc/libvirt/qemu/networks/virbrCeph.xml
sudo vim /etc/libvirt/qemu/networks/virbrCeph.xml
<network>
  <name>virbrCeph</name>
  <uuid>336758dd-3a31-4e36-9353-537976d53ce0</uuid>
  <forward dev='eno4' mode='nat'>
    <interface dev='eno4'/>
  </forward>
  <bridge name='virbrCeph' stp='on' delay='0'/>
  <mac address='52:54:00:ed:03:f1'/>
  <ip address='192.168.123.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.123.100' end='192.168.123.254'/>
    </dhcp>
  </ip>
</network>

sudo virsh net-define /etc/libvirt/qemu/networks/virbrCeph.xml
sudo virsh net-start virbrCeph
sudo virsh net-autostart virbrCeph

svir attach-interface --type bridge --source virbrCeph --model virtio Ubu22-Test
```
