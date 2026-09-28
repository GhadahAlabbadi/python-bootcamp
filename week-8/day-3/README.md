# Week 8 - Day 3

## Overview

Today focused on the foundations of relational databases and how Django applications store persistent data.

The lesson covered persistence, databases, DBMS and RDBMS concepts, relational tables, keys, relationships, constraints, data integrity, SQL operations, transactions, and how Django connects to relational databases through Models and the ORM.

---

## Topics Covered

- Data Persistence
- Databases
- DBMS and RDBMS
- Relational Tables
- Rows, Columns, and Cells
- Primary Keys
- Foreign Keys
- Relationships Between Tables
- Database Constraints
- Data Integrity
- SQL CRUD Operations
- ACID Properties
- Concurrent Database Operations
- RDBMS vs Files and Spreadsheets
- Django Models and ORM
- Course Registration Database Design

---

## Key Concepts

### Persistence

Data stored only in Python memory is temporary and disappears when the running process stops.

Persistent database storage allows records to remain available after:

- Requests finish
- The server restarts
- The application restarts

Persistence allows multiple users to work with the same stored source of data.

---

### Database, DBMS, and RDBMS

**Database**
- An organized collection of persistent data.
- Examples include student records, orders, and support tickets.

**DBMS**
- Database Management System.
- Software responsible for creating, reading, updating, protecting, and coordinating access to databases.

Examples:
- PostgreSQL
- MySQL
- SQLite

**RDBMS**
- Relational Database Management System.
- Stores related data in tables.
- Uses relationships, keys, and constraints.

---

### Relational Table Structure

A relational table represents one type of entity.

Important parts:

- **Column** — one attribute shared by records.
- **Row** — one complete record.
- **Cell** — one value at the intersection of a row and column.

Example student table fields:

- `student_id`
- `name`
- `email`
- `program`

---

### Primary Keys

A **Primary Key (PK)** uniquely identifies one row inside its table.

Properties:

- Must be unique.
- Cannot be missing.
- Allows other tables to safely reference the record.

Example:

`student_id`

---

### Foreign Keys

A **Foreign Key (FK)** stores the primary key of a related record.

It connects tables without duplicating all the related data.

Example:

An enrollment record can contain:

- `student_id`
- `course_id`

These values connect the enrollment to a student and a course.

---

### Relationships Between Tables

The lesson used three related entities:

**STUDENTS**
- `student_id` PK
- name
- email

**ENROLLMENTS**
- `enrollment_id` PK
- `student_id` FK
- `course_id` FK
- `enrolled_at`

**COURSES**
- `course_id` PK
- title
- capacity

One student can have many enrollments.

One course can also have many enrollments.

---

### Database Constraints

Constraints protect the database from invalid records.

Important constraints:

- **PRIMARY KEY** — gives every row a unique identity.
- **FOREIGN KEY** — requires the referenced record to exist.
- **UNIQUE** — prevents duplicate values.
- **NOT NULL** — prevents required values from being missing.
- **CHECK** — requires a value to satisfy a condition.

---

### Data Integrity

Data integrity means stored data remains accurate, valid, and internally consistent.

Three types discussed:

**Entity Integrity**
- Every row must have a valid and unique identity.

**Referential Integrity**
- Relationships must point to existing records.

**Domain Integrity**
- Values must follow the allowed type and rules.

---

### SQL Operations

Relational databases use SQL operations to work with stored data.

| Operation | Purpose | SQL |
|---|---|---|
| Create | Add a new record | `INSERT` |
| Read | Retrieve existing records | `SELECT` |
| Update | Change stored values | `UPDATE` |
| Delete | Remove records | `DELETE` |

Django later generates SQL through the ORM.

---

### ACID Properties

Database transactions use four important guarantees:

**Atomicity**
- All steps succeed together or none remain.

**Consistency**
- Completed transactions keep the database within its rules.

**Isolation**
- Concurrent transactions do not corrupt each other's work.

**Durability**
- Committed changes survive crashes and restarts.

---

### Concurrent Requests

The DBMS coordinates competing database changes.

Example:

Two students attempt to reserve the final seat in a course at the same time.

The database transaction:

- Checks the current capacity.
- Applies one valid reservation.
- Rejects or retries the conflicting change.
- Prevents overbooking.

---

### Files vs Spreadsheets vs RDBMS

An RDBMS provides stronger support for:

- Multiple users writing simultaneously
- Relationships between records
- Centralized constraints
- Safe concurrent changes
- Complex searching and joining

An RDBMS is useful when an application depends on shared, related, and trustworthy data.

---

### Where Django Fits

The application flow is:

**Browser → View → Model and ORM → RDBMS → Database**

Django Models describe data using Python.

The Django ORM translates Python operations into database operations.

The RDBMS still manages the underlying stored data, rules, and queries.

> The ORM simplifies database work, but it does not remove the database underneath it.

---

## Guided Lab: Course Registration Database

The guided lab focused on designing the database structure before writing Django model code.

### Tasks

1. Identify the `Student`, `Course`, and `Enrollment` entities.
2. Give each entity a primary key.
3. Add three useful attributes to Student and Course.
4. Decide which foreign keys belong in Enrollment.
5. Define the relationship between Student and Enrollment.
6. Define the relationship between Course and Enrollment.
7. Add one `UNIQUE` rule and one `NOT NULL` rule.
8. Draw the three tables and connect their keys.

---

## Key Takeaways

- Application variables are temporary, while databases provide persistent storage.
- A DBMS manages database access and operations.
- An RDBMS organizes related data using tables, keys, relationships, and constraints.
- Primary keys identify records.
- Foreign keys connect related tables.
- Constraints help maintain valid data.
- Data integrity keeps database records accurate and consistent.
- SQL supports Create, Read, Update, and Delete operations.
- ACID properties make database transactions reliable.
- Django Models and the ORM provide a Python layer for communicating with an RDBMS.
- Good database design should be understood before translating the structure into Django models.

---

**Status:** ✅ Completed
