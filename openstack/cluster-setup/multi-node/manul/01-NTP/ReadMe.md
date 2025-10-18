Network Time Protocol (NTP)
============================

### Controller node
```shell
sudo apt install chrony -y
sudo yum install chrony -y

sudo vim /etc/chrony/chrony.conf
server _NTP_SERVER_ iburst
allow 172.16.50.0/24
```

```shell
sudo systemctl enable chronyd.service
sudo systemctl start chronyd.service
```

### Other nodes
```shell
sudo apt install chrony -y

sudo vim /etc/chrony/chrony.conf
server _controller01_ iburst
```

```shell
sudo systemctl enable chronyd.service
sudo systemctl start chronyd.service
```

### Verify operation
```shell
sudo chronyc sources
```

