# Week 2 - Day 1

## Overview

The first day of Week 2 focused on improving Python development practices by introducing code quality tools, virtual environments, package management, and the standard Python development workflow. The session also marked the beginning of Unit 1 Project, which is maintained in a dedicated GitHub repository.

---

## Topics Covered

- Linters and Automated Code Checking
- Ruff
- Pylint
- Flake8
- Virtual Environments
- Standard Library vs Third-Party Packages
- Typical Python Workflow
- Writing Python Code in Visual Studio Code
- Running Python Programs
- Checking Code Quality Using Flake8

---

## Key Concepts

### Linters

Linters automatically analyze source code to detect syntax errors, style issues, and potential bugs while helping developers write clean and consistent code that follows standards such as PEP 8.

### Ruff

A modern, lightweight, and fast Python linter used to identify code quality and style issues.
ruff check .

### Pylint

A comprehensive code analysis tool that detects errors, provides suggestions for improvement, and evaluates overall code quality.
pylint main.py

### Flake8

A lightweight linter that checks Python code for syntax errors and PEP 8 style violations.
flake8 main.py

### Virtual Environments

A virtual environment creates an isolated Python environment for each project, preventing dependency conflicts between projects.

Create a virtual environment:
python -m venv venv

Activate it:
.\venv\Scripts\Activate.ps1

Deactivate it:
deactivate

### Standard Library vs Third-Party Packages

The Python Standard Library includes modules that are installed with Python by default.

Examples:
import math
import random
import datetime

Third-party packages are external libraries that must be installed using pip.

Examples:
import requests
import django
import pandas

Install a package:
pip install requests

### Typical Python Workflow

The standard workflow followed in Python projects consists of four stages:

1. Setup
2. Dependencies
3. Development
4. Snapshot
Setup → Dependencies → Development → Snapshot

### Python Development in Visual Studio Code

Practiced writing a simple Python program, running it from the integrated terminal, and checking code quality using Flake8.
python main.py

---

## Practice

Completed hands-on practice that included:

- Writing a simple Python program
- Running Python code from the terminal
- Creating and activating a virtual environment
- Installing Python packages
- Checking code quality using Flake8

---

## Unit Project

Started Unit 1 Project by creating a dedicated GitHub repository.

The project includes:

- Python source code
- Project files
- Documentation
- Screenshots
- Git version history

The project is maintained in its own repository to keep this bootcamp portfolio focused on documenting the learning journey.

### Related Repository

🔗 Unit 1 Project

https://github.com/GhadahAlabbadi/project-unit1

---

## Key Takeaways

- Learned how linters improve Python code quality.
- Understood the differences between Ruff, Pylint, and Flake8.
- Practiced creating and managing virtual environments.
- Distinguished between Python Standard Library modules and third-party packages.
- Learned the standard Python development workflow.
- Started the Unit 1 Project in a dedicated GitHub repository.

---

Status: ✅ Completed

