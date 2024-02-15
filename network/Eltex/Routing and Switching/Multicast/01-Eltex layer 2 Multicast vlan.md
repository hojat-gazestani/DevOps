# Layer 2 multicast multivlan



```text
(streamer) ----aV10----> (MES1) <---V10----> (user1)
```

## MES1:
```bash
vlan 10
vlan 20

interface vlan 10
 name streamer
 ip address 192.168.10.1 255.255.255.0

interface gi1/0/1
 switchport access vlan 10
 
interface gigabitethernet1/0/2
 switchport access vlan 10

bridge multicast filtering

ip igmp snooping
ip igmp snooping vlan 10 immediate-leave host-based
ip igmp snooping vlan 10
ip igmp snooping vlan 10 querier
ip igmp snooping vlan 10 querier address 192.168.10.1
```

```bash
# Enable IGMP Snooping on the switch
ip igmp snooping

# Enable automatic identification of ports with connected multicast routers for this VLAN group
ip igmp snooping vlan 10 mrouter learn pim-dvmrp


int vlan 1

# Set IGMP protocol version
ip igmp version 3

# Set a timeout for sending main queries to all multicast members to check their activity
ip igmp snooping query-interval 100

# If data loss occurs in the channel, robustness value should be increased.
ip igmp robustness 4

#  Set the maximum query response time.
ip igmp query-max-response-time 15
```

```bash
show ip igmp snooping groups
show ip igmp snooping mrouter
show mac address-table vlan 10
show int utliz
```


# Hoseynadeh
```bash




 
interface gigabitethernet 1/0/27
 switchport mode trunk
 switchport trunk allowed vlan add 215
 bridge multicast unregistered filtering
```
```text
(Streamer:172.25.21.226) <------------> (ShowRoom: )
239.100.0.1:1234
239.100.0.2:1234
239.100.0.3:1234
239.100.0.4:1234
```

## ShowRoom
```bash
bridge multicast filtering
ip igmp snooping
ip igmp snooping vlan 215
ip igmp snooping vlan 215 immediate-leave host-based
ip igmp snooping vlan 215 querier
ip igmp snooping vlan 215 querier address 172.25.21.230

interface vlan 215
 name IPTV
 ip address 172.25.21.230 255.255.255.240
 bridge multicast mode ipv4-group
```
## ServerRoom
```bash

```