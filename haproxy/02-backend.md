
```bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-venv python3-pip

```


```bash
python3 -m venv myenv
source myenv/bin/activate
```

```bash
	
```

```bash
django-admin startproject myproject
```

## Create my application
```bash
cd myproject
python manage.py startapp myapp

```

```bash
vim myproject/settings.py


ALLOWED_HOSTS = ['192.168.56.22']

INSTALLED_APPS = [
	...
    'myapp',
]
```

```bash
vim myapp/views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("my application")
```

```bash
vim myproject/urls.py
urlpatterns = [
	...
    path('', include('myapp.urls'))
]
```

```bash
vim myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

```bash
python manage.py migrate
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
EXPOSE 8001

# Start the server
CMD ["gunicorn", "-b", "0.0.0.0:8001", "auth_project.wsgi:application"]
```

```bash
pip freeze > requirements.txt
```

```bash
docker build -t auth_app .
docker run -p 8001:8001 auth_app
```