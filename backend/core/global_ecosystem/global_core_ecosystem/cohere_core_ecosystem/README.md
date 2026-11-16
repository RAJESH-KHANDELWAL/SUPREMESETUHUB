# Cohere CORE Ecosystem

**Location:** `backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/`

**Role:** Provider-specific CORE boundary for Cohere capabilities. It defines capability contracts, metadata, input checks, policy boundaries and orchestration-facing interfaces. It is not the Cohere HTTP client and does not execute live provider requests.

## 1. Capability inventory

| Capability | Package | CORE responsibility | Current mode |
|---|---|---|---|
| Classify | `cohere_classify_core_ecosystem/` | Classification request contract and input validation | Contract only |
| Command | `cohere_command_core_ecosystem/` | Command/chat generation request contract | Contract only |
| Embed | `cohere_embed_core_ecosystem/` | Text embedding request contract and input validation | Contract only |
| Rerank | `cohere_rerank_core_ecosystem/` | Query/document reranking request contract | Contract only |
| Tokenize | `cohere_tokenize_core_ecosystem/` | Tokenization request contract | Contract only |

The five entries are capability interfaces, not five separate connected Cohere products. Registration in the catalog does not prove that a Cohere API is reachable, authorized or enabled.

## 2. Directory map

| Path | Responsibility |
|---|---|
| `capabilities/` | Canonical capability registry and capability identifiers |
| `cohere_*_core_ecosystem/` | One focused package per capability; owns its request contract and validation entry point |
| `authentication/` | Documents the secure-runtime authentication boundary; no credentials are stored here |
| `contracts.py` | Shared request/result data contracts |
| `models/` | Capability descriptor model |
| `schemas/` | Dependency-free request payload shape checks |
| `security/` | Secret-field protection rules |
| `policies.py` | CORE operation restrictions |
| `lifecycle/` | Ecosystem lifecycle state vocabulary |
| `events/` | CORE event data contract |
| `services/` | Small shared capability lookup service |
| `service.py`, `manager.py` | Shared validation service and public manager facade |
| `php/` | PHP interoperability contract; no provider network calls |
| `tests/` | Unit tests for registry and shared validation behavior |
| `ecosystem_config.py`, `ecosystem_manifest.json` | Non-secret defaults and machine-readable status |

Each capability package currently contains its own README, Python contract module, package initializer and PHP subdirectory. A `.gitkeep` file, where present, is only a Git placeholder; it is not an implementation module.

## 3. Request flow and layer ownership

1. The application supplies an authenticated tenant/actor context and a capability request.
2. CORE checks the capability identifier, request shape and policy boundary.
3. An API adapter is responsible for HTTP transport and provider response normalization.
4. An ENGINE adapter is responsible for provider SDK execution, retries, timeouts and job execution.
5. DATABASE/STORAGE are responsible for persistence and artifacts.
6. CORE returns a typed validation/result contract to its caller.

**CORE must not** store API keys, exchange OAuth tokens, make Cohere network calls, execute retries, persist records or perform provider-side administrative/billing writes.

## 4. Current implementation boundary

**Declared status:** `interface_only`

Implemented in this directory:
- Five capability identifiers in the registry.
- Shared `CapabilityRequest` and `CoreResult` dataclasses.
- Per-capability request dataclasses and basic validation functions.
- Shared capability lookup and validation facade.
- Secret-field and blocked-operation policy helpers.
- PHP capability/shape contract.
- A small unit-test suite for registry and shared validation.

Important limitation: the shared `CohereCoreService.validate()` currently validates the registered capability and generic input mapping. It does **not yet dispatch to each capability package's `validate_request()` function**. Capability-specific validation exists, but is not yet wired into the shared request path.

Not implemented/enabled here:
- Live Cohere API calls or SDK transport.
- Credential storage, token exchange or authentication adapter.
- ENGINE execution, retries or asynchronous jobs.
- DATABASE/STORAGE persistence.
- Verified model availability, account entitlement or production smoke tests.

## 5. Security rules

- Never commit API keys, access tokens, refresh tokens, passwords or private keys.
- Inject credentials only through an approved secret manager or secure runtime/ENGINE adapter.
- Use authenticated application context for tenant and actor identity.
- Treat catalog registration as metadata, not authorization or provider entitlement.
- Require explicit authorization and audit for destructive, administrative, billing or write operations.

## 6. Validation and next steps

Before enabling live operations:
1. Wire each capability validator into the shared service and add negative/positive tests.
2. Add approved API/ENGINE adapters outside CORE, with explicit model and request configuration.
3. Add secure credential injection and tenant/authorization checks.
4. Add integration tests and provider smoke tests using approved credentials.
5. Verify persistence boundaries, observability, retries and deployment configuration.

See [ARCHITECTURE.md](ARCHITECTURE.md), [STRUCTURE_MAP.md](STRUCTURE_MAP.md) and [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) for the detailed breakdown.
