# Logging

## Configure HAProxy for logging
```bash
vim haproxy.cfg
global
    log /dev/log local0 debug
    log 127.0.0.1:51  local0 debug
globals
    log global
```

## configure rsyslog

```bash
❯ cat /etc/rsyslog.d/49-haproxy.conf
$AddUnixListenSocket /var/lib/haproxy/dev/log

:programname, startswith, "haproxy" {
  /var/log/haproxy.log
  stop
}
```

```bash
tail /var/log/haproxy.log
```

## rotate log and save disk space by using logrotate

```bash
cd /etc/logrotate.d
❯ cat haproxy
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