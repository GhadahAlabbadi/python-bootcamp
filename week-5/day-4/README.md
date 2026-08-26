# CSS Flexbox, Grid & Responsive Design

## Flexbox

Flexbox is used to align and organize elements in one direction, either a row or a column.

```css
.container {
    display: flex;
}
```

### Main Flexbox Properties

- `flex-direction` controls whether items are arranged in a row or column.
- `justify-content` moves items along the main axis.
- `align-items` moves items along the cross axis.
- `flex-wrap` allows items to move to a new line when there is not enough space.
- `gap` adds spacing between items.

```css
.container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
```

## Justify Content vs Align Items

`justify-content` controls alignment along the main axis.

```css
.container {
    justify-content: space-between;
}
```

`align-items` controls alignment along the cross axis.

```css
.container {
    align-items: center;
}
```

The direction of the main and cross axes depends on `flex-direction`.

## Flexbox Navigation

Flexbox can be used to create and align a navigation bar.

```css
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
    padding: 20px;
}

nav {
    display: flex;
    gap: 20px;
}

nav a {
    text-decoration: none;
}
```

## CSS Grid

CSS Grid is used to organize content into rows and columns.

```css
.features {
    display: grid;
}
```

Grid is useful for:

- Card galleries
- Page sections
- Two-dimensional layouts
- Responsive content blocks

## Columns, Rows, and Gap

Grid columns can be created using `grid-template-columns`.

```css
.cards {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
}
```

`fr` represents a share of the available space.

`gap` controls the spacing between rows and columns.

## Responsive Grid

A responsive grid can automatically change the number of columns depending on the available screen space.

```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

- `auto-fit` fits as many columns as the available space allows.
- `minmax()` sets a minimum and maximum size for each column.
- `1fr` allows the remaining space to be shared equally.

The Features/Courses section can display:

- Desktop: 3 cards
- Tablet: 2 cards
- Mobile: 1 card

## Grid Lines and Spanning

Grid items can span across more than one column.

```css
.featured {
    grid-column: 1 / 3;
}
```

Spanning can be used when an item needs to occupy more space than other items.

## Flexbox vs Grid

Flexbox is mainly used for alignment and one-dimensional layouts.

Examples:

- Navigation bars
- Buttons and actions
- Centering content
- One row or one column

Grid is mainly used for structured two-dimensional layouts.

Examples:

- Card galleries
- Page sections
- Responsive content blocks
- Rows and columns

Flexbox and Grid can also be used together on the same webpage.

## Combining Flexbox and Grid

Different sections of a webpage can use different layout methods.

- Header → Flexbox
- Hero → Flexbox or Grid
- Features → Grid
- About → Two-column layout
- Footer → Flexbox or Grid

## Hero Section

On desktop, the Hero section can display text and an image next to each other.

```text
Text | Image
```

On mobile, the content should stack.

```text
Text
Image
```

The content should reorganize instead of becoming too narrow.

## Media Queries

Media Queries allow CSS rules to change depending on the screen size.

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

When the screen becomes narrow:

- Change the navigation layout.
- Stack the Hero content.
- Reduce unnecessary spacing.
- Keep text readable.
- Make sure nothing extends outside the screen.

## Responsive Design

Responsive design allows the same webpage to work correctly on desktop, tablet, and mobile devices.

The goal is not only to shrink the content but to reorganize it based on the available screen space.

## Labs

### Lab 1: Flexbox Navbar

Created a navigation bar using Flexbox.

Applied:

- `display: flex`
- `justify-content`
- `align-items`
- `gap`

Tested the navigation at different browser widths.

### Lab 2: Responsive Card Grid

Created a responsive Features/Courses section using CSS Grid.

Applied:

```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

The cards adjust automatically depending on the available screen width.

### Lab 3: Project Layout Upgrade

Applied the layout concepts to the Unit Project.

The project includes:

- Flexbox navigation
- Two-column Hero section
- Responsive Features Grid
- Two-column About section
- Organized Footer
- External CSS
- Relative paths for images and CSS
- Responsive layouts for desktop, tablet, and mobile

## Key Takeaways

- Flexbox is useful for alignment and one-dimensional layouts.
- Grid is useful for rows, columns, and structured layouts.
- `justify-content` controls the main axis.
- `align-items` controls the cross axis.
- `flex-wrap` allows items to move to a new line.
- `gap` creates spacing between layout items.
- `auto-fit` and `minmax()` help create responsive grids.
- Media Queries change layouts at specific screen widths.
- Responsive layouts should reorganize content for smaller screens.
- Flexbox and Grid can be used together in the same project.

**Status:** ✅ Completed
