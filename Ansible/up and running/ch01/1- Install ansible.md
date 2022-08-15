## Install ansible
```shell
python3 -m venv .venv --prompt A
source .venv/bin/activate


pip3 install --user ansible==2.9.20
pip3 install pywinrm docker
```

```shell
python3 -m venv .venv --prompt S
source .venv/bin/activate

(S) python3 -m pip install --upgrade pip
(S) pip3 install wheel
(S) git clone https://github.com/ansible/ansible.git --recursive
(S) pip3 install -r ansible/requirements.txt

(S) cd ./ansible
(S) source ./hacking/env-setup
```

### Using Vagrant to Set Up a Test Server
```shell
mkdir playbooks
cd playbooks
vagrant init ubuntu/focal64
vagrant up
vagrant up --provider virtualbox

vagrant ssh
vagrant ssh-config

ssh vagrant@127.0.0.1 -p 2222 -i .vagrant/machines/default/virtualbox/private_key
```

### Telling Ansible About Your Test Server

```shell
mkdir inventory
vim inventory/vagrant.ini
[webservers]
testserver ansible_port=2222

[webservers:vars]
ansible_host=127.0.0.1
ansible_user=vagrant
ansible_private_key=/home/hojii/Documents/ww/ansible/up-run/ansible/playbooks/.vagrant/machines/default/virtualbox/private_key

ansible testserver -i inventory/vagrant.ini -m ping

ansible testserver -m ping
```

```shell
vim ansible.cfg
[defaults]
inventory = inventory/vagrant.ini
host_key_checking = False
stdout_callback = yaml
callback_enabled = timer

ansible testserver   -m ping

ansible testserver -m command -a uptime
ansible testserver -a uptime

ansible testserver -a "tail /var/log/dmesg"

ansible testserver -b -a "tail /var/log/syslog"

ansible testserver -b -m package -a name=nginx
ansible testserver -b -m service -a "name=nginx state=restarted"

vagrant destroy -f
```

### vagrant
```shell
vagrant box list
vagrant box remove laravel/homestead
vagrant global-status
vagrant destroy nameOfYourBox

vagrant up
```

