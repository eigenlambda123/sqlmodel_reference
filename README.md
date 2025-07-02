# SQLModel Reference

This is my personal reference repo for learning and using **SQLModel**, the hybrid ORM by FastAPI’s creator that blends **Pydantic** and **SQLAlchemy**.
It includes focused examples, async patterns, and clean model structures for building robust APIs.

---

## Structure

Each folder contains practical examples and minimal working files.

```
/
├── 00_intro_modeling/       # Basic models, table creation, Pydantic vs Table
├── 01_crud_sync/            # Sync CRUD operations with SQLModel + SQLite
├── 02_crud_async/           # AsyncEngine, AsyncSession, select, joins
├── 03_relationships/        # One-to-many, many-to-many, joins
├── 04_fastapi_async/        # Async SQLModel with FastAPI (Blog API)
├── db/                      # Async DB engine and session utils
├── models/                  # Shared model definitions across examples
├── tests/                   # Testing SQLModel code (sync & async)
└── requirements.txt
```

---

## Why This Exists

I built this to:

* Understand how SQLModel fits into real FastAPI backends
* Learn both sync and async DB patterns
* Have a clean, reusable reference for future projects

---

## Usage

You can:

* Run each folder as a standalone demo
* Copy the DB/session setup into real APIs
* Use this as a playground while exploring advanced topics like joins, migrations, async patterns

---

## Topics Covered (WIP)

* Defining SQLModel models and fields
* Using `table=True` vs `table=False` (for response-only models)
* Basic and advanced CRUD operations
* Async SQLModel with `AsyncEngine` + `AsyncSession`
* ForeignKey relationships and joins
* SQLModel with FastAPI (async)
* Testing async database code

---

> Feel free to fork, copy, or adapt this structure for your own SQLModel learning journey.
