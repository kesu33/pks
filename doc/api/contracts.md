# Shared Contracts

## 1. Concept

    {
      "id": 1,
      "topic": "Mechanics",
      "name": "Newton's Second Law",
      "description": "Net force equals mass times acceleration.",
      "formula": "F = ma"
    }

## 2. Question (planned)

    {
      "id": 1,
      "type": "mcq",
      "topic": "Mechanics",
      "prompt": "What is the net force?",
      "options": [{"id":"A","text":"3 N"},{"id":"B","text":"6 N"}],
      "correct_option_id": "B",
      "explanation": "F = ma."
    }

## 3. Answer Submission (planned)

    { "question_id": 1, "answer": "B" }

## 4. Assessment Result (planned)

    {
      "question_id": 1,
      "is_correct": true,
      "score_awarded": 1.0,
      "max_score": 1.0,
      "feedback": "Correct.",
      "verification_status": "verified"
    }

## 5. Numerical Problem (planned)

    {
      "topic": "Mechanics",
      "known_values": [
        {"symbol":"m","value":2,"unit":"kg"},
        {"symbol":"a","value":3,"unit":"m/s^2"}
      ],
      "unknown": "F"
    }

## 6. Numerical Solution (planned)

    {
      "equation": "F = m*a",
      "substitution": "F = 2 kg * 3 m/s^2",
      "result": {"value":6,"unit":"N"},
      "steps": ["Identify known values","Apply Newton's second law"],
      "verification_status": "verified"
    }

## 7. Contract Rules

- JSON field names use snake_case.
- IDs are stable and unique.
- Quantities include units.
- Errors consistent machine-readable structure in future.
- Date/time ISO 8601 with timezone.
- Contract changes require tests and review.
