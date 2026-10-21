# Parallel AI Development Workflow

## Roles
- Worker 1: Knowledge Base
- Worker 2: Assessment
- Worker 3: Numerical Problem Solver
- Worker 4: Quality and Integration
- Human Maintainer: architecture, contracts, review, merge

## Shared Rules
1. Read doc/ before coding.
2. Inspect existing code/tests.
3. Separate branches/worktrees.
4. Tests for each change.
5. Document assumptions.
6. No secrets.
7. Human approval before merge.

## Standard Worker Prompt
You are an implementation worker for PKS. Read doc/README.md, system-design.md, contracts.md. Task: [INSERT]. Constraints: follow contracts, no unrelated changes, tests, explicit physics. Before finishing: summary, changed files, commands, results, limitations.

## Integration Protocol
1. Maintainer assigns tasks.
2. Workers on separate branches.
3. Submit summaries/diffs.
4. Quality runs tests.
5. Maintainer reviews.
6. Approve and merge.
7. Update docs.

## Conflict Resolution
Maintainer decides API names, DB ownership, formula semantics, dependencies, scoring, security.
