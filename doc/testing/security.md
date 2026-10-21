# Security and Privacy Guidelines

## Development
- Bind dev server to localhost.
- No .env/credentials/keys in Git.
- Keep venv and db out of Git.
- Update deps deliberately.

## API
- Auth where user data exists.
- Authorization on private resources.
- Validate payload types/sizes/ranges.
- Rate limiting where appropriate.
- CORS narrowly configured.
- HTTPS in deployment.
- Safe error messages.

## Database
- Parameterized SQL.
- Constraints and transactions.
- Backup before migrations.
- No db files via static serving.
- Retention/deletion rules.

## AI
- Treat user text and docs as untrusted.
- Validate model outputs via schema.
- No executing generated code/SQL without review.
- Verify calculations independently.
- Mark uncertain answers honestly.
- Server-side credentials.

## Educational Integrity
- Keep answer keys private during assessments.
- Explain scoring.
- Educator review of auto-grading.
- Track sources/corrections.

## Learner Privacy
- Collect only necessary data.
- Define access/retention/deletion.
- Avoid logging full answers.
- Restrict identifiable records.
- Follow privacy/child-protection rules.

## Release Gate
No public deploy until auth, authorization, validation, logging, backup, recovery reviewed.
