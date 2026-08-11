# Week 3 - Day 3

## Overview

The third day of Week 3 focused on Python collections and how different collection types are used to organize, store, access, and process related data.

---

## Topics Covered

- Python Collections
- Lists
- List Indexing
- Modifying Lists
- List Methods
- Loops with Collections
- enumerate()
- Nested Collections
- Tuples
- Unpacking
- Sets
- Set Operations
- Dictionaries
- Adding, Updating, and Removing Dictionary Values
- Dictionary Loops
- Choosing the Right Collection
- Common Collection Operations
- Structured Data with Nested Collections
- Common Collection Errors

---

## Key Concepts

### Collections

Collections keep related values together.

The main collection types covered were:

- Lists
- Tuples
- Sets
- Dictionaries

### Lists

Lists store ordered and changeable values.
```python
fruits = ["apple", "banana", "orange"]
```

### Indexing

Indexes are used to select one item by position.
```python
print(fruits[0])
```

### Modifying Lists

Lists can be changed after creation.
```python
fruits.append("mango")
fruits.insert(1, "grape")
```

### List Methods

Practiced common list methods such as:
```python
append()
insert()
remove()
pop()
sort()
```

These methods can add, remove, or reorder items.

### Loops with Collections

Loops can process every item in a collection.
```python
for fruit in fruits:
    print(fruit)
```

### enumerate()

enumerate() provides both the index and the item while looping.
```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### Nested Collections

A collection can contain other collections.
```python
students = [
    ["Sara", 90],
    ["Ali", 85]
]
```

### Tuples

Tuples store ordered values that should not change.
```python
coordinates = (10, 20)
```

### Unpacking

Unpacking assigns collection items to separate names.
```python
x, y = coordinates
```

### Sets

Sets store unique values only.
```python
numbers = {1, 2, 3}
```

Duplicate values are not stored more than once.

### Set Operations

Set operations can compare groups of values.

Examples include:
```python
union()
intersection()
difference()
```

### Dictionaries

Dictionaries connect unique keys to values.
```python
student = {
    "name": "Sara",
    "age": 20
}
```

### Updating Dictionaries

Dictionary values can be added or updated using keys.
```python
student["grade"] = 95
student["age"] = 21
```

Values can also be removed.
```python
student.pop("grade")
```

### Dictionary Loops

Dictionary loops can read keys and values.
```python
for key, value in student.items():
    print(key, value)
```

### Choosing the Right Collection

Choose a collection based on its behavior:

- List → ordered and changeable
- Tuple → ordered and should not change
- Set → unique values
- Dictionary → key-value pairs

### Common Operations

Some operations can be used across multiple collection types, such as:

- len()
- Membership with in
- Loops
- Indexing where supported

### Structured Data

Nested collections can be used to model structured records and more complex data.

### Common Collection Errors

Collection errors often reveal an incorrect assumption about the collection, such as:

- Using an invalid index
- Looking for a missing dictionary key
- Trying to modify a tuple
- Assuming sets preserve positional indexing
- Using the wrong collection type for the required behavior

---

## Lab

Completed hands-on Python labs covering lists, tuples, sets, dictionaries, nested collections, loops, and common collection operations.

The complete lab solution is available in the lab folder.

---

## Homework

No homework was assigned.

---

## Key Takeaways

- Learned the differences between lists, tuples, sets, and dictionaries.
- Practiced accessing and modifying collection items.
- Used loops and enumerate() with collections.
- Practiced tuple unpacking.
- Applied set operations to compare groups.
- Worked with dictionary keys and values.
- Learned how to choose a collection based on its behavior.
- Used nested collections to represent structured data.

---

Status: ✅ Completed
