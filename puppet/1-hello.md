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
