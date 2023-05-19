# Proxy

* a proxy is a general term for an intermediary that handles client-server communication. 

![proxy](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-proxy.jpg)

- A proxy acts as an intermediary between a client and a server.
- It can intercept and forward requests and responses between the client and server.
- Proxies are often used for various purposes, such as caching, security, and network optimization.
- Proxies can be implemented at different layers of the network stack, including application-layer proxies and network-layer proxies.
- Proxies can be used in both forward and reverse proxy configurations.

# Forward Proxy:

* A forward proxy is used by clients to access resources on the internet

![forward](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/02-%20forward%20proxy.jpg)

- A forward proxy, also known as a client-side proxy, is used by clients to access resources on the internet.
- Clients configure their applications or devices to send requests to the forward proxy server.
- The forward proxy server then forwards the client's requests to the internet on behalf of the client.
- Forward proxies are commonly used to bypass network restrictions, enhance privacy, and improve performance through caching.

# Reverse Proxy:

* a reverse proxy is used by servers to handle incoming client requests and distribute them to multiple backend servers. 

![revers](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-reverse%20proxy.jpg)

- A reverse proxy, also known as a server-side proxy, sits between clients and servers.
- Clients send requests to the reverse proxy, which then forwards the requests to the appropriate server.
- Reverse proxies are typically used to distribute incoming client requests across multiple servers (load balancing).
- They can also provide additional functionality like SSL termination, caching, compression, and security measures.
- Reverse proxies are often used in web server environments to improve scalability, reliability, and security.