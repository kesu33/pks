# Development Roadmap

## Phase 1 — Local Foundation

- Set up the Python virtual environment.
- Run FastAPI locally.
- Establish automated tests.
- Back up the existing SQLite database.

## Phase 2 — PostgreSQL Migration

- Install and configure PostgreSQL.
- Create the application database and least-privilege user.
- Install SQLAlchemy, a PostgreSQL driver, and Alembic.
- Apply the initial Alembic migration.
- Import SQLite records while preserving record IDs.
- Compare source and destination data.

## Phase 3 — React Frontend

- Run the React + Vite development server.
- Connect the frontend to FastAPI.
- Add loading, empty, and error states.
- Test the concepts and questions screens.

## Phase 4 — Assessment

- Add validated MCQ submissions.
- Add written answers and numerical problem-solving workflows.
- Store attempts and results.
- Design transparent scoring and feedback rules.

## Phase 5 — Learning Analytics

- Track concept-level performance.
- Identify knowledge gaps.
- Recommend practice questions.
- Validate analytics against representative test cases.

## Phase 6 — Production Preparation

- Add authentication and role-based authorization.
- Configure structured logging and error handling.
- Add backup and restore procedures.
- Review privacy, security, accessibility, and performance.
- Establish deployment and rollback procedures.

## Release Gate

A phase is complete only after its tests pass, documentation is updated, data integrity is checked where applicable, and a human reviewer approves the change.
