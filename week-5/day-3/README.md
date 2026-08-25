# Week 5 - Day 3

## Overview

The third day of Week 5 focused on intermediate HTML and the fundamentals of CSS.

The session introduced how forms collect user input, how tables represent structured data, how media should be added accessibly, and how HTML forms connect to the HTTP request-response process.

CSS fundamentals were also introduced, including external stylesheets, selectors, specificity, the box model, display properties, relative units, and hover states.

Several practical labs were completed to build forms, practice CSS specificity, style HTML pages, and combine HTML and CSS in a Course Registration page.

---

## Topics Covered

- Intermediate HTML
- HTML Forms
- Form Elements and Input Types
- Form Attributes
- Labels, IDs, and Names
- Form Submission
- Built-in Form Validation
- HTML Tables
- Media in HTML
- HTML Accessibility
- CSS Fundamentals
- External CSS
- CSS Rule Structure
- CSS Selectors
- CSS Specificity
- CSS Box Model
- Display Properties
- CSS Units
- Hover States
- HTML and CSS Best Practices
- Course Registration Page

---

## Key Concepts

### HTML Forms

HTML forms are used to collect information from users.

A form can contain different controls depending on the type of information required.

Common form elements include:

- `<form>` – Defines the form
- `<label>` – Describes an input field
- `<input>` – Collects user input
- `<textarea>` – Collects longer text
- `<select>` – Provides a list of options
- `<option>` – Defines an option inside a select menu
- `<button>` – Creates a clickable button
- `<fieldset>` – Groups related form controls
- `<legend>` – Describes a fieldset

Example:

```html
<form action="/contact" method="post">
    <label for="email">Email</label>
    <input type="email" id="email" name="email">

    <button type="submit">Submit</button>
</form>
```

---

### Form Attributes

Form elements use attributes to control their behavior and identify submitted data.

Important attributes include:

- `action` – Specifies where the form data is sent
- `method` – Specifies how the data is sent
- `type` – Defines the type of input
- `id` – Identifies an element
- `name` – Identifies the field when its data is submitted
- `for` – Connects a label to an input
- `required` – Makes a field required before submission
- `checked` – Sets a checkbox or radio button as selected by default

The `name` attribute is especially important because it identifies the submitted field for the backend.

---

### Form Input Types

Different input types can be used depending on the information being collected.

Examples include:

```html
<input type="text">
<input type="email">
<input type="date">
<input type="radio">
<input type="checkbox">
```

Other form controls include:

```html
<select>
    <option>Python</option>
    <option>HTML</option>
    <option>CSS</option>
</select>
```

and:

```html
<textarea name="message"></textarea>
```

---

### Labels and Inputs

Labels should be connected to their corresponding inputs.

Example:

```html
<label for="email">Email</label>
<input type="email" id="email" name="email">
```

The `for` value of the label should match the `id` of the input.

This improves usability and accessibility.

---

### Form Validation

HTML provides built-in validation for form fields.

For example:

```html
<input type="email" name="email" required>
```

The browser can check that:

- Required fields are completed
- Email fields contain a valid email format
- Appropriate values are entered for specific input types

This provides basic validation before the data is submitted.

---

### Form Submission Journey

Forms connect HTML pages to the HTTP request-response process.

The general flow is:

```text
User
  ↓
Form
  ↓
Browser
  ↓
HTTP Request
  ↓
Server
  ↓
Application Logic
  ↓
HTTP Response
```

The user enters information into the form.

The browser collects the values and sends them to the server according to the form's `action` and `method`.

The server processes the submitted data and returns a response.

---

## HTML Tables

Tables are used to display structured data.

Common table elements include:

- `<table>` – Defines the table
- `<caption>` – Describes the table
- `<thead>` – Contains header rows
- `<tbody>` – Contains the main table data
- `<tfoot>` – Contains footer rows
- `<tr>` – Defines a table row
- `<th>` – Defines a header cell
- `<td>` – Defines a data cell

Example:

```html
<table>
    <caption>Available Courses</caption>

    <tr>
        <th>Course</th>
        <th>Duration</th>
        <th>Price</th>
    </tr>

    <tr>
        <td>Python</td>
        <td>3 months</td>
        <td>1000 SAR</td>
    </tr>
</table>
```

Tables should be used for structured data rather than for page layout.

---

## Media and Accessibility

Images and other media can make a webpage more useful and informative.

Images should include meaningful alternative text.

Example:

```html
<img src="pythonLogo.jpg" alt="Python Logo">
```

The `alt` attribute describes the image when it cannot be displayed and supports users who rely on assistive technologies.

Other good practices include:

- Using meaningful HTML structure
- Adding labels to form fields
- Supporting keyboard-friendly interactions
- Optimizing image sizes
- Using ARIA only when necessary

---

# CSS

## What Is CSS?

CSS stands for **Cascading Style Sheets**.

HTML provides the structure and meaning of a webpage, while CSS controls its presentation and visual appearance.

CSS can control:

- Colors
- Fonts
- Spacing
- Borders
- Sizes
- Layout
- Visual interaction states

---

## Connecting CSS to HTML

An external CSS file can be connected to an HTML document inside the `<head>`.

Example:

```html
<link rel="stylesheet" href="style.css">
```

A basic project structure can be:

```text
project/
├── index.html
├── style.css
├── images/
└── README.md
```

Keeping CSS separate from HTML makes the project cleaner and easier to maintain.

---

## CSS Rule Structure

A CSS rule contains a selector and one or more declarations.

Example:

```css
p {
    color: blue;
}
```

In this example:

- `p` – Selector
- `color` – Property
- `blue` – Value
- `color: blue;` – Declaration

The selector determines which HTML element receives the style.

---

## CSS Selectors

Selectors are used to target HTML elements.

### Element Selector

Targets all elements of a specific type.

```css
p {
    color: blue;
}
```

---

### Class Selector

Targets elements that have a specific class.

```css
.btn {
    padding: 1rem;
}
```

Classes are useful when the same style needs to be reused across multiple elements.

---

### ID Selector

Targets an element with a specific ID.

```css
#main {
    background-color: white;
}
```

IDs are more specific than classes and element selectors.

---

### Descendant Selector

Targets an element located inside another element.

```css
nav a {
    text-decoration: none;
}
```

This targets links located inside a `<nav>` element.

---

## CSS Specificity

Specificity determines which CSS rule wins when multiple rules target the same element.

The general priority is:

```text
Inline Style
    ↓
ID Selector
    ↓
Class / Pseudo-class
    ↓
Element Selector
    ↓
Browser Defaults
```

Example:

```css
p {
    color: blue;
}

.note {
    color: green;
}

#main-note {
    color: red;
}
```

If the same paragraph matches all three rules, the ID selector has the highest specificity and the text becomes red.

When two rules have the same specificity, the rule written later usually wins.

---

## CSS Box Model

Every HTML element can be considered a rectangular box.

The CSS Box Model consists of:

```text
Margin
└── Border
    └── Padding
        └── Content
```

### Content

The actual content of the element, such as text or an image.

### Padding

The space between the content and the border.

### Border

The line surrounding the content and padding.

### Margin

The space outside the border that separates the element from other elements.

Example:

```css
section {
    margin: 20px;
    border: 1px solid black;
    padding: 20px;
}
```

---

### Box Sizing

The `box-sizing` property can make element sizing easier to manage.

```css
* {
    box-sizing: border-box;
}
```

With `border-box`, the declared width and height include the content, padding, and border.

---

## Display Properties

The `display` property controls how an element behaves in the page flow.

### Block

```css
display: block;
```

Block elements:

- Start on a new line
- Usually take the available width

### Inline

```css
display: inline;
```

Inline elements:

- Stay within the current line
- Use only the space they need

### Inline-block

```css
display: inline-block;
```

Inline-block elements can remain on the same line while still allowing properties such as width and height.

---

## CSS Units

CSS supports different units for controlling size and spacing.

### `rem`

Relative to the root element's font size.

Example:

```css
font-size: 1.2rem;
```

It is useful for scalable and consistent sizing.

### `%`

Represents a percentage relative to the relevant containing element or context.

Example:

```css
width: 80%;
```

### `vw`

Represents a percentage of the viewport width.

```css
width: 100vw;
```

### `vh`

Represents a percentage of the viewport height.

```css
min-height: 80vh;
```

---

## Hover States

Pseudo-classes can apply styles when the user interacts with an element.

Example:

```css
button:hover {
    opacity: 0.8;
}
```

The `:hover` pseudo-class applies when the pointer is placed over the element.

Hover effects can provide visual feedback to users.

---

## Common HTML and CSS Mistakes

### Missing Labels

Form inputs without labels can reduce accessibility and usability.

### Missing Name Attributes

A form field without a `name` may not provide the expected field identifier when submitted.

### Using Tables for Layout

Tables should represent structured data rather than control the layout of a webpage.

### Using Too Many IDs

Classes should be preferred when styles need to be reused.

### Using Inline Styles Everywhere

Using an external stylesheet keeps styling organized and separates presentation from HTML structure.

---

# Labs

## Lab: Build a Complete Form

Practiced creating a complete HTML form using different controls.

The form included:

- Text input
- Email input
- Select menu
- Checkbox
- Textarea
- Submit button
- Labels
- Correct `name` attributes

The lab demonstrated how form fields collect information that can later be sent to a backend.

---

## Lab: Table Practice

Practiced creating structured data using an HTML table.

The table included:

- Caption
- Header cells
- Rows
- Data cells

The activity reinforced that tables should represent data rather than be used for page layout.

---

## Lab: CSS Selectors

Practiced applying CSS using different selector types.

The activity included:

- Element selectors
- Class selectors
- ID selectors
- Descendant selectors

This demonstrated how CSS can target individual elements or reusable groups of elements.

---

## Lab: Specificity Challenge

Practiced predicting which CSS rule would win when multiple selectors targeted the same element.

The activity compared:

```text
Element Selector
Class Selector
ID Selector
```

A hover state was also added and tested.

This helped demonstrate how specificity and rule order affect the final appearance of an element.

---

## Lab: Box Model and Display

Practiced changing spacing and element behavior using:

- Margin
- Padding
- Border
- `box-sizing`
- Block
- Inline
- Inline-block
- Relative CSS units

This demonstrated how CSS controls both spacing and the flow of elements on the page.

---

## Lab: Style the Project

Connected an external stylesheet to an HTML page and applied CSS styling.

The activity included:

- Body typography
- Section spacing
- Form styling
- Button styling
- Hover feedback

This demonstrated the separation between HTML structure and CSS presentation.

---

## Course Registration Page

Built and styled a Course Registration page to combine the HTML and CSS concepts covered during the session.

The page included:

- Semantic HTML structure
- Header, main sections, and footer
- Program information
- Images with alt text
- A table of available courses
- A registration form
- Fieldsets and legends
- Text and email inputs
- Date input
- Radio buttons
- Select menu
- Checkbox
- Required fields
- Submit button
- External CSS styling

The CSS was used to style:

- Page background
- Header
- Content sections
- Images
- Course table
- Form controls
- Buttons
- Footer
- Hover and focus states

---

## Project Build: HTML + CSS

Continued building the project by moving from the HTML skeleton into presentation and styling.

The project now combines:

```text
HTML
  ↓
Structure + Meaning

CSS
  ↓
Presentation + Styling
```

The page structure and styling are kept separate using an external CSS file.

This creates a cleaner foundation for more advanced layout techniques in future lessons.

---

## Key Takeaways

- Learned how HTML forms collect user input.
- Understood the purpose of form attributes such as `action`, `method`, `id`, `name`, and `for`.
- Practiced different HTML input types and form controls.
- Learned how built-in form validation works.
- Connected form submission to the HTTP request-response process.
- Learned how tables represent structured data.
- Reviewed accessibility practices for forms and media.
- Learned the role of CSS in webpage presentation.
- Connected HTML to an external CSS stylesheet.
- Learned the structure of a CSS rule.
- Practiced element, class, ID, and descendant selectors.
- Understood how CSS specificity determines which rule wins.
- Learned the CSS Box Model.
- Distinguished between content, padding, border, and margin.
- Practiced block, inline, and inline-block display behavior.
- Learned how `rem`, `%`, `vw`, and `vh` units work.
- Applied hover states for visual feedback.
- Reviewed common HTML and CSS mistakes.
- Completed practical HTML and CSS labs.
- Built and styled a Course Registration page.
- Continued developing the project using HTML and external CSS.

---

**Status:** ✅ Completed
