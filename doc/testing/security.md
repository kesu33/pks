# Security Notes

## Secrets

- Keep database passwords and API secrets out of source control.
- Add local `.env` files to `.gitignore`.
- Do not include credentials in logs, screenshots, test fixtures, or documentation.

## Database

- Use a dedicated application database user.
- Grant only the permissions required by the app.
- Back up the database and periodically test restoration.
- Do not expose PostgreSQL directly to untrusted networks for local development.

## API

- Validate all incoming data.
- Add authentication and authorization before exposing student-specific records.
- Avoid returning stack traces or internal database details.
- Apply request size limits and rate limiting before public deployment.

## Student Data

Before storing identifiable student data, define data minimization, access control, retention, and deletion policies.

## Deployment

The local development server is not a production security boundary. Before public deployment, configure HTTPS, trusted hosts, production settings, monitoring, and a reviewed backup/restore process.
