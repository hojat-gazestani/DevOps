# Elasticsearch 7.7.1, Kibana 7.7.1, Logstash 7.7.1, and Filebeat 7.7.1.

```sh
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch |sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch kibana nginx logstash
```

# Configuring Elasticsearch

```sh
sudo vim /etc/elasticsearch/elasticsearch.yml
network.host: 0.0.0.0
discovery.seed_hosts: ["127.0.0.1"]

sudo vim /etc/elasticsearch/jvm.options
-Xms1g
-Xmx1g
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
sudo systemctl restart elasticsearch
curl -x 127.0.0.1:9200
```

```sh
curl GET "localhost:9200"
```

# Configuring the Kibana

```sh
sudo systemctl start kibana
echo "kibanaadmin:`openssl passwd -apr1`" | sudo tee -a /etc/nginx/htpasswd.users
sudo vim /etc/nginx/sites-available/kibana_local
server {
    listen 80;

    server_name kibana.local;

    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/htpasswd.users;

    location / {
        proxy_pass http://localhost:5601;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

sudo ln -s /etc/nginx/sites-available/kibana_local /etc/nginx/sites-enabled/kibana_local
sudo nginx -t
sudo systemctl reload nginx
sudo ufw allow 'Nginx Full'
```



# 03 - simpel example

```sh
sudo apt install nginx -y
sudo usermod -aG adm logstash
```

```sh
sudo mkdir /etc/logstash/pattern
sudo chmod 755 -R /etc/logstash/pattern

sudo vim /etc/logstash/pattern/nginx
NGUSERNAME [a-zA-Z\.\@\-\+_%]+
NGUSER %{NGUSERNAME}
```

```sh
sudo vim /etc/logstash/conf.d/nginx.conf 
input {
  file {
    path => "/var/log/nginx/access.log"
    start_position => "beginning"
    sincedb_path => "/dev/null"
  }
}
filter {
    grok {
      patterns_dir => ["/etc/logstash/pattern"]
      match => { "message" => "%{IPORHOST:clientip} %{NGUSER:ident} %{NGUSER:auth} \[%{HTTPDATE:timestamp}\] \"%{WORD:verb} %{URIPATHPARAM:request} HTTP/%{NUMBER:httpversion}\" %{NUMBER:response}" }
    }
}
output {
  elasticsearch {
      hosts => ["127.0.0.1:9200"]
      index => "nginx-%{+YYYY.MM.dd}"
  }
}
```

```sh
sudo systemctl restart logstash.service 
```

# filebeat

## Do this on filebeat server
```sh
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch |sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install filebeat nginx -y
```

```sh
sudo vim /etc/filebeat/filebeat.yml
output.elasticsearch:
  hosts: ["192.168.56.41:9200"]


sudo filebeat modules list
sudo filebeat modules enable nginx
ls /etc/filebeat/modules.d/
sudo systemctl restart filebeat
```

# Filebeat and Logstash

## Change logstash configuration on ELK host
```sh
sudo vim /etc/logstash/conf.d/nginx.conf 
input {
  beats {
    port => 5044
  }
}
filter {
    grok {
      patterns_dir => ["/etc/logstash/pattern"]
      match => { "message" => "%{IPORHOST:clientip} %{NGUSER:ident} %{NGUSER:auth} \[%{HTTPDATE:timestamp}\] \"%{WORD:verb} %{URIPATHPARAM:request} HTTP/%{NUMBER:httpversion}\" %{NUMBER:response}" }
    }
}
output {
  elasticsearch {
      hosts => ["127.0.0.1:9200"]
      index => "elk_fb_logstash-%{+YYYY.MM.dd}"
  }
}

sudo systemctl restart logstash.service 
sudo tail -f /var/log/logstash/logstash-plain.log
```

## chage filebeat configuration on nginx host

```sh
sudo vim /etc/filebeat/filebeat.yml
#output.elasticsearch:
  #hosts: ["192.168.56.41:9200"]

output.logstash:
  hosts: ["192.168.56.41:5044"]

sudo systemctl stop filebeat
sudo rm -rf /var/lib/filebeat/registry
sudo filebeat -e
sudo systemctl start filebeat
sudo systemctl restart filebeat
```

```sh
sudo filebeat modules disable nginx

sudo vim /etc/filebeat/filebeat.yml
- type: filestream
  id: my-filestream-id
  enabled: true
  paths:
    - /var/log/*.log
    - /var/log/nginx/*.log

sudo systemctl restart filebeat
curl 127.0.0.1
curl 127.0.0.1/sdf