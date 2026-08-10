# Week 3 - Day 1

## Overview

The first day of Week 3 focused on Python functions and how they help organize repeated logic into reusable, readable, and testable blocks of code.

---

## Topics Covered

- Functions and Reusable Behavior
- def and Function Calls
- Function Execution
- __name__ == "__main__"
- __init__
- __doc__
- Parameters and Arguments
- Positional Arguments
- Keyword Arguments
- Default Parameters
- return
- return vs print
- Functions and Calculations
- Functions Without return
- Docstrings
- Function Contracts
- Control Flow Inside Functions

---

## Key Concepts

### Functions

Functions turn repeated logic into reusable behavior and help reduce code duplication.

### Defining and Calling Functions

A function is created using def:
```python
def greet():
    print("Hello")
```

The function runs only when it is called:
```python
greet()
```

### Function Execution

Functions are defined first and executed only when called.

The session also introduced special Python names such as:
```python
__name__
__init__
__doc__
```

and the common execution check:
```python
if __name__ == "__main__":
``` ...

### Parameters

Parameters allow a function to receive data.
```python
def greet(name):
    print(name)
```

### Parameters vs Arguments

- Parameter — the variable defined in the function.
- Argument — the actual value passed when calling the function.

Example:
```python
def greet(name):   # name = parameter
    print(name)

greet("Sara")       # "Sara" = argument
```

### Positional Arguments

Positional arguments are matched to parameters based on their order.
```python
def student(name, age):
    print(name, age)

student("Sara", 20)
```

### Keyword Arguments

Keyword arguments are matched using parameter names.
```python
student(age=20, name="Sara")
```

### Default Parameters

Default parameters make some arguments optional.
```python
def greet(name="Guest"):
    print(name)
```

### return

The return statement sends a result back to the caller.
```python
def add(a, b):
    return a + b
```

### return vs print

return sends a value back to the caller, while print() only displays output.
```python
def add(a, b):
    return a + b
```

### Functions Package Calculations

Functions can hide calculations behind clear and descriptive names.
```python
def calculate_total(price, quantity):
    return price * quantity
```

### Functions Without return

A function that does not explicitly use return produces:
None

### Docstrings

Docstrings describe what a function does or promises to provide.
```python
def calculate():
    """Calculate and return the result."""
```

A function's docstring can be accessed using:
```python
calculate.__doc__
```

### Clear Function Design

Clear functions are easier to:

- Read
- Reuse
- Test
- Maintain

### Function Contracts

Function errors often occur when the caller does not follow the expected contract, such as:

- Missing arguments
- Too many arguments
- Incorrect argument types
- Incorrect assumptions about the returned value

### Control Flow Inside Functions

Functions can contain the control flow concepts learned previously, including:

- if
- elif
- else
- for
- while

---

## Lab

Completed a hands-on Python lab covering function creation, parameters, arguments, default values, return values, docstrings, and control flow inside functions.

The complete lab solution is available in the lab folder.

---

## Homework

No homework was mentioned for this session.

---

## Key Takeaways

- Learned how functions make code reusable and organized.
- Distinguished between parameters and arguments.
- Practiced positional, keyword, and default arguments.
- Understood the difference between return and print.
- Learned that functions without an explicit return value produce None.
- Used docstrings to document function behavior.
- Applied previously learned control flow inside functions.

---

Status: ✅ Completed
