# HAProxy installation on server

* On the official HAProxy [[website](https://www.haproxy.org/)] : you can choose the distribution that suits your needs.

![Address](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-Address.png)


# install haproxy 2.6 on ubuntu 20.04
* You have the flexibility to select your preferred distribution, version, and desired HAProxy version.

![choose](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-choose.png)

```bash
sudo apt-get install --no-install-recommends software-properties-common
sudo add-apt-repository ppa:vbernat/haproxy-2.6

sudo apt-get install vim-haproxy haproxy=2.6.\*
```

# install haproxy 2.7 on ubuntu 20.04
* Version 2.7 installation 

![version7](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-address2.7.png)

```bash
sudo apt-get install --no-install-recommends software-properties-common
sudo add-apt-repository ppa:vbernat/haproxy-2.7

sudo apt-get install vim-haproxy haproxy=2.7.\*
```