# GLOBAL SERVER CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem/`  
**Layer:** CORE  
**Scope:** Provider-neutral server control-plane metadata, resource identity, lifecycle, workload governance, service tiers and Bharat-to-global deployment context.

## Mission
Provide the canonical Server Core control plane for provider identity, server/resource metadata, lifecycle contracts, capability classification, policy metadata, discovery, geographic context, workload governance and readiness. This is a metadata and contract layer, not a cloud provisioning engine.

## Google Core architecture alignment
This ecosystem follows the shared Core control-plane pattern used by GOOGLE CORE ECOSYSTEM while retaining Server-specific semantics:

| Google Core pattern | Server Core implementation |
|---|---|
| `contracts.py` | Tenant, secret-reference, readiness, result and provider-neutral server contracts |
| `policy.py` | Tenant-context validation, capability risk classification and recursive secret redaction |
| `module_service.py` | Reusable provider metadata service; no SDK or remote execution |
| `catalog.py` | Canonical provider, domain, workload, geography and service-tier inventory |
| `domain_catalog.py` | Canonical 16-domain Core inventory and coverage summary |
| `provider_catalog.py` | Seven provider metadata namespaces |
| `orchestrator.py` | Provider/domain discovery, health, readiness, scope and dependency map |
| `service.py` | Public ecosystem facade and manager registration status |
| `php/GlobalServerCoreScopeContract.php` | PHP 8+ read-only scope contract normalizer |

## Provider coverage
Seven provider metadata namespaces are registered: Abelohost, Amazon Web Services (AWS), Cloudflare, DigitalOcean, Google Cloud, Microsoft Azure and ViceTemple. The list is non-exhaustive. A catalog entry does not establish an account, subscription, credential, entitlement, region availability, API access or live connection.

## Canonical Core domains
All 16 domain directories remain direct children of this canonical root and are indexed by `domain_registry.json`:
- `server_availability_core_ecosystem/`
- `server_backup_recovery_core_ecosystem/`
- `server_compliance_core_ecosystem/`
- `server_compute_core_ecosystem/`
- `server_identity_core_ecosystem/`
- `server_lifecycle_core_ecosystem/`
- `server_network_core_ecosystem/`
- `server_observability_core_ecosystem/`
- `server_security_core_ecosystem/`
- `server_resource_core_ecosystem/`
- `server_discovery_registry_core_ecosystem/`
- `server_provider_abstraction_core_ecosystem/`
- `server_geography_core_ecosystem/`
- `server_workload_governance_core_ecosystem/`
- `server_service_tier_core_ecosystem/`
- `server_interoperability_core_ecosystem/`

No domain is nested beneath another domain. Provider packages, workload profiles, `php/`, `shared_support/`, `tests/` and existing root modules remain in their current locations.

## Bharat-to-global workload coverage
Twenty workload profile directories remain direct children of the canonical root. Each uses `workload_manifest.json` and a read-only Python loader in `__init__.py`. These are CORE requirement profiles, not complete industry applications or live services.

The profile taxonomy covers government/public services; education/research; healthcare/life sciences; agriculture/food/supply chain; business/commerce/enterprise; banking/finance/insurance; technology/software/AI/data; cloud/hosting/networking; cybersecurity/privacy; real estate/construction; transport/mobility/logistics; energy/utilities/environment; retail/manufacturing/industry; media/publishing; gaming/interactive entertainment; travel/tourism/hospitality; legal/professional services; relationships/dating/community; sexual wellness/health education; and lawful adult-only entertainment.

India is a first-class jurisdiction in the geographic catalog, with an extensible global country/region model. Jurisdiction, residency and provider-region records must be verified against authoritative sources before operational use.

The canonical service-tier order remains **NORMAL → BASIC → STANDARD → PREMIUM → PROFESSIONAL → ENTERPRISE → SUPREME**. Tier labels do not define quotas, prices, SLAs, support or provider entitlements.

## Adult-category governance
Relationship/community, sexual-wellness/health-education and lawful adult-only entertainment remain separate workload classifications. Adult-only workloads require independently enforced age assurance, consent/content rights, privacy, security, moderation, reporting/takedown and jurisdiction eligibility. Child sexual abuse material, non-consensual intimate imagery, trafficking, exploitation and unlawful content are prohibited. Core records governance metadata only; it does not host, generate, distribute, review or authorize explicit content.

## Layer ownership
| Layer | Owns |
|---|---|
| CORE | Provider identity, metadata, capability taxonomy, lifecycle contracts, policy metadata, catalogs and readiness discovery |
| API | HTTP routes, authentication, consent, provider API transport and request/response handling |
| ENGINE | Provider SDKs, adapters, provisioning, deployment and remote execution |
| DATABASE | Durable SQL/NoSQL persistence, schemas, migrations and transactions |
| STORAGE | Object, file, backup and artifact persistence |
| APPLICATION/UI | User workflows, account settings, subscription presentation and interfaces |

Core must not duplicate OAuth/token exchange, provider SDK execution, durable persistence, object storage, billing or application UI.

## Security and operational boundaries
- Tenant and actor identity originate from the authenticated application/API layer.
- Secret references are opaque pointers only; secret bytes, API keys, tokens and private keys must never be committed or returned.
- Capability registration is not authorization or provider entitlement.
- Use least privilege, explicit authorization, audit trails and external secret management.
- Production and destructive operations require explicit approval in the consuming API/engine workflow.
- Registry state is process-local unless a DATABASE implementation is explicitly integrated.
- Remote provider operations remain disabled in Core.
- Health/readiness metadata does not prove remote reachability, successful provisioning or production readiness.

## Implementation and validation boundary
This package provides metadata, contracts, policy checks and local in-process identity registration. It does not claim live provider connections, cloud provisioning, durable database/storage execution, a production monitoring service or production age-assurance enforcement. Validate JSON catalogs, Python imports/tests and PHP contract compatibility in CI before enabling operational integrations.
