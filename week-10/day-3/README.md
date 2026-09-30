# Week 10 - Day 3

## Overview

Today focused on **Django QuerySets** and how to build flexible database queries using filtering, lookups, relationships, `Q` objects, and `F` expressions.

The main idea was to **build the query first, then let the database answer it**.

---

## Topics Covered

- QuerySet mental model
- QuerySet lifecycle and lazy evaluation
- QuerySet chaining and reuse
- Field lookup syntax
- Comparison, range, and membership lookups
- Text lookups
- NULL, date, and Boolean lookups
- Lookups across relationships
- AND conditions and `exclude()`
- Complex conditions with `Q` objects
- Ordering and slicing
- Removing duplicate results with `distinct()`
- Field-to-field comparisons using `F` expressions
- Result shaping with `values()` and `values_list()`
- `exists()` and `count()`
- Guided Lab: Product Search QuerySet

---

## Key Concepts

### QuerySet Mental Model

A `QuerySet` starts as a **description of a database query**.

```python
Product.objects.filter(is_active=True)
```

The main flow is:

```text
Manager → QuerySet → Evaluation → Database Results
```

`Product.objects` starts the query, QuerySet methods refine it, and Django executes SQL when the QuerySet is evaluated.

---

### QuerySet Characteristics

QuerySets are:

- **Lazy** — creating them usually does not immediately query the database.
- **Chainable** — methods such as `filter()` return another QuerySet.
- **Independent** — refining one QuerySet does not modify the original.
- **Cacheable** — after evaluation, the same QuerySet may reuse its loaded results.

Example:

```python
active = Product.objects.filter(is_active=True)

in_stock = active.filter(stock__gt=0)
out_of_stock = active.filter(stock=0)

cheap_in_stock = in_stock.filter(price__lt=100)
```

The original `active` QuerySet remains unchanged.

---

### When QuerySets Execute

Methods such as these usually construct or refine a QuerySet:

```python
all()
filter()
exclude()
order_by()
values()
```

Database access happens when results are required, such as:

```python
list(qs)
len(qs)
bool(qs)

qs.first()
qs.get()
qs.count()
qs.exists()
qs.update()
qs.delete()
```

Printing a QuerySet in the interactive shell also evaluates it for display.

---

### Field Lookup Syntax

Django uses double underscores `__` to build lookup paths.

```python
Product.objects.filter(
    category__name__icontains="audio"
)
```

This can contain:

```text
relationship → field → lookup
```

In this example:

- `category` → relationship field
- `name` → field on `Category`
- `icontains` → case-insensitive text lookup

Without an explicit lookup, Django assumes an exact comparison.

---

### Comparison Lookups

```python
price__lt=100
```

Less than 100.

```python
price__lte=100
```

100 or less.

```python
price__gt=100
```

Greater than 100.

```python
price__gte=100
```

100 or greater.

---

### Range and Membership Lookups

Range:

```python
Product.objects.filter(
    price__range=(50, 150)
)
```

Membership:

```python
Product.objects.filter(
    stock__in=[0, 5, 10]
)
```

---

### Text Lookups

Exact match:

```python
name__exact="Keyboard"
```

Case-insensitive exact match:

```python
name__iexact="keyboard"
```

Contains:

```python
name__contains="board"
```

Case-insensitive contains:

```python
name__icontains="BOARD"
```

Starts with:

```python
name__startswith="Mech"
```

Case-insensitive ends with:

```python
name__iendswith="hub"
```

---

### NULL Lookups

Use `isnull` to test whether a database value is `NULL`.

```python
Product.objects.filter(
    category__isnull=True
)
```

This means:

```text
category IS NULL
```

It does **not** mean that `NULL == True`.

---

### Date Lookups

Parts of a `DateTimeField` can be queried directly.

```python
Product.objects.filter(
    created_at__date=today
)
```

```python
Product.objects.filter(
    created_at__year=2026
)
```

```python
Product.objects.filter(
    created_at__month=9
)
```

---

### Boolean Lookups

Boolean values can be queried directly.

```python
Product.objects.filter(
    is_active=True
)
```

---

### Lookups Across Relationships

Django can follow relationships automatically.

#### Forward Lookup

```python
Product.objects.filter(
    category__name="Audio"
)
```

Django follows the `category` ForeignKey and checks the related category's `name`.

#### Raw Foreign Key Value

```python
Product.objects.filter(
    category_id=4
)
```

This compares the stored foreign key ID directly.

#### Reverse Lookup

```python
Category.objects.filter(
    products__price__lt=100
)
```

A reverse relationship can use its `related_name`.

---

### AND Conditions

Multiple keyword arguments inside one `filter()` are combined using **AND**.

```python
products = Product.objects.filter(
    is_active=True,
    stock__gt=0,
    price__lt=500,
)
```

This means:

```text
active AND stock > 0 AND price < 500
```

---

### exclude()

`exclude()` removes matching records from a QuerySet.

```python
products = products.exclude(
    category__name="Clearance"
)
```

---

### Complex Conditions with Q Objects

`Q` objects are used for more complex conditions such as:

- OR
- explicit AND
- NOT
- grouping

Import:

```python
from django.db.models import Q
```

#### OR

```python
results = Product.objects.filter(
    Q(name__icontains=term) |
    Q(sku__icontains=term),
    is_active=True,
)
```

`|` means OR.

#### AND

```python
Q(condition1) & Q(condition2)
```

`&` means AND.

#### NOT

```python
Product.objects.filter(
    ~Q(category__name="Clearance")
)
```

`~` negates the condition.

Parentheses are useful for controlling grouping.

---

### Ordering Results

Use `order_by()`:

```python
products = Product.objects.order_by(
    "category__name",
    "-price",
    "name",
)
```

A minus sign `-` means descending order.

```python
"-price"
```

means highest price first.

---

### Slicing QuerySets

QuerySet slicing limits the returned rows.

```python
first_page = products[:10]
second_page = products[10:20]
```

Django translates slicing into database `LIMIT` and `OFFSET`.

Negative indexes are not supported.

---

### distinct()

Relationships may cause duplicate rows in query results.

Use:

```python
products = products.distinct()
```

to remove duplicate result rows.

---

### F Expressions

`F` expressions reference the **current database value of another field**.

Import:

```python
from django.db.models import F
```

#### Compare Two Fields

```python
Product.objects.filter(
    stock__lt=F("reorder_level")
)
```

Each Product compares its own `stock` with its own `reorder_level`.

#### Database-Side Arithmetic

```python
Product.objects.filter(pk=7).update(
    stock=F("stock") - 1
)
```

The calculation happens in the database using the currently stored value.

A loaded Python object may need:

```python
product.refresh_from_db()
```

after an `F` expression update.

---

### Result Shapes

Sometimes the application does not need full model instances.

#### values()

Returns dictionaries containing selected fields.

```python
names_and_prices = Product.objects.filter(
    is_active=True
).values(
    "name",
    "price",
)
```

Example result:

```python
{
    "name": "Keyboard",
    "price": 349.00
}
```

---

### values_list()

Returns tuples instead of model objects.

```python
Product.objects.values_list(
    "sku"
)
```

For one field:

```python
Product.objects.values_list(
    "sku",
    flat=True
)
```

This returns individual values rather than one-item tuples.

---

### exists()

Use `exists()` when only checking whether matching records exist.

```python
has_low_stock = Product.objects.filter(
    stock__lt=5
).exists()
```

Returns:

```text
True or False
```

---

### count()

Use `count()` when only the number of matching records is needed.

```python
Product.objects.filter(
    is_active=True
).count()
```

This asks the database for the quantity without loading every Product object.

---

### Inspecting Generated SQL

During development, the generated SQL can be inspected with:

```python
str(queryset.query)
```

This helps understand how Django translates ORM queries into SQL.

---

## Guided Lab: Product Search QuerySet

The lab focused on building one reusable search QuerySet and refining it step by step.

### Requirements

1. Start with active Product records.
2. Keep products whose stock is above zero.
3. Search name **OR** SKU using a `Q` object.
4. Apply optional minimum and maximum prices.
5. Filter by category name across the relationship.
6. Order by price, then name, then primary key.
7. Return the first 10 results.
8. Produce a `values()` result containing:
   - name
   - SKU
   - price

Example structure:

```python
from django.db.models import Q

products = Product.objects.filter(
    is_active=True,
    stock__gt=0,
)

products = products.filter(
    Q(name__icontains=term) |
    Q(sku__icontains=term)
)

products = products.filter(
    category__name=category_name
)

products = products.order_by(
    "price",
    "name",
    "pk",
)

results = products[:10].values(
    "name",
    "sku",
    "price",
)
```

---

## Key Takeaways

- QuerySets describe database queries before Django evaluates them.
- QuerySets are lazy, chainable, reusable, and independent.
- Double underscores `__` are used for lookups and relationship traversal.
- `filter()` conditions are combined with AND by default.
- `exclude()` removes matching records.
- `Q` objects support OR, NOT, AND, and grouped conditions.
- `F` expressions reference current database field values.
- `order_by()`, slicing, and `distinct()` control result ordering and shape.
- `values()` and `values_list()` return only the data that is needed.
- `exists()` and `count()` answer focused database questions efficiently.
- Relationship fields can be followed directly inside ORM queries.

---

**Status:** ✅ Completed
