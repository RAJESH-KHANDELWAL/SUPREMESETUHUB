# DIGITALOCEAN CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/digitalocean_core_ecosystem/`

## Mission

DigitalOcean Core is the provider-level control plane and canonical capability inventory for Cloud, Hosting, Server, Storage and VPS. It coordinates provider identity, capability registration, tenant context, policy boundaries, discovery, dependency mapping and readiness.

## Structure

- `manager.py`: canonical Python entry point for status, capability discovery, validation and dependency metadata.
- `manager.php`: thin PHP interoperability facade over the shared result contract.
- `catalog.py`: provider identity and five capability registrations.
- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `policy.py`: tenant/capability guardrails and public metadata sanitization.
- `service.py`: capability-specific request validation; no provider transport.
- `orchestrator.py`: discovery, health and dependency metadata.
- `digitalocean_php_core_ecosystem/DigitalOceanCoreContract.php`: PHP result-contract validation and sanitization.
- `digitalocean_*_core_ecosystem/`: five capability-specific Core packages.
- `digitalocean_shared_*_core_ecosystem/`: eleven shared responsibility packages.
- `tests/`: provider-level behavior tests.
- `ecosystem_manifest.json` and `product_ecosystem_index.json`: machine-readable registry metadata.

## Capability inventory

| Capability | Core package |
|---|---|
| Cloud | `digitalocean_cloud_core_ecosystem` |
| Hosting | `digitalocean_hosting_core_ecosystem` |
| Server | `digitalocean_server_core_ecosystem` |
| Storage | `digitalocean_storage_core_ecosystem` |
| VPS | `digitalocean_vps_core_ecosystem` |

## Layer ownership

| Layer | Owns |
|---|---|
| DigitalOcean Core | Provider identity, capability metadata, contracts, policy, lifecycle and readiness |
| DigitalOcean API Ecosystem | HTTP transport, API versioning, response normalization and provider adapters |
| DigitalOcean Engine | SDK execution, retries, timeouts, queues and scheduling |
| Database / Storage | Durable records, tenant isolation, retention and artifacts |
| Application/UI | Authenticated user context, consent and user-facing workflows |

Core validates metadata and request shape only. It must not resolve credentials, make network requests, retry, persist data or execute provider operations.

## Security and readiness rules

1. Tenant and actor identity must come from the authenticated application layer.
2. Registered capabilities do not prove authorization, entitlement, API availability or live connectivity.
3. Never commit access tokens, refresh tokens, API keys, client secrets or private keys.
4. Destructive, administrative and billing operations require explicit authorization and audit in the appropriate layer.
5. Report a live connection only after deployment authentication and provider smoke tests succeed.

**Current state:** interface and request-contract validation only. Live provider calls are disabled and no live connection is verified.
