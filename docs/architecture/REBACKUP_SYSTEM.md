# Rebackup System

Status: **design documentation; independent replication is not established by this document.**

Purpose: create a second-generation, independently verified copy of existing backups.

## Scope
- Backup-of-backup workflows
- Independent destination and access boundary
- Replication verification and checksum comparison
- Retention of multiple generations
- Rebackup failure alerts and audit trail

## Suggested modules
- `generation/`
- `replication/`
- `integrity-checks/`
- `independent-targets/`
- `retention/`
- `audit/`

## Safety
Rebackup must not overwrite the only known-good backup. Keep source and secondary copies logically and, where possible, physically independent.
