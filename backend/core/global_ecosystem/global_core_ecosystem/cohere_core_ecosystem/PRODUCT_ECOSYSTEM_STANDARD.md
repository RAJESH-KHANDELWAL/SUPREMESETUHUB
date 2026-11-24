# Cohere Capability CORE Package Standard

This standard adapts the Google product-Core package convention to Cohere's actual capability inventory.

## Inventory

The current Cohere CORE inventory has exactly five capability packages:
- classify
- command
- embed
- rerank
- tokenize

The package count represents registered capability contracts, not live provider integrations, account entitlement or model availability.

## Required package layout

Each capability package must contain these ten subfolders:

1. authentication/
2. capabilities/
3. docs/
4. events/
5. lifecycle/
6. models/
7. schemas/
8. security/
9. services/
10. tests/

Each package also owns README.md, __init__.py, contracts.py, service.py, ecosystem_config.py and ecosystem_manifest.json. The PHP caller-context contract belongs in authentication/contract.php. Do not create a duplicate package-level php/ directory.

## Ownership

- authentication/: caller/tenant context and opaque secret-reference contract only; no token exchange or secret storage.
- capabilities/: capability-specific descriptive metadata.
- docs/: capability-specific documentation.
- events/: event envelope contract only; event delivery belongs to ENGINE/runtime.
- lifecycle/: capability lifecycle vocabulary.
- models/: capability descriptor.
- schemas/: capability request shape helpers.
- security/: capability security policy boundary.
- services/: capability-owned CORE validation service.
- tests/: capability contract unit tests.

## Provider-level ownership

The parent Cohere CORE owns the canonical catalog, domain taxonomy, shared contracts, policy, provider routing, orchestration and readiness. Shared concerns belong under cohere_shared_* modules. API transport belongs in Cohere API, SDK execution belongs in Cohere ENGINE, persistence belongs in DATABASE/STORAGE, and user sessions/workflows belong in Application/UI.

## Readiness

Every capability remains contract_only and live_provider_calls_enabled=false until the approved API/ENGINE adapters, secure runtime credentials, tenant authorization, model configuration, integration tests and provider smoke tests are verified.
