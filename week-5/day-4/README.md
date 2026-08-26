# Week 5 - Day 4

## Overview

The fourth day of Week 5 focused on responsive web design using CSS Flexbox, CSS Grid, and Media Queries.

The session explained how Flexbox and Grid can be used together to organize page layouts and how responsive designs adapt to desktop, tablet, and mobile screen sizes.

Several practical labs were completed to build a Flexbox navigation bar, create responsive card layouts using Grid, and upgrade the project layout for different screen sizes.

---

## Topics Covered

- Responsive Web Design
- Flexbox
- Flex Containers and Flex Items
- Main Axis and Cross Axis
- `flex-direction`
- `justify-content`
- `align-items`
- `flex-wrap`
- `gap`
- Flexbox Navigation
- CSS Grid
- Grid Columns and Rows
- `grid-template-columns`
- `fr` Unit
- `repeat()`
- `auto-fit`
- `minmax()`
- Grid Lines and Spanning
- `grid-column`
- Flexbox vs Grid
- Media Queries
- Breakpoints
- Responsive Desktop, Tablet, and Mobile Layouts

---

## Key Concepts

### Responsive Design

Responsive design allows the same webpage to adapt to different screen sizes.

A webpage should work correctly on:

- Desktop
- Tablet
- Mobile

Responsive design does not simply shrink all elements.

Instead, the layout should reorganize its content based on the available screen space.

---

## Flexbox

Flexbox is a CSS layout system used to align and organize elements mainly in one direction.

A Flexbox layout starts by applying:

```css
.container {
    display: flex;
}
```

The parent becomes the **flex container**, and its direct children become **flex items**.

---

### Main Axis and Cross Axis

Flexbox works using two axes:

- **Main Axis**
- **Cross Axis**

The direction of these axes depends on `flex-direction`.

With:

```css
flex-direction: row;
```

The main axis is horizontal.

With:

```css
flex-direction: column;
```

The main axis is vertical.

---

### `flex-direction`

The `flex-direction` property controls the direction of flex items.

```css
.container {
    display: flex;
    flex-direction: row;
}
```

Common values include:

- `row`
- `column`

---

### `justify-content`

`justify-content` controls the alignment of flex items along the **main axis**.

Example:

```css
.container {
    justify-content: center;
}
```

Common values include:

- `flex-start`
- `center`
- `flex-end`
- `space-between`
- `space-around`
- `space-evenly`

---

### `align-items`

`align-items` controls alignment along the **cross axis**.

Example:

```css
.container {
    align-items: center;
}
```

Common values include:

- `flex-start`
- `center`
- `flex-end`
- `stretch`

The meaning of the main and cross axes changes when `flex-direction` changes.

---

### `flex-wrap`

By default, Flexbox uses:

```css
flex-wrap: nowrap;
```

This keeps flex items on the same line.

Using:

```css
flex-wrap: wrap;
```

allows items to move to another line when there is not enough space.

Example:

```css
.container {
    display: flex;
    flex-wrap: wrap;
}
```

This is useful for responsive layouts.

---

### `gap`

The `gap` property adds consistent spacing between flex or grid items.

Example:

```css
.container {
    display: flex;
    gap: 20px;
}
```

Using `gap` can be cleaner than adding separate margins to every item.

---

## Flexbox Navigation

Flexbox can be used to build and align navigation bars.

Example:

```css
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}
```

This can place a logo on one side and navigation links on the other.

---

## CSS Grid

CSS Grid is a layout system used to organize content using rows and columns.

A Grid layout starts with:

```css
.container {
    display: grid;
}
```

Grid is especially useful for:

- Cards
- Galleries
- Page sections
- Dashboards
- Two-dimensional layouts

---

### Grid Columns

Columns can be created using `grid-template-columns`.

Example:

```css
.cards {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}
```

This creates three equal columns.

---

### The `fr` Unit

`fr` stands for **fraction**.

It represents a share of the available Grid space.

Example:

```css
grid-template-columns: 1fr 1fr 1fr;
```

creates three equal columns.

Example:

```css
grid-template-columns: 2fr 1fr;
```

creates two columns where the first column receives twice as much space as the second.

---

### Responsive Grid

A responsive Grid can automatically adjust the number of columns based on the available space.

Example:

```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

In this example:

- `repeat()` repeats the column pattern.
- `auto-fit` fits as many columns as possible.
- `minmax()` defines the minimum and maximum width.
- `250px` is the minimum width.
- `1fr` allows the item to expand into available space.

This pattern allows cards to reorganize automatically across different screen sizes.

---

### Grid Lines and Spanning

Grid items can span across multiple columns.

Example:

```css
.featured {
    grid-column: 1 / 3;
}
```

This makes the element start at Grid line 1 and end at Grid line 3.

---

## Flexbox vs Grid

Flexbox and Grid solve different layout problems.

### Flexbox

Flexbox is useful for one-dimensional layouts and alignment.

Examples:

- Navigation bars
- Buttons
- Form rows
- Footer links
- Centering content

### Grid

Grid is useful for two-dimensional layouts using rows and columns.

Examples:

- Card layouts
- Galleries
- Features sections
- Dashboard layouts

A real webpage can use both Flexbox and Grid together.

For example:

- Header → Flexbox
- Hero → Flexbox or Grid
- Features → Grid
- About → Two-column layout
- Footer → Flexbox or Grid

---

## Hero Section

A Hero section can use a two-column layout on larger screens.

Example:

```text
Text | Image
```

On smaller screens, the content can stack:

```text
Text
Image
```

The goal is to reorganize the layout instead of making the content extremely narrow.

---

## Media Queries

Media Queries allow CSS rules to change based on the screen size.

Example:

```css
@media (max-width: 768px) {
    nav {
        flex-direction: column;
    }

    .hero {
        grid-template-columns: 1fr;
    }
}
```

The value `768px` acts as a **breakpoint**.

When the screen width becomes `768px` or smaller, the CSS rules inside the Media Query are applied.

---

## Responsive Layout Changes

When the screen becomes smaller, the webpage can:

- Change the navigation layout
- Stack Hero content
- Reduce unnecessary spacing
- Keep text readable
- Reorganize cards
- Prevent horizontal overflow

The goal is to make the same page usable across different devices.

---

# Labs

## Lab 1: Flexbox Navbar

Built a navigation bar using Flexbox.

Practiced:

- `display: flex`
- `justify-content`
- `align-items`
- `gap`

The layout was tested at different browser widths.

---

## Lab 2: Responsive Card Grid

Converted the Features or Services section into a responsive CSS Grid.

Used:

```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

The cards automatically reorganize depending on the available screen width.

---

## Lab 3: Project Layout Upgrade

Applied responsive layout techniques to the project.

The upgraded page structure included:

- Header → Flexbox Navbar
- Hero → Two-column layout
- Features → Responsive Grid
- About → Two-column layout
- Footer → Organized layout

The project was also tested at:

- Desktop width
- Tablet width
- Mobile width

The project continued to use:

- External CSS
- Relative paths
- Organized project files
- Responsive layouts

---

## Homework

### Features / Courses

Use CSS Grid for the Features or Courses section.

The expected responsive layout is:

```text
Desktop:
Card | Card | Card

Tablet:
Card | Card

Mobile:
Card
```

The section should use responsive Grid techniques so the cards reorganize based on the available screen width.

---

### Media Query

Add at least one mobile breakpoint.

When the screen becomes narrow:

- Change the navigation layout.
- Stack the Hero content.
- Reduce unnecessary spacing.
- Keep the text readable.
- Make sure no content extends outside the screen.

Example:

```css
@media (max-width: 768px) {
    nav {
        flex-direction: column;
    }

    .hero {
        grid-template-columns: 1fr;
    }
}
```

---

## Key Takeaways

- Learned how responsive layouts adapt to different screen sizes.
- Learned how Flexbox organizes and aligns elements.
- Understood the main axis and cross axis.
- Practiced `flex-direction`, `justify-content`, and `align-items`.
- Learned how `flex-wrap` allows items to move to another line.
- Used `gap` to create consistent spacing between elements.
- Built a navigation bar using Flexbox.
- Learned how CSS Grid organizes content into rows and columns.
- Used the `fr` unit to divide available Grid space.
- Learned how `repeat()`, `auto-fit`, and `minmax()` create responsive grids.
- Practiced Grid lines and column spanning.
- Understood when to use Flexbox and when to use Grid.
- Learned how Media Queries change layouts at specific breakpoints.
- Practiced responsive layouts for desktop, tablet, and mobile.
- Applied Flexbox, Grid, and Media Queries to the project.

---

**Status:** ✅ Completed
