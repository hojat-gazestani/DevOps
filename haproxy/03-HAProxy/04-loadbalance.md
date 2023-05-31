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

## URL parameter

![query](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/07-query.png)

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
### hash-type

- __Map-based:__ 
  - __default__ hash type
  - __hash table__ is a __static array__ containing all __alive server__ 
  - __static__ algorithm __on fly weight change__ does not affect
  - __inconvenient__ with __cach__
- __consistent:__
  - __convenient__ for __cach__
  - __a tree table__ filled with many __occurrences of server__.
  - __the hash key __looked up__ in the tree and the __closest server__ is chosen.
  - __dynamic__ algorithm

## source

[UrlUri](https://prateekvjoshi.com/2014/02/22/url-vs-uri-vs-urn/)

