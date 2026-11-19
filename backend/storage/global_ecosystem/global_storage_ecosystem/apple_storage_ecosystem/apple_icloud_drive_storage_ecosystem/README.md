# Apple iCloud Drive Storage Ecosystem

## Purpose
iCloud Drive file and folder metadata, document organization, synchronization state declarations, sharing references and lifecycle classification. Do not assume a general-purpose public iCloud Drive API exists.

## Package boundary
This child package owns the product-specific storage taxonomy and metadata classification for `APPLE_ICLOUD_DRIVE`. It remains under the canonical `apple_storage_ecosystem/` parent. Shared backend infrastructure, central persistence, credentials and Apple API clients are not duplicated here.

## Classification directories
- `domains/` — applicable business and personal-use domains; classification only
- `geography/` — Bharat, regional and global jurisdiction references
- `maturity_levels/` — normal, professional, advanced, enterprise and supreme organizational maturity labels

## Integration boundary
Provider API support, product availability, account entitlement, authorization scopes, regional restrictions and permitted data operations must be independently verified. Do not assume this product has a public API for arbitrary personal data. Keep connection state `NOT_CONFIGURED` and storage operations disabled until supported interfaces, authorization, live health checks and end-to-end tests are confirmed.

## Security
Apply least privilege, encryption, secure secret management, audit logs, data minimization, retention/deletion controls, consent and applicable jurisdictional requirements. Never commit credentials, tokens or personal content.

## Readiness
`CATEGORY_FOUNDATION_SCAFFOLD` describes catalog documentation only; it is not a live connection or working upload/download/sync/delete/backup/restore implementation.
