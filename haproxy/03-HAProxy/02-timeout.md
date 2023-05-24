# Timeout configuration

* Scenario

![Scenario](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/02-Timeout.jpg)

* HAproxy config file 
```bash
My git [Mygithut](https://github.com/hojat-gazestani/HAProxy.git) && cd HAProxy
sudo haproxy -f 02-Timeout.cfg
```

```bash
frontend myapp
    bind *:80
    mode tcp
    timeout client 30s
    default_backend myapp1

backend myapp1
    mode tcp
    timeout connect 10s
    timeout server 20s
    server myapp1 192.168.56.22:8010
```

* To HAProxy server
```bash
curl http://192.168.56.22
```