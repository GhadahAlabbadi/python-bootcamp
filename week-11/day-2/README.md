# Week 11 - Day 2

## Overview

Today focused on **summarising data with the Django ORM** using **aggregation** and **annotation**.

The main idea was to **choose the result shape before choosing the aggregate function**: one number for the whole collection, or one number beside every object or group. The database performs the calculation before Django receives the result.

---

## Topics Covered

- Core aggregate functions: `Count`, `Sum`, `Avg`, `Min`, and `Max`
- The two aggregation result shapes: `aggregate()` and `annotate()`
- Whole-QuerySet summaries with `aggregate()`
- Per-object values with `annotate()`
- Grouping with `values()` before `annotate()`
- `filter()` before or after `annotate()`
- Aggregation across relationships
- Conditional aggregates with `filter=Q()`
- Guided Lab: Catalogue Summary Report

---

## Key Concepts

### Core Aggregate Functions

Import the aggregate classes from `django.db.models`, then pass a field path to the function.

```python
from django.db.models import (
    Avg,
    Count,
    Max,
    Min,
    Sum,
)
```

| Function | Question it answers |
|---|---|
| `Count` | How many rows or values? |
| `Sum` | What is the total? |
| `Avg` | What is the mean value? |
| `Min` and `Max` | What are the lowest and highest values? |

The database performs the calculation before Django receives the result.

---

### Two Aggregation Result Shapes

The question decides whether Django should return **one summary dictionary** or **a QuerySet of annotated objects**.

| `aggregate()` | `annotate()` |
|---|---|
| Summarises the complete QuerySet. | Calculates a value for each returned object or group. |
| Returns one dictionary. | Returns another QuerySet. |
| Ends the QuerySet chain. | Filtering and ordering can continue. |

> One number for the collection uses `aggregate()`. One number beside every object uses `annotate()`.

---

### Whole-QuerySet Summaries with aggregate()

`aggregate()` returns one dictionary whose keys are the aliases and whose values are the calculated results.

```python
from django.db.models import Avg, Max, Sum

summary = Product.objects.filter(
    is_active=True
).aggregate(
    average_price=Avg("price"),
    highest_price=Max("price"),
    total_stock=Sum("stock"),
)

print(summary["average_price"])
```

- **Input:** only active Product rows enter the calculation.
- **Calculation:** the database computes three summaries in one query.
- **Output:** a dictionary is returned instead of Product objects.

---

### Per-Object Values with annotate()

`annotate()` returns model objects with an extra attribute calculated for each object.

```python
from django.db.models import Count

products = Product.objects.annotate(
    review_count=Count("reviews")
)

for product in products:
    print(
        product.name,
        product.review_count,
    )
```

- **One row per Product:** the QuerySet still contains Product instances.
- **Extra attribute:** `review_count` exists on each returned instance for this query.
- **Chainable result:** `filter()` and `order_by()` can use the annotation alias.

---

### Grouping with values() before annotate()

When `values()` appears **before** `annotate()`, it chooses the grouping fields. The result contains dictionaries instead of model instances.

```python
category_report = Product.objects.values(
    "category__name"
).annotate(
    product_count=Count("id"),
    average_price=Avg("price"),
    total_stock=Sum("stock"),
).order_by("category__name")

for row in category_report:
    print(row["category__name"])
    print(row["product_count"])
```

- **Group key:** `category__name` creates one group for each distinct name.
- **Calculated columns:** each group receives a count, an average price, and a total stock.
- **Result shape:** every row is a dictionary containing the group key and the annotations.

This is the ORM version of SQL `GROUP BY`.

---

### filter() before or after annotate()

QuerySet clauses operate on the query state created by the clauses that appear before them.

**Count only active products:** filter the related rows before the annotation.

```python
Category.objects.filter(
    products__is_active=True
).annotate(
    product_count=Count("products")
)
```

**Count all products for matching categories:** annotate first, then keep categories with an active product.

```python
Category.objects.annotate(
    product_count=Count(
        "products", distinct=True
    )
).filter(
    products__is_active=True
)
```

> Changing the clause order can change both the selected rows and the calculated value.

---

### Aggregation across Relationships

Double underscores follow the same relationship paths used in filters.

```python
review_summary = Product.objects.aggregate(
    review_count=Count(
        "reviews",
        distinct=True,
    ),
    average_rating=Avg(
        "reviews__rating"
    ),
)

category_summary = Category.objects.aggregate(
    average_product_price=Avg("products__price")
)
```

- **Count related rows:** count reviews through the reverse ForeignKey path.
- **Summarise a related field:** average `reviews__rating` or `products__price`.
- Use `distinct=True` only when duplicate joined rows would change the intended count.

---

### Conditional Aggregates with filter=Q()

The `filter` argument is most useful when one query needs **several aggregates over the same relationship with different conditions**.

```python
from django.db.models import Count, Q

products = Product.objects.annotate(
    public_reviews=Count(
        "reviews",
        filter=Q(reviews__is_public=True),
    ),
    high_reviews=Count(
        "reviews",
        filter=Q(
            reviews__is_public=True,
            reviews__rating__gte=4,
        ),
    ),
)
```

- **One relationship:** both counts summarise the Review rows of each Product.
- **Different conditions:** each `Count` applies its own `Q` expression.
- **Single aggregate:** for one condition, filter the QuerySet before `annotate()` when possible.

---

## Guided Lab: Catalogue Summary Report

Create one category report and one overall summary from the familiar catalogue models.

### Requirements

1. Keep active Product rows only.
2. Group products by category.
3. Add `product_count` for each category.
4. Add `average_price` and `total_stock` for each category.
5. Keep categories with at least three active products.
6. Order by `product_count` descending, then by category.
7. Build a separate overall aggregate with total products and average price.
8. Explain which result contains dictionaries and which contains one dictionary.

### My Solution

In my lab project, `category` is a choice field on `Product`, so the report groups by `category` directly. The queries live in `catalog/reports.py`, next to the search queries in `catalog/selectors.py`.

```python
from django.db.models import Avg, Count, Sum

from .models import Product


def category_report():
    return (
        Product.objects.filter(is_active=True)
        .values("category")
        .annotate(
            product_count=Count("pk"),
            average_price=Avg("price"),
            total_stock=Sum("quantity"),
        )
        .filter(product_count__gte=3)
        .order_by("-product_count", "category")
    )


def overall_summary():
    return Product.objects.filter(is_active=True).aggregate(
        total_products=Count("pk"),
        average_price=Avg("price"),
    )
```

**Requirement 8:**

- `category_report()` returns a QuerySet of **dictionaries**, one per category.
- `overall_summary()` returns **one dictionary** for all active products.

### Exit Ticket

**Why must `values()` appear before `annotate()` in the category report?**

`values()` placed before `annotate()` tells Django which fields to group by. Without it, `annotate()` calculates the values for each Product row, so every product would get its own count instead of one count per category.

---

## Key Takeaways

- Choose the result shape before choosing the aggregate function.
- `aggregate()` returns one dictionary and ends the QuerySet chain.
- `annotate()` adds a value to each object or group and keeps the QuerySet chainable.
- `values()` before `annotate()` groups the results, like SQL `GROUP BY`.
- The order of `filter()` and `annotate()` changes which rows are counted.
- Aggregates can follow relationship paths with double underscores.
- `filter=Q()` allows several conditional aggregates over one relationship in one query.
- Use `distinct=True` only when duplicate joined rows would change the intended count.

---

**Status:** ✅ Completed
