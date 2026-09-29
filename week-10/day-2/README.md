# Week 10 - Day 2

## Overview

Today focused on using the **Django ORM** to perform database operations through Python instead of writing SQL directly.

The lesson covered how Django models interact with the database using **Managers**, **QuerySets**, and **model instances**, and how to perform the main **CRUD operations**:

- Create
- Read
- Update
- Delete

---

## Topics Covered

- Django ORM mental model
- Django Shell for ORM practice
- Manager, QuerySet, and Model Instance
- Creating database records
- Retrieving records
- `all()`, `filter()`, and `get()`
- Field lookups using double underscores
- QuerySet chaining
- Ordering and slicing
- `first()`, `exists()`, and `count()`
- Updating model instances
- Bulk updates using `QuerySet.update()`
- Database-side calculations using `F()` expressions
- Deleting records
- Handling missing and duplicate results
- CRUD operations inside Django views
- Product Inventory CRUD guided lab

---

## Key Concepts

### Django ORM

The **Object-Relational Mapper (ORM)** connects Django models with database tables.

A Django model represents a table, while model objects represent individual rows.

```python
Product.objects
```

`Product.objects` is the usual entry point for database operations on the `Product` model.

---

### Django Shell

The Django shell provides a safe environment for practicing ORM operations against the development database.

```bash
python manage.py shell
```

Then import the model:

```python
from catalog.models import Product
```

Example:

```python
Product.objects.all()
```

Before performing destructive operations, it is important to confirm that the correct project and development database are being used.

---

### Manager, QuerySet, and Instance

#### Manager

The Manager starts database queries for a model.

```python
Product.objects
```

---

#### QuerySet

A QuerySet represents zero or more database rows.

```python
Product.objects.filter(stock__gt=0)
```

QuerySets can be refined using additional methods.

---

#### Model Instance

A model instance represents one database row.

```python
product = Product.objects.get(pk=1)
```

The instance provides access to its fields and model methods.

---

## Creating Records

### Using `create()`

`create()` creates and saves the record immediately.

```python
product = Product.objects.create(
    name="Mechanical Keyboard",
    price=349.00,
    stock=12,
)
```

---

### Creating an Instance Then Saving

A model can also be created in multiple steps.

```python
product = Product(
    name="USB Hub",
    price=89.00
)

product.stock = 25
product.save()
```

After a successful insert, Django assigns the database-generated primary key to the instance.

---

## Reading Records

### `all()`

Returns a QuerySet containing every row.

```python
products = Product.objects.all()
```

---

### `filter()`

Returns zero or more matching records.

```python
products = Product.objects.filter(stock__gt=0)
```

If nothing matches, an empty QuerySet is returned.

---

### `get()`

Used when exactly one matching record is expected.

```python
product = Product.objects.get(pk=7)
```

`get()` returns one model instance or raises an exception if the number of matching records is not exactly one.

---

## Field Lookups

Django uses double underscores `__` to express query conditions.

Example:

```python
Product.objects.filter(stock__gt=0)
```

Here:

- `stock` → field name
- `gt` → greater than

Other lookups can be used to build more specific queries.

---

## Chaining QuerySets

QuerySet methods can be chained together.

```python
products = (
    Product.objects
    .filter(is_active=True, stock__gt=0)
    .exclude(category="Clearance")
    .order_by("price")
)
```

Each method returns another QuerySet.

### `filter()`

Keeps records that match the conditions.

### `exclude()`

Removes records that match the conditions.

### `order_by()`

Sorts the results.

---

## QuerySet Slicing

QuerySets can be limited using Python-style slicing.

```python
first_five = products[:5]
```

This returns only the first five matching records.

---

## Choosing the Correct Result Type

### Exactly One Result

```python
Product.objects.get(pk=7)
```

Returns:

- one instance
- or an exception

---

### Zero or More Results

```python
Product.objects.filter(pk=7)
```

Returns a QuerySet.

---

### Zero or One Result

```python
Product.objects.filter(pk=7).first()
```

Returns:

- one instance
- or `None`

---

### Check Whether Records Exist

```python
Product.objects.filter(stock=0).exists()
```

Returns:

```text
True or False
```

---

### Count Matching Records

```python
Product.objects.filter(is_active=True).count()
```

Returns an integer.

---

## Updating One Model Instance

To update one record:

1. Retrieve the object.
2. Change its attributes.
3. Save the changes.

```python
product = Product.objects.get(pk=7)

product.price = 329.00
product.stock = 15

product.save(update_fields=["price", "stock"])
```

Changing a Python attribute alone does **not** modify the database.

The database changes only after `save()` is called.

---

## Updating Multiple Records

`QuerySet.update()` modifies matching rows directly in the database.

```python
changed = Product.objects.filter(
    category="Accessories",
    is_active=True,
).update(is_active=False)
```

It returns the number of affected rows.

This is efficient because Django does not load every matching model instance.

However, `update()`:

- does not call the model's `save()` method
- does not send `pre_save`
- does not send `post_save`

---

## F Expressions

`F()` expressions allow calculations to happen directly using the value currently stored in the database.

```python
from django.db.models import F

Product.objects.filter(pk=7).update(
    stock=F("stock") - 1
)
```

This avoids reading the value into Python and then writing it back separately.

It can also help when multiple operations may happen concurrently.

An `F()` expression does not automatically guarantee valid business values, so database constraints may still be required.

---

## Deleting Records

### Delete One Instance

```python
product = Product.objects.get(pk=7)
product.delete()
```

---

### Delete Multiple Matching Records

```python
Product.objects.filter(
    is_active=False,
    stock=0,
).delete()
```

Deletion executes immediately.

Related rows may also be affected depending on the model's `ForeignKey` `on_delete` rules.

`QuerySet.delete()` does not call each model instance's custom `delete()` method, although Django delete signals are still sent.

---

## Handling Query Outcomes

CRUD code should handle cases where database operations do not return the expected result.

### `DoesNotExist`

Raised when `get()` finds no matching row.

```python
try:
    product = Product.objects.get(sku="KB-100")
except Product.DoesNotExist:
    product = None
```

---

### `MultipleObjectsReturned`

Raised when `get()` finds more than one matching row.

```python
try:
    product = Product.objects.get(sku="KB-100")
except Product.MultipleObjectsReturned:
    print("SKU is not unique")
```

Fields used for one-record lookups should normally be protected using appropriate uniqueness constraints.

---

## Validation and Constraints

Calling:

```python
product.save()
```

does not automatically call:

```python
product.full_clean()
```

Different layers protect different boundaries:

- Forms
- Explicit validation
- Model validation
- Database constraints

---

## CRUD Inside Django Views

Django views coordinate HTTP requests while the ORM performs the database operations.

Example:

```python
from django.shortcuts import get_object_or_404, redirect

def deactivate_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(
            Product,
            pk=product_id
        )

        product.is_active = False
        product.save(
            update_fields=["is_active"]
        )

        return redirect(
            "product_detail",
            product_id=product.pk
        )
```

### GET

Used to read and display data without modifying database state.

### POST

Used for operations that create, update, or delete data after validation and permission checks.

After a successful change, Django commonly redirects using the **Post/Redirect/Get** pattern.

---

## Guided Lab: Product Inventory CRUD

The lab practiced the full CRUD workflow using the `Product` model.

### Tasks

1. Create three products with different prices and stock values.
2. Retrieve every product and display its primary key.
3. Filter active products with stock above zero.
4. Find products whose names contain a search term.
5. Retrieve one product by primary key and handle a missing record.
6. Update one product using:

```python
save(update_fields=[...])
```

7. Deactivate a category using:

```python
QuerySet.update()
```

8. Delete only inactive products with zero stock.

---

## Key Takeaways

- Django ORM allows database operations using Python model APIs.
- `objects` is the default model Manager.
- QuerySets represent collections of database rows.
- Model instances represent individual rows.
- `create()` creates and saves a record immediately.
- `all()` returns every record.
- `filter()` returns zero or more matching records.
- `get()` expects exactly one matching record.
- QuerySets can be chained, ordered, and sliced.
- `.first()`, `.exists()`, and `.count()` are useful depending on the expected result.
- Updating an instance requires `save()` to persist changes.
- `QuerySet.update()` performs efficient bulk updates.
- `F()` expressions perform calculations using current database values.
- `delete()` can remove one record or a complete filtered QuerySet.
- CRUD code should handle missing and duplicate results safely.
- Django views coordinate requests while the ORM handles database work.

---

**Status:** ✅ Completed
