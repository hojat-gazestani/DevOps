# Installing Open vSwitch on Ubuntu

```bash
sudo apt update -y
apt search openvswitch
sudo apt install openvswitch-switch -y

systemctl status openvswitch-switch.service

ovs-vsctl show
```

# Create Open vSwitch Bridge for KVM VMs

- Bridge IP address configuration

```bash
# All data traffic flows over the br-kvm network
auto br-kvm
allow-ovs br-kvm

# IP configuration of the OVS Bridge
iface br-kvm inet static
    address 192.168.20.10
    netmask 255.255.255.0
    gateway 192.168.20.1
    dns-nameservers 8.8.8.8
    ovs_type OVSBridge
    ovs_ports eth1
```



```bash
sudo ovs-vsctl add-br br-kvm
sudo ovs-vsctl add-port br-kvm eno1
```

# Enable IP Routing

```bash
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv4.conf.all.rp_filter = 2"|sudo tee -a  /etc/sysctl.conf
```

```bash
sudo sysctl -p
net.ipv4.ip_forward = 1
```


# Create Virtual Machine on the Bridge

```bash
sudo virt-builder -l

sudo virt-builder centosstream-8 --format qcow2 \
  --size 10G -o /var/lib/libvirt/images/centosstream-8.qcow2 \
  --root-password StrongRootPassword
```

```bash
sudo virt-install \
  --name centosstream-8 \
  --ram 2048 \
  --disk path=/var/lib/libvirt/images/centosstream-8.qcow2 \
  --vcpus 1 \
  --os-type linux \
  --os-variant rhel8.0 \
  --network=bridge:br-kvm,model=virtio,virtualport_type=openvswitch \
  --graphics none \
  --serial pty \
  --console pty \
  --boot hd \
  --import
  ````
