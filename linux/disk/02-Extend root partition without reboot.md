# Extend root partition without reboot



```bash
# Add space to your VM partition

echo 1>/sys/class/block/sda/device/rescan

cfdisk
	resize
	quit
	
pvresize /dev/sda3

pvdisplay

vgdisplay

lvdisplay

lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv

df -h 
```

