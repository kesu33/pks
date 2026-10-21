# System Architecture

## 1. Purpose

PKS is a learning and research platform for higher-secondary Physics.
It will organize Physics knowledge and support concept discovery,
MCQ assessment, written answers and numerical problem solving.

## 2. Architectural Principles

- Modular components with explicit interfaces.
- Scientific correctness and traceable explanations.
- Automated testing and human approval.
- Reproducible problem-solving steps.
- Separation of educational content from application logic.
- No unsupported claims of AI accuracy.

## 3. Current MVP

The initial implementation contains:
- FastAPI application in `app/main.py`
- SQLite persistence in `data/physics.db`
- Concept listing and creation
- Sample MCQ retrieval
- Exact-text answer checking
- pytest tests in `tests/test_api.py`

The current answer endpoint is not an AI evaluator.
The initial implementation does not yet provide authentication,
a student dashboard, a knowledge graph or an LLM integration.

## 4. Target Architecture

    Client / Web UI
          |
          v
    FastAPI Application
          |
          +-- Concept Service
          +-- Assessment Service
          +-- Problem Solver
          +-- Progress Service
          |
          v
    Repository / Data Access Layer
          |
          v
    SQLite (MVP) -> PostgreSQL (future)

Future optional components:
- Physics knowledge graph
- LLM adapter for explanations and written-answer feedback
- Symbolic mathematics and numerical verification
- Background jobs for document processing
- Search and retrieval over approved educational materials

## 5. Module Responsibilities

### API layer
Validates input, calls services and returns documented responses.

### Knowledge service
Manages concepts, topics, formulas, units, prerequisites and references.

### Assessment service
Creates assessments, records attempts and computes scores using
explicit marking rules.

### Problem solver
Represents known quantities, unknown quantities, equations, units,
solution steps and verification results.

### AI adapter
Calls an optional model provider. It must not be the sole authority
for numerical correctness.

### Persistence layer
Stores validated records and manages transactions.

## 6. Request Flow

1. Client submits a request.
2. API validates the payload.
3. Service applies domain rules.
4. Data layer reads or writes records.
5. Service verifies the result.
6. API returns a structured response.
7. Tests validate expected behavior.

## 7. Error Handling

Use appropriate HTTP status codes:
- 200: successful read or operation
- 201: resource created
- 400: invalid request
- 404: resource not found
- 409: duplicate or conflicting resource
- 422: request validation failure
- 500: unexpected server error

Do not return stack traces, credentials or private internal details
to API clients.

## 8. Architecture Evolution

Do not introduce distributed services, a graph database or a large
LLM framework until a tested use case requires it. Keep the MVP
small and establish stable contracts before parallel development.
