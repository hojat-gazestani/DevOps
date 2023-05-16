# Create an Authentication Application
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
ALLOWED_HOSTS = ['*']
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
```bash
python manage.py migrate
python manage.py startapp webserver
```

 ```bash

gunicorn -b 0.0.0.0:8000 myproject.wsgi:application
```

```bash
curl http://192.168.56.22:8000/hello/
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