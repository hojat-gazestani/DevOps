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

	