# Week 5 - Day 5

## Overview

The fifth day of Week 5 focused on CSS motion, transitions, transforms, and animations.

The session explained how motion can improve user feedback and make interfaces feel more responsive without distracting the user.

We practiced creating interactive hover and focus effects, animating cards and buttons, building entrance animations with `@keyframes`, and learning how animation libraries and CSS frameworks can support development when used carefully.

---

## Topics Covered

- CSS Motion
- User Interaction Feedback
- CSS Transitions
- Transition Properties
- `:hover`
- `:focus`
- CSS Transforms
- `translate()`
- `scale()`
- `rotate()`
- `skew()`
- Card Lift Effects
- CSS Animations
- `@keyframes`
- Animation Timeline
- Animation Properties
- Animation Shorthand
- Common Animation Patterns
- Hero Entrance Animation
- Animation Delays
- Animate.css
- CSS Animation Libraries
- Bootstrap
- Tailwind CSS
- Using Libraries Carefully
- Custom CSS First

---

## Key Concepts

### Why Motion Matters

Motion can help communicate changes and interactions to the user.

It can provide feedback when users:

- Hover over an element
- Click a button
- Focus on an input
- Wait for content to load

Good animation should guide the user's attention without becoming distracting.

The goal is not to add unnecessary effects.

The goal is to make the interface feel responsive, clear, and professional.

---

## From Static Page to Responsive Interface

A user interface can react visually when the user interacts with it.

The basic flow is:

```text
Normal State
     ↓
User Interaction
     ↓
Visual Response
```

User interactions can include:

- Hover
- Focus
- Click
- Page load

CSS can respond to these interactions using transitions and animations.

---

## CSS Transitions

Transitions control how an element changes from one state to another.

For example:

```text
Normal State → Hover State
```

Without a transition, the change happens immediately.

With a transition, the change happens smoothly.

Example:

```css
button {
    transition: background-color 0.3s ease,
                transform 0.3s ease;
}

button:hover {
    transform: translateY(-4px);
}
```

---

### Transition Properties

A CSS transition can include:

- Property
- Duration
- Timing Function
- Delay

---

### Property

The property defines what CSS value should change.

Example:

```css
transition: transform 0.3s ease;
```

Here, the property being animated is:

```css
transform
```

---

### Duration

Duration controls how long the transition takes.

Example:

```css
transition: transform 0.3s ease;
```

`0.3s` means the transition takes 0.3 seconds.

---

### Timing Function

The timing function controls how the speed changes during the transition.

Example:

```css
transition: transform 0.3s ease;
```

Common timing functions include:

- `ease`
- `linear`
- `ease-in`
- `ease-out`
- `ease-in-out`

---

### Delay

A delay defines how long the browser waits before starting the transition.

Example:

```css
transition-delay: 0.2s;
```

---

## Hover State

`:hover` applies styles when the mouse pointer is placed over an element.

Example:

```css
button:hover {
    transform: translateY(-4px);
}
```

This moves the button upward by 4 pixels when the user hovers over it.

---

## Focus State

`:focus` applies styles when an element receives keyboard focus.

Example:

```css
button:focus {
    transform: translateY(-4px);
}
```

Supporting focus states is important for keyboard accessibility.

A button can use the same effect for both hover and focus:

```css
.cta:hover,
.cta:focus {
    transform: translateY(-4px);
}
```

---

## What Should Transition?

Not every CSS property gives the same performance or visual experience.

### Recommended

#### `transform`

Useful for movement, scaling, and rotation.

```css
transform: translateY(-4px);
```

#### `opacity`

Useful for smooth fade effects.

```css
opacity: 0;
```

---

### Useful

#### `background-color`

Works well for buttons and interactive elements.

```css
background-color: blue;
```

---

### Avoid When Possible

Animating:

```css
width
height
```

can force the browser to recalculate the page layout and may feel less smooth.

A useful rule is to prefer:

- `transform`
- `opacity`

for most animations.

---

# CSS Transforms

CSS Transform allows an element to move, resize, rotate, or tilt without changing the document structure.

The main transform functions covered were:

- `translate()`
- `scale()`
- `rotate()`
- `skew()`

---

## Translate

`translate()` moves an element.

Example:

```css
transform: translate(10px, -6px);
```

This moves the element:

- 10px to the right
- 6px upward

Another example:

```css
transform: translateY(-8px);
```

A negative Y value moves the element upward.

---

## Scale

`scale()` makes an element larger or smaller.

Example:

```css
transform: scale(1.05);
```

Values:

- `1` → normal size
- Greater than `1` → larger
- Less than `1` → smaller

---

## Rotate

`rotate()` turns an element.

Example:

```css
transform: rotate(5deg);
```

`deg` represents degrees.

---

## Skew

`skew()` tilts or slants an element.

Example:

```css
transform: skew(8deg);
```

---

# Card Lift Effect

A common user interface interaction is the card lift effect.

When the user hovers over a card, the card can move slightly upward.

Example:

```css
.card {
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
}
```

A shadow can also increase to make the card appear elevated.

The effect should remain subtle and support the interface rather than distract from it.

---

# CSS Animation

CSS Animation is useful when an element needs more than two simple states.

Transitions usually handle:

```text
Normal → Hover
```

Animations can define a complete sequence:

```text
0% → 50% → 100%
```

Animations use:

```css
@keyframes
```

to define checkpoints in the animation timeline.

---

## Keyframes

`@keyframes` defines how an animation changes over time.

Example:

```css
@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
```

At `0%`:

- The element is invisible.
- The element is positioned 20px lower.

At `100%`:

- The element is fully visible.
- The element returns to its normal position.

---

## Animation Timeline

An animation can contain multiple checkpoints.

Example:

```text
0% → Start
50% → Middle
100% → End
```

More checkpoints can be added when a more complex animation sequence is needed.

---

# Animation Properties

CSS animations can be controlled using several properties.

---

## `animation-name`

Defines which `@keyframes` animation should run.

Example:

```css
animation-name: fadeIn;
```

---

## `animation-duration`

Defines how long the animation runs.

Example:

```css
animation-duration: 1s;
```

---

## `animation-timing-function`

Defines how the animation speed changes.

Example:

```css
animation-timing-function: ease;
```

---

## `animation-delay`

Controls how long the browser waits before starting the animation.

Example:

```css
animation-delay: 0.25s;
```

---

## `animation-iteration-count`

Controls how many times the animation repeats.

Example:

```css
animation-iteration-count: infinite;
```

`infinite` means the animation continues repeating.

---

## `animation-fill-mode`

Controls which animation state remains before or after the animation finishes.

Example:

```css
animation-fill-mode: forwards;
```

`forwards` keeps the final animation state after the animation finishes.

---

# Animation Shorthand

Animation properties can be combined into one line.

Example:

```css
.loader {
    animation: spin 0.8s linear infinite;
}
```

This means:

- `spin` → Animation name
- `0.8s` → Duration
- `linear` → Timing function
- `infinite` → Repeat continuously

Another example:

```css
.hero {
    animation: fadeIn 1s ease forwards;
}
```

---

# Common Animation Patterns

Several common animation patterns were introduced.

### Fade In

Used when content gradually appears.

```text
fadeIn
```

Common use:

- Page entrance
- Section entrance

---

### Slide In

Moves content into the page from another position.

```text
slideIn
```

Common use:

- Hero text
- Hero images

---

### Pulse

Makes an element grow and shrink slightly.

```text
pulse
```

Common use:

- Call-to-action buttons
- Elements that need attention

---

### Spin

Rotates an element continuously.

```text
spin
```

Common use:

- Loading indicators

---

### Bounce

Creates a bouncing movement.

```text
bounce
```

This effect should be used carefully because too much bouncing can distract the user.

---

### Reveal

Makes hidden content appear.

```text
reveal
```

This pattern can also be useful later with JavaScript interactions.

---

# Labs

## Lab 1: Interactive Button

Created an interactive button that clearly responds to user actions.

The lab included:

- Creating a button class
- Adding transitions
- Adding a hover state
- Adding a focus state
- Testing the result in the browser

Example:

```css
.cta {
    background: var(--main-color);
    transition: transform 0.25s ease,
                background 0.25s ease;
}

.cta:hover,
.cta:focus {
    transform: translateY(-4px);
    background: var(--accent-color);
}
```

The button changes visually when the user hovers over it or focuses on it using the keyboard.

---

## Lab 2: Hero Entrance Animation

Created entrance animations for the Hero section.

The goal was to make the Hero section appear intentionally instead of appearing suddenly.

The lab included:

- Animating the Hero heading
- Animating the supporting text
- Delaying the button slightly
- Using `opacity`
- Using `transform`
- Keeping animation duration around 600–1200ms

Example:

```css
.hero-title {
    animation: slideIn 0.9s ease forwards;
}

.hero-text {
    animation: fadeIn 1s ease 0.25s forwards;
}
```

The animation delay allows Hero elements to appear in sequence instead of appearing at exactly the same time.

Example sequence:

```text
Heading
   ↓
Supporting Text
   ↓
Button
```

---

# Animate.css

Animate.css is a CSS library that provides ready-made animations.

The library can be included using a stylesheet link:

```html
<link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
>
```

Animations can then be applied using predefined classes.

Example:

```html
<h1 class="animate__animated animate__fadeInUp">
    Welcome
</h1>
```

Examples of Animate.css classes include:

- `animate__fadeIn`
- `animate__slideInUp`
- `animate__zoomIn`
- `animate__pulse`

The main project should still demonstrate custom CSS animations.

Animate.css should only be used as an optional library example.

---

# Bootstrap vs Tailwind

Bootstrap and Tailwind are two different ways to speed up CSS development.

---

## Bootstrap

Bootstrap provides:

- Pre-built components
- Grid system
- Fast classic layouts
- Less custom CSS at the beginning

Bootstrap is useful when developers want ready-made components and layout structures.

---

## Tailwind CSS

Tailwind provides:

- Utility classes
- Design composition inside HTML
- High customization
- Utility-based styling
- Popular use in modern technology stacks

Instead of providing complete components, Tailwind provides smaller utility classes that can be combined.

---

# Using Libraries Carefully

Libraries can speed up development, but they should not replace learning CSS.

Libraries can be useful when:

- Faster components are needed.
- A small ready-made animation is needed.
- The developer understands the CSS behind the library.

Libraries should be avoided when:

- They replace learning.
- They make the page unnecessarily heavy.
- They create too many confusing classes.

---

## Project Rule

The main rule for the project is:

**Custom CSS First**

The project should:

- Demonstrate custom CSS.
- Use only one optional animation library example.
- Explain the library choice in the README if used.

---

## Key Takeaways

- Learned why motion is useful for user feedback.
- Understood the difference between transitions and animations.
- Learned how CSS transitions create smooth changes between states.
- Practiced transition properties such as duration, timing function, and delay.
- Used `:hover` and `:focus` to create interactive states.
- Learned that `transform` and `opacity` are preferred for smooth motion.
- Practiced `translate()`, `scale()`, `rotate()`, and `skew()`.
- Created a card lift effect using `translateY()`.
- Learned how `@keyframes` defines an animation timeline.
- Used percentages such as `0%`, `50%`, and `100%` to define animation checkpoints.
- Learned the main CSS animation properties.
- Used animation shorthand syntax.
- Practiced common animation patterns including fade, slide, pulse, spin, bounce, and reveal.
- Created an entrance animation for the Hero section.
- Used animation delays to create a sequence between Hero elements.
- Learned how Animate.css provides ready-made animations.
- Compared Bootstrap and Tailwind at a basic level.
- Learned why libraries should support CSS knowledge rather than replace it.
- Applied the rule of using custom CSS first.

---

**Status:** ✅ Completed
