# Week 3 - Day 4

## Overview

The fourth day of Week 3 started with a review of core Python concepts, then focused on comprehensions, concise transformations, filtering, and collection-building patterns.

---

## Topics Covered

### Review

- Indentation and Code Blocks
- Variable Naming Rules
- Variables and Object References
- Multiple Assignment
- Dynamic Typing
- Core Python Data Types
- Dictionary Keys
- Strings
- Boolean and None
- type() and isinstance()
- input()
- Validation and Casting
- print()
- Type Errors
- Loops Review

### Comprehension, Copying and Performance

- Concise Code and Predictable Behavior
- Comprehension Structure
- List Comprehension
- Filtering
- Filtering and Transformation
- Multiple for Clauses
- Conditional Expressions
- Set Comprehension
- Dictionary Comprehension

---

## Key Concepts

### Indentation and Code Blocks

Python uses indentation to define code blocks and determine which statements belong together.

### Variable Naming Rules

Variable names should follow Python naming rules and use clear, meaningful names.

### Variables Store References

Variables store references to objects rather than containing the objects themselves.

### Multiple Assignment

Python supports assigning multiple values at once.
```python
x, y = 10, 20
```

### Dynamic Typing

Python determines variable types at runtime, and the same name can later refer to a different type of object.

### Core Python Data Types

Reviewed common Python data types, including:

- Numbers
- Strings
- Booleans
- None

### Dictionary Keys

Dictionary keys must be unique and use hashable values such as immutable types.

### Strings

Strings represent ordered text and support indexing, slicing, and common string operations.

### Boolean and None

Booleans represent two-state conditions, while None represents the absence of a value.

### type() and isinstance()

Used:
```python
type()
isinstance()
```

to inspect and check value types.

### input()

input() always returns text.

Typical input handling includes:

1. Validation
2. Casting

### Casting

Casting converts values deliberately from one type to another.
```python
age = int(input("Enter age: "))
```

### print()

print() controls what is displayed to the user.

### Type Errors

Reviewed common type-related errors and how they usually come from incompatible operations or incorrect assumptions about data types.

### Loops Review

Reviewed previously learned loop concepts using for and while.

---

## Comprehensions

### Concise Code Still Needs Predictable Behavior

Shorter code should still remain readable, understandable, and predictable.

### Comprehension Structure

A comprehension can combine:

- An expression
- A loop
- An optional filter

Example:
```python
squares = [x * x for x in range(5)]
```

### List Comprehension

List comprehensions transform items into a new list.
```python
numbers = [1, 2, 3]

squares = [x * x for x in numbers]
```

### Filtering

A filter keeps only items that match a condition.
```python
numbers = [1, 2, 3, 4, 5]

even_numbers = [x for x in numbers if x % 2 == 0]
```

### Filtering and Transformation

Filtering and transformation can be combined.
```python
squares = [x * x for x in numbers if x % 2 == 0]
```

### Multiple for Clauses

Multiple for clauses follow the same order as nested loops.
```python
pairs = [(x, y) for x in range(2) for y in range(2)]
```

### Conditional Expressions

A conditional expression produces one of two values.
```python
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
```

### Set Comprehension

Set comprehensions create sets and automatically remove duplicate results.
```python
values = {x % 3 for x in range(10)}
```

### Dictionary Comprehension

Dictionary comprehensions build key-value mappings.
```python
squares = {x: x * x for x in range(5)}
```

---

## Lab

Completed a Python lab covering the reviewed fundamentals and comprehension concepts.

The complete lab solution is available in the lab folder.

---

## Homework

### Research Question

Can a tuple contain a list or dictionary, and can the values inside that list or dictionary be updated?
The research focuses on the difference between tuple immutability and mutable objects stored inside a tuple.

---

## Key Takeaways

- Reviewed core Python syntax, data types, input handling, and loops.
- Reinforced the idea that variables refer to objects.
- Practiced concise collection transformations using comprehensions.
- Used filters inside comprehensions.
- Combined filtering and transformation.
- Practiced multiple for clauses.
- Used conditional expressions inside comprehensions.
- Built sets and dictionaries using comprehension syntax.

---

Status: ✅ Completed
