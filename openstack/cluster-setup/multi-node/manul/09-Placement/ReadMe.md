Xena - Install and configure Placement for Ubuntu
=================================================

sudo mysql

CREATE DATABASE placement;

GRANT ALL PRIVILEGES ON placement.* TO 'placement'@'localhost' \
  IDENTIFIED BY 'openstack';
GRANT ALL PRIVILEGES ON placement.* TO 'placement'@'%' \
  IDENTIFIED BY 'openstack';

. admin-openrc

openstack user create --domain default --password-prompt placement

openstack role add --project service --user placement admin

openstack service create --name placement \
  --description "Placement API" placement

openstack endpoint create --region RegionOne \
  placement public http://controller01:8778
openstack endpoint create --region RegionOne \
  placement internal http://controller01:8778
openstack endpoint create --region RegionOne \
  placement admin http://controller01:8778

sudo apt install -y placement-api

sudo vim /etc/placement/placement.conf
[placement_database]
connection = mysql+pymysql://placement:openstack@controller01/placement

[api]
auth_strategy = keystone

[keystone_authtoken]
auth_url = http://controller01:5000/v3
memcached_servers = controller01:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = placement
password = openstack

sudo su -s /bin/sh -c "placement-manage db sync" placement

sudo service apache2 restart

Verify Installation
-------------------

. admin-openrc

placement-status upgrade check

sudo apt install -y  python3-pip
pip3 install osc-placement

openstack --os-placement-api-version 1.2 resource class list --sort-column name

openstack --os-placement-api-version 1.6 trait list --sort-column name
