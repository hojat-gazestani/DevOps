## SQL database for Ubuntu
* 20.04
```shell
sudo apt install -y mariadb-server python3-pymysql
```
* 18.04 
* 16.04
```shell
sudo apt install mariadb-server python-pymysql
```
```shell
sudo vim /etc/mysql/mariadb.conf.d/99-openstack.cnf
[mysqld]
bind-address = 172.25.23.2

default-storage-engine = innodb
innodb_file_per_table = on
max_connections = 4096
collation-server = utf8_general_ci
character-set-server = utf8

sudo service mysql restart

sudo mysql_secure_installation
```