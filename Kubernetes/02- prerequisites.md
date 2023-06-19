## Disable swap & add kernel settings
```bash
sudo sed -ri '/\sswap\s/s/^#?/#/' /etc/fstab
sudo swapoff -a

sudo systemctl stop apparmor
sudo systemctl disable apparmor
```

## [Install and configure prerequisites](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

* Verify 

```bash
lsmod | grep br_netfilter
lsmod | grep overlay
```