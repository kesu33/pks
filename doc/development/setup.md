# Local Linux Development Setup

## Requirements

- Linux
- Python 3 and venv support
- PostgreSQL
- Node.js and npm for the React frontend
- Git

## Backend

From the project root:

```bash
cd ~/pks
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-postgres.txt
```

Set `DATABASE_URL` in the current shell or load it from a local, untracked environment file. Do not commit real credentials.

Apply database migrations:

```bash
alembic upgrade head
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`.

## Frontend

In a second terminal:

```bash
cd ~/pks/frontend
npm install
npm run dev
```

Open the local URL printed by Vite. The Vite proxy must point to the running FastAPI service.

## Existing SQLite Data

Before importing the old data, back it up. Use the project migration script and verify record counts after the import. Keep the SQLite database until verification is complete.

## Common Checks

```bash
curl http://127.0.0.1:8000/health
pytest -q
```
