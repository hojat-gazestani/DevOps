# virt install Ubuntu22 and Ubuntu18

```sh
wget https://cloud-images.ubuntu.com/releases/bionic/release/ubuntu-18.04-server-cloudimg-amd64.img
wget https://cloud-images.ubuntu.com/releases/22.04/release/ubuntu-22.04-server-cloudimg-amd64.img
wget https://cloud-images.ubuntu.com/releases/24.10/release-20241109/ubuntu-24.10-server-cloudimg-amd64.img
```
```sh
sudo apt install -y qemu qemu-kvm libvirt-daemon libvirt-clients bridge-utils virt-manager cloud-image-utils libguestfs-tools
```
# Set a password for the new VM
```sh
cat >user-data.txt <<EOF
#cloud-config
password: secretpassword
chpasswd: { expire: False }
ssh_pwauth: True
EOF
```

- Then create the image file. We will use the user-data.img file in the virt-install step.

```sh
cloud-localds user-data.img user-data.txt
```

## Create a writable clone of the boot drive
```sh
sudo qemu-img create -b ubuntu-18.04-server-cloudimg-amd64.img -F qcow2 -f qcow2 ubuntu-vm-disk.qcow2 20G
sudo qemu-img create -b ubuntu-22.04-server-cloudimg-amd64.img -F qcow2 -f qcow2 ubuntu-vm-disk.qcow2 50G
```

## Create a running VM
```sh
virt-install --name ubuntu-18-vm \
  --virt-type kvm --memory 2048 --vcpus 2 \
  --boot hd,menu=on \
  --disk path=ubuntu-vm-disk.qcow2,device=disk \
  --disk path=user-data.img,format=raw \
  --graphics none \
  --os-type Linux --os-variant ubuntu18.04

virt-install --name ubuntu-22-vm \
  --virt-type kvm --memory 4096 --vcpus 4 \
  --boot hd,menu=on \
  --disk path=ubuntu-vm-disk.qcow2,device=disk \
  --disk path=user-data.img,format=raw \
  --graphics none \
  --os-type Linux --os-variant ubuntu22.04 \
  --network bridge=br-kvm,model=virtio
```
