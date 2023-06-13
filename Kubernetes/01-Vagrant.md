# Create VMs on Virtual Box

* Vagrant install Ubuntu 22.04

```bash
sudo apt install vagrant -y
```

* Vagrant initialize with dummy box

```bash
vim metadata.json
{
  "name": "dummy",
  "versions": [{
    "version": "0",
    "providers": [{
      "name": "virtualbox",
      "url": "/home/arman/Documents/ww/Vagrant/empty.box"
    }]
  }]
}
```

```bash
touch empty.box
```

```bash
zip dummy-virtualbox.zip metadata.json empty.box
```

```bash
vagrant init dummy
```
