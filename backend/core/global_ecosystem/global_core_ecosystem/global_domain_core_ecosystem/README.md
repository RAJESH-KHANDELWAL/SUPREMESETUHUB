# GLOBAL DOMAIN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem/`

## Mission

Global Domain Core is the provider-neutral control plane for domain registrars, registry operators, DNS/nameserver providers, domain lookup sources, certificate/TLS providers and domain-hosting infrastructure. It owns canonical identity, capability classification, tenant-aware metadata policy, lifecycle/readiness contracts, provider discovery and dependency mapping.

## Inventory model

The supplied repository directory snapshot contains **78 domain-related child folders**. They are classified as:
- **70 provider packages** — vendor, registrar, registry, DNS, lookup, certificate and hosting/infrastructure identities.
- **8 capability packages** — `deployment_domains`, `dns_services`, `dnssec`, `domain_lookup`, `hosting`, `registrars_resellers`, `registries_governance`, `tls_certificate`.
- Shared support folders `integrations/`, `services/` and `tools/` are not included in either count.

The classification is a Core inventory baseline derived from the supplied folder names. Provider/category assignments should be validated against each package's existing contents and authoritative provider documentation before API work is enabled.

## Ownership boundaries

| Layer | Owns |
|---|---|
| Global Domain Core | Provider identity, capability taxonomy, policy metadata, lifecycle/readiness and orchestration |
| Global Domain API | Provider authentication, consent, registrar/DNS/TLS clients, HTTP transport, response normalization and remote operations |
| Global Domain Engine | Execution, retries, queues, scheduling and long-running transfer/deployment workflows |
| Global Domain Database | Durable domain records, transactions, migrations and queries |
| Global Domain Storage | Domain documents, evidence, backups, certificates and stored artifacts |
| Application/UI | User sessions, portfolio workflows, consent and user-facing screens |

Core must not perform provider API calls, token exchange, DNS writes, domain registration/transfer, certificate issuance, deployment, queue execution or durable persistence.

## Core implementation

- `catalog.py`: provider-neutral root identity and capability domains.
- `provider_catalog.py`: 70 provider entries and 8 separately classified capability packages.
- `contracts.py`: tenant context, readiness and result contracts.
- `policy.py`: tenant/capability metadata policy and recursive secret filtering.
- `module_service.py`: read-only provider Core service.
- `orchestrator.py`: provider discovery, inventory, health and dependency mapping.
- `service.py`: public ecosystem status and registry integration.
- `ecosystem_manifest.json`: machine-readable identity and coverage snapshot.

## Readiness and security

- `CORE_CATALOG_ONLY`: provider metadata is registered; no adapter readiness is implied.
- `ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED`: adapter scaffold declared, but no live connection verified.
- `READY_FOR_CONFIGURATION`: configuration and verification remain.
- `READY`: only an owning integration layer may report this after deployment-level verification.

Tenant and actor identity must originate from the authenticated application layer. Core policy validates context and registered capability metadata only. Provider authorization, consent, account entitlement, secret resolution and audit enforcement remain in owning layers. Never commit credentials, API tokens, authorization codes, DNS secrets, transfer authorization codes or personal domain-owner data.

## Verification boundary

This package is a Core foundation and inventory layer. It does not claim live registrar coverage, domain availability, account authorization, API connectivity, successful registration, DNS propagation, transfer completion or certificate issuance. Run repository tests and provider-specific smoke tests before treating any adapter as production-ready.
