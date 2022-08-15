### Ansible

```shell
sudo dnf install -y ansible
```

```shell
mkdir /home/ansible
vim /home/ansible/ansible.cfg
inventrory=./inventory
remote_user=root
```

```shell
vim /home/ansible/inventory
192.168.122.[4:5]
```

```shell
ansible all --list-hosts
```

```shell
ssh 192.168.122.4
ssh 192.168.122.5

ssh-keygen -t rsa
```

```
vim vim.rc
autocmd FileType yaml setlocal ai ts=2 sw=2 et nu cuc cul
```

```
vim key.yml
` name: Add Keys to hosts
  hosts: all
  tasks:
  - name: install Key
    authorized_key:
      user: root
      state: present
      key: "{{ lookup('file', '/root/.ssh/id_rsa.pub') }}"


ansible-playbook -k key.yml
```

## Understanding inventory

```shell
ansible --version
config file = /etc/ansible/ansible.cfg

grep inventory /etc/ansible/ansible.cfg

ansible all --list-hots

ansible localhost -m ping

sudo vim /etc/ansible/hosts
# add some host 

ansible all --list-hots
[linuxs]
web
backup
app

[ubuntu]
web
backup

[centos]
app


ansible all --list-hosts
  hosts (3):
    web
    backup
    app

ansible ubuntu --list-hosts
 hosts (2):
   web
   backup

vim /home/ansible/myhosts
host1
host[4:7]
192.168.1.10[0:9]

[www]
host1
host2

[kerman]
192.168.1.1

[tehran]
192.168.1.2

[ir:children]
kerman
tehran


ansible -i myhosts kerman --list-hosts
```

### YML file


```shell
vim inventory.yml
---
all:
  children:
    ir:
      kerman:
        hosts:
          www.kerman.com:
          db.kerman.com:
      tehran:
        hosts:
          www2.example.com:
          db2.example.com:
    database:
      hosts:
        db1.example.com:
        db2.example.com:


```

### ad hoc 
```
ansible all -i inventory -m ping


###

```shell
ansible localhost -m debug -a "msg={{ 'Password1' | password_hash('sha512', 'AZ') }}"
localhost | SUCCESS => {
    "msg": "$6$AZ$tfbOH9FsYkG9EkUfU6Ms7qvQM7Jlv5hbWlfaZ4BLkUFUPWalAFW12L3cioXyrWMkmNAyjxC9tCMBiTubILv3F/"
}

vim Create_user_devops.yml
---                                      
- name: Deploy Ansible User              
  hosts: all                             
  tasks:                                 
                                         
    - name: Create User                  
      user:                              
        name: devops                     
        groups: "{{ admin_group }}"         
        create_home: true                
        comment: 'Ansible Management Account'
        expires: -1                      
        password: '$6$AZ$tfbOH9FsYkG9EkUfU6Ms7qvQM7Jlv5hbWlfaZ4BLkUFUPWalAFW12L3cioXyrWMkmNAyjxC9tCMBiTubILv3F/'
                                         
    - name: Install SSH Key              
      authorized_key:                    
        user: devops                     
        state: present                   
        manage_dir: true                 
        key: "{{ lookup('file', '/home/hojii/.ssh/id_rsa.pub') }}"
                                         
    - name: Setup Devops Sudo Access        
      copy:                              
        dest: /etc/sudoers.d/devops         
        content: 'devops ALL=(ALL) NOPASSWD: ALL'
        validate: /usr/sbin/visudo -cf %s 

ansible-playbook Create_user_devops.yml --syntax-check

ansible-playbook Create_user_devops.yml
```

### Ansible User Module
```shell
vim ansible.cfg
[defaults]
inventory = ./inventory
remote_user = devops
[privilage_esclation]
become = true
become_method = sudo
become_user = root
```

```shell
vim inventrory
[centos]
app

[ubuntu]
backup
web
```

```shell
ls group_vars
redhat ubuntu

vim group_vars/redhat
admin_group: wheel
default_user_password: Password1

vim group_vars/ubuntu
admin_group: sudo
default_user_password: Password1
```

```shell
---         
- name: Create New Users
  hosts: all
  gather_facts: true
  tasks: 
         
    - name: Create Users Task
      user:
        name: "{{ item }}"
        state: present
        password: "{{ default_user_password | password_hash('sha512', 'A512') }}"
        shell: /bin/bash
        groups: "{{ admin_group }}"                                            
      loop:
        - ali
        - hasan
        - reza
        - pary
         
...    
```

```shell
vim Delete_users.yml
- name: Clean User Accounts
  hosts: all  
  gather_facts: true
  become: true
  tasks:         
                 
    - name: Delete Users
      user:   
        name: "{{ item }}"
        state: absent
        remove: true
      loop:   
        - ali 
        - hasan
        - safar
        - pary   
```

* Vault
```shell
ansible-vault encrypt group_vars/redhat

cat group_vars/redhat
# encrypted

ansible-playbook --vault-id @prompt Create_users.yml

```

```shell
---
- name: Deploy Apache
  hosts: app
  gather_facts: true
  tasks:

    - name: Install Apache/Packages
      yum:
        name:
          - httpd
          - httpd-manual
          - firewalld
        state: latest
      
    - name: Don't Listen on All Interface
      lineinfile:
        path: /etc/httpd/conf/httpd.conf
        regexp: '^Listen 80'
        state: absent

    - name: Listen Single IPv4 Interface
      lineinfile:
        path: /etc/httpd/conf/httpd.conf
        insertafter: '^#Listen'
        line: 'Listen {{ ansible_default_ipv4.address }}:80'

    - name: Default Page
      copy:
        dest: /var/www/html/index.html
        content: |
          Welcome page
          This was developed by deveops

    - name: Start Services
      service:
        name: "{{ item }}"
        state: started
        enabled: true
      loop:
        - httpd
        - firewalld

    - name: Open Firewall
      firewalld:
        service: http
        state: enabled
        permanent: true
        immediate: true
```

### Jinja Template

```shell
ansible app -m command -a "cat /etc/hosts"
```


```shell
vim hosts.yml
---
- name: Set hostname 1


```

### ansible role - firewall

```shell
---
- name: Open Firewall
  hosts: app
  tasks:
    - name: Open HTTP
      firewalld:
        service: "{{ item }}"
        state: enabled
        immediate: true
        permanent: true
      loop:
        - http
        - https
```

```shell

---
- name: Open Firewall
  hosts: app
  vars:
  	Firewall_services:
  		- http
  		- https
  	service_state: disabe
  tasks:
    - name: Open HTTP
      firewalld:
        service: "{{ item }}"
        state: "{{ service_state }}"
        immediate: true
        permanent: true
      loop: "{{ Firewall_services }}"
```

```shell
vim /home/hojii/.ansible/roles/firewall-r/tasks/main.yml
---
# tasks file for firewall-r
- name: Manage Firewall Services
  firewalld:
    service: "{{ item }}"
    immedate: true
    permanent: true
    state: "{{ service_state }}"
  loop: "{{ firewall_services }}"

vim /home/hojii/ansible/firewall.yml
---
- name: Open Firewall
  hosts: app
  roles:
    - name: firewall_r
      firewall_services:
        - http
        - https
      service_state: enabled


```

### ansible facts and variable

```

