#!/bin/bash

sudo apt update -y 

sudo sed -i 's/nameserver 127.0.0.53/nameserver 185.51.200.2/' /etc/resolv.conf

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

if [ ! -f "/etc/apt/sources.list.d/docker.list" ]; then
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
fi

sudo apt update -y

sudo apt install docker-ce
sudo usermod -aG docker ${USER}
sudo sed -i 's/nameserver 185.51.200.2/nameserver 127.0.0.53/' /etc/resolv.conf

