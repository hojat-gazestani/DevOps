```bash

sudo chmod -x /etc/update-motd.d/*
````

```bash
sudo vim /etc/update-motd.d/00-hostname
#!/bin/bash

echo  "Welcome to " `hostname`
echo "************************************************************************"
```

```bash
sudo chmod +x /etc/update-motd.d/00-hostname


```
