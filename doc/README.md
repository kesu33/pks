# Physics Knowledge Analysis System (PKS)

## 1. Project Overview

PKS is a higher-secondary Physics learning and knowledge-analysis web application. It supports physics concepts, questions, assessments, and future learning analytics.

## 2. Current Target Architecture

- Frontend: React + Vite
- Backend: Python + FastAPI
- ORM: SQLAlchemy
- Database: PostgreSQL
- Schema migrations: Alembic
- Testing: pytest
- Initial deployment: local Linux machine

SQLite is retained as the legacy data source during migration. Do not delete the original SQLite database until PostgreSQL data has been verified and backed up.

## 3. Main Components

```text
React frontend
     |
     | HTTP / JSON
     v
FastAPI backend
     |
     | SQLAlchemy
     v
PostgreSQL database
```

Alembic manages database schema changes. It must be used for future schema migrations rather than relying on application startup to create production tables.

## 4. Documentation Index

- `architecture/system-design.md` — architecture and boundaries
- `architecture/roadmap.md` — phased development plan
- `architecture/decisions.md` — architecture decisions
- `api/api-reference.md` — API endpoint overview
- `api/contracts.md` — request and response conventions
- `database/schema.md` — database tables and relationships
- `database/knowledge-model.md` — physics knowledge model
- `development/setup.md` — local Linux setup
- `development/ai-agents.md` — parallel AI development roles
- `development/git-workflow.md` — branches, reviews, integration
- `testing/test-plan.md` — test strategy
- `testing/security.md` — security practices
- `deployment/local-linux.md` — local deployment and operations

## 5. Data Migration Safety

1. Back up `data/physics.db`.
2. Create the PostgreSQL schema with Alembic.
3. Import SQLite records into PostgreSQL.
4. Compare record counts and inspect representative records.
5. Run backend and frontend tests.
6. Keep the SQLite backup until the new system is confirmed to work.

## 6. Development Rule

AI agents may propose code and tests, but changes to shared contracts, database schema, dependencies, and deployment configuration require human review before integration.
