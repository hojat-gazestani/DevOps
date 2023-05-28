# Health check

## HTTP message

* HTTP is an asymmetric request-response client-server protocol as illustrated.  An HTTP client sends a request message to an HTTP server.

![01-ReqRes](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/01-ReqRes.png)

* First line in request: Start line - First line in response: Status line

![02-ReqRes](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/02-ResResHead.png)

* HTTP defines a set of request [methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) to indicate the desired action to be performed for a given resource.

- [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET): requests a representation of the specified resource. Requests using GET should __only retrieve data__.
- [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD): asks for a response identical to a GET request, but __without the response body__.
- [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST): submits an entity to the specified resource, often causing a __change in state__ or side effects on the server.
- [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT): __replaces__ all current representations of the target resource with the request payload.



![03](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/03-ReqMess.png)


* The following shows a sample response message:

![04](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/04-ResMess.png)

1. [Informational responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#information_responses) (100 – 199)
2. [Successful responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses) (200 – 299)
3. [Redirection messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages) (300 – 399)
4. [Client error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses) (400 – 499)
5. [Server error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (500 – 599)




# Source
[ReqRes](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html)

[haproxy](https://www.haproxy.com/blog/how-to-enable-health-checks-in-haproxy/)

[enterprice](https://www.haproxy.com/documentation/aloha/latest/load-balancing/health-checks/http/)

[mozila](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)