# ACL

## URL
* URI (uniform resource identifier) identifies a resource (text document, image file, etc)
* URL (uniform resource locator) is a subset of the URIs that include a network location
* URN (uniform resource name) is a subset of URIs that include a name within a given space, but no location

![URL](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/06-UrlUri.png)

* URL parameter

![param](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/07-query.png)

## ACL basic
- __content switching:__  __take decisions__ based on __content extracted__ from the __request__
  - __extract a data__ sample from a __stream__, __table__ or the __environment__
  - optionally apply some __format conversion__ to the extracted sample
  - apply one or multiple __pattern matching__ methods on this sample
  - __perform actions__ only when a __pattern matches__ the sample
    - __blocking__ a request
    - selecting a __backend__
    - __adding__ a header


## ACls inspect traffic via fetches

- __fetching:__ __store__ the data about __connections__ and __requests__ 
  - Client source IP / Port
  - URL
  - HTTP header 
  - etc.

### Actions
- Deny the request.
- Choose the pool of servers
- Add, remove or modify headers
- Rewrite the URL
- etc


- __extracting data__ from __request__ or __response__ streams, __client or server information__, from __tables__, __environmental information__ etc...
- these samples may be used for __various purposes__ such as a __key__ to a __stick-table__
- __matching__ them against predefined constant data called __patterns__




```bash
frontend test
    acl is_api path_beg /api
    use_backend api_server if is_api
    
    # OR
    use_backend api_server if { path_beg /api }
```

```text
path:                           exact match
path_beg | path -m beg:         Prefix match for binary or string
path_dir | path -m dir:         subdir match, binary or string samples
path_end | path -m end:         Suffix match for binary or string
path_len | path -m len:         match the sample length as integer,  binary or string samples
path_reg | path -m reg:         regex match, binary or string samples
path_sub | path -m sub:         substring match, binary or string samples
```

### Chain ACL
```bash
frontend www
    use_backend django_srv if { path_beg /api } { src 192.168.56.0/24 }

frontend www1
    acl is_php path_end .php
    acl host_found req.hdr(host) -m found
    http-request deny if is_php || !host_found
```


### 01 ACL Path

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/01-Layer7-ACLpath.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    acl is_myapp path_beg -i /app
    use_backend my_apps if is_myapp

    use_backend img_apps if { path -m beg -i /img }

    default_backend auth_apps

backend my_apps
    server myapp8010 192.168.56.22:8010 

backend img_apps
    server myapp8010 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

### 02 ACL Path length

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/02-ACL-PathLen.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    use_backend img_apps if { path_len 14 } # path length is 14

    #use_backend img_apps if { path_len ge 10 }

    #use_backend img_apps if { path_len le 20 }

    #use_backend img_apps if { path_len 10:20 }

    #acl is_image_request path_len 14
    #use_backend img_apps if is_image_request


    default_backend auth_apps

backend img_apps
    server myapp8010 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

### 03 ACL Path end

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/03-ACL-Path-end.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    use_backend img_apps if { path_end -i .jpg }

    #use_backend img_apps if { path_end -i .jpg .png .mov .mp4 }
    #use_backend img_apps if { path_reg -i .(jpg|png|mov|mp4) }

    default_backend auth_apps

backend img_apps
    server myapp8010 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020


```

### 04 ACL URL Param

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/04-ACL-URL-param.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

 
    acl is_west url_param(region) -i -m str west south
    acl is_east url_param(region) -i -m str east north
   
    #acl is_west url_param(region) -i -m reg w.*
    #acl is_west url_param(region) -i -m reg (west|south)
    #acl urlparam url_param() -i -m end 

    use_backend my_apps if is_west
    use_backend img_apps if is_east

    default_backend auth_apps

backend my_apps
    server myapp8010 192.168.56.22:8010 

backend img_apps
    server myapp8030 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020


# http://192.168.56.21/?region=west
# http://192.168.56.21/?region=east
# http://192.168.56.21/?region=south
# http://192.168.56.21/?region=north
```

### 04 ACL Host header

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/05-ACL-hostHeader.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    acl is_hojatcom hdr(Host) -i -m str hojat.com
    acl is_nethightech hdr(host) -i -m str www.nethightech.com || hdr(host) -i -m str ftp.nethightech.com || hdr(host) -i -m str mail.nethightech.com
    acl is_nethightech hdr_reg(host) -i ^(www|ftp|mail)\.nethightech\.com$

    acl is_phone  hdr_end(User-Agent) -i -m reg (Andoroid|Iphone)
    use_backend img_apps if is_phone

    #acl name req.hdr
    #acl name res.hdr
    #acl name res.hdr_reg

    use_backend my_apps if is_hojatcom
    use_backend img_apps if is_nethightech

    default_backend auth_apps

backend my_apps
    server myapp8010 192.168.56.22:8010 

backend img_apps
    server myapp8030 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

### 05 ACL Deny Source IP

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/06-ACL-Deny-srcIP.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    http-request deny if { src 192.168.56.20 }

    default_backend auth_apps

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

### 06-ACL method POST

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/07-ACL-methodPost.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    #use_backend api_app if method POST
    #use_backend api_app if method GET AND path_beg -i /api

    acl is_post_method method POST
    use_backend api_app if is_post_method

    acl is_get_api path_beg -i /api
    use_backend api_app if is_get_api

    default_backend auth_apps

backend api_app
    server ApiAPP40 192.168.56.22:8040

bbackend auth_apps
    server AuthAPP20 192.168.56.22:8020

```

### 07-ACL redirect

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/08-ACL-redirect.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    acl is_pic path_end -i .jpg .gif
    redirect prefix http://nethightech.com if is_pic

    default_backend auth_apps

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

### 08-ACL User Agent

![pic](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/2-acl/09-ACL-userAgent.jpg)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend myapp_imgeapp
    bind *:80

    acl is_phone  hdr_end(User-Agent) -i -m reg (Andoroid|Iphone)
    use_backend img_apps if is_phone

    default_backend auth_apps

backend img_apps
    server myapp8030 192.168.56.22:8030

backend auth_apps
    server AuthAPP20 192.168.56.22:8020
```

## sources

[community](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#7.1)

[1](https://www.haproxy.com/blog/introduction-to-haproxy-acls)

[2](https://www.haproxy.com/documentation/hapee/latest/configuration/acls/syntax/)