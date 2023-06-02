# Logging

## Configure HAProxy for logging
```bash
vim haproxy.cfg
global
    log /dev/log local0 debug
    log 127.0.0.1:514  format rfc3164  local0 debug
    
globals
    log global
    
frontend Germnay
    log 192.168.56.20:1514
    log-tag Germany
```

### Socket

* Can use an IP 

### Severity Level

* __emerg:__  Errors such as running out of operating system file descriptors.
* __alert:__ Some rare cases where something unexpected has happened, such as being unable to cache a response.
* __crit:__ Not used.
* __err:__ Errors such as being unable to parse a map file, being unable to parse the HAProxy configuration file
* __warning:__ Certain important, but non-critical, errors such as failing to set a request header or failing to connect to a DNS nameserver.
* __notice:__ Changes to a server’s state, such as being UP or DOWN or when a server is disabled.
* __info:__ TCP connection and HTTP request details and errors.
* __debug:__ You may write custom Lua code that logs debug messages

## 



## configure rsyslog

```bash
cat /etc/rsyslog.d/49-haproxy.conf

$AddUnixListenSocket /var/lib/haproxy/dev/log

:programname, startswith, "haproxy" {
  /var/log/haproxy.log
  stop
}
:programname, startswith, "Germany" {
  /var/log/haproxy-Germany.log
  stop
}
```

```bash
tail /var/log/haproxy.log
```

## rotate log and save disk space by using logrotate

```bash
cd /etc/logrotate.d
cat haproxy
/var/log/haproxy-Germany.log {
    daily
    rotate 7
    missingok
    notifempty
    compress
    delaycompress
    postrotate
        [ ! -x /usr/lib/rsyslog/rsyslog-rotate ] || /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
/var/log/haproxy.log {
    daily
    rotate 7
    missingok
    notifempty
    compress
    delaycompress
    postrotate
        [ ! -x /usr/lib/rsyslog/rsyslog-rotate ] || /usr/lib/rsyslog/rsyslog-rotate
    endscript
}


```


## source
[commercial](https://www.haproxy.com/blog/introduction-to-haproxy-logging)