# SUPREMESETUHUB Disaster Recovery Runbook

Status: DRAFT — procedures must be tested before production reliance.

## Safety rules
- Never force-push production branches as a recovery shortcut.
- Preserve the incident commit and a known-good recovery ref.
- Stop deployments and destructive automation before investigating.
- Verify the exact affected component: Git tree, application deployment, database, or object storage.
- Never put production secrets, customer records, or database dumps into Git.

## Git repository incident
1. Record the current main SHA and incident timeline.
2. Compare the affected commit against a known-good SHA.
3. Create an immutable recovery tag or backup branch from the known-good commit.
4. Prepare a forward-only restore commit whose parent is the current main HEAD and whose tree is the known-good tree, or use a reviewed revert PR.
5. Verify the restored tree SHA, critical files, CI checks, and deployment configuration.
6. Deploy to staging first, then production with an approved rollback window.
7. Document root cause and prevent recurrence with branch rules.

## Database recovery
1. Declare incident and isolate affected writers.
2. Identify most recent consistent snapshot and transaction log / PITR window.
3. Restore into an isolated database, never overwrite production first.
4. Validate schema, row counts, referential integrity, and representative user records.
5. Plan controlled cutover and communicate the actual data-loss window.
6. Verify application access and monitor errors after cutover.

## Uploaded files
- Restore from versioned, encrypted object storage with access controls.
- Check references in database against restored object versions.

## Restore evidence
Record incident ID, approver, source snapshot, checksum, restore start/end, tests, RPO, RTO, and postmortem link.
