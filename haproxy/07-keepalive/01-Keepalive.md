# HAProxy active passive configuration with keepalived

## install requirement 
```bsah
sudo apt install keepalived haproxy rsync psmisc -y
``` 
## First server configuration

```bash
vrrp_script chk_haproxy {
    script '/usr/bin/killall -0 haproxy'
    interval 2
}

vrrp_instance VIP_! {
    interface enp0s3
    state MASTER
    priority 101
    virtual_router_id 50
    advert_int 1
    
    unicast_src_ip 192.168.56.23
    unicast_peer {
        192.168.56.24
    }
    
    authentication {
        auth_type PASS
        auth_pass 12345678
    }
    
    virtual_ipaddress {
        192.168.56.30
    }
    
    track_script {
        chk_haproxy()
    }
}
```

```bash

```

## Second server configuration

```bash
vrrp_script chk_haproxy {
    script '/usr/bin/killall -0 haproxy'
    interval 2
}

vrrp_instance VIP_1 {
    interface enp0s3
    state BACK
    priority 100
    virtual_router_id 50
    advert_int 1
    
    unicast_src_ip 192.168.56.24
    unicast_peer {
        192.168.56.23
    }
    
    authentication {
        auth_type PASS
        auth_pass 12345678
    }
    
    virtual_ipaddress {
        192.168.56.30
    }
    
    track_script {
        chk_haproxy()
    }
}
```

## ssh key
```bash
ssh-keygen
ssh-copy-id root@192.168.56.24
```

## Syncing script

```bash
vim haproxy_reload.sh
  
#!/bin/bash
  

systemctl restart haproxy
sleep 2

rsync -azvP -e 'ssh -p 22' /etch/haproxy/ root@192.168.56.24:/etc/haproxy/
rsync -azvP -e 'ssh -p 22' /certs/ root@192.168.56.24:/certs/
sleep 60

ssh root@192.168.56.24 "sudo systemctl restart haproxy
```

```bash
chmod +x ./haproxy_reload
```

## auto mount
```bash
/certs  /var/lib/haproxy/certs/ none    defaults,bind 0 0
/run    /var/lib/haproxy/run/   none    defaults,bind 0 0
```



