# Cohere CORE Architecture

## Provider-root pattern

The provider root is the single canonical Cohere control plane:
1. Provider identity, capability inventory, product routing and domain taxonomy.
2. Shared request/result contracts, tenant context, secret references and lifecycle vocabulary.
3. Provider policy, discovery, readiness and orchestration.
4. Five dedicated capability CORE packages.
5. Explicit boundaries to API, ENGINE, DATABASE, STORAGE and Application/UI.

No duplicate root-level generic authentication/, capabilities/, events/, lifecycle/, models/, schemas/, security/ or services/ package trees are retained. Their reusable responsibilities live under the corresponding cohere_shared_* modules.

## Capability package standard

Each of the five capability packages contains the ten Google product-Core subfolders:

| Subfolder | Responsibility |
|---|---|
| authentication/ | Tenant/actor context and opaque credential-reference contract; no secret values |
| capabilities/ | Capability metadata and supported contract mode |
| docs/ | Capability-specific documentation |
| events/ | Event payload contracts only |
| lifecycle/ | Capability state vocabulary |
| models/ | Typed capability descriptor |
| schemas/ | Payload-shape helpers |
| security/ | Secret-field and policy checks |
| services/ | Capability-specific CORE validation facade |
| tests/ | Capability contract unit tests |

Each package also owns contracts.py, service.py, ecosystem_config.py, ecosystem_manifest.json, README.md and __init__.py. PHP caller-context contracts are placed at authentication/contract.php, not in duplicate package-level php/ directories.

## Five capability contracts

- Classify: non-empty text inputs and optional example mappings.
- Command: non-empty message and optional chat-history mappings.
- Embed: non-empty text sequence and optional input type.
- Rerank: non-empty query/documents and optional positive integer top-N.
- Tokenize: non-empty text input.

Provider-level CohereCoreService dispatches each request to its capability-owned validator. Unsupported fields, malformed values, nested secret-like keys and unimplemented execution options are rejected rather than silently ignored.

## Provider-wide shared areas

- cohere_shared_compatibility: contract version metadata.
- cohere_shared_configuration: non-secret defaults.
- cohere_shared_contracts: request/result, tenant, secret-reference, lifecycle and descriptor contracts.
- cohere_shared_documentation: provider documentation index.
- cohere_shared_events: event envelope; delivery belongs to ENGINE/runtime.
- cohere_shared_exceptions: provider exception taxonomy.
- cohere_shared_orchestration: capability registry and stable manager exports.
- cohere_shared_security: recursive secret-field checks and security boundary.
- cohere_shared_testing: provider-wide contract and policy tests.
- cohere_shared_utilities: pure identifier helpers.
- cohere_shared_validation: dependency-free request-shape helpers.

## Layer ownership

Application/UI -> Cohere CORE -> capability contract validation -> normalized CORE result.
Cohere API Ecosystem owns transport, authentication adapters and response normalization.
Cohere ENGINE owns SDK execution, retries, timeouts, queues and scheduling.
Cohere DATABASE owns structured state and transactions.
Cohere STORAGE owns files, artifacts and retention.

API and ENGINE are integration dependencies, not live adapters implemented by this CORE package.

## Security and readiness

No credentials are stored or resolved in CORE. Tenant identity is supplied by the authenticated application. Secret-like fields are rejected recursively. Destructive, administrative, deployment and billing actions require explicit authorization and an approved API/ENGINE workflow. Catalog registration does not prove entitlement, API access, model availability or provider authorization.

## Current behavior and limits

Provider and capability catalogs are read-only metadata. The provider facade performs contract validation only. No Cohere network calls, token exchange, SDK execution, provider writes, persistence or user-facing workflows are enabled here.
