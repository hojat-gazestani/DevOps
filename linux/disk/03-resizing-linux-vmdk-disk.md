# Resizing Partition and Filesystem after Expanding VMware VMDK Disk

## Description
This guide provides a step-by-step process for resizing a partition and filesystem after expanding the disk size of a virtual machine in VMware. It uses `parted` for partition resizing and LVM tools to extend both the physical and logical volumes, as well as the filesystem.

## Prerequisites
- A virtual machine running on VMware with an expanded VMDK disk.
- Root or sudo access on the Linux system.
- LVM is being used for volume management.
  
## Steps

### 1. Verify the Disk Expansion
First, ensure that the Linux system recognizes the newly added space on the disk.

```bash
lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   80G  0 disk 
├─sda1                      8:1    0    1M  0 part 
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   48G  0 part 
  └─ubuntu--vg-ubuntu--lv 252:0    0   48G  0 lvm  /
sr0                        11:0    1 1024M  0 rom  

fdisk -l
root@stage:/home/hojat# fdisk -l
GPT PMBR size mismatch (104857599 != 167772159) will be corrected by write.
The backup GPT table is not on the end of the device.
Disk /dev/sda: 80 GiB, 85899345920 bytes, 167772160 sectors
Disk model: Virtual disk    
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 3425E8D8-9EAA-4ADB-A495-F2B4249C2992

Device       Start       End   Sectors Size Type
root@stage:/home/hojat# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   80G  0 disk 
├─sda1                      8:1    0    1M  0 part 
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   48G  0 part 
  └─ubuntu--vg-ubuntu--lv 252:0    0   48G  0 lvm  /
sr0                        11:0    1 1024M  0 rom  
```

You should see the additional unallocated space in the output.

### 2. Rescan the Disk

To detect the new space added to the disk:

```bash
echo 1 > /sys/class/block/sda/device/rescan
cfdisk
	resize
	quit
```

### 3. Fix the GPT Table (If Required)
If prompted to fix the GPT when resizing the partition, proceed by selecting Fix. This will not affect existing data.


### 4. Resize the Partition

Use `parted` to resize the partition that you want to extend (in this case, `/dev/sda3`):

```bash
parted /dev/sda
resizepart 3 100%
quit
```

### 5. Resize the Physical Volume (PV)

Now, extend the LVM physical volume to include the newly available space.

```bash
pvresize /dev/sda3
```

### 6. Extend the Logical Volume (LV)

Extend the logical volume to use all available space:

```bash
lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
```

### 7. Resize the Filesystem

Finally, resize the filesystem to use the expanded logical volume.

```bash
resize2fs /dev/ubuntu-vg/ubuntu-lv
```
### 8. Verify the Changes

```sh
root@stage:/home/hojat# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   80G  0 disk 
├─sda1                      8:1    0    1M  0 part 
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   78G  0 part 
  └─ubuntu--vg-ubuntu--lv 252:0    0   78G  0 lvm  /
sr0                        11:0    1 1024M  0 rom  


root@stage:/home/hojat# df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              387M  2.6M  385M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   77G   41G   33G  56% /

```