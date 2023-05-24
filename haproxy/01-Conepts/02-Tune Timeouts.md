# How to Tune Timeouts for Performance

# Time format
  - us : microseconds. 1 microsecond = 1/1000000 second
  - ms : milliseconds. 1 millisecond = 1/1000 second. This is the default.
  - s  : seconds. 1s = 1000ms
  - m  : minutes. 1m = 60s = 60000ms
  - h  : hours.   1h = 60m = 3600s = 3600000ms
  - d  : days.    1d = 24h = 1440m = 86400s = 86400000ms

# Timeouts are not the problem!
- when hitting a timeout, your first reaction should __not be to increase__ the timeout.
- You should investigate why something is taking so long that you hit a timeout somewhere and fix the root cause.
  - push long running jobs to the background
  - queueing mechanisms

## The Three Basic HAProxy Timeouts

- __Timeout Client:__  maximum __inactivity__ time on the client side. when the client is expected to __acknowledge or send data__.
  - A common value for this timeout is __five minutes__.
  - as little as __thirty seconds__, if you’re attempting to __maximize security __
  - __HTTP mode:__
    - consider during the __first phase__, when the client __sends the request__
    - and during the __response__ while it is __reading data__ sent by the server. 
  - __TCP mode:__
    - it is highly recommended that the __client__ timeout remains __equal__ to the __server__ timeout
- __Timeout Connect:__ maximum time to wait for a __connection attempt__ to a server to succeed.
  -  it applies to the __server__, not the client
  - only applies to the __connection phase__, not the transfer of data 
- __Timeout Server:__ maximum __inactivity__ time on the server side. server is expected to __acknowledge or send data__.
  - HTTP mode:
    - consider during the first phase of the server's response, when it has to send the headers
    - server's processing time for the request.
    - value to put there, considered as unacceptable response times,
  - TCP mode:
    - it is highly recommended that the client timeout remains equal to the server timeout
  - if a <timeout serve> is invoked, you’ll get a 504 Gateway Timeout response from HAProxy.

## HAProxy Tuning for Good Performance

- __Timeout HTTP-Request:__ maximum allowed time to __wait for a complete HTTP request__
  - defend against denial of service __(DOS, Slow loris)__ attacks by limiting the amount of time a __single request can las__t.
    - will open as __many connections__ and __keep them open__ to consume all possible sockets
    - thereby __denying other people access__ and effectively ‘closing down’ the host.
  - Usually __ten seconds__ is a good limit.
  ![slow](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-concept/02-slow-loris.jpg)
- __Timeout HTTP-Keep-Alive:__  maximum allowed time to wait for a __new HTTP request__ to appear
  -  While the connection is alive, all data packets can pass __without__ needing to ask for a __connection again__. 
  - <timeout http-request> regulates how long a single request can persist,
  - so these two settings work hand in hand. If the __timeout http-keep-alive__ isn’t set or has a value less than the __timeout http-request__, the latter is used to determine the connection status.
  - ![keepalive](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/01-concept/01-keepalive.png) 
- __Timeout Queue:__  maximum time to __wait in the queue__ for a connection slot to be free, which can also __impact performance__.
  - If you do __not set__ it, __timeout connect__ will be used instead
- __Timeout Tunnel:__  maximum __inactivity time__ on the client and server side for __tunnels__. e.g. WebSockets.  
- __Timeout Client-Fin:__ __inactivity timeout__ on the __client side__ for __half-closed connections__.
  - Say a connection drops in the middle of a client request, if you look at the HAProxy logs you’re likely to see the lost connection is a result of __client-side network issues__. 
  - To handle these types of situations, HAProxy creates a list of __dropped client side connections__.
- __Timeout Server-Fin:__ Exactly the same as the client side version, but for the server side


# Source:
[offical](http://cbonte.github.io/haproxy-dconv/2.2/configuration.html#4-timeout%20client)

[Solarwins](https://www.papertrail.com/solution/tips/haproxy-logging-how-to-tune-timeouts-for-performance/)

[delta](https://delta.blue/blog/haproxy-timeouts/)