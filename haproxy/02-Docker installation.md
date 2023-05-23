#  Install Docker on Ubuntu 20.04

```bash
sudo apt update -y
sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu focal stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update -y

sudo apt install docker-ce docker-ce-cli containerd.io

sudo systemctl start docker
sudo systemctl enable docker

docker --version

sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
```

* On my host
```bash
sudo apt install sshfs
sudo sshfs -o allow_other,default_permissions
```

