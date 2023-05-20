# Proxy

* a proxy is a __general term__ for an __intermediary__ that handles client-server communication. 

![proxy](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-proxy.jpg)

- A proxy acts as an __intermediary__ between a client and a server.
- It can intercept and __forward requests and responses__ between the client and server.
- Proxies are often used for various purposes, such as __caching, security, and network optimization__.
- Proxies can be implemented at different layers of the network stack, including __application-layer__ proxies and __network-layer__ proxies.
- Proxies can be used in both __forward__ and __reverse__ proxy configurations.

# Forward Proxy:

* A forward proxy is __used by clients__ to access __resources on the internet__

![forward](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-%20forward%20proxy.jpg)

- A forward proxy, also known as a __client-side__ proxy, is used by clients to access __resources on the internet__.
- __Clients configure__ their applications or devices to send requests to the forward proxy server.
- The forward proxy server then __forwards the client's requests__ to the internet on behalf of the client.
- Forward proxies are commonly used to __bypass network restrictions__, __enhance privacy__, and __improve performance through caching__.
- __Block clients__ from visiting certain websites, __Monitor clients__ online activities

# Reverse Proxy:

* a reverse proxy is __used by servers__ to handle __incoming client requests__ and distribute them to __multiple backend servers__. 

![revers](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-reverse%20proxy.jpg)

- A reverse proxy, also known as a __server-side__ proxy, sits between clients and servers.
- Clients send requests to the reverse proxy, which then __forwards the requests to the appropriate server__.
- Reverse proxies are typically used to distribute incoming client requests across multiple servers (__load balancing__).
- They can also provide additional functionality like __SSL termination__, __caching__, __compression__, and __security measures__.
- Reverse proxies are often used in web server environments to __improve scalability__, __reliability__, and __security__.

# HAProxy is not :
- __forward HTTP proxy__: like Squid. the proxy that browsers use to reach the internet.
- __data scrubber__ : it will __not modify__ the body of requests nor responses.
- __static web server__: There are excellent open-source software for this such as __Apache__ or __Nginx__,
- __packet-based load balancer__ : it will not see IP packets nor UDP datagrams, will not perform NAT
- __firewall__: Providing the following features does not mean it is a firewall.
  - SSL/TLS Termination
  - Access Control
  - Rate Limiting
  - Request Filtering
  - HTTP Security Headers
  - SSL/TLS Configuration