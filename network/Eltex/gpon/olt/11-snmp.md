```bash
configure terminal
ip snmp access-control
ip snmp encrypted-community read-only 0 "lF60cFx0UGh"
ip snmp encrypted-community read-only 1 "FEg3s5+3k6u"
ip snmp encrypted-community read-write 1 "NrP37/Pfs/eCA=="
ip snmp engineID "0xef17fa365a7ace4fb161f3494b"
ip snmp allow ip 172.25.31.158 mask "32"
ip snmp allow ip 172.25.20.30 mask "32"
ip snmp allow ip 172.25.20.20 mask "32"
ip snmp traps 172.25.31.158 type v2
ip snmp traps 172.25.20.20 type v2
exit
```