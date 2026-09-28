# Week 9 - Day 1

## Overview

Today focused on designing stronger Django models by keeping related data and behaviour together, configuring model-level metadata, improving query performance with indexes, and protecting stored data using database constraints.

---

## Topics Covered

- Cohesive Django models
- Model methods
- Thin views and meaningful models
- `Meta` class options
- Default ordering
- Database table and display names
- Single and composite indexes
- Database constraints
- `UniqueConstraint`
- `CheckConstraint`
- Choosing the correct layer for business rules
- Common model design mistakes
- Strengthening the Product model

---

## Key Concepts

### 1. Cohesive Models

A model should represent one clear entity and contain behaviour related to its own data.

A `Product` model can own:

- Name and SKU
- Price and stock
- Active state
- Created and updated timestamps
- Availability logic

It should not contain unrelated responsibilities such as:

- HTTP responses
- Template rendering
- Email delivery
- Payment gateway calls
- Large workflows involving several systems

The main idea is to keep rules close to the data they describe.

---

### 2. Thin Views and Meaningful Models

Views should coordinate requests, while models should answer questions about their own state.

Example:

```python
class Product(models.Model):
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def is_available(self):
        return self.is_active and self.stock > 0
```

The view can simply call:

```python
product.is_available()
```

instead of repeating the same business rule in multiple views.

---

### 3. Model Methods

Model methods describe behaviour or calculations that belong to one model instance.

```python
def is_available(self):
    return self.is_active and self.stock > 0
```

```python
def inventory_value(self):
    return self.price * self.stock
```

Benefits:

- Keeps domain logic reusable
- Avoids duplicated rules
- Can be used from views, templates, scripts, and tests
- Keeps model-related behaviour close to its data

Simple model methods should avoid unexpected expensive database queries or network calls.

---

### 4. The `Meta` Class

The inner `Meta` class configures behaviour for the model as a whole.

```python
class Meta:
    ordering = ["category", "name"]
    db_table = "catalog_product"
    verbose_name = "product"
    verbose_name_plural = "products"
```

Common options include:

- `ordering`
- `db_table`
- `verbose_name`
- `verbose_name_plural`
- `indexes`
- `constraints`

---

### 5. Default Ordering

Default ordering controls how QuerySets are ordered when no other ordering is specified.

```python
class Meta:
    ordering = ["category", "name"]
```

Descending order uses `-`:

```python
class Meta:
    ordering = ["-price"]
```

A later `order_by()` call can override the model's default ordering.

Default ordering should only be added when it is genuinely useful because ordering has a database cost.

---

### 6. Database and Display Names

Django normally creates a table name using:

```text
app_label + model_name
```

Example:

```text
catalog_product
```

A custom table name can be provided using:

```python
db_table = "inventory_items"
```

Human-readable names can be configured using:

```python
verbose_name = "inventory item"
verbose_name_plural = "inventory items"
```

---

### 7. Database Indexes

Indexes help the database find filtered or ordered values without scanning every row.

Good candidates are fields frequently used with:

- `filter()`
- `order_by()`
- Lookups

Examples:

- SKU
- Status
- `created_at`

Indexes improve reading performance but add storage and extra work during inserts and updates.

---

### 8. Single-Field Index

A single-field index can be created with:

```python
sku = models.CharField(
    max_length=30,
    db_index=True
)
```

This is useful when queries frequently search using one field.

---

### 9. Composite Index

A composite index covers multiple fields.

```python
class Meta:
    indexes = [
        models.Index(
            fields=["category", "is_active"],
            name="product_cat_active_idx"
        )
    ]
```

The order of fields matters because:

```text
(category, is_active)
```

does not behave exactly the same as:

```text
(is_active, category)
```

Indexes should be based on queries the application actually performs.

---

### 10. Database Constraints

Database constraints protect stored data regardless of which code path writes it.

Common database rules include:

- `NOT NULL`
- `UNIQUE`
- `CHECK`
- `FOREIGN KEY`

Application validation provides friendly feedback, while database constraints provide final protection.

---

### 11. `UniqueConstraint`

For one unique field, Django can use:

```python
unique=True
```

For combinations of fields, use `UniqueConstraint`.

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["name", "category"],
            name="unique_product_name_per_category"
        )
    ]
```

This allows the same product name in different categories while preventing duplicates inside the same category.

---

### 12. `CheckConstraint`

`CheckConstraint` ensures saved rows satisfy a required condition.

```python
class Meta:
    constraints = [
        models.CheckConstraint(
            condition=models.Q(price__gte=0),
            name="product_price_gte_0"
        ),
        models.CheckConstraint(
            condition=models.Q(stock__gte=0),
            name="product_stock_gte_0"
        )
    ]
```

This prevents invalid negative price or stock values from being stored.

---

### 13. Choosing Where a Rule Belongs

Different rules belong in different layers.

| Layer | Use When | Example |
|---|---|---|
| Field option | One field has a simple rule | `null`, `blank`, `unique`, `default` |
| Validator | One value needs reusable validation | Custom price format |
| Model `clean()` | A rule compares fields | Sale price cannot exceed normal price |
| Database constraint | Invalid state must never exist | Stock cannot be negative |
| Model method | Model answers a domain question | `is_available()` |

The goal is to use the narrowest layer that clearly expresses and protects the rule.

---

## Common Design Mistakes

### Business Rules in Every View

Repeating rules across views can cause duplicated logic and inconsistent behaviour.

### Too Many Indexes

Indexes consume storage and make writes more expensive.

### Validation Only

Scripts, imports, admin actions, or concurrent writes may bypass application validation.

### Constraint Only

Users may receive database errors instead of friendly validation messages.

### Expensive `__str__()`

A simple display operation should not silently trigger many database queries.

### Vague Constraint Names

Constraint names should clearly describe the rule they enforce.

---

## Guided Lab: Strengthen the Product Model

The existing Product model was improved by adding behaviour, metadata, indexes, and constraints.

Tasks included:

1. Add `is_available()` using `is_active` and `stock`
2. Add `inventory_value()` using `price` and `stock`
3. Set default ordering by category and then name
4. Add clear singular and plural `verbose_name` values
5. Add a composite index on `category` and `is_active`
6. Add a named constraint requiring price to be non-negative
7. Add a named constraint requiring stock to be non-negative
8. Run:

```bash
python manage.py check
```

---

## Key Takeaways

- Models should keep related data and behaviour together.
- Views should coordinate requests instead of owning repeated domain rules.
- Model methods make business behaviour reusable.
- `Meta` configures model-wide behaviour.
- Default ordering should be used intentionally.
- Indexes improve selected queries but have a cost.
- Composite index field order matters.
- Database constraints protect data at the database boundary.
- `UniqueConstraint` protects unique field combinations.
- `CheckConstraint` prevents invalid stored values.
- Business rules should be placed in the most appropriate layer.
- Good Django models should be readable, reusable, and protective of their own data.

---

**Status:** ✅ Completed
