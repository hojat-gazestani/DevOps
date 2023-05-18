# How to Tune Timeouts for Performance

1. Timeout Client:  maximum time a client can be inactive when connected to the server.
   2. A common value for this timeout is five minutes.
   3.  as little as thirty seconds, if you’re attempting to maximize security 

2. Timeout Connect: maximum time the client has to connect to a server.
   3.  allows the client to try to connect again if the initial attempt fails.
   4. In addition to the connection time, you’ll need to set the numbers of retries. The default is three, 
3. Timeout Server: When a client sends a request to the server, it expects a response. If the server doesn’t respond in the configured time duration, a <timeout server> is invoked.
   4.  if a <timeout serve> is invoked, you’ll get a 504 Gateway Timeout response from HAProxy.

- Timeout Client:  maximum time a client can be inactive when connected to the server.
  - A common value for this timeout is five minutes.
  - as little as thirty seconds, if you’re attempting to maximize security 
- Timeout Connect: maximum time the client has to connect to a server.
  - allows the client to try to connect again if the initial attempt fails.
  - In addition to the connection time, you’ll need to set the numbers of retries. The default is three, 
- Timeout Server: When a client sends a request to the server, it expects a response. If the server doesn’t respond in the configured time duration, a <timeout server> is invoked.
   - if a <timeout serve> is invoked, you’ll get a 504 Gateway Timeout response from HAProxy.