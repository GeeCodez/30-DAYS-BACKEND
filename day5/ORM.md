# Django ORM Summary

## What the ORM Is
The Django ORM (Object Relational Mapper) is a system that allows developers to interact with databases using Python code instead of raw SQL. It converts Python instructions into SQL queries internally.

## Why the ORM Exists
- Increases developer productivity by reducing manual SQL writing.
- Makes applications database-agnostic so you can switch engines without rewriting logic.
- Provides built-in protection against SQL injection.
- Keeps code cleaner and more maintainable by representing tables as Python classes.

## Core Components
### Models
Python classes that represent database tables.  
Fields inside models represent database columns.

### QuerySets 
A QuerySet is a collection of records retrieved from the database.  
It is lazy, chainable, and optimized.

### Managers
Managers (like `objects`) are interfaces through which queries are executed.  
Example: `Student.objects.all()`.

## ORM Versus SQL
- Creating a record:
  - SQL: `INSERT INTO students (...)`
  - ORM: `Student.objects.create(...)`
- Retrieving data:
  - SQL: `SELECT * FROM students`
  - ORM: `Student.objects.all()`
- Updating:
  - SQL: `UPDATE students SET ...`
  - ORM: modify object then call `.save()`
- Deleting:
  - SQL: `DELETE FROM students WHERE ...`
  - ORM: `.filter(...).delete()`

## Internal Workflow
1. You write Python query code.
2. ORM translates it into SQL.
3. Database executes the SQL.
4. Django converts the results into Python objects.
5. You work with Python objects, not raw rows.

## Essential Query Methods
- `get()` – returns one object.
- `filter()` – returns multiple objects as a QuerySet.
- `exclude()` – opposite of filter.
- `create()` – creates and saves a record.
- `save()` – updates an existing record.
- `delete()` – removes records.
- `all()` – retrieves all records.

## Common Field Lookups
- `age__gt=18` – greater than.
- `age__lt=18` – less than.
- `name__startswith="A"` – string prefix match.
- `created_at__date="2025-03-01"` – date filtering.

## Practical Example
```python
Student.objects.create(name="Ama", age=17)
Student.objects.filter(age__gt=18)
student = Student.objects.get(id=1)
student.age = 20
student.save()
Student.objects.filter(age__lt=10).delete()
