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


