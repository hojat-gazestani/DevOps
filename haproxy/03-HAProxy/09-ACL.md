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

### URL Path
```bash
frontend test
    acl is_image1 path -i /img/south/image1.jpg
    use_backend img_srv if is_image1
    
    # OR
    use_backend img_srv if { path -i  /img/south/image1.jpg}
```

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

* path_dir
```bash
acl is_images path_dir -i /images
```

* path_end
```bash
acl is_html path_end -i *.html
```

* path_len
```bash
acl is_eleven path_len 11 
```

* path_reg
```bash
acl is_css_js path_reg -i .(css|js)$ 
```

* path_string
```bash
acl is_page path_string -i page 
```

### IP address

```bash
frontend hacker
    acl is_hacker src 192.168.56.20/32
    
    # OR
    
    http-request deny if { src 192.168.56.20/32 }
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


## condition
1. Does the connection or request match some criteria
2. yes. take action A
3. NO, take action B
4. 

### Actions
- Deny the request.
- Choose the pool of servers
- Add, remove or modify headers
- Rewrite the URL
- etc



















```text
  - __extracting data__ from __request__ or __response__ streams, __client or server information__, from __tables__, __environmental information__ etc...
  - these samples may be used for __various purposes__ such as a __key__ to a __stick-table__
  - __matching__ them against predefined constant data called __patterns__

```



## access list definition

```bash
acl <aclname> <criterion> [flags] [operator] [<value>] ...
```
  


## sources

[community](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#7.1)

[1](https://www.haproxy.com/blog/introduction-to-haproxy-acls)

[2](https://www.haproxy.com/documentation/hapee/latest/configuration/acls/syntax/)