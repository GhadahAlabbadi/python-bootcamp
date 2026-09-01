# Week 6 - Day 2

## Overview

Today focused on understanding the internal structure and request flow of a **Django application**.

The session covered Django's **MVT architecture**, request-response flow, URL routing, app-level URLs, views, templates, basic model concepts, troubleshooting common Django errors, and building a simple multi-page Django application.

---

## Topics Covered

- Django Request-Response Flow
- MVT Architecture
- MVC vs MVT
- Model Layer
- View Layer
- Template Layer
- URL Resolver
- URL Patterns
- Route Naming
- App-Level Routing
- `include()`
- Dynamic URL Patterns
- Template Variables
- Template Tags
- Template Inheritance
- Troubleshooting Common Django Errors
- Multi-Page Django Application
- GitHub Project Workflow

---

## Key Concepts

### Django Foundation

The main Django components introduced so far are:

```text
Environment → Workspace + venv + dependencies
Project     → manage.py, settings.py, urls.py
App         → Feature module registered in settings
View        → Python function that returns a response
URLconf     → Route that connects the browser to the view
```

These components work together to create a structured Django application.

---

### Django Request Flow

A simplified Django request flow is:

```text
Browser
   ↓
URLconf
   ↓
View
   ↓
Context
   ↓
Template
   ↓
HTML
```

Django follows a predictable chain of responsibility rather than using unrelated files.

---

### Full Request-Response Flow

The complete request flow includes more internal Django layers:

```text
Client Request
      ↓
WSGI / ASGI
      ↓
Middleware In
      ↓
URL Resolver
      ↓
View Executes
      ↓
Template Renders
      ↓
Middleware Out
      ↓
Response
```

The view is only one step inside a larger request-response pipeline.

---

### MVT Architecture

Django uses **MVT**:

```text
Model ↔ View → Template
```

MVT stands for:

- **Model**
- **View**
- **Template**

---

### MVT vs MVC

Traditional MVC uses:

```text
Model ↔ Controller ↔ View
```

Django uses:

```text
Model ↔ View → Template
```

In Django:

- The URL dispatcher and view help handle the request.
- The template represents the presentation layer.

---

### The Three Layers

#### Model

The **Model** defines:

- Data structure
- Business rules
- Database tables as Python classes

Rule:

```text
Model = Data
```

---

#### View

The **View**:

- Receives the request
- Prepares data
- Decides what response should be returned
- Passes data to templates when needed

Rule:

```text
View = Decision
```

---

#### Template

The **Template** creates the final HTML shown to the user.

It can use:

- Variables
- Template tags
- Loops
- Conditions
- Filters
- Template inheritance

Rule:

```text
Template = Presentation
```

---

### URL Resolver

The URL resolver connects a browser address to a Python view.

Example:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", book_list, name="book_list"),
    path("books/<int:id>/", book_detail, name="book_detail"),
]
```

Important rules:

- Django reads URL patterns from top to bottom.
- The first matching route is used.
- Route order matters.
- Routes should be named.
- App routes should be separated into app-level `urls.py` files.
- A 404 error can help identify where routing failed.

---

### Dynamic URL Patterns

Django can capture values from URLs.

Example:

```python
path("books/<int:id>/", book_detail, name="book_detail")
```

Here:

```text
<int:id>
```

means Django expects an integer value from the URL and passes it to the view.

---

### Naming Routes

Routes should have reusable names.

Example:

```python
path("books/", book_list, name="book_list")
```

This avoids hardcoding URLs throughout templates and redirects.

---

### App-Level Routing

For cleaner and more scalable projects, each app can have its own `urls.py`.

Project-level `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    path("", include("pages.urls")),
]
```

App-level `pages/urls.py`:

```python
from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="index"),
]
```

The request flow becomes:

```text
Browser
   ↓
Project URLs
   ↓
App URLs
   ↓
View
```

This structure keeps routing organized as the application grows.

---

### View Layer

A Django view should act as a coordinator.

Example:

```python
def book_list(request):
    books = Book.objects.all()

    context = {
        "books": books
    }

    return render(
        request,
        "books/list.html",
        context
    )
```

The view:

1. Receives the request.
2. Gets or prepares data.
3. Builds the context.
4. Chooses a template.
5. Returns a response.

Good views should be:

- Small
- Clean
- Testable

Avoid placing:

- Large HTML strings
- Heavy business logic
- Low-level SQL

directly inside the view.

> Thin views are easier to debug and easier to grow.

---

### Context

A **context** is the data passed from a view to a template.

Example:

```python
context = {
    "books": books
}
```

Then the template can access:

```django
{{ books }}
```

The context acts as the connection between Python logic and the HTML template.

---

### Template Layer

Templates turn data into the user interface.

Example:

```django
{% extends "base.html" %}

{% block content %}

<h1>Books</h1>

{% for book in books %}

    <p>{{ book.title }}</p>

{% empty %}

    <p>No books found.</p>

{% endfor %}

{% endblock %}
```

---

### Template Variables

Variables display data passed through the context.

Example:

```django
{{ book.title }}
```

---

### Template Tags

Template tags control presentation logic.

Examples:

```django
{% for book in books %}
{% endfor %}
```

and:

```django
{% if condition %}
{% endif %}
```

---

### Template Inheritance

Template inheritance prevents repeating the same page layout.

Example:

```django
{% extends "base.html" %}
```

Then a template can replace specific blocks:

```django
{% block content %}
    ...
{% endblock %}
```

This allows multiple pages to share the same main layout.

---

### Template Responsibility

Templates should focus on presenting data.

They should not contain business decisions or heavy application logic.

```text
Template = Presentation
```

---

### Model Layer

A Django model represents structured application data.

Example:

```python
class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    year = models.IntegerField()
```

A model class can represent a database table.

Example mapping:

```text
Book Model
   ↓
Database Table
```

Fields can represent table columns:

```text
title   → short text column
author  → short text column
year    → number column
```

The session only introduced the role of models at a high level.

---

### Troubleshooting Mindset

When a Django error appears:

> Read the error first, then check the correct layer.

Common issues:

#### `django-admin` Not Found

Possible solution:

```text
Activate the virtual environment and install Django.
```

---

#### `ModuleNotFoundError: core`

Check:

- App name
- `INSTALLED_APPS`

---

#### 404 Page Not Found

Check:

- URL path spelling
- `include()`
- URL order
- URL mappings

---

#### Port Already in Use

Run the development server using another port:

```bash
python manage.py runserver 8080
```

---

#### View Does Not Appear

Check:

- View import
- URL mapping
- Server refresh

---

# Labs

## Lab 1 — Multi-Page Django Starter Site

The guided lab focused on creating and testing the first multi-page Django application.

Steps:

1. Create project `mysite`.
2. Create app `core`.
3. Register `core` in `INSTALLED_APPS`.
4. Create multiple views:
   - Home
   - About
   - Contact
5. Map URLs properly.
6. Test all pages in the browser.
7. Freeze dependencies.
8. Push the project to GitHub.

Deliverables:

```text
Working browser screenshots
+
GitHub repository link
```

---

## Lab 2 — Cleaner App-Level Routing

The challenge focused on improving URL organization.

Create a `pages` app with views such as:

```text
index
faq
team
```

Project-level URLs should include the app URLs:

```python
# project/urls.py

path("", include("pages.urls"))
```

Then define app-specific routes:

```python
# pages/urls.py

path("", index, name="index")
```

Each route should have a name so it can be reused inside templates.

Example:

```django
{% url 'index' %}
```

---

## URL Flow

With app-level routing, the full route becomes:

```text
Browser
   ↓
Project URLs
   ↓
App URLs
   ↓
View
   ↓
Context
   ↓
Template
   ↓
HTML Response
```

---

## Key Takeaways

- Django follows a predictable request-response flow.
- Django uses the MVT architecture: Model, View, and Template.
- Models represent application data.
- Views receive requests and coordinate responses.
- Templates are responsible for presentation.
- Context passes data from views to templates.
- URL patterns connect browser paths to views.
- Django checks URL patterns from top to bottom.
- Route order matters.
- Named URLs make routes reusable.
- `include()` allows routing to be separated between apps.
- App-level `urls.py` files create cleaner and more scalable projects.
- Templates support variables, tags, loops, conditions, and inheritance.
- Views should remain small and focused.
- Troubleshooting should begin by identifying which Django layer caused the error.

---

**Status:** ✅ Completed
