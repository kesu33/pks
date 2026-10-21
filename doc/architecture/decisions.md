# Architecture Decision Records

## ADR-001: Modular Monolith for MVP
Status: Accepted. Context: early stage needs small testable foundation. Decision: one FastAPI app with domain services. Consequences: simpler setup, clear interfaces needed.

## ADR-002: SQLite for MVP
Status: Accepted for local dev. Move to PostgreSQL when multi-user/deployment/concurrency requires.

## ADR-003: Human Approval for AI-Generated Code
Status: Accepted. Separate branches/worktrees, tests, diffs, human review before merge.

## Future Decisions
LLM providers, knowledge graph storage, auth, frontend framework, production DB, scientific computation libs.
