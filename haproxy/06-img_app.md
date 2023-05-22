#  install Docker on Ubuntu 20.04

## Create my application
```bash
mkdir img && cd img/

python3 -m venv img
source img/bin/activate

pip install django gunicorn
django-admin startproject img_project

cd img_project
python manage.py startapp img_app
```

```python
vim img_project/settings.py

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	...
    'img_app',
]
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'img_project.context_processors.gunicorn_port',
            ],
        },
    },
]
```

```python
vim auth_project/context_processors.py                                                                                                             ─╯
import socket

def gunicorn_port(request):
    port = request.META.get('SERVER_PORT', '')
    if port and ':' in request.get_host():
        port = request.get_host().split(':')[-1]
    return {'gunicorn_port': port}
```

```python
vim img_project/urls.py
from django.urls import path, include
urlpatterns = [
	...
    path('', include('img_app.urls')),
    path('img1', include('img_app.urls')),
    path('img2', include('img_app.urls')),
]
```

```python
vim img_app/views.py
from django.http import HttpResponse
import socket
from img_project.context_processors import gunicorn_port

hostname = socket.gethostname()

def hello(request):
    return HttpResponse(f"Hello form {hostname}, port: { gunicorn_port(request)}")
    
def img1(request):
    return HttpResponse(f"img1 on {hostname}, port: { gunicorn_port(request)}")
    
def img2(request):
    return HttpResponse(f"img2 on {hostname, port: { gunicorn_port(request)}}")
```


```python
vim img_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('img/', views.hello, name='hello'),
    path('img1/', views.img1, name='img1'),
    path('img2/', views.img2, name='app'),
]
```

```bash
python manage.py migrate
python manage.py runserver 
gunicorn -b 0.0.0.0:8003 img_project.wsgi:application
```

```bash
curl http://192.168.56.22:8003/img/
curl http://192.168.56.22:8003/img1/
curl http://192.168.56.22:8003/img2/
```

## Dockerize
```bash
vim Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the hostname
ARG APP_NAME="My_App "
ARG CREATED_TIME
RUN hostname "${APP_NAME}+${CREATED_TIME}+$(cat /proc/self/cgroup | grep "docker" | sed s/\\//\\n/g | tail -1)_$(hostname | awk -F'-' '{print substr($NF, length($NF)-1, length($NF))}')"


# Expose the port that the server will run on
EXPOSE 8003

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8003", "img_project.wsgi:application"]
```bash
pip freeze > requirements.txt
```

```bash
docker build --build-arg CREATED_TIME=$(date +" ""%M-%S"" ") -t img_app .
docker run -p 8030:8003 img_app
docker run -p 8031:8003 img_app
docker run -p 8032:8003 img_app
```