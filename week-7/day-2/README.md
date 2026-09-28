# Week 7 - Day 2

## Overview

Today focused on handling **static files and media files in Django**, from local development to production-ready asset handling.

The session covered the difference between static and media files, Django settings for both, folder organization, using static files inside templates, `collectstatic`, media uploads, `FileField`, `ImageField`, upload forms, validation, security, production architecture, and troubleshooting common static and media issues.

---

## Topics Covered

- Static Files
- Media Files
- `STATIC_URL`
- `STATICFILES_DIRS`
- `STATIC_ROOT`
- `MEDIA_URL`
- `MEDIA_ROOT`
- Project-Level Static Files
- App-Level Static Files
- `{% load static %}`
- `{% static %}`
- Serving Static Files During Development
- `collectstatic`
- Media Uploads
- `FileField`
- `ImageField`
- `upload_to`
- `request.FILES`
- Multipart Forms
- Displaying Uploaded Media
- Fallback Images
- Upload Validation
- File Size Limits
- File Type Validation
- Storage Isolation
- Production Asset Architecture
- Troubleshooting Static and Media Files

---

## Key Concepts

### Static Files vs Media Files

The most important distinction is between **static files** and **media files**.

### Static Files

Static files are part of the application's codebase.

They are:

- Versioned in Git
- The same for every user
- Updated when developers deploy the application

Examples:

```text
CSS
JavaScript
Logos
Icons
Fonts
Backgrounds
```

A useful rule is:

```text
Static = assets that ship with the code
```

---

### Media Files

Media files are created or uploaded by users at runtime.

They are:

- Not normally committed to Git
- Potentially private
- Potentially large
- Frequently changing
- In need of backups and access control

Examples:

```text
Profile photos
PDFs
CVs
Product images
Attachments
```

A useful rule is:

```text
Media = assets created by users
```

---

## Static and Media Settings

Django needs both browser URL prefixes and filesystem locations.

Example:

```python
# settings.py

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
```

---

### `STATIC_URL`

Defines the browser URL prefix for static files.

Example:

```text
/static/...
```

---

### `STATICFILES_DIRS`

Defines extra locations where Django searches for static files during development.

Example:

```python
STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```

---

### `STATIC_ROOT`

Defines the single folder used after running:

```bash
python manage.py collectstatic
```

Example:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

### `MEDIA_URL`

Defines the browser URL prefix for uploaded media files.

Example:

```text
/media/...
```

---

### `MEDIA_ROOT`

Defines the physical folder where uploaded files are saved.

Example:

```python
MEDIA_ROOT = BASE_DIR / "media"
```

---

### Common Mistake

Do not point:

```text
STATIC_ROOT
```

to the same folder as:

```text
STATICFILES_DIRS
```

They serve different purposes.

---

## Organizing Folders Clearly

A clean project structure can look like:

```text
project_root/
│
├── static/
│   ├── css/
│   │   └── base.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       └── logo.png
│
├── core/
│   └── static/
│       └── core/
│           └── core.css
│
├── blog/
│   └── static/
│       └── blog/
│           └── blog.css
│
└── media/
    ├── avatars/
    └── documents/
```

---

### Project-Level Static Files

Used for shared assets such as:

- CSS
- JavaScript
- Images
- Layout assets

Example:

```text
static/
```

---

### App-Level Static Files

Used for feature-specific assets.

Example:

```text
core/static/core/
blog/static/blog/
```

Namespacing static folders helps avoid name collisions.

---

### Media Folder

Used for user uploads.

Example:

```text
media/
```

Media files are not part of the source code.

---

### `.gitignore`

Folders commonly ignored include:

```text
media/
staticfiles/
venv/
__pycache__/
```

---

## Using Static Files in Templates

Django templates should not hardcode `/static/...` directly.

First load the static template tag:

```django
{% load static %}
```

Then generate static URLs with:

```django
{% static %}
```

Example CSS:

```django
<link
    rel="stylesheet"
    href="{% static 'css/main.css' %}"
>
```

Example JavaScript:

```django
<script src="{% static 'js/app.js' %}"></script>
```

Example image:

```django
<img
    src="{% static 'images/logo.png' %}"
    alt="Logo"
>
```

The main idea is:

```text
{% load static %}
→ use {% static 'path' %}
→ Django generates the correct URL
```

This also makes the project easier to adapt later to CDNs or different storage backends.

---

## Serving Static Files During Development

Django can serve static files during development when:

```text
DEBUG = True
```

and:

```text
django.contrib.staticfiles
```

is installed.

The development server may serve requests such as:

```text
GET /static/css/main.css
GET /static/images/logo.png
```

---

### Static File Troubleshooting

If a static file returns `404`, check:

- `STATIC_URL`
- `INSTALLED_APPS`
- Folder path spelling
- Static file location

If the template shows an error, check whether you forgot:

```django
{% load static %}
```

If the path is wrong, make sure the folder path matches the value inside:

```django
{% static '...' %}
```

Examples:

```text
static/css/main.css
→ {% static 'css/main.css' %}
```

```text
blog/static/blog/blog.css
→ {% static 'blog/blog.css' %}
```

---

## `collectstatic`

For production, static files are collected into one output folder.

Run:

```bash
python manage.py collectstatic
```

Django collects static files from:

```text
App static folders
+
Project static folder
```

and copies them into:

```text
STATIC_ROOT
```

Example:

```text
staticfiles/
```

The production web server or CDN can then serve:

```text
/static/...
```

---

### Deployment Rule

Run:

```bash
python manage.py collectstatic
```

as part of deployment.

The generated `staticfiles/` folder can be added to `.gitignore` because it can be regenerated.

---

## Media Files and User Uploads

Media uploads require explicit configuration.

In `settings.py`:

```python
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
```

During development, `project/urls.py` can serve media files when `DEBUG=True`.

Example:

```python
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

---

### Media Path Example

Browser path:

```text
/media/avatars/user1.png
```

maps to:

```text
MEDIA_ROOT/avatars/user1.png
```

---

## `FileField` and `ImageField`

Django models can define uploaded files.

### `FileField`

Used for generic files such as:

```text
PDF
ZIP
DOCX
CSV
```

Example:

```python
class Document(models.Model):
    title = models.CharField(max_length=200)

    file = models.FileField(
        upload_to="documents/"
    )
```

---

### `ImageField`

Used for images.

Example:

```python
class Profile(models.Model):
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )
```

`ImageField` requires Pillow.

---

### `upload_to`

Defines the subfolder under `MEDIA_ROOT`.

For example:

```python
upload_to="documents/"
```

stores files under:

```text
MEDIA_ROOT/documents/
```

The browser path is based on:

```text
MEDIA_URL + documents/<filename>
```

---

## Upload Workflow

A successful upload requires:

```text
HTML Form
→ View
→ request.FILES
→ Form Validation
→ Storage
```

---

### HTML Form

The form must use:

```html
<form
    method="post"
    enctype="multipart/form-data"
>
```

Example:

```django
<form
    method="post"
    enctype="multipart/form-data"
>
    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Upload
    </button>
</form>
```

The important part is:

```text
enctype="multipart/form-data"
```

Without it:

```text
request.FILES
```

will be empty.

---

### Reading Uploaded Files in the View

Example:

```python
if request.method == "POST":

    form = DocumentForm(
        request.POST,
        request.FILES
    )

    if form.is_valid():
        form.save()

        return redirect(
            "document_list"
        )
```

The flow is:

```text
HTML
→ multipart/form-data

View
→ request.FILES

Form
→ validate and save

Storage
→ file saved under MEDIA_ROOT
```

---

## Displaying Uploaded Media Safely

Uploaded media paths are dynamic.

If an image field is optional, check that a file exists before accessing its URL.

Example:

```django
{% if profile.avatar %}

    <img
        src="{{ profile.avatar.url }}"
        alt="Avatar"
    >

{% else %}

    <img
        src="{% static 'images/default-avatar.png' %}"
        alt="Default avatar"
    >

{% endif %}
```

---

### Why Check First?

Accessing:

```django
profile.avatar.url
```

can raise an error if no file exists.

---

### Fallback Image

A static default image can be shown when no uploaded image exists.

This creates a clean combination of:

```text
Static default image
+
Optional uploaded image
```

---

### Alt Text

Uploaded images still need meaningful:

```html
alt=""
```

text.

---

## Security and Validation for Uploads

Every upload should be treated as untrusted input.

Important areas include:

### Size Limits

Limit upload size at multiple layers such as:

- Forms
- Django
- Web server

---

### File Type Validation

Allow only expected file extensions or MIME types.

Example:

```python
def validate_pdf(file):

    if not file.name.lower().endswith(".pdf"):

        raise ValidationError(
            "Only PDF files are allowed."
        )
```

---

### Storage Isolation

Do not upload user files into:

```text
templates/
Python code folders
```

Keep uploads isolated from the application code.

---

### Production Concerns

Production upload handling should consider:

- Permissions
- Backups
- Retention
- Malware scanning
- Cleanup of old files

---

## Production Architecture

Static files and media files scale differently.

### Static Assets

```text
Git + app static folders
        ↓
collectstatic
        ↓
STATIC_ROOT
        ↓
CDN
```

Static files are mainly part of the deployment process.

---

### Media Files

```text
User Upload
        ↓
Django View
request.FILES
        ↓
Storage
Volume / S3
        ↓
Backup
```

Media files are mainly a data management concern.

The key idea is:

```text
Static = deployment
Media  = data management
```

---

## Troubleshooting Checklist

### CSS Disappeared After Deployment

Likely cause:

```text
collectstatic was not run
or
web server points to empty STATIC_ROOT
```

Fix:

```text
Run collectstatic
and verify STATIC_ROOT
```

---

### Static File 404 Locally

Likely cause:

```text
Wrong path
or
missing {% load static %}
```

Fix:

```text
Match the folder path
and load the static tag
```

---

### Uploaded File Not Received

Likely cause:

```text
Missing multipart enctype
```

Fix:

```text
Add enctype="multipart/form-data"
and use request.FILES
```

---

### Media 404 During Development

Likely cause:

```text
MEDIA_URL route not added
```

Fix:

```python
static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
```

---

### Permission Denied

Likely cause:

```text
Application cannot write to MEDIA_ROOT
```

Fix:

```text
Configure operating system permissions securely
```

---

## Guided Lab — Static & Media-Aware Site

### Step 1

Configure:

```text
STATIC_URL
STATICFILES_DIRS
STATIC_ROOT
```

---

### Step 2

Create:

```text
static/css/main.css
```

and:

```text
static/images/default-avatar.png
```

---

### Step 3

Configure:

```text
MEDIA_URL
MEDIA_ROOT
```

---

### Step 4

Add media serving to:

```text
project urls.py
```

for DEBUG mode.

---

### Step 5

Create an upload form with:

```text
multipart enctype
```

---

### Step 6

Use:

```python
request.FILES
```

inside the upload view.

---

### Step 7

Display either:

```text
Uploaded image
```

or:

```text
Fallback static image
```

---

### Step 8

Run:

```bash
python manage.py collectstatic
```

and inspect:

```text
staticfiles/
```

---

## Lab 3 — Mini Instagram Clone

### Goal

Build one feed page where users can:

- Add image posts
- Write captions
- Like posts

---

### Core Requirements

Create a `Post` model with:

```text
username
description
image
likes
```

Store images under:

```text
media/posts/
```

Accept only:

```text
jpg
jpeg
png
```

Use:

```text
multipart/form-data
+
request.FILES
```

---

### Page Behavior

Show all posts on one feed page.

Each post displays:

- Username
- Image
- Description
- Likes

Add a Like button that increases:

```text
likes
```

by:

```text
1
```

Style the feed using:

```text
static/css/feed.css
```

---

### Challenge

If a post has:

```text
0 likes
```

display:

```text
Be the first to like this
```

Otherwise display the current number of likes.

Example:

```text
3 likes
```

---

### Exit Ticket

The completed lab should show that:

- One valid image post appears.
- Invalid file types are rejected.
- The Like button updates the count.
- `feed.css` appears inside `STATIC_ROOT` after `collectstatic`.

---

## Key Takeaways

- Static files and media files serve different purposes.
- Static files are part of the codebase and deployment process.
- Media files are user-created runtime data.
- `STATIC_URL` defines the browser prefix for static files.
- `STATICFILES_DIRS` defines development search locations.
- `STATIC_ROOT` stores collected production static files.
- `MEDIA_URL` defines the browser prefix for uploads.
- `MEDIA_ROOT` stores uploaded files.
- Use `{% load static %}` before using the static template tag.
- Use `{% static %}` instead of hardcoding static URLs.
- `collectstatic` gathers static assets into one production folder.
- `FileField` handles generic uploaded files.
- `ImageField` handles uploaded images.
- `upload_to` creates subfolders under `MEDIA_ROOT`.
- Upload forms require `multipart/form-data`.
- Uploaded files are accessed through `request.FILES`.
- Optional uploaded media should be checked before using `.url`.
- Static fallback images can be used when no media file exists.
- Uploads must be validated for file type and size.
- Uploaded media should be isolated from source code.
- Production media needs storage, backups, permissions, and security planning.
- Static asset management and media management require different production strategies.

---

**Status:** ✅ Completed
