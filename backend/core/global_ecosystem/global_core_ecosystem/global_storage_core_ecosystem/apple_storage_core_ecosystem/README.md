# APPLE STORAGE CORE ECOSYSTEM

Provider package for the Global Storage Core catalog.

## Registered product families
- iCloud Drive — PERSONAL_FILE_SYNC
- iCloud Photos — PHOTO_LIBRARY_STORAGE
- iCloud Backup — DEVICE_BACKUP

The manager exposes read-only provider metadata. It does not authenticate, connect, upload, download, delete, restore or verify account entitlements. Provider API adapters belong in the API/Provider Storage layers.
