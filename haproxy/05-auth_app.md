# Create an Authentication Application

## Create auth application
```bash
mkdir auth && cd auth/

python3 -m venv auth
source auth/bin/activate

pip install Django gunicorn
django-admin startproject auth_project

cd auth_project/
python manage.py startapp auth_app
```

```python
vim auth_project/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
	...
    'auth_app',
]
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'auth_project.context_processors.gunicorn_port',
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
vim auth_project/urls.py 
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('', include('auth_app.urls')),
]
```

```python
vim auth_app/views.py 
from django.http import HttpResponse
import socket
from auth_project.context_processors import gunicorn_port

hostname = socket.gethostname()

def auth_root(request):
    return HttpResponse(f"auth on {hostname}, port: { gunicorn_port(request)}")
    
def auth1(request):
    return HttpResponse(f"auth1 on {hostname}, port: { gunicorn_port(request)}")
    
def auth2(request):
    return HttpResponse(f"auth2 on {hostname}, port: { gunicorn_port(request)}")
```

```python
vim auth_app/urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_root, name='auth_root'),
    path('auth1/', views.auth1, name='auth1'),
    path('auth2/', views.auth2, name='auth2'),
]
```

```bash
pip freeze > requirements.txt
```

```bash
python manage.py migrate
python manage.py runserver 
gunicorn -b 0.0.0.0:8002 auth_project.wsgi:application
```

```bash
curl http://192.168.56.22:8002/auth/
curl http://192.168.56.22:8002/auth1/
curl http://192.168.56.22:8002/auth2/
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

# Expose the port that the server will run on
EXPOSE 8002

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8002", "auth_project.wsgi:application"]
```

```bash
docker build  -t auth_app .
docker run -d --hostname AuthAPP20 -p 8020:8002 auth_app
docker run -d --hostname AuthAPP21 -p 8021:8002 auth_app
docker run -d --hostname AuthAPP22 -p 8022:8002 auth_app
```