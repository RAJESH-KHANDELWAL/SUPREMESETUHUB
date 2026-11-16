# GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM — Root Catalog and Category Packages

This provider-neutral root follows the Google Storage Ecosystem root-and-child architecture. It owns the individual-storage taxonomy and category index; each taxonomy category is implemented as a separate child package using the Google category-package layout. This is a metadata foundation, not a live personal cloud drive.

## Canonical identity

- Ecosystem ID: `GLOBAL_INDIVIDUAL_STORAGE_ECOSYSTEM`
- Package: `global_individual_storage_ecosystem`
- Provider / owner: `GLOBAL_INDIVIDUAL`
- Category: `INDIVIDUAL`
- Category group: `PERSONAL_AND_INDIVIDUAL_STORAGE`
- Taxonomy: 5 groups, 17 categories
- Implementation state: `CATEGORY_FOUNDATION_SCAFFOLD`

## Root package responsibilities

The root owns canonical identity, safe runtime configuration, taxonomy source, flat category index, root metadata registry, catalog validation, API status/health handlers, root schemas, offline tests and read-only PHP metadata contract. It validates that every taxonomy item has a matching child package manifest with the expected category and group identity.

## Category child package structure

Each `global_individual_<category>_storage_ecosystem/` package follows the Google category-package structure: README, public package export, safe runtime configuration, canonical manifest, typed category metadata model, thread-safe local registry, validation service, category service entry point, API namespace/routes, public model namespace/export, manifest and category-record schemas, offline tests and read-only PHP metadata contract.

### IDENTITY_AND_OWNERSHIP
- `global_individual_individual_identity_metadata_storage_ecosystem/`
- `global_individual_storage_ownership_references_storage_ecosystem/`
- `global_individual_account_association_references_storage_ecosystem/`

### PERSONAL_CONTENT
- `global_individual_personal_document_storage_storage_ecosystem/`
- `global_individual_personal_file_and_folder_storage_storage_ecosystem/`
- `global_individual_personal_photo_and_video_storage_storage_ecosystem/`
- `global_individual_personal_audio_and_media_storage_storage_ecosystem/`

### DEVICE_AND_CLOUD
- `global_individual_personal_device_synchronization_storage_ecosystem/`
- `global_individual_personal_cloud_storage_associations_storage_ecosystem/`
- `global_individual_personal_backup_and_archive_storage_ecosystem/`

### DATA_RIGHTS_AND_LIFECYCLE
- `global_individual_personal_data_export_and_portability_storage_ecosystem/`
- `global_individual_personal_retention_and_deletion_storage_ecosystem/`
- `global_individual_personal_recovery_and_restoration_storage_ecosystem/`

### SECURITY_AND_SHARING
- `global_individual_personal_sharing_and_access_control_storage_ecosystem/`
- `global_individual_personal_encryption_and_key_references_storage_ecosystem/`
- `global_individual_personal_storage_audit_and_activity_storage_ecosystem/`
- `global_individual_consent_and_authorization_references_storage_ecosystem/`

## Foundation validation

The root service validates canonical root identity; taxonomy/index identity, equality and counts; duplicate categories; and all 17 child package manifests. Each child service validates its own canonical ecosystem, package, provider, category and group identities plus disabled integration flags. Health success means local foundation consistency only; it does not indicate an external connection.

## Data ownership and security

Identity proofing/authentication, consent decisions, cryptographic keys and external provider operations belong to their respective services. Root and child packages store minimized metadata and opaque references only. They must not store personal file content, credentials, authentication secrets or cryptographic keys. Every category record requires a non-empty opaque `owner_ref`.

## Readiness and operational boundary

Runtime enablement defaults to false. Connection remains `NOT_CONFIGURED`, provider product verification remains false and storage operations remain disabled. Authorized integration, live provider health checks and end-to-end tests are mandatory before enabling any external operation.
