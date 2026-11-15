# ADOBE Storage Ecosystem

Canonical Adobe provider storage catalog for SUPREMESETUHUB.

## Architecture

This package follows the same provider-level pattern as:

`backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`

The responsibility split is:

- **Adobe API Ecosystem:** OAuth, identity, API clients, scopes, endpoints and external API operations.
- **Adobe Storage Ecosystem:** storage-side provider catalog, asset/document metadata, ownership, version references, lifecycle definitions and storage health metadata.
- **Central database:** production persistence for normalized metadata and operational records.

## Storage families

The nine child namespaces below represent storage domains and product-specific storage surfaces. They are not nine independent general-purpose cloud drives, and a folder does not imply a live API connector.

| Storage ecosystem | Responsibility | Related API family in the current Adobe API catalog |
|---|---|---|
| `adobe_cloud_storage_and_collaboration_storage_ecosystem` | Shared cloud-storage and collaboration metadata; distinguish shared storage from product-specific file APIs | Creative Cloud and Assets APIs; verify exact product capability |
| `adobe_creative_cloud_storage_ecosystem` | Creative Cloud cloud documents, supported project references and library relationships | Creative Cloud and Assets APIs; no universal desktop-app file API is implied |
| `adobe_creative_cloud_assets_storage_ecosystem` | Reusable creative assets, asset metadata, ownership, sharing and version references | Creative Cloud and Assets APIs |
| `adobe_document_cloud_storage_ecosystem` | Document Cloud files and document lifecycle metadata | PDF Services and Acrobat Sign APIs are related document APIs, but processing/signing APIs are not automatically general file-storage APIs |
| `adobe_experience_manager_assets_storage_ecosystem` | Enterprise DAM assets, metadata, renditions, collections and permissions | Requires validation of the applicable Experience Manager API; Experience Platform APIs are not assumed to be interchangeable with AEM Assets APIs |
| `adobe_express_storage_ecosystem` | Express projects, graphics, brand assets and published-content references | No dedicated Express storage API is asserted by this catalog; verify documented API and entitlement |
| `adobe_frameio_storage_ecosystem` | Media assets, versions, review links, comments and approvals | Video and Frame.io APIs |
| `adobe_lightroom_storage_ecosystem` | Lightroom cloud photo/video assets, albums and sync metadata | Verify the currently supported Lightroom API and account entitlement; do not infer generic storage CRUD |
| `adobe_workfront_storage_ecosystem` | Workfront project asset references, proofs, approvals and attachments | Validate Workfront API and connected storage permissions separately |

## Child catalog

The canonical child IDs, names and folder paths are maintained in `adobe_storage_ecosystem.py`. Keep that catalog synchronized with the folders and `adobe_storage_capability_matrix.json`.

## Foundation modules

- `adobe_storage_ecosystem.py` — provider catalog and child ecosystem listing
- `adobe_storage_capability_matrix.json` — storage-domain to API-family mapping and capability boundaries
- `ecosystem_manifest.json` — geographic scope, readiness state and governance declarations
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider identity and truthful health contract
- `tests/` — offline catalog and foundation tests\n\nEach of the nine child namespaces contains its own `__init__.py`, `models.py`, `registry.py`, `service.py`, `config.py`, `adapter_contract.py`, `manifest.json`, README and `tests/test_foundation.py`.

## Backend integration

The Adobe API package is:
`backend/api/global_ecosystem/global_api_ecosystem/adobe_api_ecosystem/`

Storage modules must call provider-specific API adapters through the approved integration layer. Do not put OAuth secrets, tokens, HTTP clients or endpoint implementations in this storage package.

## Status and readiness

- `CATALOG_SCAFFOLD`: storage domain is catalogued; no live connection is claimed.
- `NOT_CONFIGURED`: credentials, scopes or product entitlements are not configured.
- `CONFIGURED_NOT_VERIFIED`: configuration exists, but a live authorized operation has not passed.
- `CONNECTED`: use only after an authenticated health check and the required end-to-end operations pass.

A local `FOUNDATION_READY` result means package code is available. It does not prove account entitlement, API support, authorized connectivity, or working list/upload/download/delete operations.

Production persistence belongs in the central database. Apply least privilege, encryption, audit logs, retention controls, deletion safeguards and jurisdictional compliance. Never commit credentials or personal data.
