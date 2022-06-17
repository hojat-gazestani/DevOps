## OSPF Authentication on interface

# Clear text
```bash
int f0/0
ip ospf authentication
ip ospf authentication-key HojatKey
```

# MD5 auth
```bash
int f0/0
ip ospf authentication message-digest
ip ospf message-digest-key 1 md5 HojatKey
```

## Area auth
```bash
router ospf 1
  area 2 authentication message-digest
```
  
## Redistribute with route map
```bash
ip access-list standard CONNECTED-NETWORKS
 permit 10.1.1.0 0.0.0.255
 permit 10.1.2.0 0.0.0.255
 permit 10.1.3.0 0.0.0.255
 permit 10.1.4.0 0.0.0.255

route-map REDISTRIBUTE-CONNECTED permit 10
 match ip address CONNECTED-NETWORKS

router ospf 1
 redistribute connected subnets route-map REDISTRIBUTE-CONNECTED
```
