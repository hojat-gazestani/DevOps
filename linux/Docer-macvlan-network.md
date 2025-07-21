# Docer network

+ Use `macvlan` Network (Best for Direct LAN Access)

## Create a `macvlan` Network

```sh
docker network create -d macvlan \
  --subnet=172.27.103.0/24 \
  --gateway=172.27.103.1 \          
  -o parent=bond0 \                 
  haproxy-macvlan
```

## Run HAProxy Container with Static IP
```sh
docker run -d \
  --name haproxy \
  --network=haproxy-macvlan \
  --ip=172.27.103.53 \              # Static IP for the container
  -p 6443:6443 \                    # Bind container port to host (optional)
  -v /path/to/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg \
  haproxy:latest
```


## Docker compose

```sh
services:
  haproxy:
    image: haproxy:latest
    container_name: haproxy
    networks:
      haproxy-macvlan:
        ipv4_address: 172.27.103.53  # Static IP for the container
    ports:
      - "6443:6443"                  # Bind host:container port (optional)
    volumes:
      - /path/to/haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg
    restart: unless-stopped
```