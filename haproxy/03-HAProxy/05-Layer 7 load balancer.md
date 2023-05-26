# Layer 4 load balancer

## Layer 7

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/05-layer7%20load%20balancer.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:81
    default_backend my_apps

backend my_apps
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012

frontend authapp
    bind *:82
    default_backend auth_apps

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
    server AuthAPP21 192.168.56.22:8021
    server AuthAPP22 192.168.56.22:8022
```

* ACL
```bash
defaults
    mode http   
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:80

    acl myapp_url path_beg /app
    use_backend my_apps if myapp_url

    use_backend auth_apps if { path_beg /auth }
    
backend my_apps
    server myapp8010 192.168.56.22:8010
    server myapp8011 192.168.56.22:8011
    server myapp8012 192.168.56.22:8012

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
    server AuthAPP21 192.168.56.22:8021
    server AuthAPP22 192.168.56.22:8022 
```