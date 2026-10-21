# pks

A starter Python API for high-school Physics learning.

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

## Run

    uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs

## Tests

    pytest -q

## Initial endpoints

- GET /health
- GET /concepts
- POST /concepts
- GET /questions
- POST /answer

The initial answer checker is exact text matching, not an AI evaluator.
