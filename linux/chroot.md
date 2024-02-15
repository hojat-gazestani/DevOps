[TOC]

# chroot

* Isolate a process from other processes.
* Change the root directory for a process along with its child processes.
* A chroot jail is a virtual environment created by changing the root directory of a  user or group to a new directory. This new directory serves as the fake  root directory for our chroot jail

## Use cases:

1. Create a test environment for software development and testing.
2. Initialize reinstallation of the bootloader files on your system
3. Run software which may be decrepitated
4. Enhance security using a ringfencing mechanism

## Syntax

```shell
chroot [-OPTION] [PATH FOR NEW ROOT] [PATH FOR SERVER]
```

* Necessary: path for the new root directory.

- **userspec=USER[:GROUP]** – Used to define the user or the group which we wish to use the chroot command on.
- **groups=G_List –** Used to specify supplementary groups we wish to use as G1, G2… Gn



# Creating a chroot command jail

## Create and add Required Root Directories

```shell
mkdir /home/user/chroot_jail
mkdir -p /home/user/chroot_jail/{bin,lib,lib64}
cd /home/user/chroot_jail
```



## Move the allowed Cammand Binary Files

```shell
cp -v /bin/{bash,touch,ls,rm} /home/user/chroot_jail
```



## Resolving Command Dependencies

```sh
ldd /bin/bash
cp -v {<List dependencies here>} /home/user/chroot_jail/lib64
cp -v /lib/x86_64-linux-gnu/libtinfo.so.5 /home/user/chroot_jail/lib/
cp -v /lib/x86_64-linux-gnu/libdl.so.2 /home/user/chroot_jail/lib/
cp -v /lib/x86_64-linux-gnu/libc.so.6 /home/user/chroot_jail/lib/
```



## Switching to the new Root Directory

Specify bash to run as the application which we run as the shell for our virtualized environment.

```shell
sudo chroot /user/home/chroot_jail
```



# Lighttpd FasCGI PHP, MySQL chroot Jain

## Install lighttpd php4-cgi php4-cli php4-mysql mysql-server

```shell
apt-get install lighttpd php4-cgi php4-cli php4-mysql mysql-server 
sudo apt install lighttpd php7.0-cgi php7.0-cli php7.0-mysql mysql-server
```



## Prepare the file system

```shell
mkdir -p /webroot/tmp/
chmod 1777 /webroot/{tmp,etc,var}

mkdir -p /webroot/var/tmp/lighttpd/cache/compress/
chown www-data:www-data /webroot/var/tmp/lighttpd/cache/compress/

mkdir -p /webroot/home/lighttpd
chown www-data:www-data /webroot/home/lighttpd
chmod 0700 /webroot/home/lighttpd
ls -dl /webroot/home/lighttpd
```

Put l2chroot

```shell
wget http://www.cyberciti.biz/files/lighttpd/l2chroot.txt
mv l2chroot.txt l2chroot
cp l2chroot /bin
chmod +x /bin/l2chroot
```



## Put PHP in the jail

```shell
mkdir -p /webroot/usr/bin
cp /usr/bin/php4-cgi /webroot/usr/bin/
cp /usr/bin/php4 /webroot/usr/bin/

cd /webroot/etc/
cp -avr /etc/php4 .

cp /etc/hosts /webroot/etc/
cp /etc/nsswitch.conf /webroot/etc/
cp /etc/resolv.conf /webroot/etc/
cp /etc/services /webroot/etc/
cp /etc/localtime /webroot/etc/

/bin/l2chroot /usr/bin/php4
/bin/l2chroot /usr/bin/php4-cgi

cp /lib/ld-linux.so.2 /webroot/lib
```



## Put php MySQL extension in the jail

```shell
 dpkg -L php4-mysql
```



```
mkdir -p /webroot/usr/lib/php7/20050606
cp /usr/lib/php7/20050606/mysql.so /webroot/usr/lib/php4/20050606/
/bin/l2chroot /usr/lib/php4/20050606/mysql.so
```

Repeat above procedure to copy all your php shared modules such as  php-imap (required for webmail), php-gd (GD module for php4 used by  wordpress and other softwares), php-memcache etc.

## Configure lighttpd to run from chrooted jail

```shell
lighty-enable-mod fastcgi

vim /etc/lighttpd/lighttpd.conf 
server.chroot = "/webroot"

/etc/init.d/lighttpd start
```



## Test jail setup

