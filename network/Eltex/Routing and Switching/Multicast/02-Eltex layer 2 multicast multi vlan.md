# Layer 2 multicast multivlan


```text
(streamer) ----aV10----> (MES1) <---tV20----> (MES2) <----(aV20)----(user)
```

```bash
show ip igmp snooping groups
show ip igmp snooping mrouter
show mac address-table vlan 20
show int utliz
```


## MES1:
```bash
vlan 10
vlan 20


interface vlan 10
 name streamer
 ip address 192.168.10.1 255.255.255.0


interface vlan 20
 name users
 ip address 192.168.20.1 255.255.255.0

interface gi1/0/1
 description "streamer"
 switchport mode access
 switchport access vlan 10
 
interface gigabitethernet1/0/2
 description "user on same switch and vlan"
 switchport access vlan 10

ineterface gi1/0/24
 switchport mode trunk
 switchport trunk allowed vlan add 20
 switchport trunk multicast-tv vlan 10
 selective-qinq list egress override_vlan 20 ingress_vlan 10
 switchport trunk multicast-tv vlan 10 tagged

bridge multicast filtering

ip igmp snooping
ip igmp snooping vlan 10 immediate-leave host-based
ip igmp snooping vlan 10
ip igmp snooping vlan 10 querier
ip igmp snooping vlan 10 querier address 192.168.10.1
ip igmp snooping vlan 20
Ip igmp snooping vlan 20 querier
ip igmp snooping vlan 20 querier address 192.168.20.1
```

## MES2:
```bash
bridge multicast filtering

ip igmp snooping
ip igmp snooping vlan 20
ip igmp snooping vlan 20 immediate-leave host-based

vlan 10

vlan 20

interface vlan 10
 name streamer
 ip address 192.168.10.2 255.255.255.0

interface vlan 20
 name users
 ip address 192.168.20.2 255.255.255.0

interface gi 1/0/1
  switchport mode access
  switchport access vlan 20
 
interface gi 1/0/24
 switchport mode trunk
 switchport trunk allowed vlan add 20
 

```