# Week 8 - Day 4

## Overview

Today focused on **relational database design**, starting from business requirements and transforming them into entities, attributes, relationships, keys, cardinalities, and an Entity Relationship Diagram (ERD).

The lesson also covered **normalisation** and how good database design reduces duplicated and inconsistent data.

---

## Topics Covered

- Business requirements
- Entities, attributes, and records
- Choosing stable primary keys
- Relationships between entities
- Cardinality and optionality
- One-to-one relationships
- One-to-many relationships
- Many-to-many relationships
- Linking entities
- Entity Relationship Diagrams (ERDs)
- Database normalisation
- Update, insert, and delete anomalies
- First, Second, and Third Normal Forms

---

## Key Concepts

### From Requirements to Database Design

A relational database should begin with understanding the business requirements.

The general design process is:

```text
Requirements
    ↓
Entities
    ↓
Attributes
    ↓
Relationships
    ↓
ERD
```

The main rule is:

> Understand the business first, then design the data structure.

---

### Business Requirements

Requirements describe what the system needs to remember and what rules it must enforce.

Example:

```text
A training platform registers students on courses.
Each course has a capacity.
The platform records enrollment date and status.
A student may join several courses.
```

From this description we can identify:

- Entities: Student, Course, Enrollment
- Attributes: capacity, enrollment date, status
- Business rules: students may join several courses

---

### Entity, Attribute, and Record

**Entity**

A type of object the system stores.

Example:

```text
Student
```

**Attribute**

A fact that describes an entity.

Examples:

```text
name
email
date_of_birth
```

**Record**

One specific instance of an entity.

Example:

```text
Student 101
Maha
maha@example.com
```

In a relational database:

```text
Entity     → Table
Attribute  → Column
Record     → Row
```

---

### Choosing Entities

A concept is a strong candidate for its own entity when:

- The system stores several instances of it
- Each instance needs its own identity
- It has several attributes
- Other records need to reference it
- It has its own lifecycle

A simple descriptive value is usually an **attribute** instead of a separate entity.

Examples:

```text
Course title   → Attribute
Student email  → Attribute
```

---

### Stable Primary Keys

A primary key should uniquely identify a record and remain stable even when descriptive information changes.

Good example:

```text
student_id
```

Less suitable example:

```text
email
```

An email may change, while `student_id` can remain the same.

The email can still use a `UNIQUE` constraint.

---

### Cardinality and Optionality

Relationships must describe both:

- How many related records are allowed
- Whether the relationship is optional

Common cardinalities:

```text
1       Exactly one
0..1    Zero or one
0..*    Zero or many
1..*    One or many
```

Examples:

```text
Enrollment → Student
Exactly one

User → Profile
Zero or one

Course → Enrollment
Zero or many

Order → Order Item
One or many
```

---

### Relationship Types

#### One-to-One

One record relates to one other record.

Example:

```text
Patient ↔ Medical Profile
```

A patient may have zero or one medical profile.

---

#### One-to-Many

One record may relate to many records.

Example:

```text
Patient → Appointments
Doctor  → Appointments
```

A patient may have many appointments.

Each appointment belongs to exactly one patient.

---

#### Many-to-Many

A many-to-many relationship is usually resolved using a linking entity.

Example:

```text
Student
   ↓
Enrollment
   ↑
Course
```

`Enrollment` can contain:

```text
enrollment_id
student_id
course_id
status
enrolled_at
```

This converts one many-to-many relationship into two one-to-many relationships.

---

### Entity Relationship Diagram (ERD)

An **ERD** visually represents the proposed database structure.

It can show:

- Entities
- Attributes
- Primary Keys (PK)
- Foreign Keys (FK)
- Relationships
- Cardinalities
- Optionality

Example:

```text
COURSE
----------------
course_id PK
title
capacity
instructor_id FK

        many
         |
         |
         | one

INSTRUCTOR
----------------
instructor_id PK
name
email UNIQUE
```

---

### Practical Database Modelling Sequence

A useful design process is:

1. Read the requirements
2. Identify entities
3. Assign attributes
4. Choose stable keys
5. Define relationships and cardinalities
6. Test the model against normal and edge cases

---

## Normalisation

Normalisation reduces repeated information and prevents inconsistent copies of the same fact.

Poorly designed tables can create three common problems.

### Update Anomaly

The same information appears in several rows.

If one copy is changed but another is missed, the data becomes inconsistent.

---

### Insert Anomaly

Some information cannot be stored without also storing unrelated information.

Example:

A course cannot be stored until a student enrolls if everything exists in one enrollment table.

---

### Delete Anomaly

Deleting one record accidentally removes other useful information.

Example:

Deleting the last enrollment could also remove the only stored information about a course.

---

## Normal Forms

### First Normal Form — 1NF

- Keep one value in each cell
- Avoid repeated columns
- Give each row a stable identity

Avoid structures such as:

```text
course_1
course_2
course_3
```

---

### Second Normal Form — 2NF

When using a combined key, every non-key attribute should describe the entire key.

Facts that describe only part of the key should move to the correct table.

---

### Third Normal Form — 3NF

Non-key attributes should describe the record itself.

If a fact actually describes another entity, move it into that entity's table.

A practical rule:

> Store each fact once under the entity it truly describes.

---

## Exercises

### Exercise 1 — From Requirements to Entities

Clinic scenario:

```text
A clinic schedules appointments between patients and doctors.
Each patient has a name, phone number, and date of birth.
Each doctor has a name and speciality.
An appointment records its date, time, and status.
A patient may book several appointments.
```

Entities:

```text
Patient
Doctor
Appointment
```

Patient attributes:

```text
name
phone_number
date_of_birth
```

Doctor attributes:

```text
name
speciality
```

Appointment attributes:

```text
date
time
status
```

---

### Exercise 2 — Keys, Relationships, and ERD

Stable primary keys:

```text
patient_id
doctor_id
appointment_id
profile_id
```

Foreign keys:

```text
Appointment → patient_id
Appointment → doctor_id
MedicalProfile → patient_id
```

Relationships:

```text
Patient → Medical Profile     0..1

Patient → Appointment         0..*

Doctor → Appointment          0..*

Appointment → Patient         exactly 1

Appointment → Doctor          exactly 1
```

Relationship types:

```text
Patient ↔ Medical Profile
One-to-one

Patient → Appointment
One-to-many

Patient ↔ Doctor
Many-to-many through Appointment
```

---

### Exercise 3 — Normalise and Protect the Clinic Database

The clinic example demonstrated how duplicated information can create inconsistent values.

The task included:

- Identifying repeated information
- Finding inconsistent data
- Identifying update, insert, and delete anomalies
- Separating data into normalised entities
- Assigning attributes correctly
- Identifying primary and foreign keys
- Converting business rules into database constraints

Example business rules:

```text
Every patient must have a unique phone number.

Every appointment must belong to one patient and one doctor.

A patient cannot book the same doctor twice at the same date and time.

Appointment status must be:
Confirmed, Cancelled, or Completed.
```

---

## Key Takeaways

- Database design starts with business requirements.
- Entities represent concepts that need independent records.
- Attributes describe entities.
- Records are individual instances of entities.
- Primary keys should provide stable identities.
- Foreign keys connect related tables.
- Cardinality defines how many records may participate in a relationship.
- Many-to-many relationships can be resolved using linking entities.
- ERDs provide a visual representation of the database structure.
- Normalisation reduces duplicated data and prevents anomalies.
- Good relational design stores each fact once in the correct place.

---

**Status:** ✅ Completed
