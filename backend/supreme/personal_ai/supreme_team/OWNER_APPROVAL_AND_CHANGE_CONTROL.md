# OWNER APPROVAL AND CHANGE CONTROL

## Protected action workflow

1. Identify the exact resource and current state.
2. Record why a change is needed and who requested it.
3. Prepare a proposal showing the exact old path/value and proposed new path/value.
4. List affected systems, dependencies, users, financial impact, security impact, and downtime risk.
5. Provide a backup/checkpoint and tested rollback procedure.
6. Submit the proposal to the Owner.
7. Record explicit approval tied to the exact proposal/version.
8. Execute only the approved scope.
9. Verify the result and record evidence.
10. Report completion and any deviation immediately.

## GitHub-specific controls

- No direct commits to the protected/default branch for protected changes.
- Use a dedicated branch and pull request for review.
- A PR is a proposal, not permission to merge.
- Do not rename, move, delete, or overwrite existing files without explicit Owner approval.
- Do not merge or deploy without explicit Owner approval.
- Preserve the previous version and provide a rollback commit or recovery instructions.
- If the approval does not exactly match the proposed diff, stop and request clarification.

## Required approval record

- Change ID
- Requester and responsible role
- Repository and exact file/resource paths
- Before state and proposed after state
- Business reason
- Impact and risk assessment
- Backup and rollback plan
- Proposal/PR link and commit SHA
- Owner approval reference and timestamp
- Execution evidence and verification result

No approval record means no protected change.
