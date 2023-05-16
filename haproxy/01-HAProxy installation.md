# HAProxy installation

* On the official HAProxy ![[website](https://www.haproxy.com/)] : you can choose the distribution that suits your needs.
* ![Address](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-Address.png)
* You have the flexibility to select your preferred distribution, version, and desired HAProxy version.
* ![choose](file:///home/arman/Pictures/Screenshots/Screenshot%20from%202023-05-16%2014-30-08.png)

```bash
sudo apt-get install --no-install-recommends software-properties-common
sudo add-apt-repository ppa:vbernat/haproxy-2.6

sudo apt-get install haproxy=2.6.\*
```

