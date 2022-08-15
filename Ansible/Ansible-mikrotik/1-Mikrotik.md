[TOC]





# Mikrotik



## Preparing the Linux 



Generate SSH keys in Linux

```bash
ssh-keygen -t rsa
```



Copy Linux SSH pullic key to Mikrotik

```
ssh 192.168.88.1 "/file print file=mykey; file set mykey contents=\"`cat ~/.ssh/id_rsa.pub`\";/user ssh-keys import public-key-file=mykey.txt;/ip ssh set always-allow-password-login=yes"
```



Accepted Algorighems for SSH

```bash
cat ~/.ssh/config 
host 172.31.31.*
        PubkeyAcceptedAlgorithms +ssh-rsa
        KexAlgorithms +diffie-hellman-group1-sha1
        HostKeyAlgorithms +ssh-dss

```



## Ansible

Ansible inventory file

```bash
[mikrotik]
172.31.31.3

[mikrotik:vars]
ansible_user=admin
ansible_password=123
ansible_connection=ansible.netcommon.network_cli
ansible_network_os=community.routeros.routeros
ansible_python_interpreter=/usr/bin/python3
ansible_command_timeout=120

```



install reouteros collection

```bash
ansible-galaxy  collection install  routeros_commnad
```



## MikroTik Router SNMPv2 Configuration



```bash
snmp set enabled=yes
snmp community set name=password 0
snmp community add name=Hojat
snmp set contact="Hojat <hojat@noorano.com>"
snmp set location="Universe 10 - Datacenter"

```



```bash
# apt-get install snmp
# snmpwalk -v2c -c password 10.
```





## MikroTik Router SNMPv3 Configuration



```bash
[admin@MikroTik] > snmp set enabled=yes
[admin@MikroTik] > snmp set contact="Zamasu <zamasu@dbsuper.com>"
[admin@MikroTik] > snmp set location="Universe 10 - Datacenter"
[admin@MikroTik] > snmp community add name=goku authentication-protocol=SHA1 authentication-password=0123456789 encryption-protocol=AES encryption-password=9876543210
```



* Testing the SNMPv3 Configuration

  ```bash
  apt-get install snmp
  snmpwalk -v 3 -u goku -l authPriv -a SHA -A 0123456789 -x AES -X 9876543210 192.168.0.10
  ```

  
