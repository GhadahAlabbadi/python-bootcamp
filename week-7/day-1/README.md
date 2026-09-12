# Week 7 - Day 1

## Overview

Today focused on understanding **Django Views** in more depth and how they coordinate the request-response cycle.

The session covered the `HttpRequest` object, different Django response types, Function-Based Views (FBVs), Class-Based Views (CBVs), GET and POST handling, context, request data, cookies, sessions, generic views, and best practices for keeping views clean and maintainable.

The main goal was to understand what a Django view is responsible for rather than simply memorizing view classes.

---

## Topics Covered

- Django Views
- Request-Response Cycle
- `HttpRequest`
- Request Methods
- Query Parameters
- POST Data
- Request Headers
- Cookies
- Sessions
- Uploaded Files
- Function-Based Views (FBVs)
- Class-Based Views (CBVs)
- `dispatch()`
- `.as_view()`
- Rendering Templates
- Context
- Django Response Types
- GET vs POST
- Reading Data from Requests
- Generic Class-Based Views
- FBV vs CBV
- Thin Views
- View Best Practices
- Multi-Method Views

---

## Key Concepts

### View in the Request-Response Cycle

A Django view receives a request and must return a response.

The general flow is:

```text
Request Received
      ↓
URL Matched
      ↓
View Runs
      ↓
Context Prepared
      ↓
Template Rendered
      ↓
Response Returned
```

Another way to visualize the application flow is:

```text
Browser
   ↓
URL
   ↓
View
   ↓
Model (when needed)
   ↓
Template
   ↓
Response
   ↓
Browser
```

The view acts as the coordinator between different parts of the application.

---

### The `HttpRequest` Object

Every Django view receives a `request` object.

The request contains information sent by the browser.

Important request properties include:

#### `request.method`

Contains the HTTP method used in the request.

Examples:

```text
GET
POST
PUT
```

#### `request.GET`

Contains query string parameters.

Example URL:

```text
/search/?q=django&page=2
```

Reading the values:

```python
q = request.GET.get("q", "")
page = request.GET.get("page", 1)
```

#### `request.POST`

Contains submitted POST form data.

Example:

```python
name = request.POST.get("name")
email = request.POST.get("email")
```

#### `request.headers`

Contains browser and request metadata.

Example:

```python
agent = request.headers.get("User-Agent")
```

#### `request.COOKIES`

Contains cookies sent by the browser.

Example:

```python
theme = request.COOKIES.get("theme", "light")
```

#### `request.session`

Contains server-side session state.

Example:

```python
count = request.session.get("cart_items", 0)
```

#### `request.FILES`

Contains uploaded files.

```python
request.FILES
```

#### `request.path`

Contains the current URL path.

```python
request.path
```

When debugging a view, an important question is:

> What did the browser send in the request?

---

### Function-Based Views (FBVs)

A **Function-Based View** is a normal Python function that receives a request and returns a response.

Example:

```python
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, Django!")
```

The view:

1. Receives `request`.
2. Executes Python logic.
3. Returns an HTTP response.

FBVs are:

- Simple
- Explicit
- Easy to trace
- Easy to understand

They are useful for:

- Small pages
- Quick tests
- Simple logic
- Beginner-friendly logic
- Views where full control and readability are important

A view must always return an **HttpResponse-like object**.

Avoid putting large HTML strings directly inside Python.

Instead of:

```python
return HttpResponse("<h1>Large HTML Page...</h1>")
```

prefer using templates.

FBVs are not only for beginners. They are still used professionally when the logic is clear.

---

### Rendering Templates with Context

Most Django pages return HTML using:

```python
render()
```

Example:

```python
from django.shortcuts import render

def home(request):
    context = {
        "username": "Aly",
        "age": 25
    }

    return render(
        request,
        "home.html",
        context
    )
```

The `context` dictionary transfers Python data to the template.

Inside `home.html`:

```django
<h1>Hello {{ username }}</h1>

<p>You are {{ age }} years old.</p>
```

The flow is:

```text
View
  ↓
Context
  ↓
Template
  ↓
HTML
```

> Context is the bridge between backend logic and the page the user sees.

---

### Response Types in Django

A Django view does not always return an HTML page.

Different situations require different response types.

#### `HttpResponse`

Used for plain text or simple output.

```python
return HttpResponse("Hello")
```

#### `render()`

Used to return an HTML page using a template and context.

```python
return render(request, "home.html", context)
```

#### `redirect()`

Sends the user to another route.

```python
return redirect("success")
```

#### `JsonResponse`

Returns JSON data.

Commonly used for:

- APIs
- Status endpoints

Example:

```python
return JsonResponse({
    "status": "ok"
})
```

#### `FileResponse`

Used for downloadable files such as:

- PDFs
- CSV files

#### `StreamingHttpResponse`

Used for:

- Large files
- Live streams

The view's responsibility is not always to display a page. It may also:

```text
Render HTML
Redirect
Return JSON
Download a file
Stream data
```

---

### GET vs POST Inside Views

A page can behave differently depending on the HTTP method.

Example:

```python
def contact(request):

    if request.method == "GET":
        return render(request, "contact.html")

    if request.method == "POST":
        # process submitted data
        return redirect("success")
```

#### GET

Usually used to:

- Retrieve data
- Display pages

GET requests are generally safe and repeatable.

#### POST

Usually used to:

- Submit data
- Change data
- Process forms
- Perform actions

#### Other Methods

Methods such as:

```text
PUT
PATCH
DELETE
```

are commonly used in APIs and more advanced workflows.

A useful principle is:

```text
GET  → Read / Display
POST → Submit / Change
```

Separating read logic from write logic makes views easier to understand and maintain.

---

### Reading Data from the Request

Views often need user input before deciding what response to return.

#### Query String

Example:

```text
/search/?q=django&page=2
```

Read it using:

```python
q = request.GET.get("q", "")
page = request.GET.get("page", 1)
```

#### POST Form Data

```python
name = request.POST.get("name")
email = request.POST.get("email")
```

#### Headers

```python
agent = request.headers.get("User-Agent")
```

#### Common Mistakes

Avoid directly accessing values without a fallback:

```python
request.GET["q"]
```

Prefer:

```python
request.GET.get("q", "")
```

Also avoid:

- Trusting user input without validation
- Mixing display logic and submission logic unnecessarily

Recommended flow:

```text
Read with .get()
→ Provide defaults
→ Validate
→ Use the value
```

---

### Class-Based Views (CBVs)

A **Class-Based View** organizes view behavior inside a Python class.

Example:

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello from a class view")
```

CBVs provide reusable structure for larger applications.

---

### Calling a CBV from a URL

A class itself cannot be used directly as the URL view.

Django uses:

```python
.as_view()
```

Example:

```python
path(
    "",
    HomeView.as_view(),
    name="home"
)
```

`.as_view()` converts the class into a callable Django view.

---

### CBV Dispatching

CBVs automatically route HTTP methods to matching class methods.

The flow is:

```text
Request
   ↓
dispatch()
   ↓
HTTP Method
   ↓
get()
post()
delete()
...
```

Example:

```python
class ContactView(View):

    def get(self, request):
        return render(
            request,
            "contact.html"
        )

    def post(self, request):
        email = request.POST.get("email")

        return redirect("success")
```

If the browser sends:

```text
GET
```

Django runs:

```python
get()
```

If the browser sends:

```text
POST
```

Django runs:

```python
post()
```

Main idea:

```text
GET    → get()
POST   → post()
DELETE → delete()
```

This keeps HTTP method logic separated without writing many `if/elif` checks.

---

### FBV vs CBV

Both approaches are valid.

The choice depends on the complexity and reuse requirements of the view.

#### Use FBV When

- Logic is simple
- Only GET/POST is needed
- The view is under approximately 20–30 lines
- Full control and readability are preferred

#### Use CBV When

- Reusable logic is needed
- Multiple HTTP methods are needed
- Mixins or generic views are useful
- CRUD-style features are being built

---

### Generic Views

Django provides prebuilt CBVs for common patterns.

#### `TemplateView`

Used for a page that mainly renders a template.

#### `ListView`

Shows a list of objects.

```text
ListView → many objects
```

#### `DetailView`

Shows one object.

```text
DetailView → one object
```

#### `CreateView`

Creates a new object through a form.

#### `UpdateView`

Edits an existing object.

#### `DeleteView`

Deletes an existing object.

Generic views help reduce repeated code.

---

### Cookies and Sessions Inside Views

Views can use browser and server state to personalize the user experience.

#### Cookies

Cookies are stored in the browser.

Read a cookie:

```python
theme = request.COOKIES.get(
    "theme",
    "light"
)
```

Set a cookie:

```python
response = HttpResponse("OK")

response.set_cookie(
    "theme",
    "dark"
)

return response
```

Cookies are useful for:

- Preferences
- Theme settings

#### Sessions

Sessions store state on the server side.

Set session data:

```python
request.session["cart_items"] = 3
```

Read session data:

```python
count = request.session.get(
    "cart_items",
    0
)
```

Delete session data:

```python
del request.session["cart_items"]
```

Sessions are useful for state such as:

- Shopping carts
- User-related application state

---

### Keeping Views Professional

Views should coordinate application behavior rather than become a dumping ground for all logic.

#### Avoid Fat Views

Do not place too much business logic inside the view.

Heavy logic can be moved to:

- Models
- Forms
- Services
- Utility functions

#### Avoid HTML Inside `HttpResponse`

Instead of writing UI directly inside Python:

```python
HttpResponse("<h1>...</h1>")
```

use templates.

#### Avoid Queries in Templates

Data should be fetched and prepared before rendering the template.

Prefer:

```text
View
→ prepares data
→ Template displays data
```

#### Avoid Repeated Logic

Repeated behavior can be moved to:

- Helper functions
- CBVs
- Mixins

#### Avoid Huge JSON Responses

Return only the data that the client actually needs.

---

### Thin Views

A **thin view** does not mean an empty view.

It means the view delegates responsibilities clearly.

```text
View
→ receives request
→ coordinates logic
→ prepares response
```

while other layers handle their own responsibilities.

---

## Guided Lab — Multi-Method View System

### Objective

Build views that handle:

- Pages
- Forms
- Sessions
- JSON

### Step 1 — Create Accounts App

Create:

```text
accounts
```

### Step 2 — Add `RegisterView`

Handle:

```text
GET
POST
```

### Step 3 — Add `LoginView`

Handle:

```text
GET
POST
```

### Step 4 — Add `ProfileView`

Read session data.

### Step 5 — Create One FBV Status Endpoint

Create a simple Function-Based View for status.

### Step 6 — Return `JsonResponse`

Example:

```python
return JsonResponse({
    "status": "ok"
})
```

### Step 7 — Connect URLs with Names

Connect all views to named URL routes.

### Step 8 — Test Pages

Test working pages and capture screenshots.

### Deliverables

```text
Views
+
URLs
+
Templates
+
Screenshots of working pages
```

---

## Key Takeaways

- Every Django view receives an `HttpRequest`.
- A view must return an HTTP response.
- Views coordinate requests, logic, templates, and responses.
- `request.GET` contains query parameters.
- `request.POST` contains submitted form data.
- `request.headers` provides request metadata.
- `request.COOKIES` contains browser cookies.
- `request.session` provides server-side state.
- `request.FILES` contains uploaded files.
- FBVs are simple, explicit, and useful for straightforward logic.
- CBVs organize behavior inside classes.
- `.as_view()` makes a CBV callable from URL configuration.
- `dispatch()` sends each HTTP method to the matching class method.
- GET is mainly used for reading or displaying data.
- POST is mainly used for submitting or changing data.
- Context transfers backend data to templates.
- Django views can return HTML, JSON, redirects, files, or streams.
- Generic views reduce repeated CRUD-related code.
- Cookies store browser-side state.
- Sessions store server-side state.
- Thin views delegate responsibilities instead of containing all application logic.

---

**Status:** ✅ Completed
