# Week 6 - Day 1

## Overview

Today focused on getting started with **Django** and understanding how a Django web application is structured.

The session covered why frameworks are useful, how to prepare an isolated Python environment, install Django, create a Django project and app, register the app, create the first view, connect it to a URL, and run the development server.

By the end of the session, the browser was able to send a request to a Django URL and receive a response from a custom view.

---

## Topics Covered

- Introduction to Django
- Why Web Frameworks Are Used
- Virtual Environments
- Installing Django
- `requirements.txt`
- `django-admin`
- `manage.py`
- Django Project Structure
- `settings.py`
- Django Projects vs Apps
- Creating and Registering an App
- Django Views
- `HttpRequest`
- `HttpResponse`
- URL Routing
- `urlpatterns`
- Running the Django Development Server
- Django Request–Response Flow

---

## Key Concepts

### Why Use a Framework?

Without a framework, developers need to manually implement features such as:

- Routing
- Request handling
- HTML rendering
- Forms
- Security
- Database access

Django provides reusable and production-ready building blocks with an organized project structure.

This allows developers to focus more on application features instead of rebuilding common web functionality.

---

### Django

**Django** is a Python web framework that provides tools and structure for building web applications.

It helps organize application components such as:

- URLs
- Views
- Templates
- Forms
- Models
- Security
- Database operations

---

### Virtual Environment

A **Virtual Environment** provides an isolated Python environment for a project.

Each project can have its own:

- Python packages
- Django version
- Dependencies

This helps avoid conflicts between different projects.

Create a project workspace:

```bash
mkdir myproject
cd myproject
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

When the environment is activated, `(venv)` appears in the terminal.

> The workspace folder is not yet the Django project.

---

### Installing Django

Install Django inside the virtual environment:

```bash
pip install django
```

Check the installed Django version:

```bash
django-admin --version
```

Save installed dependencies:

```bash
pip freeze > requirements.txt
```

The `requirements.txt` file records installed packages and versions so the same environment can be recreated later.

Install dependencies from the file:

```bash
pip install -r requirements.txt
```

---

### `django-admin` vs `manage.py`

Django provides two important command tools.

#### `django-admin`

Used before or outside a specific Django project.

It can create a new project structure.

Example:

```bash
django-admin startproject mysite
```

#### `manage.py`

Created inside each Django project.

It is used for project-specific commands such as:

```bash
python manage.py runserver
```

It is also used for:

- Creating apps
- Running migrations
- Opening the Django shell
- Running the development server

---

### Creating a Django Project

Create a Django project:

```bash
django-admin startproject mysite
```

Move into the project:

```bash
cd mysite
```

Django creates the following structure:

```text
mysite/
│
├── manage.py
│
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

### Main Django Project Files

#### `manage.py`

Used to run project-specific Django commands.

Examples:

```bash
python manage.py runserver
python manage.py startapp core
```

#### `settings.py`

Acts as the main control panel for the Django project.

Important settings include:

- `INSTALLED_APPS` — apps activated in the project
- `MIDDLEWARE` — processing layers around requests and responses
- `ROOT_URLCONF` — defines where URL routing starts
- `TEMPLATES` — template configuration
- `STATIC_URL` — static files such as CSS, JavaScript, and images
- `BASE_DIR` — base path of the project

#### `urls.py`

Contains the root URL configuration and maps browser paths to views.

#### `wsgi.py` and `asgi.py`

Entry points used when Django communicates with production web servers.

---

### Project vs App

A **Django Project** is the main container for the entire website.

It contains:

- Global settings
- Root URLs
- Server configuration

A **Django App** represents a specific feature or module inside the project.

An app can contain:

- Views
- URLs
- Templates
- Forms
- Models
- Tests

One Django project can contain multiple apps.

Example:

```text
Project
├── core
├── blog
└── store
```

---

### Creating a Django App

Create an app named `core`:

```bash
python manage.py startapp core
```

Django creates:

```text
core/
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

### Registering the App

Creating the app folder is not enough.

The app must also be registered inside `settings.py`.

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

This allows Django to recognize and use the app.

---

### Django Views

A **View** is Python logic that receives a request and returns a response.

Example inside `core/views.py`:

```python
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to Django!")
```

Flow:

```text
HttpRequest
    ↓
homepage()
    ↓
HttpResponse
```

---

### URL Routing

A view does nothing until a URL points to it.

Inside the project `urls.py`:

```python
from django.contrib import admin
from django.urls import path
from core.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
]
```

---

### Understanding `path()`

Example:

```python
path('', homepage, name='home')
```

Parts:

- `''` — URL path
- `homepage` — view function
- `name='home'` — reusable name for the route

An empty path represents the homepage:

```text
http://127.0.0.1:8000/
```

The admin path:

```python
path('admin/', admin.site.urls)
```

represents:

```text
http://127.0.0.1:8000/admin/
```

---

### URL Matching

Django checks `urlpatterns` from top to bottom.

The first matching URL pattern is used.

> **First match wins.**

---

### Running the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server normally runs at:

```text
http://127.0.0.1:8000/
```

---

### Django Request–Response Flow

The basic Django flow is:

```text
Browser
   ↓
Django Server
   ↓
URLconf
   ↓
View
   ↓
Response
   ↓
Browser
```

The browser sends a request, Django checks the URL configuration, calls the matching view, and returns the generated response.

---

# Labs

## Lab 1 — Prepare the Django Workspace

Created a clean project workspace and isolated Python environment.

```bash
mkdir myproject
cd myproject
python -m venv venv
venv\Scripts\activate
```

---

## Lab 2 — Install Django

Installed Django inside the virtual environment and recorded project dependencies.

```bash
pip install django
django-admin --version
pip freeze > requirements.txt
```

---

## Lab 3 — Create the Django Project

Created the Django project skeleton.

```bash
django-admin startproject mysite
cd mysite
```

Reviewed the generated files:

```text
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

## Lab 4 — Create and Register the First App

Created the `core` app:

```bash
python manage.py startapp core
```

Registered the app inside `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

---

## Lab 5 — Create the First Django View

Created a homepage view inside `core/views.py`:

```python
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to Django!")
```

---

## Lab 6 — Connect the View to a URL

Imported the homepage view and connected it to the root URL:

```python
from django.contrib import admin
from django.urls import path
from core.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
]
```

---

## Lab 7 — Run and Test the Server

Started the development server:

```bash
python manage.py runserver
```

Opened:

```text
http://127.0.0.1:8000/
```

Verified that the browser received the response:

```text
Welcome to Django!
```

---

## Key Takeaways

- Django provides reusable tools and structure for web development.
- Virtual environments isolate project dependencies.
- `requirements.txt` records installed package versions.
- `django-admin` is commonly used to create a Django project.
- `manage.py` runs project-specific Django commands.
- A Django project can contain multiple apps.
- Apps must be registered in `INSTALLED_APPS`.
- A view receives an HTTP request and returns an HTTP response.
- URLs connect browser paths to Django views.
- Django checks URL patterns from top to bottom.
- The complete flow is **Browser → Django Server → URLconf → View → Response**.

---

**Status:** ✅ Completed
