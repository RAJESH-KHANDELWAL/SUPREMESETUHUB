# GOOGLE CLOUD STORAGE CORE ECOSYSTEM

Provider package for the Global Storage Core catalog.

## Registered product families
- Google Cloud Storage — OBJECT_STORAGE
- Google Cloud Filestore — MANAGED_FILE_STORAGE
- Google Persistent Disk — BLOCK_STORAGE
- Backup and DR Service — BACKUP_AND_RECOVERY
- Storage Transfer Service — DATA_TRANSFER

The manager exposes read-only provider metadata. It does not authenticate, connect, upload, download, delete, restore or verify account entitlements. Provider API adapters belong in the API/Provider Storage layers.
