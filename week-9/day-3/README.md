# Week 9 - Day 3

## Overview

Today focused on **Django model relationships** and how relational database relationships are represented using Django model fields.

The lesson covered **ForeignKey**, **OneToOneField**, and **ManyToManyField**, along with relationship placement, reverse access, deletion behavior, optional relationships, join tables, intermediary models, and self-referencing relationships.

---

## Topics Covered

- Relationship cardinality in Django
- `ForeignKey`
- `OneToOneField`
- `ManyToManyField`
- Relationship field placement
- Forward and reverse relationship access
- `related_name`
- `on_delete` behavior
- Required and optional relationships
- Automatic many-to-many join tables
- Many-to-many relationships using `through`
- Self-referencing relationships
- Common relationship design mistakes
- Guided Lab: Online Store relationships

---

## Key Concepts

### Relationship Types

Django relationship fields are selected based on the business relationship between models.

| Relationship | Django Field | Example |
|---|---|---|
| One-to-Many | `ForeignKey` | One Author → Many Books |
| One-to-One | `OneToOneField` | One User → One Profile |
| Many-to-Many | `ManyToManyField` | Many Students ↔ Many Courses |

Relationships can also be:

- **Required** — the related object must exist.
- **Optional** — the object may exist without the relationship.

---

### ForeignKey

A `ForeignKey` represents a **many-to-one relationship**.

The field belongs on the **many side** of the relationship.

Example:

```python
class Author(models.Model):
    name = models.CharField(max_length=120)


class Book(models.Model):
    title = models.CharField(max_length=180)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )
```

Here:

- Many `Book` records can reference one `Author`.
- Django stores `author_id` in the Book table.

#### Forward Access

```python
book.author
```

Returns the related Author.

#### Reverse Access

```python
author.books.all()
```

Returns all books connected to that author.

---

### Where the Relationship Field Belongs

Relationship placement should make the database structure and domain meaning clear.

#### ForeignKey

Place the field on the **many side**.

Example:

```text
Author 1 ──── * Book
```

The `Book` model stores the reference to `Author`.

#### OneToOneField

Usually place it on the dependent or extension model.

Example:

```text
User 1 ──── 1 Profile
```

The Profile stores the reference to User.

#### ManyToManyField

Place it on the side that makes the model API easiest to understand.

Django stores the actual links in a separate join table.

---

### `related_name`

`related_name` defines how the relationship is accessed from the reverse side.

Example:

```python
author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE,
    related_name="books"
)
```

Then:

```python
author.books.all()
```

Clear reverse names are preferred over Django's default names such as:

```python
book_set
```

---

### Deletion Behavior with `on_delete`

Every `ForeignKey` and `OneToOneField` must define what happens when the referenced object is deleted.

| Option | Behavior |
|---|---|
| `CASCADE` | Delete dependent records |
| `PROTECT` | Prevent deletion |
| `RESTRICT` | Block deletion while dependent references remain |
| `SET_NULL` | Keep the dependent record and set the relationship to `NULL` |
| `SET_DEFAULT` | Replace the relationship with a default value |

Example:

```python
author = models.ForeignKey(
    Author,
    on_delete=models.SET_NULL,
    null=True
)
```

`SET_NULL` requires the field to allow `NULL`.

---

### Required and Optional Relationships

`null` and `blank` control different things.

#### `null=True`

Controls database storage.

```python
null=True
```

means the database may store no referenced object.

#### `blank=True`

Controls Django validation.

```python
blank=True
```

means forms and model validation may accept the relationship as empty.

Example:

```python
author = models.ForeignKey(
    Author,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="books"
)
```

Optional relationships should be based on the actual business requirements.

---

### OneToOneField

`OneToOneField` allows at most one related row on each side.

Example:

```python
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)
```

This is useful when one model extends another model.

#### Access

From Profile:

```python
profile.user
```

From User:

```python
user.profile
```

A one-to-one relationship enforces uniqueness between the two records.

---

### ForeignKey vs OneToOneField

Use `ForeignKey` when one parent can have several children.

```text
Author → many Books
```

Use `OneToOneField` when one parent can have only one dependent record.

```text
User → one Profile
```

The relationship name alone does not enforce cardinality. The selected Django field does.

---

### ManyToManyField

`ManyToManyField` represents relationships where many records on both sides can be connected.

Example:

```python
class Course(models.Model):
    title = models.CharField(max_length=150)


class Student(models.Model):
    name = models.CharField(max_length=120)

    courses = models.ManyToManyField(
        Course,
        related_name="students",
        blank=True
    )
```

#### Student Side

```python
student.courses.all()
```

Returns the courses joined by the student.

#### Course Side

```python
course.students.all()
```

Returns the students enrolled in the course.

---

### Automatic Join Table

Django automatically creates a join table for a normal many-to-many relationship.

Conceptually:

```text
Student
-------
id
name

        ↓

student_courses
---------------
id
student_id
course_id

        ↓

Course
------
id
title
```

Each row in the join table represents one relationship between a Student and a Course.

Use the automatic join table when the relationship itself has **no additional business data**.

---

### Many-to-Many with `through`

If the relationship itself needs additional information, create an explicit intermediary model.

Example:

```python
class Course(models.Model):
    title = models.CharField(max_length=150)

    students = models.ManyToManyField(
        "Student",
        through="Enrollment",
        related_name="courses"
    )


class Enrollment(models.Model):
    student = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    joined_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)
```

Here, `Enrollment` stores information about the relationship itself:

- student
- course
- joined date
- status

Common examples of intermediary models include:

- Enrollment
- OrderItem
- Membership
- Assignment
- Follow

---

### Self-Referencing Relationships

A model can reference another record of the same model.

Example:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )
```

This creates a hierarchy.

A category may have:

- one parent
- many child categories

#### Access

```python
category.parent
```

```python
category.children.all()
```

A top-level category can have:

```python
parent = NULL
```

---

### Choosing the Correct Relationship Field

| Business Relationship | Django Field |
|---|---|
| Many children → one parent | `ForeignKey` |
| One dependent → one parent | `OneToOneField` |
| Many records on both sides | `ManyToManyField` |
| Many-to-many with relationship data | `ManyToManyField` with `through` |
| Hierarchy inside one model | `ForeignKey("self")` |

The general process is:

1. Determine the relationship cardinality.
2. Choose the Django relationship field.
3. Decide whether the relationship is required or optional.
4. Choose the correct `on_delete` behavior.
5. Give reverse relationships clear names.

---

### Common Relationship Mistakes

#### ForeignKey on the Wrong Side

The `ForeignKey` should normally be placed on the many side.

#### Using `CASCADE` Automatically

`CASCADE` should only be used when deleting the parent should logically delete its dependent records.

#### `SET_NULL` Without `null=True`

Django cannot clear a relationship if the database column does not allow `NULL`.

#### Unclear Reverse Names

Default names such as:

```python
book_set
```

may hide the business meaning.

Use meaningful `related_name` values.

#### Storing IDs as Text

Storing comma-separated IDs in a text field breaks relational structure and database integrity.

Use Django relationship fields instead.

#### Missing a `through` Model

If a relationship has information such as:

- quantity
- joined date
- status
- unit price

that information should usually belong to an intermediary model.

---

## Guided Lab: Model an Online Store

The lab translated online-store requirements into Django model relationships.

### Requirements

1. `Category` has an optional parent `Category`.
2. `Product` belongs to one `Category`.
3. `User` has one `CustomerProfile`.
4. `Order` belongs to one `User`.
5. `Order` connects to many `Product` records through `OrderItem`.
6. `OrderItem` stores:
   - quantity
   - unit price
7. Add meaningful `related_name` values to every relationship.
8. Choose and justify the correct `on_delete` behavior for each relationship.

The lab combined:

- self-referencing relationships
- one-to-many relationships
- one-to-one relationships
- many-to-many relationships with `through`

---

## Key Takeaways

- Relationship **cardinality** determines which Django relationship field to use.
- `ForeignKey` represents many-to-one relationships.
- `OneToOneField` enforces one related object on each side.
- `ManyToManyField` uses a join table to connect records.
- Use `through` when the relationship itself contains business data.
- `related_name` provides clear reverse access to related objects.
- `on_delete` should reflect the real business rules.
- `null=True` controls database optionality, while `blank=True` controls validation optionality.
- Self-referencing relationships are useful for hierarchical data.
- Correct relationship design helps preserve relational structure and data integrity.

---

**Status:** ✅ Completed
