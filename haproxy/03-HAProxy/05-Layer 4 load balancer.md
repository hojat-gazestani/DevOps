# Layer 4 load balancer

## OSI Layer 4

* o known as the __transport layer__, the protocols such as __TCP, UDP__
* connection-oriented communication, reliability, flow control, and multiplexing
* data transfer __without visibility__ into message content.
* layer 4 load balancing can make routing decisions __without__ the need to __decrypt__ or __inspect network traffic__

## Scenario

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/08-1-layer4Loadbalancer.jpg)

```bash
defaults
    mode tcp
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:81
    default_backend myapps

backend myapps
    #balance roundrobin
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012


# for i in {1..100}; do curl localhost &&sleep 1 && echo; done;
```

* TCP sticky session

```bash
defaults
    mode tcp
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:81
    default_backend myapps

backend myapps
    balance source
    stick-table type ip size 10k
    stick on src
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012


# for i in {1..100}; do curl localhost &&sleep 1 && echo; done;
```