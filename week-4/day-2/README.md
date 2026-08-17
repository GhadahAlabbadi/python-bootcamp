# Week 4 - Day 2

## Overview

The second day of Week 4 introduced **File Handling – Part 1** in Python, focusing on how programs can preserve data beyond a single run and safely read, write, and append text files.

---

## Topics Covered

- Files and Persistent Program State
- `Path` Objects
- Inspecting Paths
- File Modes
- `with` Statement
- Reading Complete Text Files
- Iterating Over File Lines
- Writing Files
- Appending Files
- UTF-8 Encoding
- Newline Handling

---

## Key Concepts

### Files Preserve Program State

Files allow program data to remain available even after the program stops running.

### Path Objects

`Path` objects help build and manage file and folder locations.

```python
from pathlib import Path

file_path = Path("data") / "students.txt"
```

### Inspecting Paths

Paths can be checked before they are used.

```python
file_path.exists()
file_path.is_file()
file_path.is_dir()
```

### File Modes

Common file modes include:

- `"r"` – Read
- `"w"` – Write
- `"a"` – Append

### `with` Statement

The `with` statement automatically closes the file after the block finishes.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

### Reading Complete Text

Small files can be read completely at once.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

### Iterating Over Lines

Files can be processed one line at a time without loading the entire file into memory.

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line)
```

### Writing Files

Write mode replaces the existing content of a file.

```python
with open("data.txt", "w") as file:
    file.write("New content")
```

### Appending Files

Append mode preserves existing content and adds new content at the end.

```python
with open("data.txt", "a") as file:
    file.write("More content")
```

### UTF-8 and Newlines

UTF-8 helps keep text encoding predictable across systems.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Newline handling helps keep text files consistent and readable.

---

## Lab

Completed a Python lab covering the file handling concepts introduced during the session.

The complete lab solution is available in the **lab** folder.

---

## Homework

No homework was assigned.

---

## Key Takeaways

- Learned how files preserve data between program runs.
- Used `Path` objects to manage file locations.
- Practiced checking paths before using them.
- Learned common file modes.
- Used `with` for safe file handling.
- Read complete files and processed files line by line.
- Practiced writing and appending text.
- Used UTF-8 encoding for predictable text handling.

---

**Status:** ✅ Completed
