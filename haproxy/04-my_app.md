## Create my application

## Create Image application
```bash
mkdir app && cd app
python3 -m venv myapp
source myapp/bin/activate

pip install django gunicorn
django-admin startproject myproject

cd myproject
python manage.py startapp myapp
```

```python
vim myproject/settings.py

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
	...
    'myapp',
]
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'myproject.context_processors.gunicorn_port',
            ],
        },
    },
]
```

```python
vim myproject/context_processors.py                                                                                                             ─╯
import socket

def gunicorn_port(request):
    port = request.META.get('SERVER_PORT', '')
    if port and ':' in request.get_host():
        port = request.get_host().split(':')[-1]
    return {'gunicorn_port': port}
```

```python
vim myapp/views.py
from django.http import HttpResponse
import socket
from myproject.context_processors import gunicorn_port

hostname = socket.gethostname()

def hello(request):
    return HttpResponse(f"Hello form {hostname}, port: { gunicorn_port(request)}")
    
def app1(request):
    return HttpResponse(f"app1 on {hostname}, port: { gunicorn_port(request)}")
    
def app2(request):
    return HttpResponse(f"app2 on {hostname}, port: { gunicorn_port(request)}")
```

```python
vim myproject/urls.py
from django.urls import path, include
urlpatterns = [
	...
    path('', include('myapp.urls')),
    path('app1', include('myapp.urls')),
    path('app2', include('myapp.urls')),
]
```

```python
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
python manage.py runserver 
gunicorn -b 0.0.0.0:8000 myproject.wsgi:application
```
    
```bash
curl http://192.168.56.22:8000/
curl http://192.168.56.22:8000/app1/
curl http://192.168.56.22:8000/app2/
```

## Dockerize Django application
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

# Expose the port that the server will run on
EXPOSE 8001

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8001", "myproject.wsgi:application"]
```

```bash
pip freeze > requirements.txt
```

```bash
docker build  -t my_app .
docker run -d --hostname Myapp10 -p 8010:8001 my_app
docker run -d --hostname Myapp11 -p 8011:8001 my_app
docker run -d --hostname Myapp12 -p 8012:8001 my_app

docker ps
```