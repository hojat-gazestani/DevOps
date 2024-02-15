# shaping

```bash
configure
    profile shaping highbandwith
        downstream policer 0 peak-rate 20000 enable
        upstream 0 commited-rate 20000 enable
        upstream 0 peak-rate 20000 enable
        
    interface ont 0/1-20
        profile shaping highbandwith
```