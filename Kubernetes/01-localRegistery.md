# Pulling local repository docker image from kubernetes

```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2

docker inspect 9dc5021e94ad | grep IPAddress
            "IPAddress": "172.17.0.2",

sudo vim /etc/docker/daemon.json
{
  "insecure-registries": ["172.17.0.2:5000"]
}

docker tag auth_app:latest 172.17.0.2:5000/local/auth_app
docker push  172.17.0.2:5000/local/auth_app:latest
```

```bash
user@master:~/yaml$ cat auth_app.yml 
apiVersion: v1
kind: Pod
metadata:
  name: auth-app
spec:
  containers:
    - name: auth-app
      image: 192.168.56.1:5000/local/auth_app:latest
      imagePullPolicy: Always

user@master:~/yaml$ kubectl create -f auth_app.yml
```