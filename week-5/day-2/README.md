# Week 5 - Day 2

## Overview

The second day of Week 5 focused on understanding how web communication works through HTTP and how browsers interact with servers using requests and responses.

The session also introduced the fundamentals of HTML, including document structure, elements, tags, attributes, semantic HTML, and the DOM tree.

Several practical labs were completed to inspect network traffic, send HTTP requests manually, analyze HTML structure, and build basic HTML pages.

The HTML skeleton for the project was also started during the session.

---

## Topics Covered

- HTTP Requests and Responses
- HTTP Methods
- Request Headers and Body
- Response Structure
- HTTP Status Codes
- Stateless HTTP
- HTTPS and TLS
- Browser Network Traffic
- DevTools Network Inspection
- Manual HTTP Requests with cURL
- HTML Fundamentals
- HTML Document Structure
- Head vs Body
- HTML Elements, Tags, Attributes, and Values
- Block vs Inline Elements
- Common HTML Tags
- Semantic HTML
- DOM Tree
- HTML Best Practices
- Project HTML Skeleton

---

## Key Concepts

### HTTP Request and Response

Web communication follows a request-response cycle.

The client, such as a browser or application, sends a request to the server.

The server processes the request and sends a response back to the client.

```text
Client → Request → Server
Client ← Response ← Server
```

A request can contain:

- Method
- Path
- Headers
- Optional body

A response can contain:

- Status code
- Headers
- Body

The response body can contain HTML, JSON, images, files, or other content.

---

### Anatomy of an HTTP Request

An HTTP request contains information that tells the server what the client wants.

Example:

```text
GET /products/laptops HTTP/1.1
Host: www.store.com
User-Agent: Chrome
Accept: text/html
Cookie: session_id=fa123
```

The request line contains:

- **Method** – the action being requested
- **Path** – the requested resource
- **HTTP Version** – the HTTP protocol version

Headers provide additional information about the request.

---

### HTTP Methods

HTTP methods describe the action the client wants the server to perform.

- **GET** – Read or retrieve data
- **POST** – Send new data
- **PUT** – Replace or fully update a resource
- **PATCH** – Update part of a resource
- **DELETE** – Remove a resource

Examples include loading pages, logging in, registering users, uploading data, updating records, and deleting records.

---

### Headers and Body

HTTP headers provide metadata and additional context about a request.

Common request headers include:

- Host
- User-Agent
- Accept
- Content-Type
- Authorization

The body contains the actual data being sent when required.

Examples include:

- Form data
- JSON data
- File uploads

GET requests usually do not require a request body.

Example JSON body:

```json
{
  "email": "user@example.com",
  "password": "secret"
}
```

---

### Anatomy of an HTTP Response

The server returns an HTTP response after processing a request.

Example:

```text
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: session_id=fa123
Cache-Control: no-cache

<html>...</html>
```

A response contains:

- **Status Line** – describes the result of the request
- **Headers** – metadata about the response
- **Body** – the actual returned content

---

### HTTP Status Codes

Status codes provide a quick indication of what happened to a request.

#### 2xx – Success

- `200 OK`
- `201 Created`

#### 3xx – Redirect

- `301` Permanent Redirect
- `302` Temporary Redirect

#### 4xx – Client Error

- `400 Bad Request`
- `404 Not Found`

#### 5xx – Server Error

- `500 Internal Server Error`

Status codes are one of the first things to inspect when debugging HTTP problems.

---

### HTTP Is Stateless

HTTP is stateless by default.

Each request is independent, and the server does not automatically remember previous requests.

Applications can maintain user state using:

- **Cookies** – store small values on the client side.
- **Sessions** – store state on the server and connect it using a cookie.
- **Tokens** – can carry identity information, especially for APIs.

This becomes important when applications such as Django handle login, sessions, and forms.

---

### HTTPS and TLS

HTTPS is HTTP communication protected using TLS encryption.

- HTTP commonly uses port `80`
- HTTPS commonly uses port `443`
- TLS provides the handshake and encryption

HTTPS protects information while it travels between the client and server.

This is especially important for:

- Passwords
- Payments
- Personal information

**POST is not automatically secure. Security during transmission comes from HTTPS.**

---

## Browser Network Inspection

Browser DevTools can be used to inspect HTTP traffic.

Using the **Network** tab makes it possible to inspect:

- Request method
- URL
- Headers
- Status code
- Response time

This helps visualize the request-response cycle that happens when websites are loaded.

---

## Manual HTTP Requests

HTTP requests can also be sent without a browser using `curl`.

Retrieve a page:

```bash
curl https://example.com
```

Send data using POST:

```bash
curl -X POST https://httpbin.org/post -d "name=aly"
```

Request a resource that does not exist:

```bash
curl https://example.com/does-not-exist
```

This demonstrates that the browser is not the only HTTP client.

---

# HTML

## What Is HTML?

HTML provides the **structure and meaning** of a web page.

It defines elements such as:

- Headings
- Paragraphs
- Images
- Links
- Sections
- Forms

HTML is **markup**, not programming logic.

The browser parses HTML and converts it into the DOM tree.

```text
HTML → Structure → DOM → Page
```

---

## Basic HTML Document Structure

Every clean HTML page starts with a basic document skeleton.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>My first page.</p>
</body>
</html>
```

### DOCTYPE

`<!DOCTYPE html>` tells the browser to use modern standards mode.

### HTML

`<html>` is the root element.

### Head

`<head>` contains metadata and links.

### Body

`<body>` contains what the user sees.

---

## Head vs Body

### `<head>`

Contains information describing the document:

- Title
- Character encoding
- CSS links
- SEO metadata

### `<body>`

Contains visible page content:

- Headings
- Paragraphs
- Images and links
- Forms
- Navigation
- Buttons

**Simple rule: Head describes the document; Body displays the document.**

---

## Elements, Tags, Attributes, and Values

HTML is made of elements written using tags. Attributes provide extra information.

Example:

```html
<a href="/contact">Contact Us</a>
```

In this example:

- **Opening tag:** `<a>`
- **Closing tag:** `</a>`
- **Attribute:** `href`
- **Attribute value:** `"/contact"`
- **Content:** `Contact Us`

Other examples:

```html
<img src="photo.jpg" alt="Profile photo">

<input type="email" name="email">
```

Common attributes include:

- `href`
- `src`
- `alt`
- `type`
- `name`

---

## Block vs Inline Elements

### Block Elements

Block elements:

- Start on a new line
- Take the available width

Examples:

```text
div
p
h1
section
```

### Inline Elements

Inline elements:

- Stay within the current line
- Only use the width they need

Examples:

```text
span
a
strong
img
```

---

## Common HTML Tags

- `<h1>` – Main heading
- `<p>` – Paragraph
- `<a>` – Link
- `<img>` – Image
- `<ul>` / `<ol>` – Lists
- `<div>` – Generic container
- `<button>` – Clickable button
- `<section>` – Page section

Use semantic tags when meaning exists. Use `<div>` when a neutral container is needed.

---

## Semantic HTML

Semantic HTML uses tags that describe the **meaning** of content rather than only its appearance.

Common semantic elements:

- `<header>` – Top area
- `<nav>` – Navigation links
- `<main>` – Primary content
- `<section>` – Grouped content
- `<article>` – Independent content
- `<footer>` – Bottom information

### Benefits

- Cleaner code
- Better accessibility
- Easier SEO
- Easier team collaboration

---

## The DOM Tree

The browser converts HTML text into a tree of objects called the **DOM (Document Object Model)**.

Example:

```text
html
├── head
└── body
    ├── h1
    ├── p
    └── img
```

Parent elements contain child elements.

DevTools can be used to inspect the DOM tree live.

---

## Common HTML Mistakes

### Missing DOCTYPE

The browser may enter quirks mode.

### Bad Nesting

Can result in an invalid document structure.

### No Alt Text

Results in poor accessibility.

### Headings Out of Order

Can cause poor structure and SEO.

### Using Div for Everything

Removes semantic meaning from the page.

### Forgetting File Paths

Can result in broken images or links.

---

# Labs

## Lab: Inspect Browser Network Traffic

Steps:

1. Open DevTools → Network
2. Visit any website
3. Select one request
4. Read the method and URL
5. Inspect headers
6. Check status and response time

Example result:

```text
Method: GET
Status: 200 OK
Content-Type: text/html
Response time: 84 ms
```

---

## Lab: Send Requests Manually

Used `curl` to prove that the browser is not the only HTTP client.

```bash
curl https://example.com

curl -X POST https://httpbin.org/post -d "name=aly"

curl https://example.com/does-not-exist
```

The commands demonstrate:

- Retrieving a page
- Sending data
- Receiving an error response

---

## Lab: Build the First HTML Page

Steps:

1. Create `index.html`
2. Add the document skeleton
3. Add a heading and paragraph
4. Add a list and link
5. Add an image with alt text
6. Open the page in the browser

---

## Lab: Head or Body?

Practiced identifying where different HTML information belongs.

### Head

- Page title
- Character encoding
- CSS link
- SEO metadata

### Body

- Main heading
- Paragraph
- Image
- Navigation
- Button

---

## Lab: Tag, Content, Attribute, Value

Example:

```html
<a href="/contact">Contact Us</a>
```

Identification:

```text
Opening tag: <a>
Closing tag: </a>
Attribute: href
Attribute value: "/contact"
Content: Contact Us
```

---

## Lab: Semantic HTML Challenge

Practiced replacing generic `<div>` elements with semantic elements when the content has a clear meaning.

For example:

```html
<header>
    <h1>My Website</h1>

    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
    </nav>
</header>

<main>
    <section>
        <h2>About</h2>
        <p>About our website.</p>
    </section>
</main>

<footer>
    Copyright 2026
</footer>
```

---

## Lab: profile.html

Created a profile page containing:

- One `h1`
- Two `h2` headings
- Three paragraphs
- One image
- One external link
- One unordered list
- One ordered list
- One button

---

# Project Build: HTML Skeleton

Started the final page structure.

```text
project/
├── index.html
├── css/
├── images/
└── README.md
```

The HTML page structure includes:

- Header + navigation
- Hero section
- Features section
- About section
- Footer + contact information

Styling will be added in the next lesson.

---

## Key Takeaways

- Understood the HTTP request-response cycle.
- Learned HTTP methods and their purposes.
- Learned how headers and bodies work.
- Reviewed HTTP status codes.
- Understood why HTTP is stateless.
- Learned how cookies, sessions, and tokens maintain state.
- Understood HTTPS and TLS encryption.
- Practiced inspecting requests using DevTools.
- Sent HTTP requests manually using cURL.
- Learned the basic HTML document structure.
- Distinguished between `<head>` and `<body>`.
- Learned elements, tags, attributes, and values.
- Distinguished between block and inline elements.
- Learned common and semantic HTML tags.
- Understood the DOM tree and parent-child relationships.
- Reviewed common HTML mistakes and best practices.
- Completed practical HTML labs.
- Started the project HTML skeleton.

---

**Status:** ✅ Completed
