```shell
firewall-cmd --permanent --new-service=pptp

cat >/etc/firewalld/services/pptp.xml<<EOF
<?xml version="1.0" encoding="utf-8"?>
<service>
  <port protocol="tcp" port="1723"/>
</service>
EOF

firewall-cmd --permanent --zone=public --add-service=pptp
firewall-cmd --permanent --zone=public --add-masquerade
firewall-cmd --permanent --zone=public --add-protocol=gre
firewall-cmd --reload
```