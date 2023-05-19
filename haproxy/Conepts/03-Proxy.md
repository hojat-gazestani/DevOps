# Proxy

* a proxy is a general term for an intermediary that handles client-server communication. 

![proxy](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-proxy.jpg)

- A proxy acts as an __intermediary__ between a client and a server.
- It can intercept and __forward requests and responses__ between the client and server.
- Proxies are often used for various purposes, such as __caching, security, and network optimization__.
- Proxies can be implemented at different layers of the network stack, including __application-layer__ proxies and __network-layer__ proxies.
- Proxies can be used in both __forward__ and __reverse__ proxy configurations.

# Forward Proxy:

* A forward proxy is used by clients to access resources on the internet

![forward](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-%20forward%20proxy.jpg)

- A forward proxy, also known as a __client-side__ proxy, is used by clients to access __resources on the internet__.
- __Clients configure__ their applications or devices to send requests to the forward proxy server.
- The forward proxy server then __forwards the client's requests__ to the internet on behalf of the client.
- Forward proxies are commonly used to __bypass network restrictions__, __enhance privacy__, and __improve performance through caching__.

# Reverse Proxy:

* a reverse proxy is used by servers to handle incoming client requests and distribute them to multiple backend servers. 

![revers](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-reverse%20proxy.jpg)

- A reverse proxy, also known as a __server-side__ proxy, sits between clients and servers.
- Clients send requests to the reverse proxy, which then __forwards the requests to the appropriate server__.
- Reverse proxies are typically used to distribute incoming client requests across multiple servers (__load balancing__).
- They can also provide additional functionality like __SSL termination__, __caching__, __compression__, and __security measures__.
- Reverse proxies are often used in web server environments to __improve scalability__, __reliability__, and __security__.