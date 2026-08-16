# Week 4 - Day 1

## Overview

The first day of Week 4 introduced Object-Oriented Programming (OOP) in Python. The session focused on classes, objects, attributes, methods, object state, and how data and behavior can be organized together.

---

## Topics Covered

- Objects and Related Data
- Classes
- Creating Objects
- `__init__`
- `self`
- Instance Attributes
- Class Attributes
- Instance Methods
- Changing Object State
- Returning Values from Methods
- Protecting Valid State
- `__str__`
- Independent Instance State
- Collections of Objects
- `type()` and `isinstance()`
- Class, Object, and Method Roles
- Public Attribute Access
- Organizing Data and Behavior with Classes
- Common OOP Errors

---

## Key Concepts

### Objects

Objects keep related data and behavior together.

An object can store information and also provide methods that work with that information.

### Classes

A class defines a reusable object type.

```python
class Student:
    pass
```

The class acts as a blueprint for creating objects.

### Creating Objects

Calling a class creates an object.

```python
student = Student()
```

Here, `student` is an instance of the `Student` class.

### `__init__`

`__init__` establishes the starting state of an object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

When an object is created, `__init__` initializes its data.

### `self`

`self` refers to the current object.

```python
class Student:
    def __init__(self, name):
        self.name = name
```

Here, `self.name` belongs to the specific object being created.

### Instance Attributes

Instance attributes belong to one specific object.

```python
student1 = Student("Sara")
student2 = Student("Omar")
```

Each object can keep its own independent attribute values.

### Class Attributes

Class attributes are shared defaults defined on the class.

```python
class Student:
    school = "Tuwaiq Academy"
```

All instances can access the class attribute unless it is overridden on a specific instance.

### Instance Methods

Instance methods define object behavior.

```python
class Student:
    def greet(self):
        print("Hello")
```

They usually use `self` to access the current object's data.

### Changing Object State

Methods can modify the state of an object.

```python
class Student:
    def update_score(self, score):
        self.score = score
```

### Returning Values from Methods

Methods can return results using `return`.

```python
class Student:
    def get_name(self):
        return self.name
```

### Protecting Valid State

Methods can validate changes before updating object data.

```python
class Student:
    def update_score(self, score):
        if 0 <= score <= 100:
            self.score = score
```

This helps keep the object in a valid state.

### `__str__`

`__str__` provides a readable description of an object.

```python
class Student:
    def __str__(self):
        return self.name
```

Then:

```python
print(student)
```

can display a meaningful description instead of the default object representation.

### Independent Instance State

Each instance keeps its own state.

```python
student1 = Student("Sara")
student2 = Student("Omar")
```

Changing `student1` does not automatically change `student2`.

### Collections of Objects

Objects can be stored inside collections.

```python
students = [
    Student("Sara"),
    Student("Omar")
]
```

This allows programs to manage groups of related objects.

### `type()` and `isinstance()`

These functions can identify object types.

```python
type(student)
```

and:

```python
isinstance(student, Student)
```

### Class, Object, and Method Roles

- **Class** – Defines the reusable object type.
- **Object** – An instance created from a class.
- **Method** – Defines behavior available to objects.

### Public Attribute Access

Attribute access is public by default in Python.

```python
print(student.name)
```

Attributes can generally be accessed directly unless a different design is used.

### Organizing Data and Behavior

A small class can keep related data and behavior together, making code easier to understand and maintain.

### Common OOP Errors

OOP errors often reveal a broken object boundary, such as:

- Putting unrelated responsibilities in one class
- Changing object data without validation
- Confusing class attributes with instance attributes
- Forgetting to use `self`
- Calling methods on the wrong object

---

## Lab

Completed a hands-on Python lab covering classes, objects, attributes, methods, object state, and basic OOP design.

The complete lab solution is available in the **lab** folder.

---

## Homework

No homework was mentioned for this session.

---

## Key Takeaways

- Learned how objects combine related data and behavior.
- Understood the difference between classes and objects.
- Used `__init__` to define starting object state.
- Learned how `self` refers to the current object.
- Distinguished between instance attributes and class attributes.
- Created instance methods that modify and return object data.
- Used methods to help maintain valid object state.
- Practiced using `__str__` for readable object descriptions.
- Learned that each instance keeps independent state.
- Stored objects inside collections.
- Used `type()` and `isinstance()` with objects.

---

**Status:** ✅ Completed
