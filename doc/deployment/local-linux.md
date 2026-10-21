# Local Linux Deployment

## Services

Run PostgreSQL, FastAPI, and the Vite frontend locally during development.

## Startup Order

1. Start PostgreSQL.
2. Load the backend environment configuration.
3. Apply Alembic migrations.
4. Start FastAPI.
5. Start the React/Vite development server.

## Health Checks

```bash
curl http://127.0.0.1:8000/health
```

Use the URL printed by Vite to open the frontend.

## Backups

Back up PostgreSQL before schema or data migration work. Keep the original SQLite database until its records have been compared with PostgreSQL.

## Important

`uvicorn --reload` and the Vite development server are development tools, not production deployment configurations. A production deployment needs a separate reviewed setup.
