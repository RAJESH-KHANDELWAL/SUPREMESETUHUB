# Cohere CORE Architecture

## Purpose

Cohere CORE is the provider-specific domain and policy boundary for Cohere capabilities. It owns capability identity, request/result contracts, metadata, validation rules and safe orchestration interfaces.

It is deliberately separate from provider transport and execution. A CORE capability being registered does not mean the provider API is connected or that the capability is authorized for a tenant.

## Component responsibilities

| Component | Owns | Does not own |
|---|---|---|
| Capability packages | Capability-specific request dataclasses and input validation | HTTP requests, SDK execution |
| `capabilities/catalog.py` | Canonical capability names and package routing metadata | Provider availability checks |
| `contracts.py` | Shared request/result data structures | Persistence |
| `service.py` | Generic capability and input-shape validation | Capability-specific dispatch today; network I/O |
| `manager.py` | Stable public facade over the shared service | Provider execution |
| `policies.py`, `security/` | Operation restrictions and secret-field checks | Credential issuance or storage |
| `models/`, `schemas/` | Capability metadata and payload-shape helpers | Provider model discovery |
| `lifecycle/`, `events/` | State vocabulary and event payload contract | Queue processing or event delivery |
| `authentication/` | Documents secure authentication injection boundary | Secrets or token exchange |
| `php/` | PHP interoperability validation | Cohere API calls |

## Capability packages

- **Classify:** classification input contract.
- **Command:** command/chat generation input contract.
- **Embed:** text embedding input contract.
- **Rerank:** query, documents and optional top-N contract.
- **Tokenize:** text tokenization input contract.

Each package is independently named so that future API and ENGINE adapters can route to a stable capability identifier without putting transport logic in CORE.

## End-to-end responsibility boundary

```text
Application / UI
  └─ authenticated user, tenant and consent context
       ↓
Cohere CORE
  ├─ capability registry
  ├─ request/result contracts
  ├─ input and policy validation
  └─ orchestration-facing result
       ↓
Cohere API adapter
  └─ HTTP transport, SDK client boundary, response normalization
       ↓
Cohere ENGINE adapter
  └─ execution, retries, timeouts, scheduling and provider calls

DATABASE  ── structured state and transactions
STORAGE   ── files, artifacts and retention
OBSERVABILITY ── logs, metrics, traces and audit
```

The diagram describes intended layer ownership. The API and ENGINE adapters shown above are integration dependencies; they are not implemented by this CORE directory.

## Current validation behavior

The shared `CohereCoreService.validate()`:
1. normalizes the capability name;
2. rejects names absent from the canonical registry;
3. checks that inputs are mapping-like;
4. returns a shared `CoreResult`.

The five capability packages also define their own `validate_request()` functions. At present, the shared service does not call those functions. Connecting that dispatch and adding tests is a required implementation step before treating capability-specific validation as enforced by the public manager.

## Security and authorization

- CORE never stores Cohere credentials.
- Authentication must be injected by a secure runtime or approved secret manager.
- Tenant and actor identity must come from the authenticated application layer.
- Secret values must not be passed as ordinary capability metadata.
- Provider writes, billing changes, model training/fine-tuning, deletion and deployment changes require an explicitly authorized workflow outside CORE.

## Readiness states

The manifest currently declares `interface_only` and `live_provider_calls_enabled: false`. Do not report a live connection until the API/ENGINE integration, secure authentication, approved model configuration, integration tests and provider smoke tests have all succeeded.
