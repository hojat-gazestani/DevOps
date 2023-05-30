# Load Balancing Algorithms

## URI

* URI (uniform resource identifier) identifies a resource (text document, image file, etc)
* URL (uniform resource locator) is a subset of the URIs that include a network location
* URN (uniform resource name) is a subset of URIs that include a name within a given space, but no location


![UrlUri](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/06-UrlUri.png)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:80
    default_backend myapps

backend myapps
    balance uri 
    hash-type consistent
    server myapp8010 192.168.56.22:8010 
    server myapp8011 192.168.56.22:8011 
    server myapp8012 192.168.56.22:8012 
```

## query

![query](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/07-query.png)


## source

[UrlUri](https://prateekvjoshi.com/2014/02/22/url-vs-uri-vs-urn/)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp
    bind *:80
    default_backend myapps

backend myapps
    # Use this method when cash server is behind of HAProxy
    balance uri whole
    hash-type consistent
    server myapp8010 192.168.56.22:8010 
    server myapp8011 192.168.56.22:8011 
    server myapp8012 192.168.56.22:8012 
```