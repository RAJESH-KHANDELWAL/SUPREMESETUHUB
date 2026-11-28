# IBM CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Provider:** IBM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/ibm_core_ecosystem/`  
**Status:** `CORE_CATALOG_ONLY`

## Mission
IBM Core is the provider-level control plane for IBM Cloud, watsonx and enterprise service families. It owns provider identity, product registration, domain taxonomy, capability metadata, tenant/account/region context contracts, policy boundaries, readiness, discovery and dependency mapping.

## Canonical root files
- `manager.py`: stable Python entry point and `get_manager()`.
- `manager.php`: thin PHP interoperability/status facade; no transport or credentials.
- `catalog.py`: provider identity and assembled catalog.
- `product_catalog.py`: the 16 existing IBM service-family registrations and API/ENGINE routing references.
- `domain_catalog.py`: IBM responsibility taxonomy.
- `contracts.py`: tenant, account, region, secret-reference, readiness and result contracts.
- `policy.py`: sensitive-capability classification and secret-safe metadata handling.
- `module_service.py`: shared read-only service for product families.
- `domain_runtime.py`: shared read-only domain manager.
- `orchestrator.py`: discovery, health and dependency map.
- `service.py`: public status and registry-facing service.
- `test_ibm_core.py`: structural and behavior tests.

## Product families
- **IBM API Connect and Gateway** — `ibm_api_connect_gateway_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_api_connect_gateway_api_ecosystem/`.
- **IBM Billing Usage and Cost** — `ibm_billing_usage_cost_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_billing_usage_cost_api_ecosystem/`.
- **IBM Cloud Object Storage** — `ibm_cloud_object_storage_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_cloud_object_storage_api_ecosystem/`.
- **IBM Cloud Platform** — `ibm_cloud_platform_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_cloud_platform_api_ecosystem/`.
- **IBM Cloudant** — `ibm_cloudant_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_cloudant_api_ecosystem/`.
- **IBM Code Engine and Serverless** — `ibm_code_engine_serverless_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_code_engine_serverless_api_ecosystem/`.
- **IBM Db2 Database** — `ibm_db2_database_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_db2_database_api_ecosystem/`.
- **IBM IAM and Identity** — `ibm_iam_identity_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_iam_identity_api_ecosystem/`.
- **IBM Kubernetes and Containers** — `ibm_kubernetes_containers_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_kubernetes_containers_api_ecosystem/`.
- **IBM Monitoring and Activity Tracker** — `ibm_monitoring_activity_tracker_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_monitoring_activity_tracker_api_ecosystem/`.
- **IBM Resource Controller and Catalog** — `ibm_resource_controller_catalog_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_resource_controller_catalog_api_ecosystem/`.
- **IBM Secrets Manager** — `ibm_secrets_manager_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_secrets_manager_api_ecosystem/`.
- **IBM Security and Key Protect** — `ibm_security_key_protect_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_security_key_protect_api_ecosystem/`.
- **IBM VPC Compute and Networking** — `ibm_vpc_compute_networking_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_vpc_compute_networking_api_ecosystem/`.
- **IBM watsonx.ai** — `ibm_watsonx_ai_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_watsonx_ai_api_ecosystem/`.
- **IBM watsonx.data** — `ibm_watsonx_data_core_ecosystem/`; API reference: `backend/api/global_ecosystem/global_api_ecosystem/ibm_api_ecosystem/ibm_watsonx_data_api_ecosystem/`.

## Domain coverage
1. **Provider Governance** — IBM provider identity, service registration, lifecycle, readiness and cross-layer ownership.
2. **Cloud Account and Resource Governance** — Accounts, resource groups, projects, regions, service instances and resource ownership.
3. **IAM, Identity and Access** — IAM identities, service IDs, access groups, trusted profiles, policies and authorization boundaries.
4. **Compute, VPC and Networking** — Virtual servers, images, volumes, VPCs, subnets, gateways, security groups and network interfaces.
5. **Kubernetes, OpenShift and Containers** — IBM Cloud Kubernetes Service, OpenShift, container workloads and registry boundaries.
6. **Serverless and Code Engine** — Code Engine projects, applications, jobs, builds and serverless workload metadata.
7. **Object Storage and Artifacts** — Buckets, objects, multipart uploads, lifecycle, retention and artifact references.
8. **Databases and Cloudant** — Db2, Cloudant, database instances, documents, indexes, schemas and data lifecycle.
9. **watsonx AI, Models and Inference** — Foundation models, model metadata, deployments, inference and AI lifecycle governance.
10. **watsonx.data and Analytics** — Data platform, engines, catalogs, analytics and governed data access.
11. **API Management and Gateway** — API Connect catalogs, spaces, products, APIs, gateway configuration and lifecycle.
12. **Secrets Management** — Secret references, secret groups, rotation metadata, retrieval boundaries and access policy.
13. **Key Management and Cryptography** — Key Protect key lifecycle, cryptographic policy and key access boundaries.
14. **Monitoring and Observability** — Metrics, dashboards, alerts, service health and operational telemetry metadata.
15. **Activity Tracking and Audit** — Activity Tracker events, audit lineage, actor attribution and evidence metadata.
16. **Resource Catalog and Service Lifecycle** — Global Catalog, service plans, resource bindings, provisioning eligibility and lifecycle.
17. **Billing, Usage and Cost** — Usage records, billing reports, consumption, budgets and cost governance.
18. **Tenancy, Region, Quota and Compliance** — Tenant isolation, region eligibility, quota metadata, compliance and data residency.

## Master catalog alignment (2468)
The master catalog is a planning taxonomy, not a provider implementation inventory. It currently contains no IBM-specific entry. IBM Core therefore references only existing canonical technology topics: `S09_software`, `S09_cloud_computing`, `S09_artificial_intelligence`, `S09_machine_learning`, `S09_database`, `S09_data_analytics`, `S09_cybersecurity`, `S10_global_database`, `S10_global_security`, `S10_global_data_core`. These are topic-level mappings, not newly created IBM catalog entries. The master catalog JSON is not modified by this implementation.

## Layer ownership
| Layer | Responsibility |
|---|---|
| IBM Core | Provider/product identity, taxonomy, contracts, policy, readiness and dependency discovery |
| IBM API Ecosystem | IBM IAM flows, service-specific API clients, transport and response normalization |
| IBM ENGINE Ecosystem | Execution handlers, jobs, queues, retries and operational workflows |
| Database / Storage | Durable state, schemas, object persistence, retention and backups |
| Application / UI | User sessions, approvals, consent, workflows and presentation |

Core must not exchange IAM API keys for bearer tokens, call IBM APIs, store secrets, persist business records, or execute workloads.

## Security and readiness
- Never commit IBM Cloud API keys, bearer tokens, HMAC credentials, private keys or secret values.
- Keep only opaque secret references in Core contracts; resolve secrets in the authorized API/runtime boundary.
- Enforce tenant, account, resource-group, region, service entitlement, IAM role and quota checks in the appropriate execution path.
- Separate discovery/read-only metadata from create, update, delete, deploy, billing, key and secret operations.
- Require explicit authorization, confirmation and audit for sensitive or destructive actions.
- A catalog entry does not prove that a service is enabled in an account or available in a region.
- `CONNECTED` must never be inferred from configuration presence; require authenticated IBM IAM validation and a service-specific smoke test.

## Scope discipline
The 16 product packages and 18 domain packages below are responsibility boundaries. They reuse shared managers and contracts; no duplicated API clients, engine implementations, generic empty folders or speculative service families are added.
