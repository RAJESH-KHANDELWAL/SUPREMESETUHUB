# Cohere Core Implementation Status

## Google Core architecture alignment

- Canonical provider catalog and defensive-copy accessors.
- Canonical `CohereCoreManager` with `get_manager()`.
- Provider manager methods for status, health, product/capability discovery, domain inventory, offerings and dependency map.
- Four Cohere-specific domains with read-only `CohereCoreDomainManager`.
- Five capability-family packages with their own typed contracts and validators.
- Provider contracts for tenant context, opaque secret references, request/result and readiness.
- Policy guardrails for capability registration, sensitive operations and secret-field rejection.
- Provider module service, orchestrator and service facade.
- PHP interoperability facade.
- Machine-readable ecosystem manifest and product index.
- Provider-wide tests under `tests/`; capability-specific tests remain in each capability package.

## Capability inventory

Exactly five capability packages are registered: classify, command, embed, rerank and tokenize. They are grouped into four domains: language_understanding, text_generation, vector_representation and text_processing.

## Security boundaries

Core validates metadata and caller context only. It does not resolve credentials, authenticate to Cohere, call provider endpoints, execute SDK requests, persist data or run jobs. Tenant and actor identity must be supplied by the authenticated application layer. Secret-like payload fields are rejected by the validation boundary. Sensitive operations remain subject to explicit authorization and audit in API/ENGINE workflows.

## Naming audit

Capability package directories use the `cohere_<capability>_core_ecosystem` convention. The eleven existing shared support directories still use `cohere_shared_<area>` without the `_core_ecosystem` suffix. Their contents and imports have not been moved; this naming normalization remains open.

## Readiness

- Provider status: `interface_only`.
- Registered capability packages: 5.
- Domain groups: 4.
- Live provider calls enabled: false.
- Verified live connections: 0.
- API calls performed by Core: 0.
- Production authentication, model availability and provider smoke tests: unverified.

## Verification

Provider-wide alignment tests are present at `tests/test_google_core_alignment.py`. Test files being committed does not mean they have passed. Confirm the relevant GitHub Actions workflow result before treating the suite as green.

## Release gate

Do not enable live readiness until API/ENGINE adapters, secure runtime credential injection, tenant authorization, model configuration, integration tests, provider smoke tests and deployment checks are implemented and verified.
