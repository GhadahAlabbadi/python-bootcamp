# Week 2 - Day 2

## Overview

The second day of Week 2 focused on Python variables, data types, indentation, references, user input, and basic decision making. We also practiced writing Python programs in Visual Studio Code and attended an academy session about improving technical interview performance.

---

## Topics Covered

- Python Reads Structure, Not Intention
- Indentation Defines Code Blocks
- Variable Naming Rules
- Variables Store References to Values
- Python Data Types
- User Input
- Type Conversion
- isinstance()
- type()
- String Indexing
- f-Strings
- Constants
- Input Validation

---

## Key Concepts

### Python Reads Structure, Not Intention

Python executes code based on its syntax and indentation rather than the programmer's intention.

### Indentation Defines Code Blocks

Python uses indentation to determine which statements belong to the same code block.

Example:
if score >= 90:
    print("Excellent")
else:
    print("Thank you")

---

### Variable Naming Rules

A valid variable name:

- Starts with a letter or underscore (`_`)
- Cannot start with a number
- Cannot contain spaces
- Cannot use Python keywords

Example:
student_name = "Sara"
student_age = 20

---

### Variables Store References to Values

Variables reference objects in memory rather than storing the actual values.

Example:
x = 10
y = x

Both variables refer to the same value.

---

### Python Data Types

Practiced working with:

- String (`str`)
- Integer (`int`)
- Boolean (`bool`)

Examples:
student_name = "Nasser"
student_age = 24
registered = True

---

### Checking Data Types

Used:
type(variable)

Example:
print(type(student_age))

---

### isinstance()

Checked whether an object belongs to a specific type.

Example:
isinstance(student_age, int)

---

### User Input

Used:
age = input("Enter your age: ")

Since input() returns a string, it was converted to an integer when performing calculations.
int(age)

---

### f-Strings

Used formatted strings to display variables.

Example:
print(f"""
Welcome {student_name}
You are {student_age}
""")

---

### Constants

Constants were represented using uppercase variable names.

Example:
MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15

---

### String Indexing

Accessed characters in a string using indexes.

Example:
teacher_name[index]

Input validation was used to avoid index out-of-range errors.

---

## Practice

Completed hands-on practice covering:

- Variables
- Data types
- if / else statements
- User input
- Type conversion
- isinstance()
- type()
- String indexing
- f-strings

The practice code is available in the lab folder.

---

## Academy Session

Attended an academy session:

How to Showcase Your Skills in Technical Interviews and Assessments

Speaker: Mohammed Al-Munajjem

The session discussed practical tips for presenting technical skills effectively during interviews and technical assessments.

---

## Homework

### Research Task

Research how to swap two variables without using a third variable.

Example:
x = 0
y = 1

x, y = y, x

---

## Key Takeaways

- Learned how Python relies on structure and indentation.
- Practiced working with variables and data types.
- Used type() and isinstance() for type checking.
- Learned how input() works and why type conversion is necessary.
- Practiced string indexing and formatted output using f-strings.
- Learned techniques for presenting technical skills during interviews.

---

Status: ✅ Completed
