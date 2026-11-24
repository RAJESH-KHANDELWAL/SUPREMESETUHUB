# GLOBAL CLOUD CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE  
**Ecosystem ID:** `GLOBAL-CLOUD-CORE-ECOSYSTEM`

## Mission
Global Cloud Core is the read-only control plane for cloud-provider identity, provider discovery, cloud capability classification, regional scope, workload taxonomy, readiness metadata and dependency mapping.

## Canonical source registries
- Provider catalog: `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`
- Capability taxonomy: `backend/global_ecosystem/global_cloud_ecosystem/capabilities.py`
- Regional and deployment scopes: `backend/global_ecosystem/global_cloud_ecosystem/scope.py`
- Workload catalog and adult-industry guardrails: `backend/global_ecosystem/global_cloud_ecosystem/workloads.py`

The Python source registries remain authoritative. Core does not create a duplicate provider registry.

## Package files
- `manager.py`: canonical manager and `get_manager()`
- `manager.php`: PHP read-only master-catalog interoperability facade
- `service.py`: provider/workload discovery and dependency metadata
- `domain_catalog.py`: ten cloud capability domains and provider classification
- `domain_runtime.py`: shared read-only domain manager
- `__init__.py`: public exports
- `test_global_cloud_core.py`: manager, registry, domain, workload and catalog tests

## Cloud Core domains
1. Cloud Governance and Provider Lifecycle
2. Compute and Acceleration
3. Storage, Backup and Content
4. Database and Data Platforms
5. Networking, DNS and Edge
6. Application and Developer Platforms
7. Security, Identity and Compliance
8. Regional, Hybrid and Sovereign Cloud
9. Personal Storage and Collaboration Cloud
10. Enterprise and Specialty Cloud Workloads

Classification is metadata only. A provider can offer capabilities across several areas; the deterministic primary-domain assignment is for inventory navigation, not a limit on actual services.

## Master catalog bridge
The single source of truth remains `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json`, owned by `GLOBAL_ENGINE_ECOSYSTEM`. Python and PHP expose read-only on-demand reference, complete source-row inventory and exact entry lookup. No copied JSON, generated placeholder rows or artificial provider packages are created.

The master target is **2,468 unique entries**. The source snapshot currently records 246 unique entries, 2 cross-reference rows, 248 numbered source rows and 2,222 remaining unique entries. These are cross-ecosystem planning entries, not cloud providers.

## Layer boundaries
| Layer | Responsibility |
|---|---|
| Cloud Core | Provider identity, capability taxonomy, regional scope, workload classification and readiness metadata |
| Cloud API | Provider authentication, SDK clients, HTTP transport and response normalization |
| Cloud Engine | Provisioning, deployment, jobs, retries and execution |
| Cloud Database | Structured records, schemas, queries and transactions |
| Cloud Storage | Durable objects, backups, retention and tenant isolation |
| Application/UI | User sessions, consent, workflows and presentation |

Provider catalog presence does not prove account access, entitlement, region availability, partnership, API support or a live connection. Core performs no provisioning, provider API calls, credential resolution or persistence.

## Adult-industry workload safeguards
The workload taxonomy describes lawful adults-only services only. Relevant workloads must enforce age assurance, documented consent, content/distribution rights, prevention of minors and non-consensual intimate content, reporting/takedown, privacy and applicable law. Taxonomy entries do not certify that any provider permits or supports such workloads.
