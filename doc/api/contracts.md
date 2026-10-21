# API Contracts

## General Conventions

- JSON request and response bodies
- Explicit request validation
- Stable field names
- Clear HTTP status codes
- No database credentials or internal stack traces in responses

## Concepts

A concept should have a name and may include a description and topic. The backend remains responsible for validating required fields and uniqueness rules.

## Questions

Question responses should expose only the fields needed by the client. For MCQs, options should be represented as structured data. Do not reveal correct answers in student-facing question listings if the assessment workflow requires answer secrecy.

## Answer Submission

The answer endpoint should define:
- Question identifier or question context
- Submitted answer
- Evaluation result
- Feedback, when available

The current starter may use simple exact-match evaluation. That is not sufficient for general written or numerical physics answers; richer evaluation must be implemented and tested separately.

## Compatibility

When changing a shared request or response schema, update backend validation, frontend usage, tests, and this document in the same reviewed change.
