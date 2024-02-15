- [Install Bind9 on Ubuntu-20.04](#Install-Bind9-on-Ubuntu-20.04)
- [1- What is DNS Encryption](#1--What-is-DNS-Encryption)
- [2- Build a Basic BIND Infrastructure](#2--Build-a-Basic-BIND-Infrastructure)
- [3- Generating DNSSEC Keys](#3--Generating-DNSSEC-Keys)
- [4- Working with DANE](#4--Working-with-DANE)
  - [Generating a TSLA Certificate](#Generating-a-TSLA-Certificate)
- [5-DNSSEC Administration](#5-DNSSEC-Administration)



# Install Bind9 on Ubuntu-20.04
```commandline
sudo apt install bind9 dnsutils -y


sudo nano /etc/bind/named.conf.local
	zone "arcloud.local" {
	        type master;
	        file "/etc/bind/db.arcloud.local";
	};

	zone "56.168.192.in-addr.arpa" {
		type master;
		file "/etc/bind/db.192.168.56";
	};

sudo vim /etc/bind/db.arcloud.local 
@       IN      SOA     arcloud.local. root.arcloud.local. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                          86400 )       ; Negative Cache TTL
;
@       IN      NS      ns.arcloud.local.
@       IN      A       192.168.56.11
@       IN      AAAA    ::1
ns      IN      A       192.168.56.11
test    IN      A       192.168.56.11
net     IN      A       192.168.56.12
net1    IN      A       192.168.101.201
net2    IN      A       192.168.101.202

sudo vim /etc/bind/db.192.168.56 
$TTL    604800
@       IN      SOA     arcloud.local. admin.arcloud.local. (
                              3         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
; name servers
      IN      NS      ns1.arcloud.local.
      IN      NS      ns2.arcloud.local.

; PTR Records
11   IN      PTR     ns1.arcloud.local.    ; 192.168.56.11
12   IN      PTR     ns2.arcloud.local.    ; 192.168.56.12
101  IN      PTR     host1.arcloud.local.  ; 192.168.56.101
102  IN      PTR     host2.arcloud.local.  ; 192.168.56.102


sudo named-checkconf
sudo systemctl restart bind9

nslookup ns1.arcloud.local 192.168.56.11
```

## 1- What is DNS Encryption
```commandline
DNSSEC Domain Request

sudo vim /etc/named.conf
	recursion no;

	dnssec-enable yes;
	dnssec-validation yes;
	dnssec-lookasid auto;

	bindkeys-file "/etc/named.iscdlv.key";
	managed-keys-directory "/var/named/dynamic";

DNSSEC Resource Record Types
	DS (Delegation Signer)
	DNSKEY
	PRSIG
	NSEC / NSEC3 / NSEC3PARAM
	TLSA

Base environment
DNSSEC keypari generation
Configuration testing
DANE protocol
DNSSEC Administration
```

### 2- Build a Basic BIND Infrastructure


> yum install bind bind-utils
```commandline
sudo vim /etc/named.conf
sudo vim /etc/bind/named.conf
	# listen-on port 53 { 127.0.0.1 }; # comment to listen to any IPv4 port
	recursion no;	# no to run this server as authoritabe server

	dnssec-enable yes;
	dnssec-validation yes;
	dnssec-lookasid auto;	# load DLV that should come along with bind installation file

	zone "stuff.com" IN {
		type master;
		file "/var/named/stuff.com.zone";
	}
```
> systemctl restart named 

### 3- Generating DNSSEC Keys
```commandline
Generate keys
Sign zone keys
Apply and confirm

yum install epel-release
yum install haveged

haveged -r 0
centos# cd /var/named
ubuntu# cd /var/cach/bind/

dnssec-keygen -a NSEC3RSASHA1 -b 2048 -n ZONE stuff.com
dnssec-keygen -f KSK -a NSEC3RSASHA1 -b 4096 -n ZONE stuff.com

ls
kstuff.com.1..key
kstuff.com.1..private
kstuff.com.2..key
kstuff.com.3..private

echo kstuff.com.1..key >> stuff.com.zone
echo kstuff.com.2..key >> stuff.com.zone


vim stuff.com.zone
	...
	$INCLUDE Kstuff.com..
	%INCLUDE Kstuff.com..

dnssec-signzone -A -3 $(head -c 1000 /dev/random | sha1sum | cut -b 1-16) -N INCREMENT -o stuff.com -t stuff.com.zone

ls 
dsset-stuff.com.
stuff.com.zone.signed

sudo vim /etc/named.conf
...
file "var/named/stuff.com.zone.signed";

sudo systemctl restart bind

dig DNSKEY stuff.com.zone @localhost +multiline
dig A stuff.com. @localhost +noadditional +dnssec +multiline
cat dsset-stuff.com.
```

## 4- Working with DANE
> DNS-based Authentication of Named Entities (DANE)

### Generating a TSLA Certificate
```commandline
openssl x509 -in servername_crt.pem -outform DER | openssl sha256
```

## 5-DNSSEC Administration
```commandline
Automating key rollover
TSIG Key creation
Remote administation through RNDC

dnssec-keygen -a RSASHA256 -b 2048 -n ZONE -P +1d -A +4d -I +34d -D +44d stuff.com
dnssec-settime -p all Kstuff.com.1....key

dnssec-settime -I +2mo -D +10w Kstuff.com.1..key 
dnssec-settime -p all Kstuff.com.1....key

dnssec-keygen -a HMAC-MD5 -b 128 -n HOST tsigkey KtsigKey.+... 

cat Ktsigkey...private

sudo vim /etc/named.con
	..
	key tsignkey {
		algorithm hmac-md5;
		secret "secret key"
	}
	zone "stuff.com" IN {
		...
		allow-update {key tsignkey ; };
	};

	controls {
		inet 127.0.0.1 allow { localhost }
		keys { tsignkey; };
	};

sudo vim /etc/rndc.conf
	key tsigkey {
		algorithm hmac-md5;
		secret "secret-key";
	}
```