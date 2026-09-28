# Week 7 - Day 3

## Overview

Today focused on building **parameter-aware Django pages** using **path parameters** and **query parameters**.

The session covered Django path converters, receiving URL values inside views, working with `request.GET` and `QueryDict`, search and filtering, sorting, pagination, URL generation, validation, and troubleshooting common parameter-related issues.

---

## Topics Covered

- Path Parameters
- Query Parameters
- Django Path Converters
- Dynamic URL Patterns
- Function-Based Views with Parameters
- Class-Based Views with Parameters
- `request.GET`
- `QueryDict`
- `.get()`
- `.getlist()`
- Search Forms
- Filtering
- Sorting
- Pagination
- Combining Path and Query Parameters
- `{% url %}`
- `reverse()`
- Parameter Validation
- Parameter-Aware Page Architecture
- URL Troubleshooting

---

## Key Concepts

### Path Parameters vs Query Parameters

The main distinction is:

```text
Path = which object or route
Query = how to filter, sort, or display it
```

### Path Parameters

Path parameters:

- Are inside the URL path
- Are required for the route to match
- Usually identify a resource
- Are validated by Django path converters

Examples:

```text
/products/42/
/blog/django-basics/
/users/aly/
```

---

### Query Parameters

Query parameters:

- Appear after `?` in the URL
- Are optional
- Are order-independent
- Usually control page state
- Are read using `request.GET`

Examples:

```text
?q=django
?page=2
?category=backend&sort=recent
```

---

## Today's Mental Model

A path parameter can identify the resource:

```text
/products/42/
        ↓
URLconf converts and matches
        ↓
View argument
id = 42
        ↓
Template
resource detail
```

A query parameter can control how a page is displayed:

```text
?q=django&page=2
        ↓
request.GET
        ↓
Filtering logic
search / sort / page
        ↓
Template
results state
```

The main rule:

```text
Path parameters identify what page or object you want.

Query parameters control how that page is displayed.
```

---

## URL Pattern Map

Example dynamic route:

```python
# urls.py

path(
    "products/<int:id>/",
    views.product_detail,
    name="product_detail"
)
```

Here:

```text
products/
```

is the static part of the URL.

```text
<int:id>
```

is the dynamic part.

`int` is the converter.

`id` becomes an argument passed to the view.

The route name:

```python
name="product_detail"
```

can later be used by:

```django
{% url %}
```

or:

```python
reverse()
```

---

## Building URLs with Parameters

Inside a template:

```django
<a href="{% url 'product_detail' id=product.id %}">
    View Details
</a>
```

Inside Python:

```python
url = reverse(
    "product_detail",
    kwargs={"id": product.id}
)
```

All required route parameters must be provided.

Missing or incorrect parameters can cause:

```text
NoReverseMatch
```

---

## Path Converters

Django path converters control which values a route accepts.

Examples:

```python
urlpatterns = [
    path("products/<int:id>/", detail),
    path("blog/<slug:slug>/", post),
    path("orders/<uuid:order_id>/", order),
    path("files/<path:file_path>/", file_view),
]
```

### `<int:id>`

Accepts numbers only.

The view receives an integer.

Example:

```text
/products/42/
```

---

### `<slug:slug>`

Accepts URL-friendly text.

Commonly used for articles and readable URLs.

Example:

```text
/blog/django-basics/
```

---

### `<uuid:order_id>`

Accepts a UUID value.

Useful for long identifiers such as orders.

---

### `<path:file_path>`

Can contain `/`.

Use carefully because it can capture a large part of the URL.

---

### Default Converter

If a converter is not specified:

```text
<id>
```

Django treats it as:

```text
<str:id>
```

---

## Receiving Path Parameters in Views

### Function-Based View

Path parameters become function arguments.

```python
def product_detail(request, id):
    return HttpResponse(
        f"Product ID: {id}"
    )
```

For:

```text
/products/42/
```

Django effectively calls:

```python
product_detail(
    request,
    id=42
)
```

---

### Class-Based View

Parameters can also be received inside CBVs.

Example:

```python
class HelloUserView(View):

    def get(
        self,
        request,
        username
    ):
        return HttpResponse(
            f"Hello, {username}"
        )
```

CBVs may also access URL values through:

```python
self.kwargs
```

---

### Multiple Path Values

A route can contain multiple values.

Example:

```text
/blog/<int:year>/<int:month>/<slug:slug>/
```

---

## Understanding Query Parameters

Example:

```text
/search/?q=django&page=2&sort=asc
```

The path is:

```text
/search/
```

The query string is:

```text
q=django&page=2&sort=asc
```

Query parameters are optional.

The page should normally still work without them.

Example:

```text
/search/
```

should still be valid even when `q` is missing.

---

### Query Parameter Order

These represent the same values:

```text
?page=2&q=django
```

and:

```text
?q=django&page=2
```

Query parameter order does not matter.

---

### Common Uses

Query parameters are useful for:

- Search
- Filters
- Tabs
- Sorting
- Pagination

Example:

```text
/products/?q=django&category=books&page=2
```

---

## `request.GET` and `QueryDict`

Django stores query parameters inside:

```python
request.GET
```

`request.GET` is a `QueryDict`.

Example:

```python
def search(request):

    q = request.GET.get(
        "q",
        ""
    )

    page = request.GET.get(
        "page",
        "1"
    )

    categories = request.GET.getlist(
        "category"
    )

    return render(
        request,
        "search.html",
        {
            "q": q,
            "page": page,
            "categories": categories,
        }
    )
```

---

### `.get()`

Use:

```python
request.GET.get()
```

to safely retrieve one value.

Example:

```python
q = request.GET.get(
    "q",
    ""
)
```

The second argument is the default value.

---

### `.getlist()`

Use:

```python
request.GET.getlist()
```

when the same query parameter may appear multiple times.

Useful for inputs such as checkboxes.

Example:

```python
categories = request.GET.getlist(
    "category"
)
```

---

### Query Values Are Strings

Values received from:

```python
request.GET
```

arrive as text.

Even:

```text
?page=2
```

provides the value as a string.

---

### Safer Query Reading

Avoid assuming that a parameter exists.

Instead of:

```python
request.GET["q"]
```

prefer:

```python
request.GET.get(
    "q",
    ""
)
```

This prevents errors when the parameter is missing.

---

## Search and Filter Forms

GET forms are useful for search and filters because the selected values appear in the URL.

Example:

```html
<form method="get">

    <input
        name="q"
        value="{{ q }}"
        placeholder="Search"
    >

    <select name="category">

        <option value="">
            All categories
        </option>

        <option value="backend">
            Backend
        </option>

    </select>

    <button type="submit">
        Filter
    </button>

</form>
```

The view can read the values using:

```python
def product_list(request):

    q = request.GET.get(
        "q",
        ""
    )

    category = request.GET.get(
        "category",
        ""
    )
```

Example generated URL:

```text
/products/?q=django&category=backend
```

---

## Pagination with Query Parameters

Pagination also uses query parameters.

Example:

```text
?page=2
```

This represents the current page state.

Django provides:

```python
Paginator
```

to split a list into pages.

Example:

```python
from django.core.paginator import Paginator

def product_list(request):

    page_number = request.GET.get(
        "page",
        "1"
    )

    paginator = Paginator(
        products,
        10
    )

    page_obj = paginator.get_page(
        page_number
    )

    return render(
        request,
        "products/list.html",
        {
            "page_obj": page_obj
        }
    )
```

---

### Preserve Active Filters

When moving between pages, active query parameters should not disappear.

For example:

```text
?q=django&category=books&page=2
```

Changing the page should preserve:

```text
q
category
sort
```

instead of keeping only:

```text
page
```

---

## Combining Path and Query Parameters

Path and query parameters can work together.

Example route:

```python
path(
    "products/<slug:slug>/",
    views.product_detail,
    name="product_detail"
)
```

Example view:

```python
def product_detail(
    request,
    slug
):

    product = find_product(
        slug
    )

    tab = request.GET.get(
        "tab",
        "details"
    )

    return render(
        request,
        "products/detail.html",
        {
            "product": product,
            "tab": tab,
        }
    )
```

Example path:

```text
/products/django-course/
```

Example query states:

```text
?tab=details
?tab=syllabus
```

The rule is:

```text
Path is required.

Query is optional.

Always provide a default for optional query parameters.
```

---

## Tabs with Query Parameters

A detail page can use query parameters to control active tabs.

Example:

```text
/products/django-course/?tab=details
```

or:

```text
/products/django-course/?tab=syllabus
```

The path identifies the product.

The query parameter controls which tab is displayed.

---

## Validation and Safety

URL values should still be treated as user input.

### Object Existence

Verify that the requested object exists.

Use:

```python
get_object_or_404()
```

or handle missing mock data appropriately.

---

### Allowed Values

Validate values used for:

- Sorting
- Tabs
- Categories
- Difficulty

Example:

```python
def clean_sort(value):

    allowed = {
        "recent",
        "popular"
    }

    return (
        value
        if value in allowed
        else "recent"
    )
```

---

### Numeric Ranges

Validate numeric values such as:

- Page numbers
- Years
- Months
- Prices

---

### Converters vs Business Validation

A converter checks the **shape** of the value.

For example:

```text
<int:id>
```

checks that the value is numeric.

The view must still decide whether the value makes sense for the application.

---

### Sensitive Identifiers

Avoid exposing sensitive internal IDs when appropriate.

Alternatives may include:

```text
slugs
UUIDs
```

---

## Parameter-Aware Page Architecture

### Catalog Page

Example flow:

```text
/courses/
    ↓
GET form
category + difficulty
    ↓
request.GET
read filters safely
    ↓
Results UI
filtered + paginated
```

---

### Detail Page

Example flow:

```text
/courses/<id>/
    ↓
Path converter
<int:id>
    ↓
View context
course + active tab
    ↓
Template
?tab=syllabus
```

The key idea is:

```text
Path identifies the resource.

Query controls how the resource is viewed.
```

---

## Troubleshooting Checklist

### 404 on `/products/abc/`

Likely cause:

```text
<int:id> rejects a non-numeric value
```

Fix:

```text
Use a valid number
or change the converter
```

---

### `NoReverseMatch`

Likely cause:

```text
Missing id or slug in {% url %}
```

Fix:

```text
Pass all required route parameters
```

---

### `KeyError: q`

Likely cause:

```python
request.GET["q"]
```

was used when `q` was missing.

Fix:

```python
request.GET.get(
    "q",
    ""
)
```

---

### Filters Reset on Next Page

Likely cause:

```text
Pagination link only keeps page
```

Fix:

```text
Preserve the existing query string
```

---

### `/login/` Opens the Wrong Page

Likely cause:

```text
A generic route was placed before a specific route
```

Fix:

```text
Place specific routes first
```

---

## Guided Lab — Parameter-Aware Catalog

### Step 1

Create a:

```text
courses
```

app and a mock course list.

---

### Step 2

Add:

```text
/courses/
```

list route.

Add:

```text
/courses/<int:id>/
```

detail route.

---

### Step 3

Read:

```text
category
difficulty
```

from:

```python
request.GET
```

---

### Step 4

Filter the course list and handle missing values safely.

---

### Step 5

Add a search field using:

```html
method="get"
```

---

### Step 6

Add detail tabs using:

```text
?tab=details
?tab=syllabus
?tab=instructor
```

---

### Step 7

Use:

```django
{% url %}
```

with parameters for detail links.

---

### Step 8

Add basic pagination using:

```text
page
```

as a query parameter.

---

### Exit Ticket

Show:

- One filtered URL
- One detail URL
- One tab URL

working in the browser.

---

## Lab 2 — Product Explorer

Build a parameter-aware product catalog using:

- Path parameters
- Query parameters
- Filtering
- Sorting
- Tabs
- Pagination
- Safe validation

---

### Requirements

Create a:

```text
products
```

app with mock product data containing:

```text
id
name
category
price
rating
description
```

Add routes:

```text
/products/
/products/<int:id>/
```

Add GET filters for:

```text
category
min_price
```

Add a search field using:

```text
q
```

Add sorting using only:

```text
price
rating
name
```

Invalid sort values must fall back to:

```text
name
```

Paginate the filtered results while preserving active:

```text
search
filter
sort
```

parameters between pages.

---

### Product Detail Tabs

The detail page should support:

```text
?tab=details
?tab=reviews
?tab=shipping
```

The default should be:

```text
details
```

---

### Detail Links

Generate product detail links using:

```django
{% url %}
```

instead of hardcoding paths.

---

### Validation

The application should:

- Return `404` for an invalid product ID
- Handle missing query parameters safely
- Handle invalid query parameters safely

---

## Key Takeaways

- Path parameters identify a resource or route.
- Query parameters control page state.
- Path parameters are required for dynamic routes to match.
- Query parameters are normally optional.
- Django path converters validate URL value formats.
- `<int:id>` accepts numeric values.
- `<slug:slug>` is useful for URL-friendly text.
- `<uuid:...>` supports UUID identifiers.
- `<path:...>` can contain slashes.
- FBVs receive path values as function arguments.
- CBVs can receive path values through method arguments or `self.kwargs`.
- Query parameters are accessed through `request.GET`.
- `request.GET` is a `QueryDict`.
- Use `.get()` with defaults for optional values.
- Use `.getlist()` for repeated query parameters.
- Query parameter values arrive as strings.
- GET forms are useful for search and filtering.
- Pagination commonly uses the `page` query parameter.
- Active filters should be preserved between pages.
- `{% url %}` builds URLs safely inside templates.
- `reverse()` builds URLs inside Python.
- Missing required URL arguments can cause `NoReverseMatch`.
- Path converters validate value shape, but views must still validate business rules.
- URL input should always be validated safely.
- Path and query parameters can work together to build flexible pages.

---

**Status:** ✅ Completed
