# ACL

## URL
* URI (uniform resource identifier) identifies a resource (text document, image file, etc)
* URL (uniform resource locator) is a subset of the URIs that include a network location
* URN (uniform resource name) is a subset of URIs that include a name within a given space, but no location

![URL](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/06-UrlUri.png)

* URL parameter

![param](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/07-query.png)

## ACls inspect traffic via fetches

- __fetching:__ __store__ the data about __connections__ and __requests__ 
  - Client source IP / Port
  - URL
  - HTTP header 
  - etc.

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

```bash

```

- __content switching:__  __take decisions__ based on __content extracted__ from the __request__
  - __extract a data__ sample from a __stream__, __table__ or the __environment__
  - optionally apply some __format conversion__ to the extracted sample
  - apply one or multiple __pattern matching__ methods on this sample
  - __perform actions__ only when a __pattern matches__ the sample
    - __blocking__ a request
    - selecting a __backend__
    - __adding__ a header

## access list definition

```bash
acl <aclname> <criterion> [flags] [operator] [<value>] ...
```
  


## sources

[community](https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#7.1)

[1](https://www.haproxy.com/blog/introduction-to-haproxy-acls)

[2](https://www.haproxy.com/documentation/hapee/latest/configuration/acls/syntax/)