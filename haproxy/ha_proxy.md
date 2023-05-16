



## http evolution

![](/home/hojat/Pictures/haproxy/evolution-of-http.png)



## Proxys

forward proxy

revers proxy

layer 4 load balancer`

layer 7 load balancer



## Haproxy version

The 

[link]: http://www.haproxy.org/	""Official site""

 for versions



### Features

- Layer 4 and 7 load balancing (TCP and HTTP respectively)
- Protocol support for HTTP, HTTP/2, gRPC, FastCGI
- SSL/TLS termination
- Dynamic SSL certificate storage
- Content switching and inspection
- Transparent proxying
- Detailed logging
- CLI for server management
- HTTP authentication
- Multithreading
- [URL rewriting](https://www.techtarget.com/whatis/definition/URL-manipulation-URL-rewriting)
- Advanced health checking
- Rate limiting

## HAproxy is not

* Is not a web server like NGINX, IIS, Apache
* Is not a firewall, It is not design to filter traffic beween network. use ModSecurity or Citrix NetSaler
* Is not a forward proxy



## SSH

Host ha
  hostname 192.168.56.105
  port 22
  user user

Host web1
  hostname 192.168.57.11
  port 22
  user user
  proxyjump ha

Host web2
  hostname 192.168.57.12
  port 22
  user user
  proxyjump ha





## HAproxy installation

The

[https://haproxy.debian.net/#distribution=Ubuntu&amp;release=bionic&amp;version=2.6link]: www.google.com	"A guide"



[link]: www.haproxy.org	"cummunity"
[ Link ]: www.haproxy.com "Enterprice"

sudo apt install vim-haproxy



## web1 

```bash
sudo apt install nginx -y

cd /etc/nginx/sites-enabled/

vim default
server_name hojat.local;

service nginx restart
```



```bash
cd /var/www/html/
vim index.html
<h1>Welcome to hojat.local server web1 !</h1>
```



## web2

## 

```bash
sudo apt install nginx -y

cd /etc/nginx/sites-enabled/

vim default
server_name hojat.local;

service nginx restart
```



```bash
cd /var/www/html/
vim index.html
<h1>Welcome to hojat.local server web2 !</h1>
```



## Main configuration

````bash
vim /etc/haproxy/haproxy.cfg
global	# prcesss, security, log, threathing, 
	user # user which run haproxy
	daemon # run as daemon
	maxconn 5 # accept 5 request
	
defaults
	mode # http: layer 7 load balancer
		 # tcp : layer 4 load balancer
	timeout connect 5s # for backend server for first time
	timeout client 5m  # wait for client's answer
	timeout server 5h  # wait for backend server's answer
````



## listen configuration

```bash
listen default_back
        bind 192.168.56.105:80
        server webserver1 192.168.57.11:80 check
        server webserver2 192.168.57.12:80 check

```





## tcp mode - layer 4 loadbalancing

````bash
vim /etc/haproxy/haproxy.cfg
	
defaults
	mode http

frontend front_name
	bind 0.0.0.0:80
	mode tcp
	default_backend back_name
	
backend back_name
	mode tcp
	server srv_name1 192.168.57.11:80
	server srv_name2 192.168.57.12:80
	
sudo haproxy -c -f  /etc/haproxy/haproxy.cfg
sudo systemctl restart haproxy.service 
````

* Note: It is not load balancing, by default sticky session is enables.

*  Implement sticky sessions with a cookie. HAProxy can save a cookie in the user's browser to remember which server to send them back to.

  

## http mode - layer 7 loadbalancing

````bash
vim /etc/haproxy/haproxy.cfg
	
defaults
	mode http

frontend front_name
	bind 0.0.0.0:80
	default_backend back_name
	
backend back_name
	server srv_name1 192.168.57.11:80
	server srv_name2 192.168.57.12:80
	
sudo haproxy -c -f  /etc/haproxy/haproxy.cfg
sudo systemctl restart haproxy.service 
````



## Health check

````bash
vim /etc/haproxy/haproxy.cfg
	
defaults
	mode http

frontend front_name
	bind 0.0.0.0:80
	default_backend back_name
	
backend back_name
	server srv_name1 192.168.57.11:80 check
	server srv_name2 192.168.57.12:80 check
	
sudo haproxy -c -f  /etc/haproxy/haproxy.cfg
sudo systemctl restart haproxy.service 

# Web 1
sudo systemctl stop nginx.service
````



## Load balancing

````bash
vim /etc/haproxy/haproxy.cfg
	
defaults
	mode http

frontend front_name
	bind 0.0.0.0:80
	default_backend back_name
	
backend back_name
	balance roundrobin
	server srv_name1 192.168.57.11:80 weight 1 # 1/4 to srv_name1 # 0-255
	server srv_name2 192.168.57.12:80 weight 3 # 3/4 to srv_name2
	
sudo haproxy -c -f  /etc/haproxy/haproxy.cfg
sudo systemctl restart haproxy.service 
````



## disabled servers

````bash
vim /etc/haproxy/haproxy.cfg
	
defaults
	mode http

frontend front_name
	bind 0.0.0.0:80
	default_backend back_name
	
backend back_name
	balance roundrobin
	server srv_name1 192.168.57.11:80 weight 1 disabled
	server srv_name2 192.168.57.12:80 weight 0
	server srv_name3 192.168.57.13:80 weight 3 # responding server
	
sudo haproxy -c -f  /etc/haproxy/haproxy.cfg
sudo systemctl restart haproxy.service 
````



## ACL

### Basic

* Fetching sample: extract data from request or response stream (client, server, table, environmental)

* Content switching: take decisions based contenct (fetched data)

  * header parameter

  * url

  * uri

    

    ![](/home/hojat/Pictures/haproxy/Picture/url-structure-and-scheme-2022.png)

  

  ![](/home/hojat/Pictures/haproxy/Picture/param.png)

  

  ![](/home/hojat/Pictures/haproxy/Picture/param2.png)

  

  

  1. extract a data sample from s stream, table or the environment
  2. optionally apply some format conversion to the extracted sample
  3. apply one or multiple pattern matching methods on this sample
  4. perform action only when a pattern matches the sample.

### path check beg

```html
# web1
cat /var/www/html/api/auth/index.html 
<!DOCTYPE html>
<html>
<head>
<title>Auth API</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to Auth API server !</h1>
<p><em>This is the Auth API on my web1 server.</em></p>
</body>
</html>
```



```html
user@web2:~$ cat /var/www/html/api/log/index.html 
<html>
<head>
<title>Log API</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to log API server !</h1>
<p><em>This is the log API on my web2 server.</em></p>
</body>
</html>

```



```bash
user@ha:~$ sudo vim /etc/haproxy/haproxy.cfg 
frontend http80
        bind 192.168.56.105:80

        acl path_check1 path_beg    -i /api/auth
        #acl path_check2 path -m beg -i /api/log
        use_backend srv1 if path_check1
        use_backend srv2 if { path -m beg -i /api/log }

        default_backend webs

backend srv1
        server webserver1 192.168.57.11:80

backend srv2
        server webserver1 192.168.57.12:80

backend webs
        balance roundrobin
        server webserver1 192.168.57.11:80 check weight 1
        server webserver2 192.168.57.12:80 check weight 3

```



### path check len

```html
user@web1:~$ cat /var/www/html/len/one/two/three/index.html 
<!DOCTYPE html>
<html>
<head>
<title>Patch len</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to Patch len web1 !</h1>
<p><em>This is the Path len on my web1 server.</em></p>
</body>
</html>
```



```bash
user@ha:~$ sudo vim /etc/haproxy/haproxy.cfg 

frontend http80
        bind 192.168.56.105:80
        use_backend srv3 if { path -m len ge 2 }

backend srv3
        server webserver1 192.168.57.11:80
```



### TODO

### path check IP

path check end

```bash
root@web1:~# ls /var/www/html/pic/
param.png
```



```bash
frontend http80
        bind 192.168.56.105:80
        
        use_backend obj if { path_end -i .png .jpg .mp4 .mov }

backend obj
        server webserver1 192.168.57.11:80
```



### Query parameter str

```bash
frontend http80
        bind 192.168.56.105:80
        
        acl url_param_str_west url_param(region) -i -m str west sourh
        acl url_param_str_east url_param(region) -i -m str east north
        use_backend west if url_param_str_west
        use_backend east if url_param_str_east

backend obj
        server webserver1 192.168.57.11:80

backend west
        server webserver1 192.168.57.11:80
```



```bash
http://ha.hojat.local/?region=west
```



```bash
http://ha.hojat.local/?region=east
```



### Query parameter reg

```bash
frontend http80
        bind 192.168.56.105:80
        
        acl url_param_reg_akh url_param(word) -i -m str *.akhond.*
        (easg|child|hojat)
        use_backend akh if url_param_reg_akh

backend akh
        server webserver1 192.168.57.12:80
```



```bash
http://ha.hojat.local/akhond/?word=akhond
```



HTTP Header





