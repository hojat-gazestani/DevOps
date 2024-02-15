# PAM

## Automatin Home Directory creation at user login
```bash
ls /etc/pam.d/
ls /lib64/security/
ls /etc/security/

sudo vi /etc/login.defs
CREATE_HOME no

sudo useradd bob
ls /home

grep bob /etc/passwd

sudo passwd bob
rpm -qa | grep oddjob

systemctl start oddjobd
systemctl enable oddjobd

sudo authconfig --enablemkhomedir --update
sudo -i
cd /etc/pam.d
grep mkhomedir *

su - bob
```

## Implementing Password Policies
```bash
cat /etc/pam.d/system-auth
password	requisite	pam_pwquality.so 

less /etc/security/pwquality.conf 
pwscore
```
## Restrictin or Limiting access to resources
```bash
ulimit 
ulimit -u
ulimit -u 10

sudo vi /etc/security/limit.conf
@users soft nproc 50
@users hard nproc 75

id -Gn

ulimit -u
```

# LDAP

## Insallation OpenLDAP
```bash
hostname
server1.example.com

su -

ip a s
echo "192.168.56.105 server1.example.com" >> /etc/hosts
ping server1.example.com

netstat -ltn

firewall-cmd --permanent --add-service=ldap
firewall-cmd --reload

yum install -y openldap openldap-clients openldap-servers migrationtools.noarch
```
## Configure OpenLDAP
```bash
cp /usr/share/openldap-servers/DB_CONF.example /var/lib/ldap/DB_CONFIG

ls /var/lib/ldap/
slaptest
chown ldap.ldap /var/lib/ldap/*

systemctl start slapd
systemctl enable slapd

netstat -ltn
		::389
		
netstat -lt
		::ldap
		
cd /etc/openldap/schema/
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f consine.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -D "cn=config" -f nis.ldif

cd
slappasswd -s Password1 -n > rootpwd
cat rootpwd

vi config.ldif
olcSuffix: dc=example,dc=com
olcRootDN: cn=Manager, dc=example, dc=com
olcRootPW: [ESC] :r rootpwd
olcLogLevel: 0

ldapmodify -Y EXTERNAL -H ldapi:/// -f config.ldif
```

## Create Directory Structure
```bash
cat structure.ldif

ldapadd -X -W -D "cn=Manager,dc=example,dc=com" -f structure.ldif
ldapsearch -x -W -D "cn=Manager,dc=example,dc=com" -b "dc=example,dc=com" -s sub "(objectclass=organizationalUnit)"
```

## Adding User and Groups
```bash
cat group.ldif
ldapadd -X -W -D "cn=Manager,dc=example,dc=com" -f group.ldif

cd /usr/share/migrationtools
vim migrate_common.ph
$DEFAULT_MAIL_DOMAIN = "example.com"
$DEFAULT_BASE = "dc=example,dc=com"

cd
grep tux /etc/passwd
grep tux /etc/passwd > passwd

/usr/share/migrationtolls/migrate_passwd.pl passwd user.ldif
vi user.ldif
dn: uid=fred
uid=fred
cn=fred
uidNumber: 4000
gidNumber: 4000
homeDirectory: /home/fred
gecos: fred bloggs

ldapadd -X -W -D "cn=Manager,dc=example,dc=com" -f user.ldif
```

## OpenLDAP Client
```bash
tux@server2$ su -
echo "192.168.56.105 server1.example.com" >> /etc/hosts
ping server1.example.com

yum install oddjob oddjob-
systemctcl start oddjob
systemctcl enable oddjob

yum install openldap-clents nss-pam-ldapd

authconfig-tui
ldap://server1.example.com
authconfig --enableldap --ldapserver=server1.example.com --ldapbasedn="dc=example,dc=com" --enablemkhomedir --update
grep passwd /etc/nsswitch.conf

getnt passwd

su - fred
```

## listing users and groups
```bash
root@server2$ getent passwd
getent group
grep ldap /etc/nsswitch.conf

vim /etc/nsswitch.conf
services:	files sss
automount:	files

ssh tux@server1
getent passwd
getent group
```

## Searching LDAP Users
```bash
root@server2# ldapsearch -x -H ldap://server1.example.com -b dc=example,dc=com
root@server2# ldapsearch -x -LLL -H ldap://server1.example.com -b dc=example,dc=com
root@server2# ldapsearch -x -LLL -H ldap://server1.example.com -b dc=example,dc=com "(objectclassaccount=account)"
root@server2# ldapsearch -x -LLL -H ldap://server1.example.com -b dc=example,dc=com "(&(objectclassaccount=account)(uid=fred))"
root@server2# ldapsearch -x -LLL -H ldap://server1.example.com -b dc=example,dc=com "(&(objectclassaccount=account)(uid=fred))" uidNumbr uid

root@server2# ldapsearch -x -LLL -H ldap://server1.example.com -b dc=example,dc=com "(&(objectclassaccount=account)(uid=fred))" > newuser.ldif
vim !$
:%s/fred/sally/g
uidNumber: 4001
gidNumber: 4000

root@server2# ldapsearch -x -W -D cn=Manager,dc=example,dc=com -f newuser.ldif

getent passwd

su sally
```

# Implementing Kerboros Authentication

## Configuring NTP
```bash
root@server1# yum install -y ntp
vim /etc/ntp.conf
restrict 192.168.56.0 mask 255.255.255.0 nomodify notrap
systemctl enable ntpd
systemctl start ntpd

ntpq -p

firewall-cmd --add-service=ntp --permanent
firewall-cmd --reload

echo "192.168.56.104 server2.example.com" >> /etc/hosts

ssh tux@server2
su -

yum install -y ntp
vim /etc/ntp.conf
server server1.example.com iburst prefer

systemctl enable ntpd
systemctl start ntpd

ntpq -p
```

## Install and Configure KDC
```bash
yum install -y rng-tools

systemctl start rngd
vim /usr/lib/systemd/system/rngd.service

ExecStart=/sbin/rngd -f -r /dev/urandom
systemctl daemon-reload
systemctl start rngd

yum install -y krb5-server krb5-workstation pam_krb5

cd /var/kerberos/krb5kdc/
cat kadm5.acl
*/admin@EXAMPLE.COM	*

vi kdc.conf

vi /etc/krb5.conf
default_realm = EXAMPLE.COM

[realms]
  EXAMPLE.COM = {
    kdc = server1.example.com
    admin_server = server1.example.com
  }
  
[domain_realm]
 .example.com = EXAMPLE.COM
 example.com = EXAMPLE.COM
:x

/var/kerberos/krb5kdc/ $ kdb5_util create -s -r EXAMPLE.COM

/var/kerberos/krb5kdc/ $ ls

systemctl start krb5kdc kadmin
systemctl enable krb5kdc kadmin
```

## Adding kerberos principals
```bash
root@server1 # netsat -lt

firewall-cmd -add-service=kpasswd --permanent
firewall-cmd -add-service=kerberos --permanent
firewall-cmd -add-port=749/tcp --permanent
firewall-cmd --reload

kadmin.local
listprincs

addprinc root/admin
addprinc tux
addprinc -randkery host/server1.example.com

listprincs

ktadd host/server1.example.com
quit
```

## Enabling kerberos authentication
* Authenticate to SSH
```bash
root@server1 # vi /etc/ssh/ssh_config
GSSAPIAuthentication yes
GSSAPIDelegateCredentials yes

systemctl reload sshd

authconfig --enablekrb5 --update
exit
tux@server1 $ klist
kinit
klist

ssh server1.example.com

kdestroy
lkist
```

## Adding Additional hosts
```bash
tux@server2 $ su -
echo "192.168.56.104 server1.example.com" >> /etc/hosts

yum install -y krb5-workstation pam_krb5

scp tux@server1.example.com:/etc/krb5.conf /etc/

kadmin
listprincs
addprincs -randkey host/server2.example.com
listprincs
ktadd host/server2.example.com
quit

vim /etc/ssh/ssh_config
GSSAPIAuthentication yes
GSSAPIDelegateCredentials yes

suthconfig-tui
systemctl reload sshd

klist
exit

lkist
kinit
```

  


