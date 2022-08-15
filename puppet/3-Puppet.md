

[TOC]

​	

# Puppet

## 2- Installation CentOS

### MASTER

```bash
sudo hostnamectl set-hostname puppet
sudo systemctl stop firewalld

sudo rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
sudo yum -y install puppetserver

sudo vim /etc/syconfig/puppetserver
JAVA_ARGS="-Xms512m -Xmx512m -XX:MaxPermSize=256m"

export PATH=$PATH:/opt/puppetlabs/bin
sudo systemctl enable puppetserver
sudo systemctl start puppetserver
```

### CLIENT

```bash
sudo vim /etc/hosts
192.168.1.1 puppet puppet-master

sudo rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
sudo yum install -y puppet-agent

export PATH=$PATH:/opt/puppetlabs/bin
[user@client ~]$ sudo /opt/puppetlabs/bin/puppet resource service puppet ensure=running enable=true
Notice: /Service[puppet]/ensure: ensure changed 'stopped' to 'running'
service { 'puppet':
  ensure => 'running',
  enable => 'true',
}
```


-------

### MASTER

```bash
sudo /opt/puppetlabs/bin/puppet cert list
  "client" (SHA256) 41:B8:47:C9:8B:77:77:64:6C:1F:F7:B7:C4:A4:70:FE:2E:23:14:E6:69:22:AA:D8:2C:3A:DF:72:CF:66:F0:3E
  
sudo /opt/puppetlabs/bin/puppet cert sign client
Signing Certificate Request for:
  "client" (SHA256) 41:B8:47:C9:8B:77:77:64:6C:1F:F7:B7:C4:A4:70:FE:2E:23:14:E6:69:22:AA:D8:2C:3A:DF:72:CF:66:F0:3E
Notice: Signed certificate request for client
Notice: Removing file Puppet::SSL::CertificateRequest client at '/etc/puppetlabs/puppet/ssl/ca/requests/client.pem'


sudo touch /etc/puppetlabs/code/environments/production/manifests/sample.pp
```



### CLIENT

```bash
sudo /opt/puppetlabs/bin/puppet agent --test
```



Error: Could not request certificate: The certificate retrieved from the master does not match the agent's private key.

```bash
sudo rm /etc/puppetlabs/puppet/ssl/certs/client.pem
```



### MASTER

```bash
sudo /opt/puppetlabs/bin/puppet cert clean client
sudo /opt/puppetlabs/bin/puppet cert list
sudo /opt/puppetlabs/bin/puppet cert sign client
sudo touch /etc/puppetlabs/code/environments/production/manifests/sample.pp
```



### CLIENT

```bash
sudo /opt/puppetlabs/bin/puppet agent -t
```



Puppet architecture

## Master/Slave

![image-20220529160857612](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529160857612.png)



## SSL Connection

All communication between Master and Slave are encrypted 



![image-20220529160951054](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529160951054.png)





## Code basic for Puppet

resource : something about the state of the system. such as a certain user or file should exist, or a package should be installed, etcd. 

![image-20220529162724696](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529162724696.png)



```bash
resource_type { 'resource_name' :
	attribute => value,
	...
}
```



3- Puppet Hello world

```bash
sudo vim /etc/puppetlabs/code/environments/production/manifests/hellopuppet.pp
node 'puppet' {
        file { '/tmp/puppet_hello' :
                ensure => present,
                content => "Hello World!",
        }
}


```



4- resource file

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Getting started with Vagrant!</h1>
  </body>
</html>
```



```bash
openssl passwd -1
$1$2tpxyNyr$eG4Adkj.sGzD5O7UXQH8E/

sudo vim /etc/puppetlabs/code/environments/production/manifests/web.pp
node 'client' {
        user { 'hojii':
                ensure     => 'present',
                comment    => 'Hi hojii',
                managehome => true,
                password   => '$1$2tpxyNyr$eG4Adkj.sGzD5O7UXQH8E/',
        }
             
        package { 'httpd' :
                ensure => installed,
        }
        
              user { 'www-data' :
                ensure => 'present',
        }

        file { '/var/www' :
                ensure => 'directory',
        }
        
        file { '/var/www/index.html' :
               ensure => present,
               content => "<!DOCTYPE html>
<html>
  <body>
    <h1>Getting started with Vagrant!</h1>
  </body>
</html>",

               mode => '755',
               owner => 'www-data',
               group => 'www-data',
        }
        
        service { "httpd":
                ensure  => running,
                start   => "/usr/sbin/apachectl start",
                stop    => "/usr/sbin/apachectl stop",
                pattern => "/usr/sbin/httpd",
        }
}

```





```bash
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



### MASTER

```bash
sudo vim /etc/puppetlabs/code/environments/production/manifests/sample.pp
node 'client' {
        package { 'httpd' :
                ensure => installed,
        }
        
        service { "httpd":
                ensure  => running,
                start   => "/usr/sbin/apachectl start",
                stop    => "/usr/sbin/apachectl stop",
                pattern => "/usr/sbin/httpd",
        }
}
```




### CLIENT

```bash
sudo /opt/puppetlabs/bin/puppet agent -t
```







## Manifest

Collection of resource declarations, using extention .pp



![image-20220529162940188](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529162940188.png)



![image-20220529163117878](/home/hojii/snap/typora/57/.config/Typora/typora-user-images/image-20220529163117878.png)



### Variables 

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





### Conditions

Dynamically decide whether or not a block of code should be executed, based on a variable or an output from a command, for instance

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



