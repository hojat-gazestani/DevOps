#  install Docker on Ubuntu 20.04




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

# Install python

```bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-venv python3-pip
```

## Create my application
```bash
python3 -m venv myapp
source myapp/bin/activate

pip install django gunicorn
django-admin startproject myproject

cd myproject
python manage.py startapp myapp

```

```bash
vim myproject/settings.py

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	...
    'myapp',
]
```

```bash
vim myapp/views.py
from django.http import HttpResponse
import socket

hostname = socket.gethostname()

def hello(request):
    return HttpResponse(f"Hello form {hostname}")
    
def app1(request):
    return HttpResponse(f"app1 on {hostname}")
    
def app2(request):
    return HttpResponse(f"app2 on {hostname}")
```

```bash
vim myproject/urls.py
from django.urls import path, include
urlpatterns = [
	...
    path('', include('myapp.urls')),
    path('app1', include('myapp.urls')),
    path('app2', include('myapp.urls')),
]
```

```bash
vim myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('app1/', views.app1, name='app1'),
    path('app2/', views.app2, name='app'),
]
```

```bash
python manage.py migrate
gunicorn -b 0.0.0.0:8000 myproject.wsgi:application
```

```bash
curl http://192.168.56.22:8000/hello/
```

```bash
curl http://192.168.56.22:8000/
```

## Dockerize
```bash
vim Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the server will run on
EXPOSE 8000

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "myproject.wsgi:application"]
```bash
pip freeze > requirements.txt
```

```bash
docker build -t my_app .
docker run -p 8010:8000 my_app
docker run -p 8011:8000 my_app
docker run -p 8012:8000 my_app
```