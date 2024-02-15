## OSPF
```bash
router ospf 1
  router-id 3.3.3.3
  area 0.0.0.0
    network 200.200.200.0/30
    network 3.3.3.3/32
    enable
  enable
```
```bash
interface gigabitethernet 1/0/2
  ip firewall disable
  mode routerport
  ip ospf instance 1
  ip address 200.200.200.2/30x
  ip ospf network point-to-point
  ip ospf area 0.0.0.0
  ip ospf

interface loopback 7
  ip address 3.3.3.3/32
  ip ospf instance 1
  ip ospf area 0.0.0.0
  ip ospf
```