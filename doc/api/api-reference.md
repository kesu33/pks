# API Reference

Base URL for local development: `http://127.0.0.1:8000`

Interactive API documentation: `/docs`

## GET /

Returns project identity and status.

## GET /health

Returns a simple health status.

## GET /concepts

Lists all concepts. Optional query `topic`.

## POST /concepts

Creates a concept. Success 201, duplicate 409.

## GET /questions

Lists available questions.

## POST /answer

Submits an answer. Current: exact case-insensitive text match.

## Current Limitations

- No authentication or user-specific attempts.
- No pagination or versioned API.
- Questions not managed via public creation endpoint.
- Correct answers exposed with result.
- Error response formats not standardized.
