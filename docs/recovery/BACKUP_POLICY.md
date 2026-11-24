# Backup Policy — SUPREMESETUHUB

Status: PROPOSED, NOT IMPLEMENTED.

## Scope
- Source code and Git refs (independent off-platform mirror)
- Production databases (encrypted snapshots + transaction logs where supported)
- Uploaded user content (versioned object storage)
- Infrastructure-as-code, deployment configuration, and secret *references*
- Audit logs and recovery documentation

## Proposed targets (validate against budget and architecture)
| Component | Backup cadence | Retention | Recovery objective |
| --- | --- | --- | --- |
| Git | On every approved merge; daily independent mirror | 90 days + releases | 30 min RTO |
| Database | Daily full + PITR/incremental as supported | 30 days | 15 min RPO; 4 h RTO |
| User files | Versioning + daily integrity check | 30–90 days | 1 h RPO |
| Config/IaC | On every change | 90 days | 30 min RTO |

## Minimum controls
- Backup storage in a separate security boundary/account; least-privilege credentials.
- Encrypt in transit and at rest; rotate keys and restrict restore privileges.
- Use immutable retention / object lock where supported and affordable.
- Alert on missed backups, failed verification, and retention expiry.
- Test one sample restore weekly and a full disaster recovery exercise monthly.
- Keep a dated inventory of backups, hashes, owners, and test outcomes.
- Set deletion and retention policy based on legal/privacy requirements.
- Do not commit tokens, passwords, or customer data into Git.

## Implementation prerequisites
Choose actual database, hosting, storage provider, backup service, budget, and compliance jurisdiction. Configure real backup jobs, credentials, monitoring, and restore tests before calling this production-ready.
