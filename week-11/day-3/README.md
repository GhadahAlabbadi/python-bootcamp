# Week 11 - Day 3

## Overview

Today focused on **querying across relationships** with the Django ORM.

The main idea was to **follow the relationship path, then choose how Django should load it**: a lookup path can travel from one model to related models, while the model that starts the query still decides which objects are returned.

---

## Topics Covered

- The connected catalogue model used in all examples
- The relationship query mental model
- Forward `ForeignKey` traversal
- Reverse relationship traversal with `related_name`
- Multi-hop query paths
- `ManyToMany` traversal in both directions
- Result multiplicity and `distinct()`
- Duplicate base rows after joins and inspecting the generated SQL

---

## Key Concepts

### The Connected Catalogue Model

Every example used the same set of related models, so each new query path built on an existing idea.

| Model | Fields | Relationship to Product |
|---|---|---|
| `Supplier` | `name`, `country` | One supplier has many products |
| `Category` | `name` | One category has many products |
| `Product` | `name`, `price`, `stock` | The centre of the graph |
| `ProductDetail` | `warranty_months` | `OneToOneField` to Product |
| `Review` | `rating`, `is_public` | `ForeignKey` to Product |
| `Tag` | `name` | `ManyToManyField` from Product |

A simplified version of the `Product` model:

```python
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products")
```

One model graph gives several directions of travel.

---

### The Relationship Query Mental Model

A relationship query has three parts:

| Part | Meaning |
|---|---|
| Starting model | `Product.objects` means the result contains **Product** objects. |
| Relationship path | `category__name` follows `Product.category` and reads `Category.name`. |
| Database work | Django creates the joins or extra queries the operation needs. |

```python
Product.objects.filter(category__name="Audio")
```

This returns **products**, even though the condition lives on `Category`.

---

### Forward ForeignKey Traversal

Use the field name on the current model, then continue with a field or lookup on the related model.

```python
# Products supplied from Kenya
Product.objects.filter(
    supplier__country="Kenya"
)

# Products in categories containing "audio"
Product.objects.filter(
    category__name__icontains="audio"
)
```

- `supplier__country` → `Product.supplier`, then `Supplier.country`.
- `category__name__icontains` → `Product.category`, then `Category.name`, then a text lookup.

The QuerySet still returns `Product` objects.

---

### Multi-Hop Query Paths

Each double underscore `__` either crosses one relationship or applies the final lookup.

```python
# Public reviews for products from Kenya
Review.objects.filter(
    product__supplier__country="Kenya",
    is_public=True,
)

# Suppliers with highly rated audio products
Supplier.objects.filter(
    products__category__name="Audio",
    products__reviews__rating__gte=4,
).distinct()
```

Reading `product__supplier__country` one segment at a time:

| Segment | Meaning |
|---|---|
| `product` | Review to Product |
| `supplier` | Product to Supplier |
| `country` | Field on Supplier |

In the second query, `products` and `reviews` are **reverse** paths, named by each relationship's `related_name`, and `gte` is the comparison lookup.

> Read long paths one segment at a time.

---

### ManyToMany Traversal

The same path syntax works in both directions of a `ManyToManyField`.

```python
class Product(models.Model):
    tags = models.ManyToManyField(
        Tag,
        related_name="products",
    )

# Products with an eco tag (forward path)
Product.objects.filter(tags__name="eco")

# Tags used by inexpensive products (reverse path)
Tag.objects.filter(products__price__lt=50)
```

- **Forward path:** Product to tags uses `tags__name`.
- **Reverse path:** Tag to products uses `products__price`.

---

### Result Multiplicity and distinct()

When a query crosses a "many" relationship, one base object can match several related rows.

For example, a product with two matching tags, or a supplier with several matching reviews, can appear **more than once** in the results.

```python
Supplier.objects.filter(
    products__reviews__rating__gte=4,
).distinct()
```

`distinct()` removes the repeated rows, so each object is returned once.

---

### Duplicate Base Rows after Joins

A database join returns matching row combinations, so several matches can repeat the same base object.

```python
products = Product.objects.filter(
    tags__name__icontains="e"
)

unique_products = products.distinct()

print(products.query)
```

- **Why repetition appears:** one Product can join to several Tag rows that match the condition.
- **What `distinct()` does:** it asks the database to remove duplicate result rows.
- **What to inspect:** check the generated SQL and the ordering when distinct results surprise you.

---

## Key Takeaways

- The starting manager decides which model's objects are returned.
- A relationship path describes where Django should look; Django builds the joins.
- Forward paths use the field name defined on the current model.
- Reverse paths use the `related_name` of the relationship.
- Each `__` crosses one relationship or applies the final lookup.
- Long paths are easiest to read one segment at a time.
- `ManyToManyField` paths work in both directions with the same syntax.
- Queries across "many" relationships can repeat rows; `distinct()` removes duplicates.
- `print(queryset.query)` shows the generated SQL when results look unexpected.

---

**Status:** ✅ Completed
