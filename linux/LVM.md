Extended LVM partition
======================

### List physical partions

```shell
fdisk -l
Disk /dev/sda: 32.2 GB,
Disk /dev/mapper/vg_vmware-lv_root: 29.6 GB, 29569843200 bytes
Disk /dev/mapper/vg_vmware-lv_swap: 2113 MB, 2113929216 bytes
```

-------------------------------------------------------------------

```shell
df -lh

/dev/mapper/vg_vmware-lv_root        28G   15G   12G  57% /

increase the “physical” size of our disk 
fdisk -l
Disk /dev/sda: 64.4 GB,
Disk /dev/mapper/vg_vmware-lv_root: 29.6 GB, 
```

--------------------------------------------------------------------

```shell
fdisk /dev/sda
p   primary partition (1-4)
p
Partition number (1-4): 3

Command (m for help): w


fdisk -l
Disk /dev/sda: 64.4 GB, 64424509440 bytes
/dev/sda3            3917        7832    31453260   83  Linux
```


---------------------------------------------------------------------

```shell
pvdisplay
PV Name               /dev/sda2
PV Size               29.51 GiB 
 
 
pvcreate /dev/sda3
  Physical volume "/dev/sda3" successfully created
  
```

---------------------------------------------------------------------

```shell
pvdisplay

PV Name               /dev/sda2
VG Name               vg_vmware
 
PV Name               /dev/sda3
PV Size               30.00 GiB
```

----------------------------------------------------------------------------

```shell
vgdisplay | grep Name
VG Name               vg_vmware
```
--------------------------------------------------------------------------

```shell
vgextend vg_vmware /dev/sda3

Volume group "vg_vmware" successfully extended
```

---------------------------------------------------------------------

```shell
vgdisplay
 VG Size               59.50 GiB
```
---------------------------------------------------------------------------

```shell
lvdisplay | grep Path

 LV Path                /dev/vg_vmware/lv_root
```

-------------------------------------------------------

```shell
lvextend -l +100%FREE /dev/vg_vmware/lv_root
  Extending logical volume lv_root to 57.53 GiB
```
 ----------------------------------------------------

```
  lvdisplay
  LV Name                lv_root
  
   LV Size                57.53 GiB
```
------------------

```shell
    resize2fs /dev/vg_vmware/lv_root 
``` 

---

# Adding space to existed partion

```shell
lsblk

sda
  disk-partition
    vg
    
df -l

```