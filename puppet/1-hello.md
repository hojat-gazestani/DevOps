```shell
mkdir puppet
cd puppet
mkdir manifests
vim manifests/site.pp
  import 'hello.pp'
  
vim manifests/hello.pp
node 'hostname-localhost' {
    file {'/tmp/helloWorld':
        content => "Hello World\n",
        }
}
```
puppet apply manifests/site.pp



## Configuration File

The main configuration file

```bash
/etc/puppet/puppet.conf
```



Server configuration files (HOCON format)

When the Puppet startup takes place it picks up all .cong files from conf.d directory

Any changes in these files only takes place when the server is restarted.

```bash
/etc/puppetlabs/puppetserver/conf.d/
	master-code-dir: /etc/puppetlabs/code
```



Puppet’s main configuration file

```bash
/etc/puppetlabs/puppet/puppet.conf
```

