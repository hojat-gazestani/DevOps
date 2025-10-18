## Memcached for Ubuntu

### controller
* 16.04
```shell
sudo apt install memcached python-memcache
```

* 18.04
```shell
sudo apt install memcached python3-memcache etcd   -y 
```
```shell
sudo vim /etc/memcached.conf
-l 172.16.50.41
```
### Finalize installation
```shell
sudo service memcached restart
```