# GLOBAL CLOUD STORAGE ECOSYSTEM — ENGINEERING FOUNDATION

## 1. Canonical hierarchy
`GLOBAL CLOUD → WHAT GLOBAL CLOUD PROVIDES → STORAGE ECOSYSTEM`

The root package is provider-neutral. Storage categories describe *what kind of storage capability is being cataloged*; provider packages describe *which vendor or platform supplies a service*. Do not merge these two dimensions.

## 2. Package layout
- Root catalog: ecosystem identity, configuration, models, registry, service, taxonomy loader, read-only catalog facade, category index, provider index, and tests.
- `categories/<category_package>/`: one package per storage domain.
- `providers/<provider_package>/`: one namespace per cloud or storage provider.
- `taxonomy/`: canonical storage-domain vocabulary and taxonomy documentation.
- `tests/`: offline tests for safe readiness, taxonomy integrity, and catalog consistency.

## 3. Category package convention
Each category package follows the same structure:
- `README.md`, `__init__.py`
- `ecosystem_config.py`, `ecosystem_manifest.json`, `ecosystem_models.py`, `ecosystem_service.py`, `service.py`
- `api/` — API boundary placeholders; routes remain disabled in this storage catalog layer
- `models/` — category-specific metadata records
- `schemas/` — JSON schema contracts
- `php/` — metadata reader where required by the package convention
- `tests/` — offline category contract tests

## 4. Provider package convention
Provider packages carry provider identity, configuration, manifest, metadata models, service contract, model/schema namespaces, PHP metadata support where applicable, and offline tests. Provider packages do not gain API connectivity merely by existing.

## 5. Ownership boundaries
- Storage package owns provider identity, taxonomy, storage metadata, lifecycle definitions, catalog records, and health/readiness metadata.
- API/integration packages own authentication, provider SDKs, network calls, callbacks, and actual provider operations.
- Central database owns durable production persistence.

## 6. Readiness contract
- Local foundation: `FOUNDATION_READY`.
- Default provider connection: `NOT_CONFIGURED`.
- External connectivity verified: `false`.
- Live storage operations enabled: `false`.
- Region support and account entitlements: unverified until checked.

Only enable a provider after explicit authorization, least-privilege credentials from an approved external secret manager, successful live health checks, and end-to-end tests for each permitted operation.

## 7. Governance and security
Apply privacy, security, encryption, least privilege, audit, retention/deletion, consent where required, and jurisdictional compliance. Never commit credentials, tokens, private keys, personal data, or customer file contents.

## 8. Meaning of foundation readiness
`FOUNDATION_READY` describes the local catalog foundation only. It must never be represented as proof of provider availability, account entitlement, region support, connectivity, or working upload/download/delete operations.
