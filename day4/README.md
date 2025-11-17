# 📘 Day 4 — Django Setup & Your First Project  
*A beginner-friendly guide to getting started with Django.*

---

## 🎯 What You Will Accomplish

By the end of Day 4, you will:

- ✔ Install Django  
- ✔ Create a Django **project**  
- ✔ Create a Django **app**  
- ✔ Understand the Django folder structure  
- ✔ Run the Django development server  
- ✔ Create a **Hello World** page using templates  
- ✔ Understand the request → view → template → response cycle  

---

## 🚀 1. Install Django

### Create and activate a virtual environment

```bash
python -m venv venv
Activate (Windows)
bash
Copy code
venv\Scripts\activate
Activate (Mac/Linux)
bash
Copy code
source venv/bin/activate
Install Django
bash
Copy code
pip install django
🏗️ 2. Create a Django Project
Run:

bash
Copy code
django-admin startproject mysite
Your project structure will look like this:

markdown
Copy code
mysite/
│── manage.py
└── mysite/
    │── __init__.py
    │── settings.py
    │── urls.py
    │── asgi.py
    └── wsgi.py
📂 What These Files Mean
manage.py – Command-line tool for running tasks (server, migrations).

settings.py – Project configuration (database, apps, middleware).

urls.py – Controls which URLs map to which views.

asgi.py / wsgi.py – Server interface files (not needed for now).

▶️ 3. Run the Development Server
bash
Copy code
python manage.py runserver
Open your browser:

👉 http://127.0.0.1:8000/

You should see the Django welcome page.

🧩 4. Create Your First Django App
Apps are modular components inside a Django project.

Create your app:

bash
Copy code
python manage.py startapp hello
Folder structure:

pgsql
Copy code
hello/
│── admin.py
│── apps.py
│── models.py
│── tests.py
└── views.py
🔗 5. Build a “Hello World” Page
Step 1 — Create a view
Edit hello/views.py:

python
Copy code
from django.shortcuts import render

def hello_world(request):
    context = {
        "message": "Hello from Django Template!"
    }
    return render(request, "hello_world.html", context)
Step 2 — Create a template
Create this structure:

markdown
Copy code
hello/
└── templates/
    └── hello_world.html
Add the HTML:

html
Copy code
<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
Step 3 — Add URLs for your app
Create hello/urls.py:

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
]
Step 4 — Connect app URLs to the main project
Edit mysite/urls.py:

python
Copy code
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
]
Step 5 — Register the app in settings
Open mysite/settings.py and add:

python
Copy code
INSTALLED_APPS = [
    ...
    'hello',
]
▶️ 6. Run the Server Again
bash
Copy code
python manage.py runserver
Visit:

👉 http://127.0.0.1:8000/

You should now see:

Hello from Django Template!