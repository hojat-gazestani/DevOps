#  install Docker on Ubuntu 20.04
the new line

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
python manage.py runserver 
gunicorn -b 0.0.0.0:8000 myproject.wsgi:application
```

```bash
curl http://192.168.56.22:8000/hello/
```

## Web Server
```bash
python manage.py startapp webserver
```

```bash
vim myproject/settings.py
INSTALLED_APPS = [
	...
    'myapp',
    'webserver',
]
```


```bash
vim webserver/views.py 
from django.http import HttpResponse

def webserver(request):
    return HttpResponse("Web Server")
```

```bash
vim myproject/urls.py
urlpatterns = [

    path('', include('myapp.urls')),
    path('webserver/', include('webserver.urls'))
]
```

```bash
vim webserver/urls.py 
from django.urls import path
from . import views

urlpatterns = [
        path('webserver/', views.webserver, name='webserver')
]
```

```bash
curl http://192.168.56.22:8000/webserver/webserver/
```

## Create an Authentication Application
```bash
mkdir auth
cd auth/

python3 -m venv auth
source auth/bin/activate

pip install Django gunicorn
```

```bash
django-admin startproject auth_project
cd auth_project/
python manage.py startapp auth_app
```

```bash
vim auth_project/settings.py
ALLOWED_HOSTS = ['192.168.56.22']
INSTALLED_APPS = [
	...
    'auth_app',
]

vim auth_project/urls.py 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
]
```

```bash
vim auth_app/views.py 
from django.shortcuts import render
from django.http import HttpResponse

def auth(request):
    return HttpResponse("Authentication Application"

vim auth_app/urls.py 
from django.urls import path
from . import views

urlpatterns = [
        path('auth/', views.auth, name='auth'),
]
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
EXPOSE 8003

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8003", "myproject.wsgi:application"]
```bash
pip freeze > requirements.txt
```

```bash
docker build -t my_app .
docker run -p 8030:8003 my_app
docker run -p 8031:8003 my_app
docker run -p 8032:8003 my_app
```
