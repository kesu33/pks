# API Reference

Run the backend locally and open `/docs` for FastAPI's interactive API documentation.

## Current Starter Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Basic service information |
| GET | `/health` | Service/database health check |
| GET | `/concepts` | List concepts; may accept a topic filter |
| POST | `/concepts` | Create a concept |
| GET | `/questions` | List questions |
| POST | `/answer` | Submit an answer for evaluation |

The exact request fields and response formats are defined by the running application and its Pydantic models. Verify them in `/docs` after each API change.

## Error Handling

Use appropriate HTTP status codes and avoid returning database credentials, stack traces, or internal secrets to clients.
