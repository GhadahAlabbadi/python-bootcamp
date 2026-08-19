# Week 4 - Day 4

## Overview

The fourth day of Week 4 focused on practical Object-Oriented Programming exercises and reviewing previously learned Python concepts through a roadmap activity.

The session was mainly hands-on, with no new presentation topics introduced.

---

## Topics Covered

- Object-Oriented Programming Practice
- Private Attributes
- Name Mangling
- `@property`
- Property Setters
- Object State
- Inheritance
- Parent and Child Classes
- `super()`
- Inherited Methods
- Python Learning Roadmap Review

---

## Key Concepts

### Private Attributes

Used double underscores to create attributes intended for internal class use.

```python
self.__enrolled = True
```

Python applies name mangling to attributes that begin with double underscores.

### `@property`

Used `@property` to provide controlled access to an internal attribute.

```python
@property
def enrolled(self):
    return self.__enrolled
```

This allows:

```python
student.enrolled
```

instead of calling a regular method.

### Property Setter

Used a property setter to control changes to an attribute.

```python
@enrolled.setter
def enrolled(self, _):
    self.__enrolled = not self.__enrolled
```

The setter toggles the enrollment state between `True` and `False`.

### Object State

The `Student` class stores and manages data such as the student's name, scores, and enrollment status.

### Calculated Properties

Used `@property` to expose a calculated value.

```python
@property
def average(self):
    if not self.score:
        return 0
    return sum(self.score) / len(self.score)
```

This allows:

```python
student.average
```

### Inheritance

Practiced inheritance by creating a child class from a parent class.

```python
class Food:
    pass

class Fruits(Food):
    pass
```

The child class can reuse behavior defined in the parent class.

### `super()`

Used `super()` to call the parent class constructor.

```python
class Fruits(Food):
    def __init__(self, name, cal):
        super().__init__(name)
        self.cal = cal
```

### Inherited Methods

Methods defined in the parent class can also be used by objects created from the child class.

---

## Lab

Completed practical Object-Oriented Programming exercises covering:

- Properties and setters
- Private attributes
- Object state
- Inheritance
- `super()`
- Inherited methods

The complete lab code is available in the **lab** folder.

---

## Activity

Created a Python learning roadmap covering the concepts learned from Week 2 through Week 4.

---

## Homework

Debugged and improved the OOP code practiced during the session.

---

## Key Takeaways

- Practiced controlling object state using properties.
- Used private attributes and name mangling.
- Applied property setters.
- Practiced inheritance between Python classes.
- Used `super()` to reuse parent class initialization.
- Reinforced previously learned Python concepts through a roadmap activity.

---

**Status:** ✅ Completed
