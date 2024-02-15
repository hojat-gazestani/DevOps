# Isolation
```bash
switch
    configure 
        isolation group 2
            allow pon-port 0
            allow front-port 0
            
        vlan 2
            tagged pon-port 0
            tagged fron-port 0
            isolation assign group 2 to pon-port 0
            isolation enable
```