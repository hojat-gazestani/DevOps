## Simple Backend and frondend

* Scenario

![BackFront](https://github.com/hojat-gazestani/DevOps/blob/main/haproxy/pictures/03-HAProxy/01-BackFront.jpg)


```bash
mkdir django && cd django
git clone https://github.com/hojat-gazestani/My_app.git && cd My_app/
source myapp/bin/activate
pip install --no-cache-dir -r requirements.txt

docker build  -t my_app .
docker run -d --hostname Myapp10 -p 8010:8001 my_app
docker run -d --hostname Myapp11 -p 8011:8001 my_app
docker run -d --hostname Myapp12 -p 8012:8001 my_app
```

* HAproxy config file 

My git [Mygithut](https://github.com/hojat-gazestani/HAProxy.git)

```bash
vim 01-simpleBackFront.cfg
frontend myapp
    bind *:80
    mode tcp
    default_backend myapp

backend myapp
    mode tcp
    server myapp1 192.168.56.22:8010
```

```bash
haproxy -f 01-simpleBackFront.cfg
```

* To Backend server
```bash
curl http://127.0.0.1:8001
```

* To HAProxy server
```bash
curl http://127.0.0.1:8010
```