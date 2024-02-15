## eBGP
```bash
router bgp 1
  router-id 3.3.3.3
  neighbor 2.2.2.2
    remote-as 2
    ebgp-multihop 2
    update-source 3.3.3.3
    enable
  enable


```