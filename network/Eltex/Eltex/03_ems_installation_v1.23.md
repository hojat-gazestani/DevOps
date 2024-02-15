root@ubuntu-bionic:~# echo "deb [arch=amd64] http://archive.eltex-co.ru/wireless softwlc-1.22-xenial main" >> /etc/apt/sources.list.d/eltex.list
root@ubuntu-bionic:~# echo "deb [arch=amd64] http://archive.eltex-co.ru/wireless radius-1.22-bionic main" >> /etc/apt/sources.list.d/eltex.list


root@ubuntu-bionic:~# wget -O - http://archive.eltex-co.ru/wireless/repo.gpg.key | sudo apt-key add -

apt update

apt install mysql-server-5.7 && apt install mysql-client-5.7
apt install eltex-auth-service-db
apt install eltex-radius-db
apt install rsyslog-mysql

mysql
GRANT ALL PRIVILEGES ON `Syslog`.* TO 'javauser'@'%';
flush privileges;

echo "deb [arch=amd64] http://archive.eltex-co.ru/wireless softwlc-1.22-xenial main" >> /etc/apt/sources.list.d/eltex.list
sudo wget -O - http://archive.eltex-co.ru/wireless/repo.gpg.key | sudo apt-key add -
apt update

vim /etc/hosts
127.0.0.1 <YOUR_HOSTNAME>

apt install --yes ntp tftp-hpa tftpd-hpa snmpd snmp rsyslog libpcap0.8-dev ffmpeg curl software-properties-common python-pexpect unzip zip pcscd opensc pcsc-tools python-suds libtalloc2 libwbclient0 openjdk-8-jdk eltex-oui-list

update-alternatives --config java
OpenJDK8

apt install eltex-portal
sed -i 's/host = localhost/host = <MYSQL_SERVER_IP>/g' /etc/eltex-portal/application.conf
eltex-portal create-db-user -h <MYSQL_SERVER_IP>
systemctl restart eltex-portal
 
mysql
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| ELTEX_PORTAL       |
| Syslog             |
| eltex_alert        |
| eltex_auth_service |
| eltex_ems          |
| eltex_ont          |
| mysql              |
| performance_schema |
| radius             |
| sys                |
| wireless           |
+--------------------+

select * from portals; 
+----+---------+-------+
| id | name    | scope |
+----+---------+-------+
|  1 | default |       |
+----+---------+-------+

apt purge eltex-portal

apt install eltex-ems

sed -i 's/localhost/<MYSQL_SERVER_IP>/' /usr/lib/eltex-ems/conf/config.txt


echo "deb [arch=amd64] http://archive.eltex-co.ru/wireless softwlc-1.22-xenial main" >> /etc/apt/sources.list.d/eltex.list
echo "deb [arch=amd64] http://archive.eltex-co.ru/wireless radius-1.22-bionic main" >> /etc/apt/sources.list.d/eltex.list
echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.0.list

sudo wget -O - http://archive.eltex-co.ru/wireless/repo.gpg.key | sudo apt-key add -
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

apt update

apt install --yes mongodb-org ntp libpcap0.8-dev ffmpeg curl tomcat8 software-properties-common python-pexpect unzip zip python-suds libtalloc2 libwbclient0 tomcat8-admin openjdk-8-jdk eltex-axis

sed -i 's/127.0.0.1/127.0.0.1,<NBI_SERVER_IP>/g' /etc/mongod.conf
systemctl enable mongod.service
service mongod restart

update-alternatives --config java

curl http://localhost:8080
curl -v http://localhost:8080/axis2

apt install eltex-radius-nbi
 
vim /etc/eltex-radius-nbi/radius_nbi_config.txt
# DB radius(alias=radius)
radius.jdbc.driver=org.gjt.mm.mysql.Driver
radius.jdbc.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/radius?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000
radius.jdbc.username=javauser
radius.jdbc.password=javapassword
radius.jdbc.maxPoolSize=48
radius.jdbc.inUse=yes
 
# DB radius replica(alias=radiusReplicaPool)
#TODO: Change it to replica url
radius.jdbc.replica.driver=org.gjt.mm.mysql.Driver
radius.jdbc.replica.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/radius?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000
radius.jdbc.replica.username=javauser
radius.jdbc.replica.password=javapassword
radius.jdbc.replica.maxPoolSize=48
radius.jdbc.replica.inUse=yes
 
# DB ems(alias=ems)
ems.jdbc.driver=org.gjt.mm.mysql.Driver
ems.jdbc.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/eltex_ems?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000&noAccessToProcedureBodies=true
ems.jdbc.username=javauser
ems.jdbc.password=javapassword
ems.jdbc.maxPoolSize=48
ems.jdbc.inUse=yes
 
# DB wireless (alias=wireless)
wireless.jdbc.driver=org.gjt.mm.mysql.Driver
wireless.jdbc.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/wireless?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000
wireless.jdbc.username=javauser
wireless.jdbc.password=javapassword
wireless.jdbc.maxPoolSize=48
wireless.jdbc.inUse=yes
 
# DB logs (alias=logs)
logs.jdbc.driver=org.gjt.mm.mysql.Driver
logs.jdbc.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/eltex_alert?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000
logs.jdbc.username=javauser
logs.jdbc.password=javapassword
logs.jdbc.maxPoolSize=48
logs.jdbc.inUse=yes
 
# DB logs (alias=eltex_auth_service)
eltex_auth_service.jdbc.driver=org.gjt.mm.mysql.Driver
eltex_auth_service.jdbc.dbUrl=jdbc:mysql://<MYSQL_SERVER_IP>/eltex_auth_service?zeroDateTimeBehavior=convertToNull&useUnicode=true&characterEncoding=utf8&relaxAutoCommit=true&connectTimeout=5000
eltex_auth_service.jdbc.username=javauser
eltex_auth_service.jdbc.password=javapassword
eltex_auth_service.jdbc.maxPoolSize=48
eltex_auth_service.jdbc.inUse=yes
 
# адрес ems-northbound
ems.nbi.host=<EMS_SERVER_IP>
ems.nbi.port=8080
ems.nbi.path=northbound
ems.nbi.protocol=http
 
# freeradius-domain-1
freeradius-domain-1.port=22
freeradius-domain-1.host=192.168.0.1
freeradius-domain-1.username=username
freeradius-domain-1.password=password
 
# freeradius-domain-2
freeradius-domain-2.port=22
freeradius-domain-2.host=192.168.0.2
freeradius-domain-2.username=username
freeradius-domain-2.password=password
 
# tomcat url
tomcat.host=localhost
tomcat.port=8080
 
# pcrf stuff
pcrf.enabled=false
pcrf.url=http://localhost:7070
pcrf.username=admin
pcrf.password=password
pcrf.readtimeout=11
pcrf.writetimeout=11
 
# pcrf mongodb connector
pcrf.mongodb.enabled=true
pcrf.mongodb.uri=mongodb://localhost:27017/pcrf
 
# wifi-customer-cab mongodb connector
wificab.mongodb.enabled=true
wificab.mongodb.uri=mongodb://localhost:27017/wifi-customer-cab
 
# Eltex.SORM2.replicator MongoDB 'sorm2' connect
sorm2.mongodb.enabled=false
sorm2.mongodb.uri=mongodb://localhost:27017/sorm2
 
# wifi-customer-cab request settings
wificab.timeout=90000
 
# Eltex.SORM2.replicator host to use API
sorm2.enabled=false
sorm2.url=http://localhost:7071
sorm2.username=admin
sorm2.password=password
 
#It enables records export to SORM3 while editing wifi users
sorm3.enabled=false
 
# ott mongodb connector
ott.mongodb.enabled=false
ott.mongodb.uri=mongodb://localhost:27017/ott
 
# metrics
metric.interval.s=900
 
# SSO settings
sso.enabled=false
sso.clientSecret=
sso.clientId=
 
# SSO REST
sso.rest.server.protocol=http
sso.rest.server.address=
sso.rest.server.port=80
sso.rest.server.timeout.sec=10
sso.rest.protocol.version=2.0
sso.rest.username=
sso.rest.password=
 
sso.rest.getToken.path=/apiman-gateway/b2b_test/getToken
sso.rest.getUserInfo.path=/apiman-gateway/b2b_test/getUserInfo
sso.rest.addUser.path=/apiman-gateway/b2b_test/addUser
sso.rest.updateUser.path=/apiman-gateway/b2b_test/updateUser
sso.rest.delUser.path=/apiman-gateway/b2b_test/delUser
sso.rest.addUserParam.path=/apiman-gateway/b2b_test/addUserParam
sso.rest.delUserParam.path=/apiman-gateway/b2b_test/delUserParam
sso.rest.getUserByName.path=/apiman-gateway/b2b_test/getUserByName
sso.rest.getUserByEmail.path=/apiman-gateway/b2b_test/getUserByEmail
sso.rest.resetPassword.path=/apiman-gateway/b2b_test/resetPassword
sso.rest.getUserByParam.path=/apiman-gateway/b2b_test/getUserByParam
 
###########################################################################
##########################DB ELTEX_PORTAL settings#########################
###########################################################################
portal.db.driver=com.mysql.jdbc.Driver
portal.db.url=jdbc:mysql://<MYSQL_SERVER_IP>:3306/ELTEX_PORTAL?max_allowed_packet=32362048&useUnicode=true&characterEncoding=utf8
portal.db.username=javauser
portal.db.password=javapassword
 
# NGW
ngw.url=http://localhost:8040
 
# DOORS
doors.url = http://localhost:9097/
doors.timeout = 60
doors.username = user
doors.password = password
 
# ELVIS
elvis.url=http://localhost:9001/epadmin/
elvis.timeout=60

systemctl restart tomcat8
curl http://localhost:8080/axis2/services/RadiusNbiService?wsdl
