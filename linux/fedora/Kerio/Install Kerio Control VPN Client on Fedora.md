Install Kerio Control VPN Client on Fedora
==========================================

### Download DEB file
```
Download  'Kerio Control VPN Client .deb'
https://www.gfi.com/products-and-solutions/network-security-solutions/kerio-control
```

### Installation
```
sudo dnf install alien
alien -r --scripts kerio-control-vpnclient-%VERSION%-linux-amd64.deb
sudo rpm -ivh kerio-control-vpnclient-%VERSION%-linux-amd64.rpm --replacefiles
sudo chkconfig kerio-kvc on
```

### commands to control VPN Client
```
sudo systemctl start kerio-kvc
sudo systemctl stop kerio-kvc
sudo systemctl enable kerio-kvc
sudo systemctl disable kerio-kvc
sudo systemctl status kerio-kvc
```

### Configuration
```
sudo nano /etc/kerio-kvc.conf
 <config>
   <connections>
     <connection type="persistent">
       <server>%SERVER%</server>
       <port>4090</port>
       <username>%USERNAME%</username>
       <password>%PASSWORD%</password>
       <fingerprint>%FINGERPRINT%</fingerprint>
       <active>1</active>
     </connection>
   </connections>
 </config>

```

### Obtaining the fingerprint
```
openssl s_client -connect %HOST%:%PORT% < /dev/null 2>/dev/null | openssl x509 -fingerprint -md5 -noout -in /dev/stdin
```