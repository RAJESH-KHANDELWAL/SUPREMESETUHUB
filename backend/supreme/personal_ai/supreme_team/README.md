# SUPREME TEAM

Central directory for SUPREME team identities, ownership governance, and organizational designations.

## Structure

- `supreme_owner_admin_founder_ceo/` — owner/admin/founder/CEO authority and the four owner brand profiles.
- `cmd/` — CMD designation only.
- `md/` — MD designation only.
- `directors/` — director-level designations.
- `executives/` — executive-level designations.
- `managers/` — management-level designations.
- `advisors/` — advisory designations.
- `team_members/` — other team-member identities.

Each designation has its own package. The four owner profiles remain separate identity packages; they are not merged into one profile.

## Governance

This directory defines identity and role structure only. It does not grant operational permissions, financial authority, or access to secrets. Those must be enforced by the existing authorization and permissions layers.

## Operating governance

- [Governance charter](GOVERNANCE_CHARTER.md)
- [Owner approval and change control](OWNER_APPROVAL_AND_CHANGE_CONTROL.md)
- [Daily Owner reporting standard](DAILY_OWNER_REPORTING_STANDARD.md)
- [Role accountability matrix](ROLE_ACCOUNTABILITY_MATRIX.md)

CMD is the highest delegated operational authority and reports to the Owner. Owner approval is mandatory for protected rename, move, delete, overwrite, merge, deployment, structural, access-control, and other reserved changes. Daily reports must include exact before/after locations and evidence for every verified movement or change.

## Management service

- `management.py` provides persistent task tracking, department daily reports, protected-change proposals, Owner-only approval decisions, execution evidence records, and an Owner-only audit view.
- `tests/test_management.py` covers authenticated-actor rejection, Owner approval, approved-state matching, task completion evidence, daily-report completeness, and audit access.
- Protected GitHub/filesystem/database changes are **not executed by this service**. CMD can coordinate execution only after the exact proposal is Owner-approved, then record evidence. A separate authenticated executor and GitHub branch protection are required before production mutation endpoints are enabled.
- The service uses the existing `DatabaseService` and its configured `SUPREME_DB_PATH` (default `data/supreme.db`).

The API must obtain Actor identity from a trusted authentication dependency. Never accept `actor_id`, `role`, or `authenticated` from a public request body.

## Authenticated management API

The existing Personal AI router now includes the Team Management router. The API uses the existing bearer-session validator and a server-side role map.

Before enabling access, configure `SUPREME_TEAM_ROLE_MAP` in the server environment as JSON keyed by authenticated usernames, for example:

```json
{"owner-login":"OWNER","cmd-login":"CMD","md-login":"MD"}
```

Replace these example usernames with actual, verified account usernames. Do not put this mapping in a public repository, request payload, or frontend bundle. Assign exactly one trusted Owner account first. Do not assign CMD/MD until those people have been formally appointed and their accounts secured. If the variable is absent or a user has no role assignment, access is denied.

### Endpoints

- `GET /api/v1/supreme/personal-ai/team-management/status`
- `GET|POST /api/v1/supreme/personal-ai/team-management/tasks`
- `GET /api/v1/supreme/personal-ai/team-management/tasks/{task_id}`
- `PATCH /api/v1/supreme/personal-ai/team-management/tasks/{task_id}/status`
- `POST /api/v1/supreme/personal-ai/team-management/change-proposals`
- `GET /api/v1/supreme/personal-ai/team-management/change-proposals/{proposal_id}`
- `POST /api/v1/supreme/personal-ai/team-management/change-proposals/{proposal_id}/owner-decision`
- `POST /api/v1/supreme/personal-ai/team-management/change-proposals/{proposal_id}/execution-record`
- `GET|POST /api/v1/supreme/personal-ai/team-management/daily-reports`
- `GET /api/v1/supreme/personal-ai/team-management/daily-reports/consolidated?report_date=YYYY-MM-DD`
- `GET /api/v1/supreme/personal-ai/team-management/audit`

All endpoints require a valid existing Bearer session. CMD can coordinate tasks and submit/read consolidated reports. Only the Owner role can approve/reject protected changes and read the audit log. Completion requires evidence. Execution recording requires an approved proposal and an exact match with the approved after-state.

**Deployment gate:** the existing `backend/app/main.py` already imports and mounts `backend.supreme.personal_ai.api.router`. Still configure the private role map, run the test suite, and enable GitHub branch protection / required reviews before treating this as production-ready. The API code is committed. Runtime deployment must still be verified separately. The service records approvals and evidence; it does not itself rename, move, delete, merge, or deploy repository resources.


## CI and deployment configuration

- Workflow: `.github/workflows/supreme-team-management.yml` (compile + unittest on matching pushes/PRs and manual dispatch).
- Environment template: `backend/.env.example` contains an empty `SUPREME_TEAM_ROLE_MAP={}`. Configure the real mapping only in the private hosting environment after verifying the application usernames and appointing role holders.
- Branch-protection status could not be read with the current GitHub integration (403); configure/verify required reviews and status checks in repository Settings as the owner.
- The latest SUPREME Team Management workflow completed successfully, including module compilation and the unit-test step. See the Actions run linked from the repository's Actions tab.
