# AMAZON WEB SERVICES STORAGE CORE ECOSYSTEM

Provider package for the Global Storage Core catalog.

## Registered product families
- Amazon S3 — OBJECT_STORAGE
- Amazon S3 Glacier storage classes — ARCHIVE_OBJECT_STORAGE
- Amazon EFS — MANAGED_FILE_STORAGE
- Amazon FSx — MANAGED_FILE_STORAGE
- Amazon EBS — BLOCK_STORAGE
- AWS Storage Gateway — HYBRID_STORAGE
- AWS Backup — BACKUP_AND_RECOVERY

The manager exposes read-only provider metadata. It does not authenticate, connect, upload, download, delete, restore or verify account entitlements. Provider API adapters belong in the API/Provider Storage layers.
