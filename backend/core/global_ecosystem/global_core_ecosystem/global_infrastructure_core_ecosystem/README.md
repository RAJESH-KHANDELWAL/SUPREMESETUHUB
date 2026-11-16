# GLOBAL INFRASTRUCTURE CORE ECOSYSTEM

Provider-neutral CORE foundation for infrastructure resource identity, contract validation, domain discovery and policy metadata.

## Layer ownership
- CORE: canonical resource contracts, taxonomy, validation boundaries, lifecycle/policy metadata and read-only orchestration.
- API: HTTP contracts, authentication, request/response serialization and external API routing.
- ENGINE: runtime execution, scheduling and lifecycle coordination under explicit policy.
- INTEGRATION / ADAPTERS: provider SDKs, network transport and provider-specific translation.
- DATABASE / STORAGE: persistence and asset/data storage; CORE does not own provider credentials or raw infrastructure state.

## Scope
The catalog groups compute, server, virtualization, containers, serverless, networking, DNS, load balancing, CDN/edge, storage, database, backup/recovery, identity/access, security, observability, logging, monitoring, orchestration, cost/billing and governance/compliance domains.

Provider entries are discovery metadata only. No provider credentials, live connectivity, provisioning, billing actions or remote operations are implemented or claimed here.

## Safety
Never store secrets in catalog metadata. Use secret references owned by a dedicated security/configuration boundary. Validate tenant and authorization context in API/runtime before any future operation. Destructive actions require explicit authorization, idempotency, audit evidence and provider-specific safeguards.

## Status
CORE_CATALOG_ONLY. The existing resource validator remains the canonical validation dependency. This package does not claim production readiness or live provider integration.
