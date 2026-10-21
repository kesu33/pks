# Testing and Quality Plan

## Levels
- Unit: scoring, conversions, validation, prerequisites.
- API: status codes, payloads, validation, errors.
- Integration: service-to-DB, transactions.
- Regression: keep tests for bugs.
- Scientific verification: compare with approved references.

## Current Commands
    source .venv/bin/activate
    pytest -q

## Minimum Coverage
Concepts: listing, creation, filtering, duplicates, empty/oversized, persistence.
Questions: empty collection, options structure, correct/incorrect, unknown id, invalid submission.
Problem solving (future): correct answer, unit conversion, dimensional mismatch, zero/negative, missing vars, ambiguous, unsupported, precision.
Assessment (future): scoring, partial credit, unanswered, duplicates, confidentiality, rubric.

## Definition of Done
Requirements met, tests cover success/failure, tests pass, contracts/docs updated, no unrelated changes, human review complete.

## CI Recommendation
Add CI after repo established: install deps, lint, tests, report. CI != scientific review.
