## Simple Backend and frondend

* Scenario

![BackFront](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-BackFront.jpg)


* HAproxy config file 
```bash
vim 01-simpleBackFront.cfg
frontend myapp
    bind *:80
    mode tcp
    default_backend myapp

backend myapp
    mode tcp
    server myapp1 192.168.56.22:8010
```

* To Backend server
```bash
curl http://127.0.0.1:8001
```

* To HAProxy server
```bash
curl http://127.0.0.1:8010
```