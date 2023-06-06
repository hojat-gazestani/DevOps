# Peers protocol in high availability 

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s
    
peers Italy-Peers
    peer HA1 192.168.56.23:50000
    peer HA2 192.168.56.24  :50000

frontend Italy
    bind *:81
    default_backend myapps

backend myapps
    balance source
    stick-table type ip size 100k expire 30m peers Italy-Peers store conn_cur
    http-request track-sc0 src
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012
```

## show tables 

```bash
echo "show table" | nc 127.0.0.1 9999
echo "show table front-Italy" | nc 127.0.0.1 9999
```
