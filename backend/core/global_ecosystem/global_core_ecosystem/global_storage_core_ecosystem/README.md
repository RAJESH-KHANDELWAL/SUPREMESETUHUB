# GLOBAL STORAGE CORE ECOSYSTEM

Provider-neutral CORE control plane for storage-provider identity, capability metadata, lifecycle contracts, policy gates and deterministic operation plans.

## Boundaries
CORE owns metadata and contracts only. Provider API execution, OAuth/token exchange, secret storage, file bytes, persistence, infrastructure provisioning and data transfer belong to their respective API, SECURITY, STORAGE, ENGINE and service layers. No live provider calls are performed here.

## Providers
Apple, AWS, DigitalOcean, Google and Microsoft are initial, non-exhaustive provider families. Catalog registration does not imply API access, account entitlement, live connectivity or successful transfer.

## Root modules
`contracts.py`, `catalog.py`, `domain_catalog.py`, `policy.py`, `lifecycle.py`, `orchestrator.py`, `service.py`, `ecosystem_manifest.json`, `providers_catalog.json`, `tests/`.

Credentials and encryption keys must remain in an approved external secret manager. Apply tenant isolation, least privilege, encryption, retention/deletion controls, audit trails, residency rules and malware scanning in execution layers.
