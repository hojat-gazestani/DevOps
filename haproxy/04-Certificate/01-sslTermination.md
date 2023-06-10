# SSL Termination

![01-ssltermination](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/04-certificate/01-SSL-Termination.jpg)

* __compromised__  server included certificate
```bash
sudo ls /etc/letsencrypt/live/armangzni.ddns.net
README	cert.pem  chain.pem  fullchain.pem  privkey.pem

mkdir certs && cd /certs
cat fullchain.pem privkey.pem > /certs/arman-main.pem

sudo mkdir /var/lib/haproxy/certs
sudo mount --bind /certs /var/lib/haproxy/certs

sudo vim /etc/fstab
/certs /var/lib/haproxy/certs   none defaults,bind      0 0
```

```bash
frontend sshTerm
        bind *:443 ssl /certs/armangzni.ddns.net.pem
        mode http
        default backend myapp

backend myapp
        server MyApp8010 192.168.56.22:8010
```