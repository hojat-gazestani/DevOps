# Active Passive Cluster with keepalive

![cluster](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/03-ActivePassiveCluster.png)


```bash
HA1:
    192.168.254.81
    
HA2:
    192.168.254.47
    
VIP:
    192.168.254.100

# HAProxy1
sudo apt-get install keepalived
sudo vim /etc/keepalived/keepalived.conf
vrrp_instance HA1 {
    state MASTER
    interface eth0
    virtual_router_id 101
    priority 100
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    
    virtual_ipaddress {
        192.168.254.100
    }
}

sudo systemctl start keepalived

# HAProxy2
sudo apt-get install keepalived
sudo vim /etc/keepalived/keepalived.conf
vrrp_instance HA2 {
    state BACKUP
    interface eth0
    virtual_router_id 102
    priority 200
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    
    virtual_ipaddress {
        192.168.254.100
    }
}

sudo systemctl start keepalived
```


# Active Active cluster keepalive

![ActiveActive](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/04-ActiveActiveCluster.png)



# Active Active cluster using KeepAlived with FloatingIP