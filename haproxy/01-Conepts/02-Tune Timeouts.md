# How to Tune Timeouts for Performance

## The Three Basic HAProxy Timeouts

- __Timeout Client:__  maximum time a client __can be inactive__ when connected to HAProxy server.
  - A common value for this timeout is __five minutes__.
  - as little as __thirty seconds__, if you’re attempting to __maximize security __
  - __HTTP mode:__
    - consider during the __first phase__, when the client __sends the request__
    - and during the __response__ while it is __reading data__ sent by the server. 
  - __TCP mode:__
    - it is highly recommended that the __client__ timeout remains __equal__ to the __server__ timeout
- __Timeout Connect:__ maximum time the client has to connect to a server.
  - allows the client to try to __connect again__ if the initial attempt fails.
  - In addition to the connection time, you’ll need to set the numbers of retries. The default is three, 
- __Timeout Server:__ When a client sends a request to the server, it expects a response. If the server doesn’t respond in the configured time duration, a <timeout server> is invoked.
   - if a <timeout serve> is invoked, you’ll get a 504 Gateway Timeout response from HAProxy.

## HAProxy Tuning for Good Performance

- __Timeout HTTP-Request:__  limits the total amount of time each request can persist. 
  - defend against denial of service attacks by limiting the the amount of time a single request can last.
  - Usually ten seconds is a good limit.
- __Timeout HTTP-Keep-Alive:__  timeout designed to keep a single connection between the client and the server “alive” for a desired amount of time. 
  -  While the connection is alive, all data packets can pass without needing to ask for a connection again. 
  - <timeout http-request> regulates how long a single request can persist,
  - so these two settings work hand in hand. If the <timeout http-keep-alive> isn’t set or has a value less than the <timeout http-request>, the latter is used to determine the connection status.
- __Timeout Queue:__  limits the number of concurrent connections, which can also impact performance.
  - etting the queue timeout shortens wait times by limiting connections and allowing clients try connecting again if the queue is full. 
  - If you don’t set the <timeout queue>, HAProxy will default 
- __Timeout Tunnel:__  variable only applies when you’re working with WebSockets. 
  - Essentially it’s <timeout keep-alive> on steroids, often with durations exceeding minutes. 
- __Timeout Client-Fin:__ Say a connection drops in the middle of a client request, if you look at the HAProxy logs you’re likely to see the lost connection is a result of client-side network issues. 
  - To handle these types of situations, HAProxy creates a list of dropped client side connections. 
  - he <timeout client-fin> limits the amount of time a client request will be maintained on this list. 
  - sort of connection while others are denied service. 
- __Timeout Server-Fin:__ abrupt disconnections can occur on the server side of the application, as well. An optimal setup would include redundant servers for load-balancing. When a server has too many requests, redundancy would allow you to reroute overflow requests to less busy servers and speed up response times. The <timeout server-fin> limits the time client waits for a server response before an alternate server is queried.


# Source:
[offical](http://cbonte.github.io/haproxy-dconv/2.2/configuration.html#4-timeout%20client)

[Solarwins](https://www.papertrail.com/solution/tips/haproxy-logging-how-to-tune-timeouts-for-performance/)