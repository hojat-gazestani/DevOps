nter telnet in response to the password prompt that appears during the registration via the Telnet
session.
4.5.2.3 Setting SSH password
console(config)# aaa authentication login authorization default line
console(config)# aaa authentication enable default line
console(config)# ip ssh server
console(config)# line ssh
console(config-line)# login authentication default
console(config-line)# enable authentication default
console(config-line)# password ssh


--------------------------------------------------------

crypto key generate dsa
—
Generate a DSA private and public key pair for SSH service.
If one of the keys has already been created, the system will
prompt to overwrite it.

--------------------------------------------------------
management access-list SSH-Access
permit vlan 2 service ssh ace-priority 30 


ip ssh-client source-interface vlan 2

ip ssh server

vlan 2

vlan 3

interface gigabitethernet1/0/2
 switchport access vlan 2
exit
!
interface gigabitethernet1/0/3
 switchport access vlan 3
exit

interface vlan 1
 ip address 172.16.1.254 255.255.255.0
 no ip address dhcp
exit
!
interface vlan 2
 ip address 172.16.2.254 255.255.255.0
exit
!
interface vlan 3
 ip address 172.16.3.254 255.255.255.0
exit
!


interface vlan 4
 ip address 172.16.4.254 255.255.255.0
exit

interface gigabitethernet1/0/4
 swit mode acce
 switchport access vlan 4
exit

interface vlan 4
 ip address 172.16.4.254 255.255.255.0
 no ip address dhcp
exit
!



----------------------------------------------------------------

ip access-list extended 2
 permit ip any any 172.16.2.0 0.0.0.255 172.16.3.0 0.0.0.255 ace-priority 10
 deny ip any any any any ace-priority 30
exit
!

interface vlan 2
 ip address 172.16.2.254 255.255.255.0
 service-acl input 2
exit

