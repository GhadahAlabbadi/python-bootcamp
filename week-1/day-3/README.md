# Week 1 - Day 3

## Overview

The third day focused on automation using PowerShell scripts, setting up Python projects, managing virtual environments, and working with Python packages using pip.

---

## Topics Covered

- Automation fundamentals
- PowerShell script files (`.ps1`)
- Running PowerShell scripts
- Scheduling scripts using Task Scheduler
- Writing a backup script
- Automating Python project setup
- Creating and managing virtual environments
- Package management using pip
- Freezing project dependencies

---

## Key Concepts

### Automation

Learned how repetitive tasks can be executed automatically using scripts instead of performing them manually each time.

### PowerShell Scripts

PowerShell commands can be saved inside a file with the .ps1 extension and executed as one script.

Example:
.\startupProject.ps1

Scripts can be:

- Run manually from the terminal
- Scheduled to run automatically using Windows Task Scheduler

### Backup Script

Learned how to write a PowerShell script that copies files and folders to a backup location.

Example:
Copy-Item ".\Documents\*" ".\Backup\" -Recurse

### Python Project Setup Script

Learned how a .ps1 script can automate Python project setup tasks, such as:

- Creating project folders
- Creating a virtual environment
- Activating the environment
- Installing packages
- Creating project files

### Virtual Environment

Created a virtual environment using:
python -m venv venv

Activated it using:
.\venv\Scripts\Activate.ps1

Deactivated it using:
deactivate

### Package Management with pip

Practiced common pip operations:
pip install requests
pip list
pip uninstall requests
pip install -r requirements.txt

### Freezing Dependencies

Saved the installed packages and their exact versions inside requirements.txt:
pip freeze > requirements.txt

This allows the same project environment to be recreated on another machine.

---

## Lab

Completed a practical lab involving:

- Writing and running PowerShell scripts
- Automating file backup
- Setting up a Python project using a script
- Creating and activating a virtual environment
- Installing and managing packages with pip
- Generating a requirements.txt file

---

## Homework

No homework was assigned for this session.

---

## Key Takeaways

- Learned how PowerShell scripts automate repetitive tasks.
- Understood how .ps1 files can be run manually or through Task Scheduler.
- Practiced creating isolated Python environments.
- Learned how to install, remove, and list Python packages.
- Understood how pip freeze records project dependencies and versions.

---

Status: ✅ Completed
