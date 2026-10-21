# Parallel AI Development Roles

Use four workers with separate branches or Git worktrees. A human reviewer approves changes before integration.

## Worker 1 — Backend/API

Owns FastAPI endpoints, validation, service logic, and API tests. Must coordinate shared contracts before changing them.

## Worker 2 — Database

Owns SQLAlchemy models, Alembic migrations, data migration, and database integrity tests. Must never run destructive migration commands against the only copy of user data.

## Worker 3 — Frontend

Owns React components, API integration, form states, loading/error states, and frontend tests.

## Worker 4 — QA/Documentation

Owns test planning, regression checks, API contract review, and documentation updates. May identify defects and propose fixes but must not silently rewrite another worker's contract.

## Shared Rules

- Assign clear file ownership.
- Agree on request/response contracts first.
- Do not let two workers edit the same migration simultaneously.
- Keep work isolated in branches or worktrees.
- Require tests and human review before merging.
- Never commit credentials, local database files, or `.env` secrets.
