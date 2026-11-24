# Global Backup Ecosystem

Canonical package for backup-domain infrastructure capabilities.

- Parent module: `backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/backup/`
- Ecosystem path: `backend/infrastructure/global_ecosystem/global_infrastructure_ecosystem/backup/global_ecosystem/global_backup_ecosystem/`
- Status: local manifest and integrity verification available; backup execution is not enabled

## Implemented capability

`backup_manifest.py` builds a sorted SHA-256 manifest for explicitly selected
regular files and verifies file presence, byte size, and digest. It rejects
duplicate paths, path traversal, and symbolic links. The JSON writer uses an
atomic replace within the chosen destination directory.

## Existing service boundary

The parent `backup/service.py`, `model.py`, and `controller.py` remain the
canonical backup-record CRUD layer. This package does not duplicate those
services or imply that a record represents a completed physical backup.

## Not yet implemented

- Copying data to a backup destination
- Provider credentials, provider integrations, or scheduled jobs
- Encryption/key management and immutable retention
- Incremental backup orchestration and operational restore execution

Never store credentials, encryption keys, production dumps, or private user
data in this repository. Select and protect an external manifest destination
according to the deployment's security policy.
