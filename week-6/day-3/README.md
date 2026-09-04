# Week 6 - Day 3

## Overview

Today focused on strengthening the understanding of **Django's MVT architecture** and exploring how data, templates, middleware, and URL routing work together inside a Django application.

The session covered context as the bridge between Python and HTML, template inheritance, middleware, complete MVT flow, clean Django architecture, app-level routing, `include()`, routing vocabulary, URL matching order, dynamic routes, and the full URL dispatch process.

---

## Topics Covered

- Django MVT Architecture Review
- Context
- Middleware
- Template Inheritance
- Complete MVT Flow
- Clean Django Architecture
- Common Architecture Mistakes
- URL Routing
- URLconf
- `path()`
- `include()`
- App-Level URLs
- Project-Level URLs
- URL Names
- Namespaces
- Dynamic URL Parameters
- Path Converters
- URL Matching Order
- URL Resolver
- URL Dispatch Flow
- Guided MVT Lab
- Movie Catalog Challenge

---

## Key Concepts

### Context: The Bridge Between Python and HTML

The **context** is a dictionary that transfers data from a Django view to an HTML template.

Example:

```python
context = {
    "title": "Library",
    "books": books,
    "count": len(books),
}

return render(
    request,
    "books/list.html",
    context
)
```

The template can access these values:

```django
<h1>{{ title }}</h1>

<p>Total: {{ count }}</p>

{% for book in books %}
    <p>{{ book.title }}</p>
{% endfor %}
```

The flow is:

```text
Python View
    ↓
Context
    ↓
Template
    ↓
HTML
```

> If a template knows something, the view usually passed it through the context.

---

### Middleware

Middleware represents processing layers around Django requests and responses.

A request may pass through layers such as:

```text
Browser
   ↓
Security
   ↓
Session
   ↓
Authentication
   ↓
CSRF
   ↓
View
```

Middleware can inspect or modify:

- Requests before they reach the view
- Responses before they return to the browser

Examples:

- Security headers
- Session state
- User authentication information
- CSRF protection

The request moves:

```text
Top → Bottom
```

The response returns:

```text
Bottom → Top
```

---

### Template Inheritance

Template inheritance allows multiple pages to reuse one shared layout.

Example structure:

```text
base.html
├── home.html
├── books/list.html
└── contact.html
```

The base template can contain shared elements such as:

- Navigation
- Footer
- CSS links
- Main layout
- Content blocks

Child templates contain only page-specific content.

Example:

```django
{% extends "base.html" %}

{% block content %}
    <h1>Books</h1>
{% endblock %}
```

This avoids repeating the same HTML on every page.

> Avoid copy-paste HTML. Extend the base template and override blocks.

---

### Complete MVT Example

A simple books page connects all Django MVT concepts.

```text
Model
Book(title, author, year)

        ↓

View
book_list gets books
and sends context

        ↓

URL
path("books/", book_list)

        ↓

Template
Loops over books in HTML
```

Full browser flow:

```text
Browser requests /books/
        ↓
URLconf matches book_list
        ↓
View prepares books
        ↓
Context passes books
        ↓
Template renders list
        ↓
Browser displays HTML
```

---

### Clean Django Architecture

Each Django layer should have a clear responsibility.

```text
Model    → Data
View     → Application decisions
Template → Presentation
URLconf  → Routing
Context  → Data bridge
```

Good Django architecture includes:

- Thin views
- Clean templates
- App-level `urls.py`
- Named routes
- Template inheritance
- Clear separation of responsibilities

---

### Common Architecture Mistakes

#### Huge Views

Avoid putting too much logic inside one view.

Heavy decisions can later be moved to:

- Helper functions
- Models
- Other application layers

---

#### HTML Inside Python

Avoid large HTML strings inside:

```python
HttpResponse(...)
```

Use:

```python
render()
```

with templates instead.

---

#### Unnamed URLs

Avoid routes without names.

Use:

```python
path("books/", book_list, name="book_list")
```

Named routes make links more stable.

---

#### Copy-Paste Templates

Avoid repeating the same HTML.

Use:

- `base.html`
- Blocks
- Template inheritance
- Includes

---

#### Wrong Folder Paths

Use a clear template structure such as:

```text
app/
└── templates/
    └── app/
        └── page.html
```

---

#### Circular Imports

Keep app dependencies clean and import only what is needed.

---

### Django Architecture Summary

The foundation of Django architecture includes:

```text
MVT
→ Model, View, Template have clear responsibilities

Request Flow
→ Browser request moves through middleware,
  URLconf, view, and template

URL Resolver
→ Reads routes top to bottom
→ First match wins

Context
→ Connects Python data to HTML

Clean Structure
→ Thin views
→ Clean templates
→ App-level urls.py
```

---

# Django Routing

## Routing Mental Model

URLs are the road system of a Django application.

The simplified routing flow is:

```text
Browser
   ↓
URLconf
   ↓
Pattern Match
   ↓
View
   ↓
Response
```

Routing connects:

```text
Requested Path
        ↓
Python Function / Class
```

---

## Routing Vocabulary

### URLconf

The Django URL configuration module.

Usually stored in:

```text
urls.py
```

---

### Path

A route definition inside:

```python
urlpatterns
```

Example:

```python
path("about/", views.about, name="about")
```

---

### Converter

Validates and converts dynamic URL values.

Example:

```python
<int:id>
```

Django verifies that the value is an integer.

---

### `include()`

Loads routes from another app.

Example:

```python
path("", include("core.urls"))
```

---

### Namespace

Helps prevent naming conflicts between routes in different apps.

---

### Reverse

Builds a URL using its route name instead of hardcoding the URL.

---

### Route

A route consists of:

```text
URL Pattern
+
Connected View
+
Optional Name
```

---

## Project-Level vs App-Level URLs

Large Django projects should separate routing responsibilities.

### Project-Level `urls.py`

Example:

```text
project/urls.py
```

Responsibilities:

- Global router
- Admin route
- Routes to apps using `include()`
- Global error handlers
- Static/media routes during development

The project router should mainly distribute traffic to the correct app.

---

### App-Level `urls.py`

Example:

```text
core/urls.py
```

Responsibilities:

- Feature-specific routes
- Route names
- Dynamic parameters
- App namespace
- Local routing rules

The root URL file should not contain every route in the application.

---

## Basic App-Level Routing

Example:

```python
# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
```

### Empty Path

```python
path("", views.home, name="home")
```

The empty string represents the app's landing page.

---

### Trailing Slash

Use trailing slashes consistently.

Example:

```text
about/
contact/
```

---

### `name=`

Provides a stable reference for a URL.

Example:

```python
name="about"
```

---

### View

Example:

```python
views.home
```

This is the function or class executed when the URL matches.

> A URL pattern is useless unless it points to a view.

---

## `include()`: Modular Routing

The project router can delegate routing to different apps.

Example:

```python
urlpatterns = [
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

This can produce routes such as:

```text
core.urls
→ home
→ about

blog.urls
→ posts
→ detail

shop.urls
→ products
→ cart
```

`include()` keeps each app responsible for its own routes.

---

## URL Matching Order

Django reads URL patterns:

```text
Top → Bottom
```

The first matching pattern wins.

Example:

```python
urlpatterns = [
    path("product/create/", create_view),
    path("product/<str:id>/", detail_view),
]
```

When requesting:

```text
/product/create/
```

Django matches:

```python
product/create/
```

before checking the generic dynamic route.

### Specific Routes First

Put fixed and specific routes before generic dynamic routes.

---

### Generic Routes Later

A route such as:

```python
product/<str:id>/
```

may match more values than expected.

---

### No Longest Match Rule

Django does not search for the longest route.

It simply uses:

> First match wins.

---

### No Match

If no URL pattern matches the request:

```text
404 Page Not Found
```

---

## URL Dispatch Flow

The internal URL dispatch process is:

```text
Request
   ↓
ROOT_URLCONF
   ↓
urlpatterns[]
   ↓
Resolver checks routes
   ↓
First Match
   ↓
View
   ↓
Response
```

### `ROOT_URLCONF`

A setting that tells Django where the root URL configuration file is located.

---

### `urlpatterns`

The ordered list containing URL patterns.

---

### Resolver

Django's routing engine checks patterns from top to bottom.

---

### View

The Python logic triggered by the matching route.

Django follows one ordered routing table rather than searching randomly.

---

# Labs

## Guided Lab — Complete MVT Workflow

The goal was to connect:

```text
URL
→ View
→ Context
→ Template
```

inside one complete working feature.

Steps:

1. Create a `library` app.
2. Add app-level `urls.py`.
3. Create an in-memory books list.
4. Create a list view.
5. Create a detail view using a dynamic parameter:

```text
<int:id>
```

6. Create base and child templates.
7. Add a navigation menu.
8. Draw the MVT flow in the README.

Deliverables:

```text
Working pages
+
Screenshots
+
MVT flow diagram
```

---

## Challenge — Movie Catalog MVT System

The challenge focused on independently applying the MVT architecture.

### App

Create a:

```text
movies
```

app with its own:

```text
urls.py
```

### Data

Use an in-memory list containing:

- Movie title
- Year
- Rating

### Pages

Create:

- Movie list page
- Movie detail page

### Routing

Use:

- Named URLs
- Dynamic parameters

Example:

```text
/movies/
→ list all movies

/movies/3/
→ show one movie
```

### Templates

Use template inheritance from:

```text
base.html
```

### README

Explain the full MVT flow.

---

## Key Takeaways

- Context transfers data from Python views to HTML templates.
- Middleware processes requests before the view and responses after the view.
- Template inheritance prevents repeated HTML.
- Django MVT separates data, decisions, and presentation.
- Clean architecture means each layer has one responsibility.
- Project-level routing should delegate traffic to apps.
- App-level `urls.py` keeps feature routes organized.
- `include()` creates modular routing.
- Route names provide stable references.
- Dynamic URL converters capture and validate values.
- Django checks URL patterns from top to bottom.
- The first matching route always wins.
- Specific routes should appear before generic dynamic routes.
- If no route matches, Django returns a 404 response.
- The routing flow is **Request → ROOT_URLCONF → urlpatterns → first match → View → Response**.

---

**Status:** ✅ Completed
