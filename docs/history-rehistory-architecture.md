# History / Rehistory Preservation Architecture

## Purpose
Keep an append-only commit-history preservation lane for changes integrated into `main`, with a second archive ref for redundancy.

## Branch roles
- `history/main`: chronologically advances with integrated `main` commits. The workflow uses normal (non-force) pushes so divergent history is not silently overwritten.
- `rehistory/main`: secondary archive ref advanced from `history/main`; also uses normal pushes and rejects divergence rather than rewriting.

## Automation
Workflow: `.github/workflows/history-rehistory-archive.yml`
- Runs on every push to `main` and can be manually run.
- Pushes `main` into `history/main` (fast-forward only).
- Pushes `history/main` into `rehistory/main` (fast-forward only).
- If a ref diverges, the job fails safely; it does not force-reset or erase archived commits.

## What is preserved
Integrated commits reachable from `main` are retained in the two archive refs, including their commit graph and merge history, as long as the refs remain.
GitHub's native PR, issue, branch, workflow-run, and artifact pages remain the source for discussion and run-specific metadata.

## Important boundary
This workflow archives **integrated main history**, not every unmerged feature branch or every workflow artifact. Unmerged work should remain in its branch/PR until reviewed and merged; use GitHub's native PR/issue/workflow pages for those records. This archive is not a substitute for periodic external backups.

## Recovery guidance
1. Inspect `main`, `history/main`, and `rehistory/main` before recovery.
2. Compare refs and identify the latest verified commit.
3. Never force-update the archive refs to resolve divergence. Investigate and reconcile with a reviewed PR or recovery procedure.
4. Preserve the archive branches while making repairs.
