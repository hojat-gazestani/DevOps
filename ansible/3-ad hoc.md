### Why use ad hoc commands
* execute a quick one-liner in Ansible without writing a playbook
```shell
ansible [pattern] -m [module] -a "[module options]"
```

### Rebooting servers
```shell
ansible atlanta -a "/sbin/reboot"

ansible atlanta -a "/sbin/reboot" -f 10

ansible atlanta -a "/sbin/reboot" -f 10 -u username

ansible atlanta -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]
```

### Managing files
```shell
ansible atlanta -m ansible.builtin.copy -a "src=/etc/hosts dest=/tmp/hosts"
```

* changing ownership
```shell
ansible webservers -m ansible.builtin.file -a "dest=/srv/foo/a.txt mode=600"
ansible webservers -m ansible.builtin.file -a "dest=/srv/foo/b.txt mode=600 owner=mdehaan group=mdehaan"
```

* create directories, similar to mkdir -p
 ```shell
ansible webservers -m ansible.builtin.file -a "dest=/path/to/c mode=755 owner=mdehaan group=mdehaan state=directory"
```

* delete directories (recursively) and delete files
```shell
ansible webservers -m ansible.builtin.file -a "dest=/path/to/c state=absent"
```

### Managing packages
* To ensure a package is installed without updating it:
```shell
ansible webservers -m ansible.builtin.yum -a "name=acme state=present"
```

* To ensure a specific version of a package is installed
```shell
 ansible webservers -m ansible.builtin.yum -a "name=acme-1.5 state=present"
```

* To ensure a package is at the latest version:
```shell
ansible webservers -m ansible.builtin.yum -a "name=acme state=latest"
```

* To ensure a package is not installed:
```shell
ansible webservers -m ansible.builtin.yum -a "name=acme state=absent"
```

### Managing users and groups
```shell
ansible all -m ansible.builtin.user -a "name=foo password=<crypted password here>"

ansible all -m ansible.builtin.user -a "name=foo state=absent"
```

### Managing services
* Ensure a service is started on all webservers:
```shell
ansible webservers -m ansible.builtin.service -a "name=httpd state=started"
```
* restart a service on all webservers
```shell
ansible webservers -m ansible.builtin.service -a "name=httpd state=restarted"
```

* service is stopped:
```shell
ansible webservers -m ansible.builtin.service -a "name=httpd state=stopped"
```

### Gathering facts
```shell
ansible all -m ansible.builtin.setup
```

