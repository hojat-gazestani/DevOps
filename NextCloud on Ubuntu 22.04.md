

# Install NextCloud on Ubuntu 22.04 (Nginx + PostgreSQL + PHP8)



## Step 1: Download NextCloud on Ubuntu 22.04

```shell
wget https://download.nextcloud.com/server/releases/nextcloud-24.0.0.zip
```



```shell
sudo apt install unzip -y
```



```
sudo mkdir -p /var/www/
sudo unzip nextcloud-24.0.0.zip -d /var/www/
```



## Step 2: Create a Database and User for Nextcloud in PostgreSQL

```shell
sudo apt install -y postgresql postgresql-contrib
sudo -u postgres psql

CREATE DATABASE nextcloud TEMPLATE template0 ENCODING 'UNICODE';
CREATE USER arccloud WITH PASSWORD 'ARC@cloud2022';
ALTER DATABASE nextcloud OWNER TO arccloud; 
GRANT ALL PRIVILEGES ON DATABASE nextcloud TO arccloud;

psql -h 127.0.0.1 -d nextcloud -U arccloud -W
```





## Step 3: Create an Nginx Virtual Host for Nextcloud

```shell
sudo apt install nginx -y 

sudo vim /etc/nginx/conf.d/nextcloud.conf
server {
    listen 80;
    listen [::]:80;
    server_name nextcloud.arccloud.com;

    # Add headers to serve security related headers
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
    add_header Referrer-Policy no-referrer;

    #I found this header is needed on Ubuntu, but not on Arch Linux. 
    add_header X-Frame-Options "SAMEORIGIN";

    # Path to the root of your installation
    root /var/www/nextcloud/;

    access_log /var/log/nginx/nextcloud.access;
    error_log /var/log/nginx/nextcloud.error;

    location = /robots.txt {
        allow all;
        log_not_found off;
        access_log off;
    }

    # The following 2 rules are only needed for the user_webfinger app.
    # Uncomment it if you're planning to use this app.
    #rewrite ^/.well-known/host-meta /public.php?service=host-meta last;
    #rewrite ^/.well-known/host-meta.json /public.php?service=host-meta-json
    # last;

    location = /.well-known/carddav {
        return 301 $scheme://$host/remote.php/dav;
    }
    location = /.well-known/caldav {
       return 301 $scheme://$host/remote.php/dav;
    }

    location ~ /.well-known/acme-challenge {
      allow all;
    }

    # set max upload size
    client_max_body_size 512M;
    fastcgi_buffers 64 4K;

    # Disable gzip to avoid the removal of the ETag header
    gzip off;

    # Uncomment if your server is build with the ngx_pagespeed module
    # This module is currently not supported.
    #pagespeed off;

    error_page 403 /core/templates/403.php;
    error_page 404 /core/templates/404.php;

    location / {
       rewrite ^ /index.php;
    }

    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {
       deny all;
    }
    location ~ ^/(?:\.|autotest|occ|issue|indie|db_|console) {
       deny all;
     }

    location ~ ^/(?:index|remote|public|cron|core/ajax/update|status|ocs/v[12]|updater/.+|ocs-provider/.+|core/templates/40[34])\.php(?:$|/) {
       include fastcgi_params;
       fastcgi_split_path_info ^(.+\.php)(/.*)$;
       try_files $fastcgi_script_name =404;
       fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
       fastcgi_param PATH_INFO $fastcgi_path_info;
       #Avoid sending the security headers twice
       fastcgi_param modHeadersAvailable true;
       fastcgi_param front_controller_active true;
       fastcgi_pass unix:/run/php/php8.1-fpm.sock;
       fastcgi_intercept_errors on;
       fastcgi_request_buffering off;
    }

    location ~ ^/(?:updater|ocs-provider)(?:$|/) {
       try_files $uri/ =404;
       index index.php;
    }

    # Adding the cache control header for js and css files
    # Make sure it is BELOW the PHP block
    location ~* \.(?:css|js)$ {
        try_files $uri /index.php$uri$is_args$args;
        add_header Cache-Control "public, max-age=7200";
        # Add headers to serve security related headers (It is intended to
        # have those duplicated to the ones above)
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection "1; mode=block";
        add_header X-Robots-Tag none;
        add_header X-Download-Options noopen;
        add_header X-Permitted-Cross-Domain-Policies none;
        add_header Referrer-Policy no-referrer;
        # Optional: Don't log access to assets
        access_log off;
   }

   location ~* \.(?:svg|gif|png|html|ttf|woff|ico|jpg|jpeg)$ {
        try_files $uri /index.php$uri$is_args$args;
        # Optional: Don't log access to other assets
        access_log off;
   }
}

sudo chown www-data:www-data /var/www/nextcloud/ -R
sudo nginx -t
sudo systemctl reload nginx
```



## Step 4: Install and Enable PHP Modules

```
sudo apt install -y imagemagick php-imagick php8.1-common php8.1-pgsql php8.1-fpm php8.1-gd php8.1-curl php8.1-imagick php8.1-zip php8.1-xml php8.1-mbstring php8.1-bz2 php8.1-intl php8.1-bcmath php8.1-gmp
```



## Step 5: Enable HTTPS

```she
nextcloud.arccloud.com
```



```
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 443 -j ACCEPT
```



```
sudo apt install certbot python3-certbot-nginx
```



```
sudo certbot --nginx --agree-tos --redirect --hsts --staple-ocsp --email you@example.com -d nextcloud.arccloud.com
```



```shell
sudo nano /etc/nginx/conf.d/nextcloud.conf

add_header Strict-Transport-Security "max-age=31536000" always;

listen [::]:443 ssl http2; # managed by Certbot
listen 443 ssl http2; # managed by Certbot

sudo nginx -t
sudo systemctl reload nginx
```



## Step 6: Launch the Web-based Setup Wizard in your Web Browser



```
https://nextcloud.arccloud.com
```



```
sudo mkdir /var/www/nextcloud-data
sudo chown www-data:www-data /var/www/nextcloud-data -R
```



![nextcloud-ubuntu-22.04-install-guide](https://www.linuxbabe.com/wp-content/uploads/2017/03/nextcloud-ubuntu-22.04-install-guide.png)



## How to Set up NextCloud Email Notification

```
Settings` -> `Personal Info
```



## How to Reset Nextcloud User Password From Command Line

```
sudo -u www-data php /var/www/nextcloud/occ user:resetpassword nextcloud_username
sudo -u www-data php /var/www/nextcloud/occ
# OR
sudo -u www-data php /var/www/nextcloud/console.php
```



## How to Move the Data Directory

```
sudo mkdir /media/linuxbabe/b43e4eea-9796-4ac6-9c48-2bcaa46353731/nextcloud-data/
sudo cp /var/www/nextcloud-data/* /media/linuxbabe/b43e4eea-9796-4ac6-9c48-2bcaa46353731/nextcloud-data/ -R
sudo cp /var/www/nextcloud-data/.ocdata /media/linuxbabe/b43e4eea-9796-4ac6-9c48-2bcaa46353731/nextcloud-data/

sudo chown www-data:www-data /media/linuxbabe/b43e4eea-9796-4ac6-9c48-2bcaa46353731/nextcloud-data/ -R

sudo nano /var/www/nextcloud/config/config.php
'datadirectory' => '/var/www/nextcloud-data',
```



## Step 7: Increase PHP Memory Limit

```
sudo vim /etc/php/8.1/fpm/php.ini
memory_limit = 128M
memory_limit = 512M
# OR
sudo sed -i 's/memory_limit = 128M/memory_limit = 512M/g' /etc/php/8.1/fpm/php.ini

sudo systemctl reload php8.1-fpm
```



## Step 8: Set Up PHP to Properly Query System Environment Variables

```
sudo vim /etc/php/8.1/fpm/pool.d/www.conf
clear_env = no
#OR
sudo sed -i 's/;clear_env = no/clear_env = no/g' /etc/php/8.1/fpm/pool.d/www.conf

sudo systemctl reload php8.1-fpm
```



## Step 9: Increase Upload File Size Limit

```
sudo vim /etc/nginx/conf.d/nextcloud.conf
client_max_body_size 1024M;

sudo systemctl reload nginx

sudo vim /etc/php/8.1/fpm/php.ini
upload_max_filesize = 1024M

#OR
sudo sed -i 's/upload_max_filesize = 2M/upload_max_filesize = 1024M/g' /etc/php/8.1/fpm/php.ini

sudo systemctl restart php8.1-fpm
```



## Step 10: Configure Redis Cache for NextCloud

 **settings** -> **overview**

```
No memory cache has been configured. To enhance your performance please configure a memcache if available.
```



```shell
sudo apt install redis-server -y

redis-server -v

systemctl status redis
sudo systemctl start redis-server
sudo systemctl enable redis-server	

sudo apt install php8.1-redis -y
php8.1 --ri redis

sudo phpenmod redis

sudo nano /var/www/nextcloud/config/config.php
'memcache.distributed' => '\OC\Memcache\Redis',
'memcache.local' => '\OC\Memcache\Redis',
'memcache.locking' => '\OC\Memcache\Redis',
'redis' => array(
     'host' => 'localhost',
     'port' => 6379,
     ),
     
sudo systemctl restart nginx php8.1-fpm
```

![nextcloud memory cache redis local cache](https://www.linuxbabe.com/wp-content/uploads/2018/05/nextcloud-memory-cache-redis-local-cache.png)





## Adding Missing Indexes

**Settings** -> **Overview**

```
The database is missing some indexes. Due to the fact that adding indexes on big tables could take some time they were not added automatically.
```



```
cd /var/www/nextcloud/
sudo -u www-data php occ db:add-missing-indices
```



## Conversion to Big Int

**Settings** -> **Overview**

```
Some columns in the database are missing a conversion to big int. Due to the fact that changing column types on big tables could take some time they were not changed automatically.
```



```
cd /var/www/nextcloud/
sudo -u www-data php occ maintenance:mode --on
sudo -u www-data php occ db:convert-filecache-bigint
sudo -u www-data php occ maintenance:mode --off
```



## How to Install NextCloud Client on Ubuntu 22.04 Desktop

```
sudo apt install nextcloud-client
```



## How to Enable OnlyOffice/Collabora Online

```
Apps` -> `Office & Text
community document server app
```



![nextcloud onlyoffice community document server](https://www.linuxbabe.com/wp-content/uploads/2020/04/nextcloud-onlyoffice-community-document-server.png)



## Adding Local DNS Entry

```shell
sudo vim /etc/hosts
127.0.0.1   localhost nextcloud.arccloud.com
127.0.0.1   localhost focal ubuntu nextcloud.arccloud.com collabora.example.com
```



## Using Cron to Run Background Jobs

**Settings** -> **Basic Settings** and select **Cron**.

![Nextcloud Use system cron service to call the cron.php file every 5 minutes](https://www.linuxbabe.com/wp-content/uploads/2020/04/Nextcloud-Use-system-cron-service-to-call-the-cron.php-file-every-5-minutes.png)



```
sudo -u www-data crontab -e
*/5 * * * * php8.1 -f /var/www/nextcloud/cron.php
```



## (Optional) Prevent Malicious Login Attempts

```
sudo nano /etc/nginx/conf.d/nextcloud.conf
location ~* ^/login{
       try_files $uri /index.php;
       include fastcgi_params;
       fastcgi_split_path_info ^(.+\.php)(/.*)$;
       fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
       fastcgi_param PATH_INFO $fastcgi_path_info;
       #Avoid sending the security headers twice
       fastcgi_param modHeadersAvailable true;
       fastcgi_param front_controller_active true;
       fastcgi_pass unix:/run/php/php8.1-fpm.sock;
       fastcgi_intercept_errors on;
       fastcgi_request_buffering off;

       allow 78.56.34.12;
       deny all;
}

sudo nginx -t
sudo systemctl reload nginx
```