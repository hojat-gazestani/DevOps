```bash
sudo apt install rsyslog

sudo vim /etc/rsyslog.conf
# provides UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")

# provides TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")

sudo systemctl restart rsyslog
```
