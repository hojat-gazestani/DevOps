## Configuring the Primary DNS Server
```shell
sudo apt update
sudo apt install bind9 bind9utils bind9-doc

sudo vim /etc/bind/named.conf.options
options {
	directory "/var/cache/bind";

	dnssec-validation auto;

	auth-nxdomain no;    # conform to RFC1035
	listen-on-v6 { any; };
};
```

### Configuring the Local File
```shell
sudo vim /etc/bind/named.conf.local
zone "arccloud.ir" {
        type master;
        file "/etc/bind/db.arccloud.ir";
};

zone "91.98.100.118.in-addr.arpa"{
        type master;
        file "/etc/bind/rev.91.98.100.1.in-addr.arpa";
};
```

### Creating the Forward Zone File
```shell
sudo vim /etc/bind/db.arccloud.ir
$TTL	604800
@	IN	SOA	ns1.arccloud.ir. info.arccloud.ir. (
			      7		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;

; name servers - NS records
@       IN      NS      ns1.arccloud.ir.

; name servers - A records
ns1     IN      A       91.98.100.1
ns1.arccloud.ir.	IN	A	91.98.100.1

; A records
www		IN	A	92.99.101.1
```
* test
sudo named-checkzone ns1.arccloud.ir /etc/bind/db.arccloud.ir 
### Creating the Reverse Zone File(s)
```shell
sudo vim /etc/bind/rev.100.98.91.in-addr.arpa
$TTL 1500
@  IN SOA ns.arccloud.ir. info.arccloud.ir. (
                             2007062703        ;serial
                             28800             ;refresh
                             3600              ;retry
                             604800            ;expire
                             38400 )           ;minimum 25 minutes

@                  IN    NS     ns.
1                  IN    PTR    ns1.arccloud.ir.
```