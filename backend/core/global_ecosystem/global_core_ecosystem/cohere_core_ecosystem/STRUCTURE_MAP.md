# Cohere CORE Structure Map

**Root:** `backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem/`

```text
cohere_core_ecosystem/
├── README.md
├── ARCHITECTURE.md
├── IMPLEMENTATION_STATUS.md
├── STRUCTURE_MAP.md
├── __init__.py
├── ecosystem_config.py
├── ecosystem_manifest.json
├── catalog.py
├── product_catalog.py
├── product_ecosystem_index.json
├── domain_catalog.py
├── contracts.py
├── policy.py
├── policies.py
├── module_service.py
├── orchestrator.py
├── manager.py
├── service.py
├── php/
├── cohere_classify_core_ecosystem/
├── cohere_command_core_ecosystem/
├── cohere_embed_core_ecosystem/
├── cohere_rerank_core_ecosystem/
├── cohere_tokenize_core_ecosystem/
└── cohere_shared_*/
```

## Capability package layout

Every `cohere_*_core_ecosystem/` package follows this standard:

```text
cohere_<capability>_core_ecosystem/
├── README.md
├── __init__.py
├── contracts.py
├── service.py
├── ecosystem_config.py
├── ecosystem_manifest.json
├── authentication/
├── capabilities/
├── docs/
├── events/
├── lifecycle/
├── models/
├── schemas/
├── security/
├── services/
└── tests/
```

## Capability inventory

| Package | Capability |
|---|---|
| `cohere_classify_core_ecosystem` | classify |
| `cohere_command_core_ecosystem` | command |
| `cohere_embed_core_ecosystem` | embed |
| `cohere_rerank_core_ecosystem` | rerank |
| `cohere_tokenize_core_ecosystem` | tokenize |

## Provider-wide shared areas

- `cohere_shared_compatibility`
- `cohere_shared_configuration`
- `cohere_shared_contracts`
- `cohere_shared_documentation`
- `cohere_shared_events`
- `cohere_shared_exceptions`
- `cohere_shared_orchestration`
- `cohere_shared_security`
- `cohere_shared_testing`
- `cohere_shared_utilities`
- `cohere_shared_validation`

The package count intentionally remains five capabilities. Do not copy Google's 129-offering count or invent Cohere product families. Add a new package only when a separately owned Cohere capability is defined and verified.

## Boundaries

CORE owns contracts, validation, capability metadata, policy and readiness. API owns transport, ENGINE owns execution, DATABASE/STORAGE own persistence and artifacts, and Application/UI owns user-facing workflows. Live calls remain disabled until the integration and security checks pass.
