# Week 8 - Day 2

## Overview

Today focused on managing **user state** and handling **validated form input** in Django.

The lesson covered how **cookies and sessions** preserve information between HTTP requests, followed by Django Forms and ModelForms for validating and processing user-submitted data safely.

**Date:** September 14

---

## Topics Covered

- Cookies and Sessions
- Reading and Writing Cookies
- Session Management
- Cookie and Session Lifetime
- Safe State Handling
- Cookie and Session Security
- Django Forms
- Form Fields and Widgets
- GET and POST Form Flow
- Form Validation
- `cleaned_data`
- Custom Validation
- ModelForms
- CSRF Protection
- Post / Redirect / Get Pattern
- Rendering Forms in Templates
- Form Troubleshooting

---

## Key Concepts

### Cookies vs Sessions

HTTP does not remember previous requests automatically, so cookies and sessions are used to maintain state.

#### Cookies

Cookies store small values directly in the browser.

Common uses include:

- Theme preference
- Language preference
- Dismissed banners

Cookies can be accessed using:

- `request.COOKIES`
- `response.set_cookie()`
- `response.delete_cookie()`

Cookies should always be read with safe default values because users can remove or modify them.

---

### Sessions

Sessions store application state on the server while the browser stores only the `sessionid`.

Common uses include:

- Shopping carts
- Login state
- Multi-page forms

Sessions are managed through:

- `request.session.get()`
- `request.session[...]`
- `request.session.pop()`
- `request.session.flush()`
- `request.session.set_expiry()`

---

### Cookie and Session Lifetime

Cookies can use `max_age` or `expires` to control how long they remain in the browser.

Sessions can use:

- `set_expiry()` to control session lifetime
- `set_expiry(0)` to expire when the browser closes
- `flush()` to destroy the current session

---

### Safe State Handling

Browser values should never be trusted automatically.

Good practices include:

- Using `.get()` with default values
- Validating cookie values
- Providing safe defaults for missing session values
- Avoiding sensitive information inside normal cookies

---

### Cookie Security

Important cookie and session security options include:

- `secure=True` — cookie is sent only over HTTPS
- `httponly=True` — prevents JavaScript from reading the cookie
- `samesite="Lax"` — limits cross-site cookie sending

Sensitive values such as passwords, raw tokens, or trusted identity information should not be stored in normal cookies.

---

## Django Forms

Django Forms provide a validation layer between browser input and application logic.

The general flow is:

**Browser Form → POST Request → Django Form → `is_valid()` → `cleaned_data` → View Action → Redirect**

Raw `request.POST` values should not be trusted before validation.

---

### `forms.Form`

A Django form class defines:

- Fields
- Validation rules
- HTML widgets

Common fields include:

- `CharField`
- `EmailField`
- `BooleanField`
- `ChoiceField`

---

### Fields and Widgets

A **Field** defines what data is valid.

A **Widget** controls how the field appears in HTML.

Examples of widgets include:

- `Textarea`
- `PasswordInput`
- `Select`
- `CheckboxInput`

---

### GET and POST Form Flow

#### GET

A GET request usually displays an empty, unbound form.

GET forms are also useful for:

- Search
- Filters
- Query parameters

#### POST

A POST request binds submitted data to the form and runs validation.

If the form is invalid:

- Render the same template again
- Display validation errors

If the form is valid:

- Use `cleaned_data`
- Perform the required action
- Redirect to another page

---

### Form Validation

Validation runs before submitted data should be used.

Important methods include:

- `is_valid()`
- `cleaned_data`
- `clean_<field>()`
- `clean()`

`clean_<field>()` validates one specific field.

`clean()` can validate relationships between multiple fields.

`cleaned_data` should only be accessed after `is_valid()` returns `True`.

---

### ModelForm

`ModelForm` connects a Django form directly to a model.

It can automatically generate fields from the model and reduce repeated form code.

Important parts include:

- `class Meta`
- `model`
- `fields`
- `form.save()`

`Meta.fields` controls which model fields users are allowed to edit.

---

### CSRF Protection

POST forms require CSRF protection.

Templates should include:

`{% csrf_token %}`

CSRF protects the request, while Django Forms validate the submitted values.

Both are required.

---

### Rendering Forms in Templates

A simple form can be rendered using:

`{{ form.as_p }}`

Forms can also be rendered manually when more control over:

- Labels
- Fields
- Validation errors
- CSS classes

is required.

---

### Post / Redirect / Get

After a successful POST request, the application should redirect instead of directly returning the success page.

Flow:

**POST → Validate → Redirect → GET**

This prevents duplicate form submissions when the user refreshes the browser.

---

## Guided Labs

### Preferences and Cart

The lab practiced cookies and sessions by:

- Reading a theme preference from cookies
- Validating light and dark themes
- Saving the theme for 30 days
- Storing cart data in a session
- Adding products to the cart
- Clearing the cart using `session.pop()`
- Testing persistence using refresh, new tabs, and browser DevTools

### Feedback Form

The form lab included:

- Creating a `feedback` app
- Creating a `ContactForm`
- Adding name, email, message, and optional rating fields
- Adding custom validation
- Handling GET and POST requests
- Redirecting after a successful POST
- Adding CSRF protection
- Displaying form validation errors
- Rendering form fields manually
- Styling invalid fields

---

## Common Troubleshooting

- Missing `{% csrf_token %}` can cause a `403 Forbidden`.
- Redirecting after an invalid form can hide validation errors.
- `cleaned_data` must not be accessed before `is_valid()`.
- POST requests must bind submitted data to the form.
- Successful POST requests should redirect to avoid duplicate submissions.

---

## Key Takeaways

- Cookies store small values in the browser.
- Sessions store application state on the server.
- Browser-controlled values should always be validated.
- Django Forms centralize input validation.
- Fields define valid data while widgets define presentation.
- `cleaned_data` should only be used after successful validation.
- ModelForms simplify forms that create or edit model records.
- POST forms require CSRF protection.
- Successful form submissions should follow the Post / Redirect / Get pattern.

---

**Status:** ✅ Completed
