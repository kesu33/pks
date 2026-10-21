# Architecture Decision Records

## ADR-001: React + FastAPI

**Decision:** Use React for the web interface and FastAPI for the API.

**Reason:** This separates presentation from backend logic and provides a clear JSON API boundary.

## ADR-002: PostgreSQL as the Target Database

**Decision:** Use PostgreSQL for the target application database.

**Reason:** It provides transactions, constraints, concurrent access, and a robust foundation for future growth.

**Migration rule:** Retain SQLite as a read-only migration source until data verification is complete.

## ADR-003: SQLAlchemy

**Decision:** Use SQLAlchemy for database access.

**Reason:** It provides mapped models, session management, and database operations without embedding raw SQL throughout API handlers.

## ADR-004: Alembic

**Decision:** Use Alembic for schema migrations.

**Reason:** Database schema changes should be reviewable, versioned, and repeatable.

## ADR-005: Human Approval for AI Changes

**Decision:** AI workers can draft code and tests, but shared contracts, migrations, dependencies, and release changes require human review.
