# Object and Blob Storage

Canonical category namespace under `GLOBAL_CLOUD_STORAGE_ECOSYSTEM`.

## Subcategory architecture

This category contains 8 independent subcategory ecosystem packages. Each package has its own README and manifest and remains catalog-only until provider-specific integration is authorized and verified.

- [Object Storage](subcategories/global_cloud_object_storage_storage_ecosystem/README.md) — `OBJECT_STORAGE`
- [Blob Storage](subcategories/global_cloud_blob_storage_storage_ecosystem/README.md) — `BLOB_STORAGE`
- [Bucket Storage](subcategories/global_cloud_bucket_storage_storage_ecosystem/README.md) — `BUCKET_STORAGE`
- [Multipart Object Storage](subcategories/global_cloud_multipart_object_storage_storage_ecosystem/README.md) — `MULTIPART_OBJECT_STORAGE`
- [Archival Object Storage](subcategories/global_cloud_archival_object_storage_storage_ecosystem/README.md) — `ARCHIVAL_OBJECT_STORAGE`
- [Edge Object Storage](subcategories/global_cloud_edge_object_storage_storage_ecosystem/README.md) — `EDGE_OBJECT_STORAGE`
- [Static Website Asset Storage](subcategories/global_cloud_static_website_storage_storage_ecosystem/README.md) — `STATIC_WEBSITE_STORAGE`
- [Data Lake Object Storage](subcategories/global_cloud_data_lake_object_storage_storage_ecosystem/README.md) — `DATA_LAKE_OBJECT_STORAGE`

## Integration boundary

Provider availability is not implied by a taxonomy entry. Keep connections unconfigured and storage operations disabled until authorized credentials, provider-specific health checks, security review, and end-to-end tests pass. Do not commit secrets or customer data.
