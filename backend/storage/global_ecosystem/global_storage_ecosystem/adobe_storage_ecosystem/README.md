# Adobe Storage Ecosystem

Canonical Adobe provider storage catalog for SUPREMESETUHUB.

## Child storage ecosystems

- `adobe_cloud_storage_and_collaboration_storage_ecosystem` — Adobe cloud projects, folders, files, cloud documents, Creative Cloud Libraries and brands where supported.
- `adobe_creative_cloud_storage_ecosystem` — Creative Cloud cloud documents, libraries and supported application storage surfaces.
- `adobe_creative_cloud_assets_storage_ecosystem` — reusable creative assets, asset metadata and supported asset operations.
- `adobe_lightroom_storage_ecosystem` — Lightroom cloud photo/video assets, albums and sync metadata.
- `adobe_express_storage_ecosystem` — Express projects and brand assets.
- `adobe_frameio_storage_ecosystem` — Frame.io media, versions, review and collaboration records.
- `adobe_experience_manager_assets_storage_ecosystem` — enterprise digital asset management.
- `adobe_workfront_storage_ecosystem` — Workfront asset workflows, proofs and approvals.
- `adobe_document_cloud_storage_ecosystem` — Document Cloud documents and sharing metadata.

## Architecture boundary

The Adobe API Ecosystem owns Adobe API clients, OAuth, endpoints, scopes and API operations:
`backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`.

This Storage Ecosystem owns storage-side models, provider-specific storage metadata, object lifecycle, storage mappings and storage health. It references API operations; it does not duplicate API clients or OAuth.

## Truthful readiness

This catalog is not a live Adobe connection. Product availability, API support, account entitlements, OAuth scopes, organization permissions and region-specific behavior must be verified per product. Mark a child CONNECTED only after authorized live health checks and required read/write tests pass. Never assume every Adobe product exposes a generic storage API or a common quota.

## Coverage

The provider catalog is intended for Bharat, regional and global use, subject to each Adobe product's availability, contract, data residency and applicable law. Normal, Professional, Advanced, Enterprise and Supreme are target maturity levels, not claims that those capabilities are deployed.
