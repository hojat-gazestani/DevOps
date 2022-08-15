### Selecting machines from inventory
```shell
sudo vim /etc/ansible/hosts
192.0.2.50
aserver.example.org
bserver.example.org
```

```shell
mail.example.com

[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
three.example.com
```

```shell
[webservers]
www[01:50].example.com

...
  webservers:
    hosts:
      www[01:50].example.com:

```
### Assigning a variable to many machines: group variables
```shell
[atlanta]
host1
host2

[atlanta:vars]
ntp_server=ntp.atlanta.example.com
proxy=proxy.atlanta.example.com
```

### Action: run your first Ansible commands
```shell
ansible all -m ping
ansible all -m ping -u user
```

```shell
 ansible all -a "/bin/echo hello"
```

### Action: Run your first playbook
```shell
---
- name: My playbook
  hosts: all
  tasks:
     - name: Leaving a mark
       command: "touch /tmp/ansible_was_here"

ansible-playbook mytask.yaml
```

### Beyond the basics
```shell
ansible all -m ping -u bruce

ansible all -m ping -u bruce --become

ansible all -m ping -u bruce --become --become-user batman
```





