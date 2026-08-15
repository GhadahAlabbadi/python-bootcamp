# Week 3 - Day 5

## Overview

The fifth day of Week 3 focused on intermediate Python techniques related to generator expressions, object mutability, copying strategies, collection performance, and dictionary indexing.

The session also included guided practice and hands-on labs to apply the concepts in a practical program.

---

## Topics Covered

- Generator Expressions
- Lazy Evaluation
- Mutable and Immutable Objects
- Reassignment and Object References
- Aliasing
- Shallow Copy
- Nested Mutable Objects
- Deep Copy
- Choosing the Correct Copy Strategy
- Collection Operation Costs
- Big O Basics
- List Membership
- Set and Dictionary Lookup
- Building Dictionary Indexes
- Comprehensions and Readability
- Safe Collection Mutation

---

## Key Concepts

### Generator Expressions

Generator expressions produce values only when they are needed instead of storing all results in memory at once.

```python
numbers = range(1_000_000)

total = sum(
    number ** 2
    for number in numbers
)
```

Generator expressions use parentheses and support lazy evaluation.

```python
(x * 2 for x in numbers)
```

### Mutable and Immutable Objects

Mutable objects can be changed after creation.

Examples:

- Lists
- Dictionaries
- Sets

Immutable objects cannot be modified after creation.

Examples:

- Numbers
- Strings
- Tuples

Reassignment makes a name refer to a different object rather than modifying an immutable object.

### Aliasing

Assignment can make two names refer to the same object.

```python
original = ["Python", "Git"]
alias = original
```

No copy is created.

Changes made through either name affect the shared object.

### Shallow Copy

A shallow copy creates a new outer container.

```python
clone = original.copy()
```

For flat collections, changes to the copied outer container do not affect the original.

However, nested mutable objects are still shared.

```python
original = [["Sara", 90], ["Omar", 85]]
clone = original.copy()
```

In this case:

```python
original[0] is clone[0]
```

returns:

```text
True
```

### Deep Copy

A deep copy creates independent copies of nested mutable objects.

```python
from copy import deepcopy

clone = deepcopy(original)
```

Changes inside the copied nested objects no longer affect the original.

### Choosing a Copy Strategy

The copy strategy should depend on how much independence is required.

- **Assignment** – Same object is shared.
- **Shallow Copy** – New outer container, nested mutable objects remain shared.
- **Deep Copy** – Outer and nested mutable objects become independent.

The lightest correct strategy should be chosen.

### Collection Operation Costs

Reviewed how the choice of collection affects performance.

Common examples:

- `list.append()` – Usually `O(1)`
- `x in list` – `O(n)`
- `x in set` – `O(1)` on average
- Dictionary key lookup – `O(1)` on average

Operation cost becomes especially important when the same work is repeated many times.

### Building an Index

A dictionary can be used as an index when records need repeated lookup.

```python
students = [
    {"id": 101, "name": "Sara"},
    {"id": 102, "name": "Omar"}
]

students_by_id = {
    student["id"]: student
    for student in students
}
```

This allows direct lookup:

```python
students_by_id[102]
```

instead of repeatedly searching through the entire list.

### Readability and Predictable Behavior

Intermediate Python code should remain clear and predictable.

Important practices included:

- Use a normal loop when a comprehension becomes difficult to read.
- Remember that assignment does not create a copy.
- Remember that shallow copies still share nested mutable objects.
- Avoid modifying a collection while iterating over that same collection.

---

## Guided Practice

Built a score-report program using the intermediate Python techniques covered during the session.

The practice included:

- Creating a list of student dictionaries with names and nested score lists.
- Using a list comprehension to calculate each student's average.
- Filtering the report to keep students whose average is at least `60`.
- Building a dictionary index that maps each student name to the report record.
- Creating an independent backup using `deepcopy()`.
- Verifying that nested changes remain separate between the original and the backup.

---

## Lab

Completed hands-on Python labs covering generator expressions, object mutability, copying strategies, nested collections, collection performance, and dictionary indexing.

The complete lab solution is available in the **lab** folder.

---

## Homework

No homework was assigned.

---

## Key Takeaways

- Learned how generator expressions produce values on demand.
- Understood the difference between mutable and immutable objects.
- Distinguished between aliasing, shallow copy, and deep copy.
- Learned how nested mutable objects behave with shallow copies.
- Practiced choosing the appropriate copy strategy.
- Introduced basic collection performance using Big O notation.
- Learned why sets and dictionaries are useful for repeated lookups.
- Built dictionary indexes for faster record access.
- Applied intermediate Python concepts through guided practice and labs.

---

**Status:** ✅ Completed
