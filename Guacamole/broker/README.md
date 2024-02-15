# broker

## Install docker

```shell
sudo apt install docker.io

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

```


## Quick connection broker start 
Clone the GIT repository :

~~~bash
git clone "https://github.com/hojat-gazestani/broker.git"
cd broker
./prepare.sh
docker-compose up -d
~~~

Your server should now be available at `https://ip of your server:8443/`. The default username is `guacadmin` with password `guacadmin`.


