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
