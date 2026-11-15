# ATLASSIAN STORAGE ECOSYSTEM

Canonical Atlassian provider storage catalog for SUPREMESETUHUB.

## 1. Ecosystem purpose
This package defines the Atlassian provider namespace, product catalog, storage metadata classification, geographic scope, maturity vocabulary and readiness governance. It is the parent catalog for eight Atlassian product ecosystems.

## 2. Product ecosystem catalog
| Child package | Product | Catalog scope |
|---|---|---|
| `atlassian_bamboo_storage_ecosystem` | Bamboo | CONTINUOUS_INTEGRATION_BUILD |
| `atlassian_bitbucket_storage_ecosystem` | Bitbucket | SOURCE_CODE_REPOSITORY |
| `atlassian_compass_storage_ecosystem` | Compass | DEVELOPER_CATALOG_COMPONENTS |
| `atlassian_confluence_storage_ecosystem` | Confluence | KNOWLEDGE_CONTENT_DOCUMENTATION |
| `atlassian_jira_product_discovery_storage_ecosystem` | Jira Product Discovery | PRODUCT_IDEATION_PRIORITIZATION |
| `atlassian_jira_service_management_storage_ecosystem` | Jira Service Management | ITSM_SERVICE_OPERATIONS |
| `atlassian_jira_storage_ecosystem` | Jira | PROJECT_ISSUE_WORKFLOW |
| `atlassian_trello_storage_ecosystem` | Trello | KANBAN_BOARD_WORKSPACE |

Each child owns product-specific classification documentation. The `domains/`, `geography/` and `maturity_levels/` directories are maintained within each child package.

## 3. Parent foundation modules
- `atlassian_storage_ecosystem.py` — provider catalog and manifest validation
- `ecosystem_manifest.json` — product catalog, geographic scope, maturity and readiness declarations
- `ecosystem_config.py` — runtime configuration; no embedded secrets
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry for foundation/testing
- `ecosystem_service.py` — provider-neutral identity and health contract
- `tests/` — offline tests for catalog and foundation behavior

Production persistence belongs in central database/object-storage services, not the in-memory registry.

## 4. Architecture boundaries
- **Storage catalog:** product identity, metadata, lifecycle classification and health/readiness contracts.
- **Authentication/integration:** OAuth, API clients, webhooks, credentials and product operations belong in dedicated Atlassian API/integration layers.
- **Central infrastructure:** database, object storage, queues, cache, secrets management, audit and observability remain shared backend services.
- **Product capability:** each Atlassian product has its own API surface, permission model, plan/tenant constraints and data semantics.

## 5. Readiness and verification
All eight child entries are catalog scaffolds. No live provider connection, account entitlement, generic file-storage API, export right or provider-side storage guarantee is implied. Mark a product connected only after documented API support, authorized authentication, least-privilege permission checks, live health checks and end-to-end tests pass.

## 6. Security and governance
Apply least privilege, encryption in transit and at rest, secure token handling, audit logging, retention/deletion controls, data minimization, privacy and jurisdictional compliance. Never commit credentials, access tokens or private customer content.

## 7. Current implementation status
This is a provider/product catalog foundation. External connection state remains `NOT_CONFIGURED`; no product storage operations are represented as enabled.
