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
- [DELET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) : deletes the specified resource.
- [OPTIONS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS) : requests __permitted communication__ options for a given URL or server. A client can specify __a URL__ with this method, or an __asterisk (*)__ to refer to the __entire server__.

![03](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/03-ReqMess.png)


* The following shows a sample response message:

![04](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-healthCheck/04-ResMess.png)

1. [Informational responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#information_responses) (100 – 199)
2. [Successful responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses) (200 – 299)
3. [Redirection messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages) (300 – 399)
4. [Client error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#client_error_responses) (400 – 499)
5. [Server error responses](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (500 – 599)

## Enable Health Checks in HAProxy

* HAProxy makes your web applications __highly available__ by spreading requests across a __pool of backend servers__. If one or even several servers fail, clients can still use your app as long as there are __other servers still running__.
* HAProxy needs to know which servers are __healthy__. That’s why health checks are crucial. Health checks __automatically detect__ when a server becomes unresponsive or begins to __return errors__.
* HAProxy can then __temporarily remove__ that server from the pool __until__ it begins to __act normally again__.

### Active Health Checks
* attempting to connect at a __defined interval__.
* If HAProxy __doesn’t__ get a __response back__, it determines that the server __is unhealthy__ and after a certain number of failed connections, it __removes__ the server from the rotation.

```bash
backend webservers
  server server1 192.168.50.2:80 check
  server server2 192.168.50.3:80 check
  server server3 192.168.50.4:80 check  
```

- Default
  - every __two seconds__
  - After __three failed__ connections, the server __is removed__, temporarily
  - __until__ HAProxy gets __at least two successful__ connections,

```bash
server server1 192.168.50.2:80 check  inter 10s  fall 5  rise 5
```
* The __inter__ parameter changes the __interval between checks__
* The __fall__ parameter sets __how many failed checks__ are allowed;
* The __rise__ parameter sets how many __passing checks__ there __must__ be before returning a previously failed server __to the rotation__;

#### TCP Checks

* sends out a __simple packet__ and waits for a __reply__ back from the __destination server__.
* This verifies that the __network interface__ on the host being checked __is online__.
* What it __won’t do__ is tell whether the __service__ being hosted by the backend server __is healthy__.

##### Mail Server Health Checks

```bash
listen smtpcluster1 0.0.0.0:8080
    mode tcp
    server smtp1 10.0.0.1:25 check fall 3 rise 2
    server smtp2 10.0.0.2:25 check fall 3 rise 2
```

##### Memcached Cluster

```bash
listen memcachedcluster 0.0.0.0:8080
    mode tcp
    server memcached1 10.0.0.1:11211 check fall 3 rise 2
    server memcached2 10.0.0.2:11211 check fall 3 rise 2
```

##### Redis Cluster

```bash
listen rediscluster 0.0.0.0:8080
    mode tcp
    server redis1 10.0.0.1:6379 check fall 3 rise 2
    server redis2 10.0.0.2:6379 check fall 3 rise 2
```

##### MYSQL Checks

```bash
mysql -u root -p
INSERT INTO mysql.user (Host,User) values ('10.0.0.10','haproxy_check');
FLUSH PRIVILEGES;

sudo apt-get install mysql-client
```

```bash
listen mysql-cluster
    mode tcp
    option mysql-check user haproxy_check
    balance roundrobin
    server mysql1 10.0.0.1:3306 check
    server mysql2 10.0.0.2:3306 check
```
#### HTTP Checks

* verify that a __specific website URL__ is healthy. 
* If it returns a __status 200 or 300__ response, everything is __good__. 
* Anything above that, such as a __500 status__ response, will be considered __bad health__ and HAProxy will mark the backend __server as offline__

```bash
backend webservers
  option httpchk
  server server1 192.168.50.2:80 check
  server server2 192.168.50.3:80 check
  server server3 192.168.50.4:80 check
```

- By default __GET request to the URL path /__

*  we send a __GET request to the URL path /health__

```bash

backend webservers
  option httpchk
  http-check send meth GET  uri /health
  server server1 192.168.50.2:80 check
  server server2 192.168.50.3:80 check
  server server3 192.168.50.4:80 check
```

* To send a POST request with a JSON body, use this form, which includes a Content-Type request header and a message body:
```bash

backend webservers
  option httpchk
  http-check send meth POST  uri /health  hdr Content-Type application/json  body "{ \"foo\": \"bar\" }"
  server server1 192.168.50.2:80 check
  server server2 192.168.50.3:80 check
  server server3 192.168.50.4:80 check
```

- use a HEAD request against the index page of your domain using HTTP version 1.0.
```bash
listen myapp2 0.0.0.0:8080
    mode http
    option httpchk HEAD / HTTP/1.0
    server node1 10.0.0.1:80 check fall 3 rise 2
    server node2 10.0.0.2:80 check fall 3 rise 2
```
-  This check will use a HEAD request against a specific URL using HTTP version 1.1. It also sets the domain name, which is needed for backends that use virtual hosts.
```bash
listen myapp2 0.0.0.0:8080
   mode http
   option httpchk HEAD /health_check.php HTTP/1.1\r\nHost:\ serverlab.com
   server node1 10.0.0.1:80 check fall 3 rise 2
   server node2 10.0.0.2:80 check fall 3 rise 2
```

### Passive Health Checks

### Agent Health Checks


## Source
[ReqRes](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/http_basics.html)

[haproxy](https://www.haproxy.com/blog/how-to-enable-health-checks-in-haproxy/)

[enterprice](https://www.haproxy.com/documentation/aloha/latest/load-balancing/health-checks/http/)

[mozila](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)