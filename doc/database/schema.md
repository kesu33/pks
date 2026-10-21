# Database Schema

## Current MVP Schema

### concepts
id INTEGER PK autoincrement, topic TEXT NOT NULL, name TEXT NOT NULL UNIQUE, description TEXT NOT NULL, formula TEXT nullable.

### questions
id INTEGER PK autoincrement, question TEXT NOT NULL, options TEXT JSON array, correct_answer TEXT NOT NULL, explanation TEXT NOT NULL.

Tables created at startup; no migration framework yet.

## Recommended Future Schema

topics, concepts, concept_relations, formulas, questions, question_options, assessment_attempts, attempt_answers, problem_solutions.

## Data Integrity

- Foreign keys for relationships.
- Indexes for common searches.
- Transactions for multi-step writes.
- Migrations for schema changes.
- No secrets in DB.

## Migration Strategy

1. Agree schema and tool.
2. Write versioned migration.
3. Test on temp DB.
4. Backup before migration.
5. Apply and verify.
6. Document rollback.
