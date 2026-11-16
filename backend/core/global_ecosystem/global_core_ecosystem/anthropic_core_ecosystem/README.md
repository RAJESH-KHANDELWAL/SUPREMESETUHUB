# ANTHROPIC CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/`

## Mission

Anthropic Core is the provider-level control plane and canonical capability inventory for Anthropic/Claude product surfaces. It owns provider/product identity, capability metadata, tenant context contracts, policy classification, lifecycle, readiness and dependency references.

## Product coverage

Nine product-family Core packages are registered: Messages, Message Batches, Models, Token Counting, Files, Admin Workspaces, Managed Agents, Tool Use, and Authentication/Identity.

Each product package has ten standard subfolders, a manifest, configuration metadata, capability catalog, lifecycle contract, security policy, event contract, service entry point, documentation and offline tests.

## Layer boundaries

| Layer | Owns |
|---|---|
| Anthropic Core | Identity, capability metadata, lifecycle, policy, readiness and orchestration |
| Anthropic API Ecosystem | API-key/OAuth or workload identity flows, HTTP transport, endpoint adapters, response normalization |
| Storage | Durable files and records |
| Database | Persistence, schemas, queries and migrations |
| Runtime/Engine | Jobs, queues, scheduling and tool execution |
| Application/UI | User sessions, consent, user workflows and UI |

Core does not store API keys, exchange tokens, call Anthropic endpoints, persist provider files, execute tools or run jobs.

## Security and readiness

1. Tenant and actor identity must come from the authenticated application layer.
2. Capability registration is not authorization, API-key validity, workspace access or product entitlement.
3. Secret values never enter Core manifests, logs or status responses; use opaque secret references.
4. Administrative, file mutation and other sensitive capabilities require explicit application authorization and audit.
5. Only a separately verified API-layer operation may report a live connection.
6. Catalog-only status remains distinct from configured or connected status.

## Implementation boundary

This is a Core catalog, policy and lifecycle foundation. It does not claim live Anthropic connectivity or that every catalog capability is enabled for an account.
