# command line

```bash
defaults
    mode tcp
    timeout client 30s
    timeout connect 10s
    timeout server 30s

global
    stats socket /run/haproxy/admin.sock mode 660 level admin
    stats socket ipv4@*:9999 level admin

frontend myapp
    bind *:81
    default_backend myapps

backend myapps
    balance source
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012
```


```bash
echo "help" | socat stdio /run/haproxy/admin.sock
echo "show info" | socat stdio /run/haproxy/admin.sock
echo "show stat" | socat stdio /run/haproxy/admin.sock
echo "show threads" | socat stdio /run/haproxy/admin.sock
```

```bash
echo "set server backend-my_app state maint" | nc 127.0.0.1 9999
```

```bash
htop -s /run/haproxy/admin.sock
```