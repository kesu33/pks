# PKS System Architecture

## Goals

- Provide a web-based Physics learning platform for higher-secondary students.
- Support concepts, questions, answers, and assessments.
- Keep the system maintainable as usage grows from approximately 20 to 1,000 users.
- Preserve existing SQLite data during the PostgreSQL transition.

## Technology Stack

| Layer | Technology | Responsibility |
|---|---|---|
| Frontend | React + Vite | User interface |
| API | FastAPI | Validation and business logic |
| ORM | SQLAlchemy | Database access |
| Database | PostgreSQL | Persistent application data |
| Schema migrations | Alembic | Versioned schema changes |
| Tests | pytest | Automated backend tests |

## Request Flow

1. The user interacts with the React application.
2. React sends HTTP requests to FastAPI.
3. FastAPI validates input and runs application logic.
4. SQLAlchemy queries or updates PostgreSQL.
5. FastAPI returns JSON.
6. React renders the result.

## Architectural Boundaries

- Frontend code must not connect directly to PostgreSQL.
- API handlers must validate incoming data.
- Database access must use SQLAlchemy sessions.
- Database schema changes must be versioned with Alembic.
- Secrets and database passwords must not be committed to Git.
- Tests must use a separate test database or isolated test setup.

## Current Scope

The initial scope includes concepts, questions, health checks, and answer submission. Authentication, user progress, advanced assessment, search, analytics, and research workflows are future features unless implemented explicitly.

## Reliability

- Keep regular database backups.
- Use environment variables for configuration.
- Test migrations before applying them to important data.
- Verify database connectivity and API health after deployment.
