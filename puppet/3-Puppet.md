​	

# Puppet



Puppet architecture

Master/Slave

![image-20220529160857612](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529160857612.png)



SSL Connection

All communication between Master and Slave are encrypted 

![image-20220529160951054](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529160951054.png)





Code basic for Puppet

resource : something about the state of the system. such as a certain user or file should exist, or a package should be installed, etcd. 

![image-20220529162724696](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529162724696.png)



```bash
resource_type { 'resource_name' :
	attribute => value,
	...
}
```









```bash
sudo vim /etc/puppetlabs/code/environments/production/manifests/hellopuppet.pp
node 'puppet' {
        file { '/tmp/puppet_hello' :
                ensure => present,
                content => "Hello World!",
        }
}

node 'client' {
        file { '/tmp/it_works.txt' :
                ensure => present,
                mode   => '0644',
                content => "It works on ${ipaddress_enp0s10}!\n",
        }
        
        package { 'httpd' :
                ensure => installed, 
        }
}
```





## Manifest

Collection of resource declarations, using extention .pp



![image-20220529162940188](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529162940188.png)



![image-20220529163117878](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529163117878.png)



Variables 

Variables can be defined at any point in a manifest. the most common type of variables are strings and arrays of strings, but other types are also supported, such as booleans and hashes.

![image-20220529164744081](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529164744081.png)



```bash
node 'client' {
        $text = "This is devops course"
        file { '/tmp/works.txt' :
                ensure => present,
                mode   => '0644',
                content => $text,
        }
}

```



### loop 

Repeat a task using different input values. 

![image-20220529165222230](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529165222230.png)



```bash
node 'client' {
       package { ['epel-release', 'nginx'] :
               ensure => installed,
       }
}
```





Conditions

### Dynamically decide whether or not a block of code should be executed, based on a variable or an output from a command, for instance

![image-20220529170646640](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529170646640.png)



```bash
## Conditions if yes
node 'client' {
        exec { "conditions" :
                command => "/bin/echo apache2 is installed > /tmp/status_apache.txt",
                onlyif =>  "/bin/which apache2",
        }

## Condition if no

        exec { "conditions" :
                command => "/bin/echo apache2 is not installed > /tmp/status_apache.txt",
                unless =>  "/bin/which apache2",
        }
}

```



