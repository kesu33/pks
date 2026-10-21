# Git Workflow

## Branches

Use a short-lived branch per task, for example:

- `feat/concept-api`
- `feat/react-concepts`
- `db/postgres-migration`
- `test/api-regression`

## Change Process

1. Start from the latest agreed integration branch.
2. Make a small, focused change.
3. Run relevant tests and formatting checks.
4. Review the diff and remove secrets or local data.
5. Open a pull request or ask for human review.
6. Merge only after contract and regression checks pass.

## Database Migrations

- Give each schema change its own Alembic revision.
- Review generated migration scripts before applying them.
- Test upgrade behavior against a disposable database.
- Document rollback limitations; data migrations may not be reversible.
