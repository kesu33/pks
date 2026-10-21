# Git and Human Approval Workflow

## Branch Naming
main, feat/knowledge-base, feat/assessment, feat/problem-solver, test/integration.

## Initial
    cd /mnt/external/proj/pks
    git init
    git add .
    git commit -m "Initial PKS starter"

## Feature branch
    git switch -c feat/knowledge-base

## Review
    git status
    git diff --check
    git diff
    pytest -q

## Worktrees
    git worktree add ../pks-knowledge -b feat/knowledge-base
    git worktree add ../pks-assessment -b feat/assessment
    git worktree add ../pks-solver -b feat/problem-solver
    git worktree add ../pks-quality -b test/integration

## PR Checklist
- Scope matches.
- No secrets/db files.
- Contracts compatible.
- Tests pass.
- Scientific assumptions reviewed.
- Docs updated.
- Human approved.

## Recovery
Use git status/diff before discarding. Avoid reset --hard unless intended.
