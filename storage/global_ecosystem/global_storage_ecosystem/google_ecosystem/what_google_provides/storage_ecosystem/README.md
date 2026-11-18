# GOOGLE STORAGE ECOSYSTEM

Storage-owned taxonomy and metadata foundation for Google's storage-related products and services. This layer catalogs storage domains; provider API clients, OAuth, authentication, and external operations remain in the API/integration layer.

## Product storage ecosystems

1. [GOOGLE GMAIL STORAGE ECOSYSTEM](google_gmail_storage_ecosystem/README.md) — mailbox, messages, threads, labels, attachments, and export metadata.
2. [GOOGLE DRIVE STORAGE ECOSYSTEM](google_drive_storage_ecosystem/README.md) — My Drive, Shared Drives, files, folders, revisions, and lifecycle metadata.
3. [GOOGLE PERSONAL & CLOUD FILE STORAGE ECOSYSTEM](google_personal_and_cloud_file_storage_ecosystem/README.md) — account-level storage usage, Google One plan metadata, personal backup, and cloud file sync.
4. [GOOGLE PHOTO & VIDEO STORAGE ECOSYSTEM](google_photo_and_video_storage_ecosystem/README.md) — Google Photos media, albums, sharing, backup, and export metadata.

## Existing storage capability catalogs

The broader Google storage taxonomy also contains personal/cloud storage, photo/media storage, cloud object storage, file/network storage, block/performance storage, backup/recovery, data transfer/migration, business/enterprise storage, developer/AI storage, geographical scope, storage levels, and content classification/policy.

## Architecture boundary

- Storage owns storage identity, object metadata, taxonomy, lifecycle definitions, quota/health metadata, and storage-side governance.
- API/integration layers own OAuth flows, provider API clients, remote reads/writes, upload/download, and provider-specific operations.
- A catalog entry does not prove API availability, account entitlement, authorized connectivity, or working operations.
- Mark a provider connected only after authorized live health checks and end-to-end tests pass.

## Security

Never commit credentials, access tokens, private messages, personal files, photos, videos, or other personal data. Apply least privilege, encryption, consent, retention, deletion, audit, and jurisdictional controls.
