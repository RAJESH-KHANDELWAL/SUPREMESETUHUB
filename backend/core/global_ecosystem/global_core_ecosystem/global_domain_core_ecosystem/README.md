# GLOBAL DOMAIN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem/`

## Mission

Global Domain Core is the provider-neutral control plane for domain-name, registrar, registry, DNS/nameserver, domain discovery, TLS/certificate and domain-hosting provider metadata. It provides canonical provider identity, provider-family classification, capability metadata, tenant-aware policy checks, lifecycle/readiness contracts, discovery and dependency mapping.

The current repository snapshot contains **78 provider package directories** plus shared `integrations/`, `services/` and `tools/` directories. This count is a folder-inventory snapshot, not proof that all provider packages are implemented or connected.

## Ownership boundaries

| Layer | Owns |
|---|---|
| Global Domain Core | Canonical provider identity, capability metadata, domain capability taxonomy, policy metadata, lifecycle/readiness and orchestration |
| Global Domain API | Provider authentication, consent, registrar/DNS/TLS clients, HTTP transport, response normalization and remote operations |
| Global Domain Engine | Execution, retries, queues, scheduling and long-running transfer/deployment workflows |
| Global Domain Database | Relational records, transactions, migrations and durable domain metadata |
| Global Domain Storage | Domain documents, evidence, backups, certificates and stored artifacts |
| Application/UI | User sessions, domain portfolio workflows, consent and user-facing screens |

Core must not perform provider API calls, OAuth/token exchange, DNS writes, domain registration/transfer, certificate issuance, deployment, queue execution or durable persistence.

## Canonical provider inventory

`provider_catalog.py` is the Core-side index of the 78 provider folders shown in the repository snapshot. It records provider identity, primary classification and descriptive capability metadata. It does not claim that a provider has a public API, that an API adapter exists, or that a customer account is connected.

Primary provider groups:
- Registrar and reseller providers
- DNS and nameserver providers
- Certificate and TLS providers
- Registry governance and lookup sources
- Hosting and infrastructure providers
- Cross-provider domain operations

Some providers span multiple groups. The primary category is a routing hint only; it is not an exclusive capability boundary.

## Readiness and security

- `CORE_CATALOG_ONLY`: provider metadata is registered; no adapter readiness is implied.
- `ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED`: an adapter scaffold is declared but no live connection is verified.
- `READY_FOR_CONFIGURATION`: configuration and verification remain.
- `READY`: only an owning integration layer may report this after deployment-level verification.

Tenant and actor identity must originate from the authenticated application layer. Core policy validates context and registered capability metadata only. Provider authorization, consent, account entitlement, secret resolution and audit enforcement remain in their owning layers. Never commit credentials, API tokens, authorization codes, DNS secrets, transfer authorization codes or personal domain-owner data.

## Implementation modules

- `catalog.py`: provider-neutral root identity and capability domains.
- `provider_catalog.py`: canonical 78-provider inventory from the supplied repository folder snapshot.
- `contracts.py`: tenant context, readiness and result contracts.
- `policy.py`: tenant/capability metadata policy and recursive secret filtering.
- `module_service.py`: read-only provider Core service.
- `orchestrator.py`: provider discovery, inventory, health and dependency mapping.
- `service.py`: public ecosystem status and registry integration.
- `ecosystem_manifest.json`: machine-readable ecosystem identity and coverage snapshot.

## Verification boundary

The package is a Core foundation and inventory layer. It does not claim live registrar coverage, domain availability, account authorization, API connectivity, successful registration, DNS propagation, transfer completion or certificate issuance. Run the repository test suite and provider-specific smoke tests before treating any adapter as production-ready.
