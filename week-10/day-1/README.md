# Week 10 - Day 1

## Overview

Today focused on **Django migrations** and how model changes become a repeatable history of database schema changes.

We learned how Django connects:

- `models.py`
- Migration files
- Database schema

We also practiced how to create, inspect, apply, reverse, and safely design migrations.

---

## Topics Covered

- Migration mental model
- Migration workflow
- Migration files
- `makemigrations`
- `migrate`
- Migration inspection commands
- Common schema operations
- Adding required fields safely
- Renaming fields without losing data
- Data migrations with `RunPython`
- Safe schema evolution
- Rollbacks and team practices

---

## Key Concepts

### Migration Mental Model

Django keeps three related states:

- **`models.py`** → the structure the application expects now
- **Migration files** → ordered instructions describing how the structure changed
- **Database schema** → tables, columns, indexes, and constraints currently applied

`makemigrations` compares the current models with the recorded migration state.

`migrate` applies the recorded migration history to the database.

---

### Migration Workflow

A typical migration workflow is:

1. Change `models.py`
2. Run `makemigrations`
3. Inspect the generated migration
4. Run `migrate`
5. Test and commit the model changes and migration files together

```bash
python manage.py makemigrations
python manage.py migrate
```

Migration files should travel with the project code and be used consistently across development, testing, staging, and production.

---

### Inside a Migration File

A migration is a Python file that mainly contains:

#### `dependencies`

Defines which migrations must run before the current migration.

#### `operations`

Defines the ordered database changes Django should perform.

Example operations may include:

- `CreateModel`
- `AddField`
- `AlterField`
- `RenameField`
- `RemoveField`
- `AddConstraint`

Django uses the migration history to reconstruct previous model states.

---

### Creating Migrations

Create migrations for all changed apps:

```bash
python manage.py makemigrations
```

Create one for a specific app:

```bash
python manage.py makemigrations catalog
```

Give the migration a meaningful name:

```bash
python manage.py makemigrations catalog --name add_product_sku
```

Check whether model changes are missing migrations:

```bash
python manage.py makemigrations --check --dry-run
```

Generated migrations should always be reviewed before applying them.

---

### Applying Migrations

Apply all pending migrations:

```bash
python manage.py migrate
```

Apply migrations for one app:

```bash
python manage.py migrate catalog
```

Move an app to a specific migration:

```bash
python manage.py migrate catalog 0003
```

Django records successfully applied migrations in its migration history.

---

### Inspecting Migration Status

Show applied and unapplied migrations:

```bash
python manage.py showmigrations
```

Limit the output to one app:

```bash
python manage.py showmigrations catalog
```

An `X` indicates that a migration has been applied.

---

### Previewing the Migration Plan

Before modifying a database, the planned operations can be inspected with:

```bash
python manage.py migrate --plan
```

This shows the forward or reverse operations Django intends to perform.

---

### Inspecting Generated SQL

`sqlmigrate` displays the SQL for a migration without applying it:

```bash
python manage.py sqlmigrate catalog 0004
```

This helps inspect operations such as:

- Table changes
- Columns
- Indexes
- Constraints
- Possible table rebuilds

The generated SQL may differ depending on the database backend.

---

### Common Schema Operations

#### `CreateModel`

Creates a new table and its initial fields.

#### `AddField`

Adds a new column or relationship.

#### `AlterField`

Changes an existing field definition.

#### `RenameField`

Renames a field while preserving its existing data.

#### `RemoveField`

Removes a column and usually its stored data.

#### `AddConstraint`

Adds a database rule or constraint.

---

### Adding a Required Field to Existing Data

Adding a required field can be risky because existing records already need a value.

Possible approaches include:

#### Immediate Default

Use a meaningful default when all existing rows can correctly share the same value.

#### Temporary `null=True`

Add the field as nullable first:

1. Add the nullable field
2. Populate existing rows
3. Verify the data
4. Later make the field required

#### One-Off Value

`makemigrations` may ask for a one-time value to fill existing rows.

This value affects existing rows only and should make sense for the application data.

---

### Renaming Fields Safely

When changing a field name, the expected migration should use `RenameField`.

Example:

```python
migrations.RenameField(
    model_name="product",
    old_name="stock",
    new_name="quantity",
)
```

A migration containing `RemoveField` followed by `AddField` may lose the existing data.

The generated migration must therefore be reviewed carefully.

---

### Data Migrations with `RunPython`

A **data migration** changes existing stored records as part of migration history.

Django provides:

```python
migrations.RunPython()
```

Data migrations should use historical models:

```python
Product = apps.get_model("catalog", "Product")
```

This loads the version of the model that existed at that point in migration history.

A reverse function can also be provided so the data change can be undone.

---

### Safe Schema Evolution

Risky changes should be separated into smaller reversible steps.

A safe sequence can be:

1. **Expand**  
   Add a nullable field or compatible structure.

2. **Backfill**  
   Populate and verify values for existing rows.

3. **Switch Code**  
   Update the application to use the new structure.

4. **Enforce**  
   Add required, unique, or check constraints.

5. **Clean Up**  
   Remove the old field after every environment has moved to the new structure.

---

### Rollback Practices

A migration can be reversed by targeting an earlier migration:

```bash
python manage.py migrate catalog 0003
```

However, not every operation is safely reversible.

Some migrations:

- Lose data
- Require explicit reverse logic
- Need additional planning before rollback

A reverse migration also does not replace a proper database backup and restore strategy.

---

### Team Practices

Good migration practices include:

- Commit model changes and migration files together
- Review migration files before applying them
- Keep migrations small and focused
- Test migrations using realistic data
- Use the same migration history across environments
- Review migration conflicts created by parallel branches
- Keep old migrations until every environment has upgraded
- Squash long migration histories only later when appropriate

---

## Guided Lab: Evolve the Product Schema

The lab practiced safely evolving an existing `Product` model.

### Steps

1. Add `Product.code` with:

```python
null=True
```

2. Create a named schema migration.

3. Inspect the migration using:

```bash
python manage.py showmigrations
python manage.py migrate --plan
python manage.py sqlmigrate catalog <migration_number>
```

4. Create an empty data migration.

5. Populate `code` using each Product primary key.

6. Change `code` to:

```python
null=False
unique=True
```

7. Rename:

```text
stock → quantity
```

using `RenameField`.

8. Apply the migrations, verify the data, and test a rollback.

---

## Key Takeaways

- `models.py` describes the desired model structure.
- Migration files record how that structure changes over time.
- `makemigrations` creates migration operations.
- `migrate` applies those operations to the database.
- Migration files should always be inspected before being applied.
- `showmigrations`, `migrate --plan`, and `sqlmigrate` help inspect migration state and behavior.
- Required fields need special handling when existing rows already exist.
- `RenameField` should preserve data when a field is renamed.
- `RunPython` is used when existing data must be transformed.
- Historical models should be accessed using `apps.get_model()`.
- Complex database changes are safer when divided into small reversible steps.
- Models and their migration files should be committed together.

---

**Status:** ✅ Completed
