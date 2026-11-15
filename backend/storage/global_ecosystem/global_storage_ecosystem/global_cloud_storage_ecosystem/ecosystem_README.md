# GLOBAL CLOUD STORAGE ECOSYSTEM — PACKAGE FOUNDATION

## 1. Package ownership
The GLOBAL CLOUD STORAGE ECOSYSTEM package owns:
- Canonical cloud-storage provider and service identity
- Storage taxonomy and category vocabulary
- Storage metadata schemas and catalog records
- Object and file lifecycle definitions
- Storage health metadata and readiness contracts

Provider authentication, SDK clients, external API calls, and real storage operations belong to dedicated API/integration packages. Durable production persistence belongs to the central database layer.

## 2. Standard provider namespace
A future provider-specific package may contain:
- Provider manifest and configuration
- Provider metadata models and JSON schemas
- Provider service contract
- API/integration boundary
- Provider model namespace
- Offline contract and validation tests
- Optional PHP metadata reader where required by the repository architecture

A provider namespace is a catalog/contract boundary. Its presence does not imply that an SDK integration exists or that a provider account is connected.

## 3. Readiness contract
- Foundation state: `FOUNDATION_READY` after local initialization.
- Default provider connection state: `NOT_CONFIGURED`.
- External connectivity verified: `false`.
- Storage operations enabled: `false`.
- Region and account entitlement: unverified until checked.
- Credentials: supplied only through an approved external secret manager.

## 4. Verification required before activation
A future provider integration must have explicit authorization, least-privilege credentials, a successful live health check, and end-to-end tests for each operation it exposes. Record provider limitations and supported regions from verified evidence.

## 5. Security requirements
Never commit credentials, access tokens, private keys, personal data, customer file contents, or production secrets. Keep external operations outside this catalog package.

## 6. Meaning of readiness
`FOUNDATION_READY` describes the local metadata foundation only. It must never be presented as proof of provider connectivity, service availability, or working upload/download/delete operations.
