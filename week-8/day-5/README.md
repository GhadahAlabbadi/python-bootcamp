# Week 8 - Day 5

## Django Models and Field Types

## Overview

Today focused on how Django models represent relational database structures using Python classes and model fields.

A Django model class represents a database table, model fields represent columns, model instances represent rows, and field values represent stored cells.

---

## Topics Covered

- Django `models.py`
- Django model classes
- Model fields and field types
- Field options
- `null` vs `blank`
- Text field types
- Boolean and date fields
- Decimal and integer fields
- UUID, JSON, image, and file fields
- Automatic primary keys
- `pk` alias
- `TextChoices`
- Model-to-table mapping

---

## Key Concepts

### Django Models

Models are defined inside the application's `models.py` file.

```python
from django.db import models
```

Each model class represents one entity from the relational design.

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
```

Conceptually:

- Model class → database table
- Model field → database column
- Model instance → table row
- Attribute value → stored cell

The application must also be included in `INSTALLED_APPS` so Django can discover its models.

---

### Choosing Field Types

The field type should match the meaning and expected structure of the data.

Common field types covered:

- `CharField` → short or limited text
- `TextField` → long text
- `SlugField` → URL-friendly text
- `EmailField` → email values
- `URLField` → URL values
- `DecimalField` → decimal numbers such as prices
- `PositiveIntegerField` → non-negative whole numbers
- `BooleanField` → `True` or `False`
- `DateField` → date only
- `DateTimeField` → date and time

Example:

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

---

### Date and Time Fields

```python
start_date = models.DateField()

starts_at = models.DateTimeField()

created_at = models.DateTimeField(auto_now_add=True)

updated_at = models.DateTimeField(auto_now=True)
```

- `auto_now_add=True` records the creation time.
- `auto_now=True` records the time whenever the object is saved.

---

### Common Field Options

Field options add rules and behavior to fields.

```python
name = models.CharField(max_length=120)

stock = models.IntegerField(default=0)

sku = models.CharField(unique=True)

status = models.CharField(db_index=True)
```

Important options:

- `max_length` → maximum character length
- `default` → value used when none is supplied
- `unique` → database uniqueness rule
- `db_index` → creates an index for frequent lookup or ordering
- `editable` → controls whether the field appears in forms such as `ModelForm`

---

### `null` vs `blank`

`null` and `blank` answer different questions.

#### `null`

Controls database storage.

```python
published_at = models.DateTimeField(
    null=True,
    blank=True
)
```

`null=True` means the database column may store SQL `NULL`.

The default is:

```python
null=False
```

#### `blank`

Controls validation.

```python
bio = models.TextField(blank=True)
```

`blank=True` means forms and model validation may accept an empty value.

The default is:

```python
blank=False
```

---

### Django's Automatic Primary Key

If a model does not define a primary key, Django creates one automatically.

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
```

Django supplies an automatically increasing primary key named:

```text
id
```

Both of these can refer to the object's primary key:

```python
product.id
product.pk
```

`pk` is a generic alias for the model's primary key.

A common project default is `BigAutoField`.

---

### Controlled Values with `TextChoices`

`TextChoices` provides a fixed set of meaningful values for a field.

```python
class Product(models.Model):

    class Category(models.TextChoices):
        LAPTOP = "laptop", "Laptop"
        PHONE = "phone", "Phone"
        ACCESSORY = "accessory", "Accessory"

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACCESSORY
    )
```

This separates:

- Stored value → `laptop`
- Display label → `Laptop`
- Python constant → `Category.LAPTOP`

Choices guide validation and forms, but they do not create a separate related entity.

---

### Other Practical Field Types

#### UUIDField

Useful for UUID values and public identifiers.

```python
import uuid

public_id = models.UUIDField(
    default=uuid.uuid4,
    editable=False,
    unique=True
)
```

#### JSONField

Stores structured JSON data.

```python
metadata = models.JSONField(default=dict)
```

#### ImageField

Stores an image reference and adds image validation.

```python
image = models.ImageField(
    upload_to="products/"
)
```

#### FileField

Stores a file name or storage reference.

```python
attachment = models.FileField(
    upload_to="files/"
)
```

---

## From Python Class to Relational Table

Example model:

```python
class Product(models.Model):
    name = models.CharField(max_length=120)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
```

Conceptually this becomes a relational table containing fields such as:

| id | name | price |
|---|---|---|
| 1 | Keyboard | 249.90 |
| 2 | Mouse | 89.00 |

Django normally creates the table name using the app label and model name and automatically adds an `id` primary key when one is not defined manually.

---

## Exercises

### Exercise 1 - Build the Product Model

The Product model was designed using suitable Django field types for:

- `name` → short text, maximum 120 characters
- `description` → long text
- `price` → decimal value
- `stock` → non-negative whole number with default `0`
- `is_active` → Boolean with default `True`
- `available_from` → date
- `created_at` → automatically set when created
- `product_image` → uploaded image

---

### Exercise 2 - Improve the Product Model

The model was extended with additional rules:

- Optional description without storing `NULL`
- Optional `available_from`
- Unique `sku` with maximum length of 30
- Category values using `TextChoices`
- Default category of `Accessory`
- `db_index=True` for `name`
- Allow Django to generate the primary key automatically
- Compare `blank=True` with `null=True, blank=True`
- Understand `product.pk`
- Combine the exercises into one complete Product model

---

## Key Takeaways

- Django models describe relational database structure using Python classes.
- A model class represents a table.
- Model fields represent database columns.
- Model instances represent rows.
- Choose field types based on the meaning of the stored data.
- `null` controls database storage.
- `blank` controls validation.
- Django can automatically create the primary key.
- `pk` is a generic alias for a model's primary key.
- `TextChoices` provides controlled field values.
- Field options define rules such as defaults, uniqueness, indexes, and editability.
- The model definition comes first; database structure is applied later through migrations.

---

**Status:** ✅ Completed
