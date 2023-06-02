## ssl passthrough

![pass](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/04-certificate/02-SSL-Passthrough.jpg)

```bash
defaults
    mode tcp
    timeout client 30s
    timeout connect 10s
    timeout server 30s

frontend sshPass
	bind *:80
	use_backend nginx

backend nginx
	server MyApp8010 192.168.56.22:443

```