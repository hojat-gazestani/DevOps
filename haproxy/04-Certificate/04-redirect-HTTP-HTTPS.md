# Redirect HTTP to HTTPS

![scheme](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/06-UrlUri.png)

```bash
defaults
    mode http
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend redirect
        bind *443 ssl /certs/armangzni.ddns.net.pem
        mode http
        use_backend nginx

frontend redirect
        bind *:80
        mode http
        redirect scheme https if !{ssl_fc}

backend nginx
	server MyApp8010 192.168.56.22:443 ssh verify none

```