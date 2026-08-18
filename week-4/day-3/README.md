# Week 4 - Day 3

## Overview

The third day of Week 4 continued **File Handling & Exception Management – Part 2** in Python, focusing on structured file formats, exception handling, raising errors, and creating custom exceptions.

---

## Topics Covered

- CSV Files
- JSON Files
- `try` and `except`
- Specific Exception Handling
- `else`
- `finally`
- Exception Flow
- `raise`
- Custom Exceptions
- Common File Handling Failures

---

## Key Concepts

### CSV Stores Rows and Columns

CSV files store structured data in rows and columns.

Example:

```text
name,age,course
Sara,22,Python
Omar,24,Django
```

Python's `csv` module can be used to read and write CSV files.

```python
import csv
```

### JSON Preserves Lists and Dictionaries

JSON is commonly used to store structured data similar to Python lists and dictionaries.

Example:

```json
{
  "name": "Sara",
  "age": 22,
  "courses": ["Python", "Django"]
}
```

Python's `json` module can convert between Python objects and JSON data.

```python
import json
```

### `try` and `except`

`try` and `except` define what should happen when an operation may fail.

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
```

The `try` block contains the operation that may fail, while `except` handles the expected error.

### Catch Specific Exceptions

It is better to catch the specific exception that is expected.

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

This makes error handling clearer and more predictable.

### `else`

The `else` block runs only when no exception occurs.

```python
try:
    number = int("10")
except ValueError:
    print("Invalid value")
else:
    print(number)
```

### `finally`

The `finally` block runs whether an exception occurs or not.

```python
try:
    print("Trying...")
except Exception:
    print("Error")
finally:
    print("Finished")
```

### Exception Blocks Have Different Jobs

Each block has a specific role:

- `try` – Code that may fail
- `except` – Handles an expected failure
- `else` – Runs when no exception occurs
- `finally` – Runs regardless of success or failure

### `raise`

`raise` is used to reject invalid data immediately by creating an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

### Custom Exceptions

Custom exceptions can be created to represent application-specific failures.

```python
class InvalidScoreError(Exception):
    pass
```

Then:

```python
score = 150

if score > 100:
    raise InvalidScoreError("Score must be between 0 and 100")
```

Custom exceptions make domain-specific errors clearer.

### Common File Handling Failures

File code often fails when assumptions about files or data are not checked.

Common examples include:

- File does not exist
- Invalid file path
- Incorrect file mode
- Invalid CSV structure
- Invalid JSON data
- Unexpected data types
- Missing required values

Validating assumptions and handling specific exceptions makes file operations safer and easier to debug.

---

## Lab

Completed a hands-on Python lab covering CSV, JSON, exception handling, raising exceptions, and custom exceptions.

The complete lab solution is available in the **lab** folder.

---

## Homework

No homework was assigned.

---

## Key Takeaways

- Learned how CSV stores tabular data.
- Learned how JSON preserves structured lists and dictionaries.
- Used `try` and `except` to handle expected failures.
- Practiced catching specific exceptions.
- Understood the roles of `else` and `finally`.
- Used `raise` to reject invalid data.
- Created custom exceptions for domain-specific failures.
- Learned how hidden assumptions can cause file handling errors.

---

**Status:** ✅ Completed
