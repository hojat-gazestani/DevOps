## Message queue

### controller
```shell

sudo apt install -y rabbitmq-server

sudo rabbitmqctl add_user openstack openstack

sudo  rabbitmqctl set_permissions openstack ".*" ".*" ".*"
```