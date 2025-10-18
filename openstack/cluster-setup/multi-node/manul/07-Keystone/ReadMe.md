
Xena - Keystone Installation Tutorial for Ubuntu
================================================

Install and configure
---------------------

sudo mysql

CREATE DATABASE keystone;

GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' \
IDENTIFIED BY 'openstack';
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' \
IDENTIFIED BY 'openstack';


sudo apt install -y keystone


sudo vim  /etc/keystone/keystone.conf
[database]
connection = mysql+pymysql://keystone:openstack@controller01/keystone

[token]
provider = fernet

sudo su -s /bin/sh -c "keystone-manage db_sync" keystone

sudo keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone
sudo keystone-manage credential_setup --keystone-user keystone --keystone-group keystone

sudo keystone-manage bootstrap --bootstrap-password openstack \
  --bootstrap-admin-url http://controller01:5000/v3/ \
  --bootstrap-internal-url http://controller01:5000/v3/ \
  --bootstrap-public-url http://controller01:5000/v3/ \
  --bootstrap-region-id RegionOne

sudo vim  /etc/apache2/apache2.conf
ServerName controller01

sudo service apache2 restart

export OS_USERNAME=admin
export OS_PASSWORD=openstack
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://controller01:5000/v3
export OS_IDENTITY_API_VERSION=3

openstack domain create --description "An Example Domain" example

openstack project create --domain default \
  --description "Service Project" service

openstack project create --domain default \
  --description "Demo Project" myproject

openstack user create --domain default \
  --password-prompt myuser

openstack role create myrole

openstack role add --project myproject --user myuser myrole


Verify operation
----------------

unset OS_AUTH_URL OS_PASSWORD

openstack --os-auth-url http://controller01:5000/v3 \
  --os-project-domain-name Default --os-user-domain-name Default \
  --os-project-name admin --os-username admin token issue

openstack --os-auth-url http://controller01:5000/v3 \
  --os-project-domain-name Default --os-user-domain-name Default \
  --os-project-name myproject --os-username myuser token issue


Create OpenStack client environment scripts
-------------------------------------------

vim  admin-openrc
export OS_PROJECT_DOMAIN_NAME=Default
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=openstack
export OS_AUTH_URL=http://controller01:5000/v3
export OS_IDENTITY_API_VERSION=3
export OS_IMAGE_API_VERSION=2

vim  demo-openrc
export OS_PROJECT_DOMAIN_NAME=Default
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_NAME=myproject
export OS_USERNAME=myuser
export OS_PASSWORD=openstack
export OS_AUTH_URL=http://controller01:5000/v3
export OS_IDENTITY_API_VERSION=3
export OS_IMAGE_API_VERSION=2

. admin-openrc
openstack token issue
