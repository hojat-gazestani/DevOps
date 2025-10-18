Xena - Glance Installation Tutorial for Ubuntu
==============================================

sudo mysql

CREATE DATABASE glance;

GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' \
  IDENTIFIED BY 'openstack';
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' \
  IDENTIFIED BY 'openstack';

. admin-openrc

openstack user create --domain default --password-prompt glance

openstack role add --project service --user glance admin

openstack service create --name glance \
  --description "OpenStack Image" image


openstack endpoint create --region RegionOne \
  image public http://controller01:9292
openstack endpoint create --region RegionOne \
  image internal http://controller01:9292
openstack endpoint create --region RegionOne \
  image admin http://controller01:9292

Register quota limits (optional):
---------------------------------

sudo vim /etc/glance/glance-api.conf
	use_keystone_quotas=True 

openstack --os-cloud devstack-system-admin registered limit create \
  --service glance --default-limit 1000 --region RegionOne image_size_total
openstack --os-cloud devstack-system-admin registered limit create \
  --service glance --default-limit 1000 --region RegionOne image_stage_total
openstack --os-cloud devstack-system-admin registered limit create \
  --service glance --default-limit 100 --region RegionOne image_count_total
openstack --os-cloud devstack-system-admin registered limit create \
  --service glance --default-limit 100 --region RegionOne image_count_uploading


sudo apt install glance -y

sudo vim /etc/glance/glance-api.conf
[DEFAULT]
use_keystone_quotas = True

[database]
connection = mysql+pymysql://glance:openstack@controller01/glance

[keystone_authtoken]
www_authenticate_uri = http://controller01:5000
auth_url = http://controller01:5000
memcached_servers = controller01:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = glance
password = openstack

[paste_deploy]
flavor = keystone

[glance_store]
stores = file,http
default_store = file
filesystem_store_datadir = /var/lib/glance/images/

[oslo_limit]
auth_url = http://controller013:5000
auth_type = password
user_domain_id = default
username = glance_limit
system_scope = all
password = openstack
endpoint_id = ENDPOINT_ID
region_name = RegionOne

openstack role add --user glance --user-domain Default --system all reader

sudo su -s /bin/sh -c "glance-manage db_sync" glance

sudo service glance-api restart

Verify operation
----------------

. admin-openrc


wget http://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img

  glance image-create --name "cirros" \
  --file cirros-0.4.0-x86_64-disk.img \
  --disk-format qcow2 --container-format bare \
  --visibility=public

glance image-list
