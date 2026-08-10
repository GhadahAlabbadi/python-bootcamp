# Week 3 - Day 2

## Overview

The second day of Week 3 focused on Python namespaces, scopes, name lookup rules, modules, imports, and package-related concepts.

---

## Topics Covered

- Names and Objects
- Namespaces
- Python Scopes
- LEGB Rule
- Local Scope
- Enclosing Scope
- Global Scope
- Built-in Scope
- Shadowing
- Shared State
- Modules
- import
- from ... import
- Import Aliases
- Python Standard Library
- Creating Custom Modules
- Main Guard
- Modules, Packages, and Dependencies
- Common Import Errors

---

## Key Concepts

### Names and Namespaces

Names in Python refer to objects stored within a namespace.

The same name can exist in different scopes without necessarily referring to the same object.

### Function Local Namespace

Each function call creates a fresh local namespace.
```python
def greet():
    message = "Hello"
    print(message)
```

The variable message belongs to that specific function call.

### LEGB Rule

Python searches for names using the LEGB lookup order:

1. Local
2. Enclosing
3. Global
4. Built-in

### Local Scope

Local scope belongs to the current function call.
```python
def test():
    value = 10
```

value exists inside the function.

### Enclosing Scope

Enclosing scope appears when functions are nested inside other functions.
```python
def outer():
    message = "Hello"

    def inner():
        print(message)
```

The inner function can access names from the enclosing function.

### Global Scope

Global scope belongs to the current Python module.
```python
name = "Python"
```

A name defined outside functions belongs to the module's global scope.

### Built-in Scope

Built-in scope provides standard Python names such as:
```python
print()
len()
range()
```

### Shadowing

Shadowing happens when an inner scope defines a name that already exists in an outer scope.
```python
name = "Global"

def test():
    name = "Local"
    print(name)
```

The local name hides the global name inside the function.

### Shared State

Shared state should be used deliberately because changing shared values can affect different parts of a program.

### Modules

Modules help organize related code into separate Python files.

For example:
```text
main.py
calculator.py
```

### Importing Modules

A module can be imported using:
```python
import math
```

### from import

from ... import brings selected names from a module into the current scope.
```python
from math import sqrt
```

### Import Aliases

Aliases make long module names or conflicting names easier to use.
```python
import datetime as dt
```

### Standard Library

Python provides many ready-made modules through its standard library.

Examples include:
math
random
datetime

### Custom Modules

Your own Python file can also become a module.

For example:
```text
calculator.py
```

can be imported from another Python file:
import calculator

### Main Guard

The main guard separates code that should run directly from code that should only be available when imported.
```python
if __name__ == "__main__":
    main()
```

### Module, Package, and Dependency

- Module — A Python file containing code.
- Package — A collection of related Python modules.
- Dependency — External code or packages that a project relies on.

### Import Errors

Import errors usually have traceable causes such as:

- Incorrect module name
- Incorrect file location
- Missing package
- Naming conflicts
- Incorrect import syntax

---

## Lab

Completed hands-on Python labs covering namespaces, scopes, the LEGB rule, modules, imports, aliases, and module organization.

The complete lab solution is available in the lab folder.

---

## Homework

No homework was mentioned for this session.

---

## Key Takeaways

- Learned how Python names refer to objects inside namespaces.
- Understood Python's LEGB name lookup order.
- Distinguished between local, enclosing, global, and built-in scopes.
- Learned how shadowing affects name lookup.
- Practiced organizing code using modules.
- Used different forms of Python imports.
- Learned how custom Python files can become modules.
- Understood the purpose of the main guard.
- Reviewed common causes of import errors.

---

Status: ✅ Completed
