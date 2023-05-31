# Listen section

* used to define a __complete proxy__ with the functions of a __frontend__ and __backend__ combined.
* route traffic to a __specific set of servers__ or for __non-HTTP-related__ configurations such as TCP gateways.

* If you need to split traffic towards __separate pools of servers__ or your application is getting larger then it's better to __use distinct frontend and backend__ sections.

# Specific Servers

![scenario](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/04-1-liten.jpg)

```bash
listen myapp
    bind *:80
    mode tcp

    timeout client 30s
    timeout connect 10s
    timeout server 30s

    server myapp8010 192.168.56.22:8010
```

# Seprate pool

![scenaro1](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/04-2-listen.jpg)

```bash
defaults
    mode tcp
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:80
    default_backend my_app10

backend my_app10
    server myapp8010 192.168.56.22:8010

frontend auth_app
    bind *:81
    default_backend auth_app20

backend auth_app20
    server myapp8020 192.168.56.22:8020
```