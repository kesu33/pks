# Test Plan

## Backend Tests

- Health endpoint responds correctly.
- Concepts can be listed and created with valid input.
- Invalid concept input is rejected.
- Questions return the documented schema.
- Answer evaluation handles valid and invalid submissions.
- Database failures do not expose secrets.

## Database Tests

- Alembic migrations work on a clean test database.
- Foreign keys and uniqueness constraints behave as intended.
- SQLite import preserves expected IDs and values.
- Source and target row counts are compared.
- Re-running the import does not create unintended duplicates.

## Frontend Tests

- Concepts and questions load successfully.
- Loading, empty, and API error states are visible.
- Forms validate required fields.
- API response changes are handled safely.

## Test Data Isolation

Use a dedicated test database or temporary test database. Tests must not rely on existing local production-like records or fixed names in a persistent database.

## Release Gate

Run the full test suite, review migration scripts, check the frontend build, and verify the app manually before approving a release.
