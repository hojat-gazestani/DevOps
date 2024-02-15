#auto backup to tftp
```bash
configure terminal
backup on save
backup on timer
backup timer period "600"
backup uri "tftp://172.25.20.65"
exit
commit
```