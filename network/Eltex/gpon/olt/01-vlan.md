# OLT configuration
```bash
switch
    configure terminal
        vlan 101
            name Data-101
            tagged pon-port 0
            tagged front-port 0

configure terminal
    profile cross-connect Data-101
        outer vid 101

    do show interface ont 0 connected 
    do show interface ont 0 unactivated
    interface ont 0/0
        serial ELTX5F016610
        service 0 profile cross-connect Data-101 dba db-00
```

# ONT Web
```bash
Pon WAN
    VLAN-ID: 101
    Channel-mode: IPoE
    Connection Type: Internet
    IP Protocol: IPv4
    WAN: DHCP
```
    