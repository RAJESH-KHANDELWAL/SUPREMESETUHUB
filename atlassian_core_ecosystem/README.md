# ATLASSIAN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/`

## Mission
Provider metadata control plane aligned to Google Core manager, domain runtime, inventory, tests and interoperability conventions. Owns provider identity, product-family registration, domain routing, capability metadata, policy boundaries, lifecycle/readiness and dependency discovery. It does not implement API transport.

## Product families
- Atlassian Administration and Identity
- Bitbucket
- Confluence
- Jira
- Jira Service Management

Family package naming: `atlassian_<family>_core_ecosystem`. Registration does not imply authorization, entitlement or live connectivity.

## Core files
- `manager.py`: canonical manager for status, health, products, domains, inventory, offerings, lookup and dependencies.
- `manager.php`: PHP interop facade.
- `catalog.py`: provider and family registry.
- `contracts.py`: tenant, secret-reference, readiness and result contracts.
- `policy.py`: capability classification and safe summaries.
- `module_service.py`: read-only family service.
- `product_catalog.py`: family offering inventory.
- `domain_catalog.py`: domain taxonomy, routing and offering inventory.
- `domain_runtime.py`: read-only domain manager.
- `orchestrator.py`: discovery, health and dependency metadata.
- `service.py`: provider facade and registry status.
- `product_ecosystem_index.json`: machine-readable package map.
- `test_atlassian_core_domains.py`: structure and behavior tests.
- `php/AtlassianCoreContract.php`: PHP payload contract.

## Domains
- `atlassian_provider_governance_core_ecosystem`
- `atlassian_identity_and_organization_core_ecosystem`
- `atlassian_developer_and_source_control_core_ecosystem`
- `atlassian_knowledge_and_collaboration_core_ecosystem`
- `atlassian_work_management_and_planning_core_ecosystem`
- `atlassian_it_service_and_operations_core_ecosystem`
- `atlassian_governance_and_security_core_ecosystem`
- `atlassian_integration_and_automation_core_ecosystem`

Shared directories use `atlassian_shared_<capability>_core_ecosystem` naming (compatibility, configuration, contracts, documentation, events, exceptions, orchestration, security, testing, utilities, validation).

## Layer boundaries
| Layer | Responsibility |
|---|---|
| Atlassian Core | Identity, taxonomy, capability metadata, policy, lifecycle, readiness, discovery |
| Atlassian API Ecosystem | OAuth/API tokens, SDKs, transport and response normalization |
| Storage | Durable records, tenant isolation, retention and backups |
| Database | Schemas, queries, migrations and transactions |
| Runtime/Engine | Jobs, queues, retries, scheduling and execution |
| Application/UI | Sessions, consent, user workflows and UI |

Core performs no provider API calls, credential exchange, persistence or background execution.

## Security/readiness
Authenticated application supplies tenant and actor identity. Capabilities are metadata, not authorization/entitlement. Core stores opaque secret references only. Administrative/destructive/write operations require explicit authorization and audit. Live connectivity remains unverified until deployed auth and provider smoke tests succeed.
