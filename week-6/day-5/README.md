# Week 6 - Day 5

## Overview

Today focused on building a **clean, scalable, and modular Django URL routing system**.

The session covered the difference between simple and dynamic URLs, built-in path converters, passing URL parameters to views, named URLs, reverse resolution, namespaces, routing debugging, common routing anti-patterns, and designing modular URL structures for projects with multiple apps.

---

## Topics Covered

- Simple Paths vs Dynamic Paths
- URL Path Parameters
- View Arguments
- Built-in Path Converters
- Passing Parameters to Views
- Named URLs
- Reverse Resolution
- `{% url %}` Template Tag
- `reverse()`
- URL Namespaces
- Routing Debugging
- `resolve()`
- Routing Anti-Patterns
- Modular Routing
- Dynamic Routes
- App-Level `urls.py`
- Custom 404 Pages
- URL Architecture Design

---

## Key Concepts

### Simple Paths vs Dynamic Paths

A **simple path** represents one fixed page.

Example:

```python
path("about/", views.about, name="about")
```

This represents:

```text
/about/
```

and always points to the same page.

---

### Dynamic Paths

Dynamic paths contain values that can change.

Example:

```python
path(
    "product/<int:id>/",
    views.product_detail,
    name="product_detail"
)
```

This can represent many different pages:

```text
/product/1/
/product/2/
/product/4/
```

For:

```text
/product/4/
```

Django extracts:

```text
id = 4
```

Dynamic URLs allow one view to serve many related pages.

---

### Path Parameters

A **path parameter** is a value extracted from the URL.

Example:

```python
<int:id>
```

Here:

- `int` is the converter
- `id` is the parameter name

For:

```text
/product/4/
```

Django extracts:

```text
id = 4
```

---

### Built-in Path Converters

Django provides built-in converters that define which values a dynamic URL can accept.

#### Integer

```python
<int:x>
```

Accepts a positive integer.

Example:

```text
/product/12/
```

---

#### String

```python
<str:x>
```

Accepts text without `/`.

Example:

```text
/user/aly/
```

---

#### Slug

```python
<slug:x>
```

Accepts URL-friendly text.

Example:

```text
/blog/my-post/
```

---

#### UUID

```python
<uuid:x>
```

Accepts UUID values.

Example:

```text
/order/550e.../
```

---

#### Path

```python
<path:x>
```

Accepts text including `/`.

Example:

```text
/files/a/b/
```

Use the narrowest converter that matches the requirement.

Avoid using:

```python
<path:x>
```

unless it is really needed because it can capture a large part of the URL.

---

### Passing Parameters to Views

Django extracts dynamic values from the URL and passes them directly to the view.

Example in `urls.py`:

```python
path(
    "product/<int:id>/",
    views.product_detail,
    name="product_detail"
)
```

View:

```python
def product_detail(request, id):
    return render(request, "product.html")
```

Request:

```text
/product/4/
```

Flow:

```text
/product/4/
     ↓
id = 4
     ↓
product_detail(request, id)
```

Because the converter is:

```python
<int:id>
```

the value passed to the view is already a Python integer.

The parameter name in the URL must match the view argument name.

```python
<int:id>
```

should match:

```python
def product_detail(request, id):
```

The URL is therefore not only used for navigation; it can also carry data into the backend.

---

## URL Names

Instead of relying directly on URL text, Django allows each route to have a stable name.

Example:

```python
path(
    "products/",
    views.product_list,
    name="product_list"
)
```

Here:

```text
product_list
```

is the route name.

---

### Hardcoded URLs

A hardcoded link might look like:

```html
<a href="/products/">Products</a>
```

The problem is that if the route changes later, the HTML link must also be manually updated.

---

### Named URLs in Templates

Instead, Django can build the URL from its route name.

```django
<a href="{% url 'product_list' %}">Products</a>
```

Django finds the actual path associated with:

```text
product_list
```

This makes route changes easier and safer.

---

## Reverse Resolution

**Reverse resolution** means generating a URL from its route name.

In Python:

```python
from django.urls import reverse
```

Example:

```python
return redirect(reverse("home"))
```

Instead of manually writing the path, Django finds the route named:

```text
home
```

---

### Reverse Resolution in Templates

Example:

```django
<a href="{% url 'home' %}">Home</a>
```

This allows routes to be changed without searching through every template for hardcoded links.

---

## Namespaces

Different Django apps may use the same route names.

For example:

```text
blog → index
shop → index
```

Without namespaces, Django may not know which `index` route is intended.

---

### App Namespace

Inside `blog/urls.py`:

```python
app_name = "blog"
```

A route may be:

```python
path("", views.index, name="index")
```

Inside `shop/urls.py`:

```python
app_name = "shop"
```

with another:

```python
path("", views.index, name="index")
```

Now the routes can be distinguished as:

```text
blog:index
shop:index
```

---

### Namespace in Templates

Blog:

```django
{% url 'blog:index' %}
```

Shop:

```django
{% url 'shop:index' %}
```

Namespaces avoid route-name collisions when a project contains multiple apps.

---

# Debugging Routing Issues

When a routing problem occurs, start by checking the requested URL and then follow the routing map.

---

### 404

A `404` may happen because of:

- App not included
- Typo in the path
- Wrong converter
- Wrong route order

---

### `NoReverseMatch`

This can happen because of:

- Missing route name
- Wrong namespace
- Wrong arguments

---

### Wrong View

The wrong view may run if a generic route appears before a more specific route.

Because Django checks routes from top to bottom:

```text
First match wins
```

Specific routes should generally appear before generic routes.

---

### Template URL Error

Use correct quotes and syntax:

```django
{% url 'home' %}
```

---

## `resolve()`

Django provides:

```python
resolve()
```

to check which view a URL resolves to.

Example:

```python
from django.urls import resolve

resolve("/products/15/")
```

This is useful when debugging routing problems.

The key troubleshooting question is:

> Did Django find the route you expected it to find?

---

# Routing Anti-Patterns

## Everything in Root `urls.py`

Avoid putting every route in the project-level URL file.

This makes the root routing file difficult to read and maintain.

Instead:

```text
Project URLs
    ↓
include()
    ↓
App URLs
```

---

## Hardcoded Links

Avoid:

```html
<a href="/products/">
```

Prefer:

```django
{% url 'products:list' %}
```

Named URLs make refactoring safer.

---

## Using `<path:x>` Too Early

Avoid using:

```python
<path:x>
```

when a narrower converter is enough.

It can capture more of the URL space than expected.

Prefer appropriate converters such as:

```python
<int:id>
<slug:slug>
<str:name>
```

---

## Duplicate Route Names

Avoid using duplicate names in the same routing scope because reverse resolution becomes confusing.

Namespaces help separate routes from different apps.

---

## Inconsistent Slashes

Keep URL formatting consistent.

For example, prefer consistently using:

```text
/about/
/contact/
/products/
```

rather than mixing routes with and without trailing slashes.

---

## Clean Routing Principle

A clean routing structure follows this separation:

```text
Root URLs
→ distribute traffic

App URLs
→ define routes

Templates
→ reverse named routes
```

---

# Labs

## Guided Lab — Fully Modular Routing System

The objective was to build a clean Django URL tree using app-level routing.

### Step 1 — Create `pages` App

Create an app responsible for general website pages.

---

### Step 2 — Add Pages

Create routes for:

```text
home
about
contact
```

---

### Step 3 — Create `blog` App

Create a separate app for blog functionality.

---

### Step 4 — Add Blog Routes

Create routes for:

```text
list
detail
category
```

---

### Step 5 — Use Namespaces

Give apps namespaces so route names remain unique.

Example:

```text
pages:home
blog:list
blog:detail
```

---

### Step 6 — Use Dynamic Parameters

Create routes containing dynamic parameters.

Example:

```python
path(
    "<int:id>/",
    views.detail,
    name="detail"
)
```

---

### Step 7 — Add a Custom 404 Page

Create a custom page for URLs that do not match any registered route.

---

### Step 8 — Use Named URLs in Templates

Use:

```django
{% url 'namespace:name' %}
```

instead of hardcoded paths.

---

### Deliverables

```text
Screenshots of working routes
+
URL tree diagram
```

---

# Challenge — Startup Platform URL Architecture

The challenge focused on designing a scalable URL architecture before writing the implementation.

The platform contains several apps.

---

## Users App

Routes:

```text
login
profile
```

Possible structure:

```text
/users/login/
/users/profile/
```

---

## Courses App

Routes:

```text
list
detail
category
```

A detail page can use a slug:

```python
path(
    "courses/<slug:slug>/",
    views.course_detail,
    name="detail"
)
```

Example:

```text
/courses/python-basics/
```

---

## Payments App

Routes:

```text
checkout
receipt
```

Possible structure:

```text
/payments/checkout/
/payments/receipt/
```

---

## Dashboard App

Routes:

```text
home
reports
```

Possible structure:

```text
/dashboard/
/dashboard/reports/
```

---

## Challenge Requirements

The architecture must include:

- App-level `urls.py`
- `include()` for modular routing
- Namespaces
- At least one dynamic route

Example architecture:

```text
Project URLs
│
├── users/
│   └── users.urls
│
├── courses/
│   └── courses.urls
│
├── payments/
│   └── payments.urls
│
└── dashboard/
    └── dashboard.urls
```

---

### Bonus

Add one **Class-Based View (CBV)** route using:

```python
.as_view()
```

---

## Key Takeaways

- Simple URLs represent fixed pages.
- Dynamic URLs allow one view to serve multiple related pages.
- Path converters validate and convert URL parameters.
- Django passes dynamic URL parameters directly to view arguments.
- Use the narrowest path converter that satisfies the requirement.
- Named URLs are safer than hardcoded links.
- `reverse()` builds URLs from route names in Python.
- `{% url %}` builds URLs from route names inside templates.
- Namespaces prevent route-name conflicts between apps.
- `resolve()` helps identify which view Django selects for a path.
- Routing problems often come from route order, incorrect converters, namespaces, or missing `include()`.
- Root `urls.py` should distribute traffic rather than contain every route.
- Clean routing uses app-level URL files, namespaces, named routes, and consistent paths.
- A scalable Django project should design its URL architecture before implementation.

---

**Status:** ✅ Completed
