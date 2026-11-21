# GLOBAL PHOTO CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_photo_core_ecosystem/`  
**Reference architecture:** `google_core_ecosystem/`  
**Master taxonomy:** `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` (read-only)

## Mission

Photo Core is the read-only control plane for photo provider identity, domain taxonomy, capability metadata, discovery, governance, dependency mapping and readiness. It is not a media storage engine, API client, transcoder, publishing system, marketplace checkout, CDN or user interface.

## Architecture

- `catalog.py`: canonical ecosystem identity, 10 verified repository-backed provider records and capability metadata.
- Each provider package: `README.md`, `__init__.py`, `ecosystem_manifest.json` and `service.py.
- `domain_catalog.py`: 15 responsibility domains and domain coverage.
- `contracts.py`: stable tenant, provider, readiness and result contracts.
- `master_catalog.py`: read-only references to relevant numbered master-catalog topics; never edits or duplicates the 2468-target file.
- `policy.py`: tenant, sensitive capability, rights, consent, privacy and credential-boundary checks.
- `orchestrator.py`: provider/domain discovery, health and dependency metadata.
- `service.py`: public ecosystem status and registry-facing facade.
- `manager.py`: canonical Python entry point; `manager.php` is a thin interoperability facade.
- `domain_runtime.py`: shared read-only domain manager.
- `module_service.py`: shared read-only provider metadata service.
- `test_photo_core.py`: structural and behavior tests.

## Layer boundaries

Core owns identity, taxonomy, metadata, policy and readiness only. API adapters, OAuth, provider SDKs, media upload/download, storage, database writes, transcoding, streaming, CDN delivery, moderation execution, payments, queues and UI belong to their dedicated layers.

## Safety and truthfulness

Catalog registration does not prove an API exists, a provider account is connected, content is licensed, a creator has consented, a user is age-verified, or a service is live. Never store credentials or private media in Core. Sensitive publishing, billing, administrative and destructive actions require explicit authorization and audit. Images require rights-aware handling; non-consensual intimate imagery, child sexual abuse material and unlawful content are prohibited.

## Master catalog alignment

The canonical planning source is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. Its current count and target are read dynamically; this CORE does not create entries to inflate the target. Only explicit matching references are exposed. The master file remains the sole source of numbered topics.

## Implementation status

Provider records are catalog metadata only. `connected` and `live_connection_verified` remain false until separately deployed integrations pass authorized provider smoke tests. A domain with no verified provider package remains a taxonomy domain, not a claimed integration.
