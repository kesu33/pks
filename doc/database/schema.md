# Database Schema

## Target Database

PostgreSQL is the target database. SQLAlchemy models define application mappings, while Alembic revisions manage schema evolution.

## Initial Tables

### concepts

Expected fields:
- `id`: primary key
- `name`: concept name
- `description`: explanation
- `topic`: topic or chapter classification

### questions

Expected fields:
- `id`: primary key
- `concept_id`: optional or required relationship to a concept
- `question`: question text
- `options`: structured options for MCQs
- `answer`: expected answer
- `question_type`: question format, if implemented

Always check `app/models.py` and the active Alembic revision for the actual schema.

## Migration Rules

1. Back up SQLite before migration.
2. Apply schema migrations before importing records.
3. Preserve primary keys where possible.
4. Check foreign-key integrity and row counts after import.
5. Do not delete the source database until the import is verified.
6. Create a new Alembic revision for future schema changes.
