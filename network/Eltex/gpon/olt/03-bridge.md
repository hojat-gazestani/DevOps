# OLT
```bash
switch
    configure terminal
        vlan 10
            name "Private-Servers"
            tagged front-port 0
            tagged pon-port 0
        exit
```

```bash
configure terminal
    profile cross-connect data
        bridge
        bridge group 10
        outer vid 10

    profile ports NTU1
        port 0 bridge group 10

    interface ont 0/0
        serial ELTX5F016610
        service 0 profile cross-connect data
        service 0 profile dba dba-00
        profile ports NTU1
```