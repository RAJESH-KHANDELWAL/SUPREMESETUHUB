# GLOBAL HUMAN LANGUAGE CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem/`

## Mission

A read-only CORE control plane for human-language taxonomy, language-provider identity, capability metadata, lifecycle state, policy boundaries and readiness. It is organized using the same architectural separation used by `google_core_ecosystem/`, adapted to a language-domain registry rather than copying Google's product inventory.

## Canonical package architecture

| Component | Responsibility |
|---|---|
| `catalog.py` | Parent ecosystem identity and provider-module registry |
| `catalog.json` | Canonical human-language domain taxonomy |
| `domain_catalog.py` | Domain definitions, lookup and coverage summary |
| `provider_catalog.json` | Provider identities, module paths, metadata and readiness |
| `provider_catalog.py` | Provider inventory and lookup |
| `constants.py` | Canonical ecosystem identifiers and status constants |
| `contracts.py` | Tenant context, secret references, result, domain and tier contracts |
| `module_service.py` | Reusable read-only provider Core service |
| `orchestrator.py` | Provider/domain discovery, health and dependency metadata |
| `policy.py` | Capability classification, tenant-context checks and metadata redaction |
| `service.py` | Public ecosystem status and registry facade |
| `ecosystem_manifest.json` | Machine-readable identity, counts, boundaries and package standard |
| `shared_support/` | Shared contracts, security, lifecycle, validation and support concerns |
| `tests/` | Catalog, provider-layout, contract and ecosystem-integrity regression tests |

## Provider module standard

Each provider module follows the same ten-part layout:

```text
<provider>_language_core_ecosystem/
├── README.md
├── __init__.py
├── ecosystem_config.py
├── ecosystem_manifest.json
├── service.py
├── authentication/contract.py
├── capabilities/catalog.py
├── docs/README.md
├── events/contracts.py
├── lifecycle/state.py
├── models/provider_model.py
├── schemas/provider_schema.py
├── security/policy.py
├── services/core_service.py
└── tests/test_manifest.py
```

Provider modules are catalog-only metadata adapters. They do not contain credentials, exchange tokens, call provider APIs or claim live connections.

## Domains

The domain catalog covers Bharat/Indic and global natural human languages, signed languages, dialects, writing systems, transliteration, speech, OCR, translation, dictionaries, learning, preservation, localization and the defined adult-safety metadata domains. The 22 current domain entries are not an exhaustive language census. The canonical domain folders are declared by `catalog.json`; integrity tests verify that every declared folder exists.

## Providers

The current provider registry contains Alibaba, AWS, Baidu, DeepL, Google, IBM, Microsoft, Naver, OpenAI, Tencent and Yandex. Registration means that a provider metadata module exists; it does not prove that a product API is public, available to a tenant, configured or connected. The provider registry and manifest counts are checked by automated tests.

## Layer ownership and security

- CORE owns identity, taxonomy, provider metadata, capability classification, lifecycle and readiness.
- API owns OAuth/authentication flows, SDK clients and HTTP transport.
- Storage and Database own durable records, persistence and migrations.
- Runtime/Engine owns jobs, retries, queues and execution.
- Application owns user sessions, consent screens and user workflows.
- Secrets remain in an external secret manager and are represented only by opaque references.
- A CORE capability check is not provider authorization, legal approval, API entitlement or proof of consent.

## Adult-content boundary

Only lawful material involving consenting adults may be considered by age-restricted metadata domains. Exclude minors, non-consensual intimate imagery, coercion, trafficking, exploitation and illegal content. Age assurance, consent/rights verification, moderation and takedown procedures remain mandatory.

## Validation

Run the focused regression suite from the repository root:

```bash
python -m pytest backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem/tests -q
```

The suite checks catalog and manifest counts, unique registry identifiers, canonical domain/provider folders, provider package layout, service metadata behavior, layer boundaries and non-live integration claims. A passing structural test suite does not prove external provider API availability or live connectivity.

## Completeness and runtime claims

Coverage is extensible and not claimed exhaustive. Provider connections are unverified, API calls performed by CORE are zero, and all provider modules remain `CORE_CATALOG_ONLY` until separately verified and implemented.
