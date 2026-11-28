# DIGITALOCEAN STORAGE CORE ECOSYSTEM

Provider package for the Global Storage Core catalog.

## Registered product families
- DigitalOcean Spaces — OBJECT_STORAGE
- DigitalOcean Volumes — BLOCK_STORAGE
- DigitalOcean Droplet Backups — BACKUP_AND_RECOVERY

The manager exposes read-only provider metadata. It does not authenticate, connect, upload, download, delete, restore or verify account entitlements. Provider API adapters belong in the API/Provider Storage layers.
