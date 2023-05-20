## load balancer 

* a device that __acts as a reverse proxy__ and __distributes network or application traffic__ across a number of __servers__. 

![loadBalancer](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-load%20blalancer.jpg)

- __Distributes__ client requests or __network load__ efficiently across __multiple servers__
- Ensures __high availability__ (Reduced downtime) and __reliability__ by sending requests only to servers that are online
- Provides the __flexibility__ to add or subtract servers as demand dictates

# Load Balancing Algorithms

[source](http://cbonte.github.io/haproxy-dconv/2.4/configuration.html)

[Definition](https://www.haproxy.com/blog/fundamentals-load-balancing-and-the-right-distribution-algorithm-for-you/)

- __Dynamic:__ adaptive and capable of changing how it sorts incoming requests based on the __current demand__ servers face.
  - __roundrobin:__ Each server is __used in turns__, according to their __weights__.
      - __smoothest__ and __fairest__
      - __equally__ distributed.
      - __weights__ may be adjusted on the fly for slow __starts for instance__
  - __leastconn:__ The server with the __lowest number of connections__ receives the connection.
    - very __long sessions__ are expected, such as __LDAP__, __SQL__, __TSE__
    - is __not__ very well suited for protocols using short sessions such as __HTTP__.
    - __weights__ may be adjusted __on the fly__ for slow __starts for instance__.
    - It will also consider the number of __queued connections__

- __static:__ is more fixed and is __unchanging__ regardless of the state of incoming traffic,
  - __static-rr:__ Each server is used in turns, according to their weights.
    - changing a server's  __weight on the fly will have no effect__.
    - it is always  __immediately reintroduced __ into the farm, once the full map is recomputed.
  - __first:__ The  __first server__ with available connection slots  __receives__ the connection. 
    - Once a server reaches its __maxconn__ value, the __next server__ is used.
    - It does __not make sense__ to use this algorithm __without setting maxconn__.
    - always use the __smallest number of servers__ so that extra servers __can be powered off__ during non-intensive hours.
    - it is recommended that a __cloud controller regularly__ checks server usage
    - This algorithm ignores the server weight, and brings more benefit to long session such as __RDP__ or __IMAP__ than __HTTP__,
  - __source:__ This ensures that the __same client IP__ address will always reach the __same server__ as long as no server goes down or up.
  - __uri:__:  This ensures that the __same URI__ will always be directed to the __same server__ as long as no server goes up or down.
    - This is used with __proxy caches__ and __anti-virus proxies__ in order to __maximize the cache hit rate__

* Others 
- url_param
- hdr(<name>)
- random(<draws>)
- rdp-cookie(<name>)

# Layer 4 and Layer 7 Proxy Mode

[source](https://www.haproxy.com/blog/layer-4-and-layer-7-proxy-mode/)


![osi](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-OSI%20model.jpg)

## Layer 4 load balancer
Set the <span style="background-color: yellow;">mode</span> to tcp.
```bash

defaults
    # mode is inherited by sections that follow
    mode tcp

frontend db
    # receives traffic from clients
    bind :3306
    default_backend databases

backend databases
    # relays the client messages to servers
    server db1 192.168.0.10:3306
    server db2 192.168.0.11:3306
```
- it has access to which __IP address__ and __port__ the client is trying to connect to on the backend server. It intercepts the messages by standing in for the server on the __expected address__ and port.
- Proxying at this layer is __lightweight__ and __fast__ because it is only concerned with transport. HAProxy __doesn’t read__ the messages,

* __hiding your internal__ network from the public Internet,
* __queuing connections__ to prevent server overload,
* __rate limiting__ connections
* It __works well for load balancing__ services that communicate over TCP such as __database traffic__ to __MySQL__, __Postgres__ and __Redis__ servers.


## Layer 7 Load balancer

Set the <span style="background-color: yellow;">mode</span> to http.

```bash
defaults
    # mode is inherited by sections that follow
    mode http

frontend www
    # receives traffic from clients
    bind :80
    default_backend web_servers

backend web_servers
    # relays the client messages to servers
    server s1 192.168.0.10:3000
    server s2 192.168.0.11:3000
```

- HAProxy can make __routing decisions__ based on any detail of a message that’s defined in __layers 4 through 7__.
  - __source__ and __destination IP__ addresses and __ports__
  - __SSL handshake metadata__
  - HTTP metadata including __headers__, __cookies__, __URL__and __method__

- In this mode, you get what you had with mode tcp, __but more__.
- based on information found in the __SSL handshake__, such as __SNI fields__.
- you can route to a specific set of servers based on the requested __URL path__.
- route based on the __HTTP headers received__,  __host__ or __cookie headers__.

- more sophisticated __health checking__, 
- ability to __rate limit__ requests.
- setting __new request or response headers__ on message as they pass through HAProxy,
- issuing __HTTP redirects__,
- enabling __Basic authentication__,
- introducing __cookie-based__ server persistence.