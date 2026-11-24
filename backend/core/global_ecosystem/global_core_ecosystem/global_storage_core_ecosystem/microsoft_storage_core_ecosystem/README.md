# MICROSOFT STORAGE CORE ECOSYSTEM

Provider package for the Global Storage Core catalog.

## Registered product families
- Azure Blob Storage — OBJECT_STORAGE
- Azure Files — MANAGED_FILE_STORAGE
- Azure Managed Disks — BLOCK_STORAGE
- Azure NetApp Files — ENTERPRISE_FILE_STORAGE
- Azure Backup — BACKUP_AND_RECOVERY
- OneDrive — PERSONAL_FILE_SYNC
- SharePoint document libraries — COLLABORATIVE_DOCUMENT_STORAGE

The manager exposes read-only provider metadata. It does not authenticate, connect, upload, download, delete, restore or verify account entitlements. Provider API adapters belong in the API/Provider Storage layers.
