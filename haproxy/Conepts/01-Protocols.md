# TCP
* The TCP [rfc](https://www.ietf.org/rfc/rfc793.txt)

![img.png](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-tcp.png)



* Three way handshake

![ThreeWay](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/04-three-way-handshake.png)


* Timing events

![events](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/05-Timing%20events.png)


* Client to HAProxy and then to Server [rfc](http://cbonte.github.io/haproxy-dconv/2.4/configuration.html#8.4)

![timing](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/06-%20Time%20events.png)

```text
Tq:
    - total time to get the client request from the accept date (Th + Ti + TR)
    TH: total time to accept tcp connection and execute handshakes
    Ti: is the idle time before the HTTP request
    TR: total time to get the client request
    
Tw: the time needed for the server to complete previous requests
Tc: between the moment the proxy sent the connection request, and the moment it was acknowledged by the server
Tr: between the moment the TCP connection was established to the server and the moment the server sent its complete response headers.
```
