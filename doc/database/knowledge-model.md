# Physics Knowledge Model

## Goal

Represent Physics knowledge in structured form for learning, search, assessment and numerical problem solving.

## Main Entities

Subject, Topic, Concept, Formula, Quantity, Unit, Question, Problem, Explanation, Relation.

## Example Concept

    {
      "name": "Newton's Second Law",
      "topic": "Mechanics",
      "description": "The net force equals mass times acceleration.",
      "formula": "F = ma",
      "variables": [
        {"symbol":"F","meaning":"net force","unit":"N"},
        {"symbol":"m","meaning":"mass","unit":"kg"},
        {"symbol":"a","meaning":"acceleration","unit":"m/s^2"}
      ],
      "prerequisites": ["Mass","Acceleration","Net force"]
    }

## Knowledge Relationships

acceleration related to velocity; Newton's Second Law uses mass and acceleration; momentum depends on mass and velocity.

Prerequisite edges form DAG for learning sequence. Related-to may be cyclic.

## Formula Requirements

Symbolic expression, variable definitions, SI units, assumptions, derivation/source, example use, dimensional consistency.

## Numerical Reasoning Pipeline

1. Parse problem.
2. Extract known values and units.
3. Identify unknown.
4. Select formula, verify assumptions.
5. Convert units.
6. Check dimensions.
7. Compute.
8. Verify independently.
9. Return steps, final value, unit.
10. State limitations.

## Source and Quality Metadata

Track source title, author, edition/date, page/section, reviewer, review date, content version. Use authorized materials.
