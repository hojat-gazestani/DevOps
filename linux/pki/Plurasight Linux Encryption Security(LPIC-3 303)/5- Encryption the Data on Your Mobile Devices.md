- [1- File systemc Encryption. introduction](#1-File-systemc-Encryption.-introduction)
- [2- Encrypt a User Account with eCryptfs](#2-Encrypt-a-User-Account-with-eCryptfs)
  - [Create encrypted user account](#Create-encrypted-user-account)
  - [Create a single encrypted directory within an existing unencrypted account](#Create-a-single-encrypted-directory-within-an-existing-unencrypted-account)
  - [Manage unecrypted archives](#Manage-unecrypted-archives)
  - [Migrate data](#Migrate-data)
- [3- Encrypt a Mobile Storage Device with Cryptsetup](#3-Encrypt-a-Mobile-Storage-Device-with-Cryptsetup)
  - [Loading Encrypted Partitions](#Loading-Encrypted-Partitions)



## 1- File systemc Encryption. introduction

* Encryption at Rest: Popular Solutions
  * eCryptfs:
    * Partial or full file system encryption
    * metadata stored with individual files
  * cryptsetup
    * dm-crypt
      * kernel-space resource
      * "Backend" for encryption managers
    * LUKS - Linux Unified Key Setup
      * Widespread standard
      * Multiple key support
      * Header quickly identifies volume to OS
  * EncFS   
    * Cloud or local storage integration     
    * Dynamically sized directories     
    * Kernel-agnostic, cross-plactform
    
## 2- Encrypt a User Account with eCryptfs
```commandline
sudo modprobe ecryptfs
sudo apt install ecryptfs-utils
```

### Create encrypted user account 
```commandline
sudo adduser mydata

sudo ecryptfs-migrate-home -u mydata

su mydata
ecryptfs-unwarp-passphrase ~/.ecryptfs/wrapped-passphrase
ecryptfs-mount-private
cd /home/mydata
touch newfile

cd /home/
sudo diff mydata mydata.y10o2iAA

sudo rm -r mydata.y10o2iAA

ecryptfs-setup-swap	# encrypt swap eara

ls /home/mydata/.ecryptfs
auto-mount auto-umount Private.mnt Private.sig wrapped-passphrase

cat /home/mydata/.ecryptfs/Private.mnt
/home/mydata
```

### Create a single encrypted directory within an existing unencrypted account
```commandline
sudo adduser newacc

su newacc

ecryptfs-setup-private

logout ligin
ls
private

```

### Manage unencrypted archives
```commandline
sudo mount -t ecryptfs /home/.ecryptefs/mydata/.Private/ /home/mydata/
sudo umount.ecryptfs /home/mydata

su mydata
ls /home/.ecryptfs/mydata/.ecryptfs/
auto-mount auto-umount Private.mnt Private.sig wrapped-passphrase
```

### Migrate data



## 3- Encrypt a Mobile Storage Device with Cryptsetup
```commandline
Prepare the partition
Format the partition
Configure encryption
Name the partition
Apply file system
Mount partition

lsblk
sdb

dd if=/dev/zero of=/dev/sdb bs=4096 # wipping the partition

cryptsetup luksFormat --cipher aes-xts-plain64 --key-size 512 --hash sha512 --iter-time 2000 /dev/sdb
YES
password

cryptsetup luksOpen /dev/sdb MyArchive	# Assign a mapping name to the archive

mkfs.ext4 /dev/mapper/MyArchive

mkdir /home/archive
mount /dev/mapper/MyArchive /home/archive
cyrptsetup -v status MyArchive

cryptsetup luksDump /dev/sdb > header-data

vim /home/atchive/stuff
	Hello, I am data.
```

### Loading Encrypted Partitions
```commandline
/etc/fstab
/etc/crypttab
	MyArchive UUID=454.. nove luks,timeout=180
```


