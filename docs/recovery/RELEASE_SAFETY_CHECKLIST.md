# Production Release Safety Checklist

Status: REQUIRED PROCESS PROPOSAL.

- [ ] Protect main with PR-only changes and restricted bypass permissions.
- [ ] Require at least one independent reviewer and passing CI.
- [ ] Require status checks for unit tests, integration tests, lint, secret scan, and destructive-diff guard.
- [ ] Fail CI on unexpected mass deletions until explicitly approved.
- [ ] Preserve a known-good release tag and tested rollback package.
- [ ] Build and test in staging before production promotion.
- [ ] Validate database migrations and backward compatibility.
- [ ] Verify backups and restore point before schema/data migrations.
- [ ] Deploy progressively; monitor health, latency, error rates, and saturation.
- [ ] Keep a clear rollback owner, command, and decision threshold.
- [ ] Verify auth, API, storage, and core user journeys after release.

Note: This checklist does not itself configure GitHub rules, backups, or deployment.
