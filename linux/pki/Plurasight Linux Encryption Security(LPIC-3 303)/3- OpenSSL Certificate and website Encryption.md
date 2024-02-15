- [2-The openssl command line interface](#2-The-openssl-command-line-interface)
- [3-Generating a Certificate Signing Request](##3-Generating-a-Certificate-Signing-Request)
  - [Generate a CSR](#Generate-a-CSR)
- [4-Building-a-Private-Certificate-Authority](#4-Building-a-Private-Certificate-Authority)
  - [Generate CA root certificate](#Generate-CA-root-certificate)
  - [Generate a self-sign certificate to go with my root certificate](#Generate-a-self-sign-certificate-to-go-with-my-root-certificate)
- [5-Revoking a Certificate](#5-Revoking-a-Certificate)
	



## 2-The openssl command line interface

```commandline
sudo apt install openssl
sudo apt-cache search libssl
sudo apt install libssl1.1

openssl enc -help
openssl
```

## 3-Generating a Certificate Signing Request

### Generate a CSR
```commandline
openssl req -nodes -days 10 -newkey rsa:2048 -keyout keyfile.pem -out certfile.pem
IR
Tehran
Tehran
ArcFava
www.Arcfava.ir
info@gmail.com
password
[]

ls
certfile.pem keyfile.pem

openssl req -in certfile.pem -noout -verify -key keyfile.pem

openssl req -in certfile.pem -noout -text
```


## 4- Building a Private Certificate Authority
```commandline
mkdir ~/ArcFava-CA; cd ~/ArcFava-CA; mkdir certs private newcerts
echo '01' >  serial
touch index.txt

cp /etc/ssl/caconfig.cnf ~/ArcFava-CA
grep -v '^#'  /etc/ssl/openssl.cnf   > ~/ArcFava-CA/caconfig.cnf

vim ~/ArcFava-CA/caconfig.cnf
	[ CA_default ]
	dir			= /home/administrator/ArcFava-CA
	private_key     = $dir/privkey.pem

	[ tsa_config1 ]
	dir             = /home/administrator/ArcFava-CA
```

### Generate CA root certificate
```commandline
export OPENSSL_CONF=~/ArcFava-CA/caconfig.cnf

openssl req -x509 -newkey rsa:2048 -out cacert.pem -outform PEM -days 1825

mv privkey.pem private/cacert.pem

ls
cacert.pem

ls priavte
cakey.pem
```

### Generate a self-sign certificate to go with my root certificate
```commandline
vim testserver.cnf
	[req]
	distinguished_name	= server_distinguished_name
	x509_extensions 	= v3_req
	prompt 				= no

	[ server_distinguished_name ]
	commonName         		= www.testserver.com
	stateOrProvinceName 	= Tehran
	countryName        		= IR
	emailAddress        	= gazestani@arcfava.com
	organizationName    	= testserver
	organizationalUnitName 	= IT


	[v3_req]
	basicConstraints = CA:FALSE
	keyUsage = nonRepudiation, digitalSignature, keyEncipherment
	subjectAltName = @alt_names

	[alt_names]
	DNS.1 = www.ArcFava.com
	DNS.2 = Arcfava.com

export OPENSSL_CONF=~/ArcFava-CA/testserver.cnf
openssl req -newkey rsa:2048 -keyout basekey.pem -keyform PEM -out basereq.pem -outform PEM


export OPENSSL_CONF=~/ArcFava-CA/caconfig.cnf

openssl ca -in basereq.pem -out server_crt.pem

cat signedcerts/01.pem
```

### sign csr
```
openssl x509 -req -in ../first-crt.pem -days 365 -CA cacert.pem -CAkey private/cakey.pem -CAcreateserial -out ../first-crti.pem
```

## 5-Revoking a Certificate
```commandline
mkdir revoked
echo 1000  > crlnumbersudo
openssl ca -gencrl -config ~/my-ca/caconfig.cnf -out revoked/crl.pem
openssl crl -in revoked/crl.pem -noout -text

Openssl x509 -req -days 365 -in server.csr -signkey server.key -sha256           -out server.crt
openssl x509 -req -days 365 -sha256 -nodes  -newkey rsa:4096 -keyout private.key -out certificate.crt

openssl ca -config caconfig.cnf -revoke signedcerts/02.pem

openssl ca -gencrl -config ~/my-ca/caconfig.cnf -out revoked/crl.pem
openssl crl -in revoked/crl.pem -noout -text

ArcFava-CA
```

