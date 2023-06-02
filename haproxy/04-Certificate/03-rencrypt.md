# rencrypting 

![rencry](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/04-certificate/03-SSL-Rencryption.jpg)

```bash
frontend sshTerm
        bind *443 ssl /certs/armangzni.ddns.net.pem
        mode http
        default backend myapp

backend myapp
        server MyApp8010 192.168.56.22:8010 ssl verify none

```