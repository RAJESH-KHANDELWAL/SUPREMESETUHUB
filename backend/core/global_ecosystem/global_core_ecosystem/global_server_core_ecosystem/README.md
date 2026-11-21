# GLOBAL SERVER CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem/`  
**Layer:** CORE  
**Scope:** Bharat-to-global server infrastructure metadata, provider-neutral contracts, workload classification and service-tier metadata.

## Mission
Provide a provider-neutral control-plane foundation for server identity, resource metadata, lifecycle policy, provider discovery, geographic deployment context, workload classification and service-tier metadata. This package is a metadata and contract layer; it is not a cloud provisioning engine.

## Existing provider namespaces
The current catalog registers seven provider metadata namespaces: Abelohost, Amazon Web Services (AWS), Cloudflare, DigitalOcean, Google Cloud, Microsoft Azure and ViceTemple. The catalog is explicitly non-exhaustive. Provider registration does not establish an account, subscription, entitlement, credential, region availability, API access or live connection.

## Bharat-to-global coverage
The geographic scope catalog defines India as a first-class deployment jurisdiction and supports a global region/country model. Country, state, region, data-residency and jurisdiction records must be verified against authoritative provider and legal sources before operational use. The catalog does not claim an exhaustive list of countries or provider regions.

## Workload domain folders and files
Twenty workload profile folders are present directly under this canonical root. The workload taxonomy defines five named workload areas per profile (100 total). Each folder contains:
- `workload_manifest.json`: domain identity, risk profile, service-tier references, geographic scope reference, required control areas and layer boundaries.
- `__init__.py`: read-only Python loader functions for the profile manifest and required control areas.

Folder naming convention: `<domain>_server_workload_profile/`. These are CORE-level server requirement profiles, not complete industry applications, API implementations, provider engines, databases or storage services.

The 20 domains are government/public services; education/research; healthcare/life sciences; agriculture/food/supply chain; business/commerce/enterprise; banking/finance/insurance; technology/software/AI/data; cloud/hosting/networking; cybersecurity/privacy; real estate/construction; transport/mobility/logistics; energy/utilities/environment; retail/manufacturing/industry; media/publishing; gaming/interactive entertainment; travel/tourism/hospitality; legal/professional services; relationships/dating/community; sexual wellness/health education; and lawful adult-only entertainment.

Adult-category entries are workload classifications only. Any deployment must enforce applicable law, robust age assurance, consent, privacy, security, moderation, reporting and geographic restrictions. The platform must prohibit child sexual abuse material, non-consensual intimate imagery, trafficking, exploitation and any other unlawful content. This CORE package does not host, generate, distribute, review or authorize explicit content.

## Service tiers
The canonical service-tier progression is **NORMAL → BASIC → STANDARD → PREMIUM → PROFESSIONAL → ENTERPRISE → SUPREME**. Tier names are labels only. Actual quotas, pricing, SLAs, support levels, security controls and availability must be defined by the consuming product or commercial contract; CORE does not invent or guarantee them.

## Root-level implementation files
- `catalog.json`: canonical provider metadata catalog.
- `catalog.py`: assembled read-only catalog across providers, 16 CORE domains, workloads, geography and service tiers.
- `manager.py`: canonical manager, domain-manifest validation, master-catalog reference validation and offline readiness status.
- `domain_registry.json` and `domain_registry.py`: 16-domain registry and strict directory/manifest validation.
- `ecosystem_manifest.json`: ecosystem identity, boundaries and capability declarations.
- `geographic_scope_catalog.json`: India-first and global geographic scope model.
- `workload_domain_catalog.json`: server workload domain taxonomy.
- `service_tier_catalog.json`: canonical tier order and semantics.
- `scope_catalog.py`: read-only loader and query helpers for scope catalogs.
- `php/GlobalServerCoreScopeContract.php`: PHP 8+ read-only contract normalizer for scope metadata.
- Existing Python modules continue to own provider-neutral identity, contracts, policies, registry and orchestration.

## Layer ownership
| Layer | Owns |
|---|---|
| CORE | Provider identity, metadata, capability taxonomy, lifecycle contracts, policy metadata, catalogs and readiness discovery |
| API | HTTP routes, authentication transport, consent and request/response handling |
| ENGINE | Provider SDKs, adapters, provisioning, deployment and remote execution |
| DATABASE | Durable SQL/NoSQL persistence, schemas, migrations and transactions |
| STORAGE | Object, file, backup and artifact persistence |
| APPLICATION/UI | User workflows, account settings, subscription presentation and content interfaces |

CORE must not duplicate API transport, OAuth/token exchange, cloud SDK execution, durable persistence, object storage, billing or application UI.

## Security and operational boundaries
- Tenant and actor identity must originate from the authenticated application/API layer.
- Secrets, API keys, access tokens, refresh tokens and private keys must never be committed or returned in catalog payloads.
- Use least privilege, explicit authorization, audit trails and external secret management.
- Production changes and destructive operations require explicit approval.
- Adult-only workloads require independently enforced age assurance and legal eligibility; a metadata label is never an access-control mechanism.
- Registry state is process-local unless a separate DATABASE implementation is explicitly integrated.
- Remote provider operations remain disabled in CORE.
- Health and readiness metadata do not prove remote reachability or successful provisioning.

## Validation
Run the repository's configured test suite and JSON validation in CI. Verify catalog consistency, imports, Python/PHP contract compatibility and security policy behavior before enabling any operational integration.

## Canonical 16-domain SERVER CORE architecture
All 16 domain directories are direct children of this canonical root and are indexed by `domain_registry.json`; `domain_registry.py` validates and reads the registry.

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

The added domains cover resource inventory, discovery/registry, provider abstraction, geography, workload governance, service tiers and interoperability. Each of the 16 direct-child domain folders now has one `domain_manifest.json` with six named control areas, ownership boundaries and operational constraints (96 control areas total). Existing provider and workload-profile folders remain in their current locations; no folder has been nested under another domain.

## Bharat-to-global and NORMAL-to-SUPREME
India remains a first-class jurisdiction in the shared geographic catalog, with an extensible global country/region model. The service-tier order remains NORMAL → BASIC → STANDARD → PREMIUM → PROFESSIONAL → ENTERPRISE → SUPREME. Tier names do not imply quotas, pricing, SLAs or provider entitlements.

## Relationships, Kamasutra, sexual wellness and lawful adult-only workloads
The existing relationship, sexual-wellness/health-education and lawful adult-only entertainment workload profiles remain separate. Workload governance maps to those existing profiles; Kamasutra/cultural knowledge is educational/cultural classification, sexual-health education is distinct from adult entertainment, and adult-only entertainment requires independently enforced age assurance, consent/content rights, privacy/security, moderation, reporting/takedown and jurisdiction eligibility. CSAM, non-consensual intimate imagery, trafficking, exploitation and unlawful content are prohibited. CORE records governance metadata only; it does not host, generate, distribute or authorize explicit content.

## Implementation boundary
This commit adds metadata manifests, domain contracts and registry definitions only. It does not claim live provider connections, remote provisioning, production readiness, durable database/storage execution or production age-assurance enforcement. Those responsibilities remain in API, ENGINE, DATABASE, STORAGE and APPLICATION layers.


## Master ecosystem catalog alignment
The canonical master source is `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`. This ecosystem is registered in both `ecosystem_module_index` and `implementation_registry`. The server domain registry and each domain manifest reference existing master entry IDs, and `manager.py` validates those references at runtime. These are implementation and cross-reference records, not additional unique master topics; they do not inflate the 2,468-topic target.

The master catalog currently reports 246 unique entries against a target of 2,468, with 2,222 remaining. Server references are mapped to existing infrastructure, technology, geography, governance, business and capability-tier topics; this package does not claim that the master catalog itself is complete.

## Domain control areas
Each of the 16 CORE domains defines six named control areas (96 total). These are provider-neutral metadata and contract scopes, not implemented cloud controls or remote operations. Each of the 20 industry workload profiles remains a separate workload classification and is not duplicated as a CORE domain. Each profile has five workload areas (100 total), mirrored exactly in its `workload_manifest.json`.

## Validation and status
Use `GlobalServerCoreManager.status()` or `manager_status()` for offline structural readiness and exact master-reference validation. A successful catalog check does not establish provider connectivity, credentials, account entitlement, region availability, provisioning capability, SLA, certification or production readiness.