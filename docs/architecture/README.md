# Data Protection Architecture Index

Status: **architecture documentation only — implementation and production operation are not certified by these documents.**

This directory defines the boundaries and responsibilities of the data-protection domains.

## Domain map

- **BACKUP** creates point-in-time copies from approved sources.
- **REBACKUP** creates an independently protected second copy of verified backups.
- **RECOVERY** coordinates the incident plan, recovery objectives, and dependency order.
- **RERECOVERY** provides an independent fallback path when the first recovery attempt fails.
- **RESTORE** executes a selected restore to an isolated target and validates it before cutover.
- **STORAGE** owns physical storage targets, adapters, access, capacity, and lifecycle.
- **RESTORAGE** rebuilds, relocates, or rehydrates physical storage after failure or migration.
- **STORE** defines logical persistence contracts and repository interfaces.
- **DATABASE** owns database engines, schemas, migrations, transactions, and database-specific operations.
- **REDATABASE** provides a controlled secondary database reconstruction/recovery path.

## Responsibility boundaries

| Concern | Owning domain |
|---|---|
| Logical record/repository contract | STORE |
| Database engine, schema, migration, transaction | DATABASE |
| Physical object/file/block storage | STORAGE |
| Creating backup copies | BACKUP |
| Independent second backup copy | REBACKUP |
| Incident coordination and RPO/RTO | RECOVERY |
| Secondary incident recovery path | RERECOVERY |
| Restore execution to an isolated target | RESTORE |
| Physical storage reconstruction | RESTORAGE |
| Secondary database reconstruction | REDATABASE |

## Required implementation gates

No domain is considered production-ready until its implementation, configuration, access controls, automated tests, external destination, monitoring, and a successful restore/recovery exercise have been independently verified.

Never commit credentials, production database dumps, private user data, encryption keys, or connection strings to Git. Do not point these documents at production execution or enable destructive cutover without explicit approval.
