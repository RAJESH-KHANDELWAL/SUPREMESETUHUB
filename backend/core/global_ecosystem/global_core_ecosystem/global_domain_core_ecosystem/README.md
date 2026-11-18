# GLOBAL DOMAIN CORE ECOSYSTEM

Provider-neutral Core contracts and metadata for domain registration, DNS, registry governance, domain lookup, TLS automation, deployment custom domains and hosting references.

## Source of truth and scope

- The provider inventory mirrors the 71 unique provider IDs in the existing Global Domain API catalog.
- Seven domain capability groups are represented separately from external providers.
- The source API catalog contains a duplicate `desec` key; Core registers that provider once and records the duplicate as a source-catalog quality issue.
- Existing provider and category directory paths are preserved. The support directories `integrations/`, `services/` and `tools/` are retained and are not provider packages.

## Layer boundaries

- **CORE** owns provider identity, normalized contracts, capability classification, policy decisions and metadata-only orchestration.
- **API** owns HTTP routes, API schemas, provider API adapters, transport and endpoint-specific request/response handling.
- **ENGINE** owns execution/runtime adapters and operational workflows.
- **DATABASE** owns durable domain records, registration state, DNS state and audit persistence.
- **STORAGE** owns certificate artifacts, DNS exports and related files.
- **IDENTITY / SECURITY** own authentication, authorization, secret storage, consent and audit enforcement.

Core must not import API, ENGINE, DATABASE or STORAGE implementation modules.

## Safety and readiness

All providers are `CORE_CATALOG_ONLY`; live connections are unverified. This package does not perform domain purchases, renewals, transfers, DNS changes, nameserver changes, certificate issuance/revocation, WHOIS/RDAP network queries, account login, deployment or billing actions. No credentials, API keys, tokens or private keys belong in Core metadata.

Destructive or externally mutating operations are denied by default and require separately implemented authorization, confirmation, audit and provider-specific runtime support outside this catalog layer.

## Provider package convention

Each provider package contains `README.md`, `ecosystem_manifest.json`, `ecosystem_config.py`, `contracts.py`, `__init__.py` and the ten responsibility folders: authentication, capabilities, docs, events, lifecycle, models, schemas, security, services and tests. Provider PHP authentication files define shape-only contracts; they do not authenticate users or verify tokens.

## Validation

Run:

```bash
python -m unittest backend.core.global_ecosystem.global_core_ecosystem.global_domain_core_ecosystem.tests.test_global_domain_core_contracts -v
```
