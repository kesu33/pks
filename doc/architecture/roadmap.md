# Development Roadmap

## Phase 0 — Working Foundation
- [x] FastAPI application
- [x] SQLite database
- [x] Concept endpoints
- [x] Sample MCQ endpoint
- [x] Basic answer checking
- [ ] Confirm a clean test run
- [ ] Establish CI and branch protection

## Phase 1 — Reliable Domain Model
- Define concept, formula, unit and question schemas.
- Add stable identifiers and timestamps.
- Add migrations before changing production schemas.
- Validate formula and answer data.
- Add duplicate, invalid-input and persistence tests.

## Phase 2 — Assessment
- Support multiple-choice questions.
- Add written-answer rubric data structures.
- Record student attempts and score breakdowns.
- Separate marking policy from HTTP endpoint code.
- Test partial credit and unanswered questions.

## Phase 3 — Numerical Problem Solving
- Define structured problem inputs and outputs.
- Parse quantities with units.
- Check dimensional consistency.
- Solve supported equation types.
- Independently verify numerical results.
- Return understandable solution steps.

## Phase 4 — Knowledge Relationships
- Add prerequisite and related-concept links.
- Prevent invalid or cyclic prerequisite relationships.
- Add topic and concept search.
- Build prerequisite-based learning recommendations.

## Phase 5 — AI Assistance
- Add a provider-neutral model adapter.
- Require structured outputs and schema validation.
- Ground generated explanations in approved materials.
- Track model, prompt version and evaluation results.
- Clearly label uncertain or unverified answers.

## Phase 6 — Student Experience
- Build a web interface.
- Add accounts only after authentication design and tests.
- Track learning progress and weak topics.
- Support Bengali and English content.
- Add accessible and mobile-friendly layouts.

## Release Criteria
- Tests pass in a clean environment.
- API and data contracts are documented.
- Security checks are complete.
- Database migrations are repeatable.
- Human reviewer approves the changes.
- Known limitations are documented.
