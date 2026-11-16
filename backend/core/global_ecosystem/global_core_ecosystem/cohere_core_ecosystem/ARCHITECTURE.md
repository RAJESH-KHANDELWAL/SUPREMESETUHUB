# Cohere CORE Architecture

## Provider-root pattern

The provider root follows the Google CORE organization model:
1. Provider-level catalog, product/capability routing, domain taxonomy and orchestration.
2. Dedicated capability Core packages.
3. Provider-wide `cohere_shared_*` modules for reusable contracts and cross-capability concerns.
4. Explicit boundaries to API, ENGINE, DATABASE, STORAGE and Application/UI.

## Capability package standard

Each of the five Cohere capability packages contains these ten subfolders:

| Subfolder | Responsibility |
|---|---|
| `authentication/` | Tenant/actor and opaque credential-reference contract; no secret values |
| `capabilities/` | Capability metadata and supported mode |
| `docs/` | Capability-specific documentation |
| `events/` | Event payload contracts only |
| `lifecycle/` | Capability state vocabulary |
| `models/` | Typed capability descriptor |
| `schemas/` | Payload-shape helpers |
| `security/` | Secret-field and policy checks |
| `services/` | Capability-specific CORE validation facade |
| `tests/` | Capability contract unit tests |

Each package also owns `contracts.py`, `service.py`, `ecosystem_config.py`, `ecosystem_manifest.json`, `README.md` and `__init__.py`.

## Five capability packages

- **Classify:** text classification request contract.
- **Command:** command/chat generation request contract.
- **Embed:** text embedding request contract.
- **Rerank:** query/document relevance ranking contract.
- **Tokenize:** text tokenization request contract.

## Provider-wide shared areas

`cohere_shared_compatibility`, `cohere_shared_configuration`, `cohere_shared_contracts`, `cohere_shared_documentation`, `cohere_shared_events`, `cohere_shared_exceptions`, `cohere_shared_orchestration`, `cohere_shared_security`, `cohere_shared_testing`, `cohere_shared_utilities` and `cohere_shared_validation`.

## Layer ownership

```text
Application / UI
      ↓
Cohere CORE
  ├─ provider catalog and capability routing
  ├─ capability contracts and validation
  ├─ shared policy and lifecycle metadata
  └─ readiness/discovery result
      ↓
Cohere API Ecosystem  → HTTP transport and response normalization
      ↓
Cohere ENGINE         → SDK execution, retries, timeouts, jobs

Cohere DATABASE       → structured state and transactions
Cohere STORAGE        → files, artifacts and retention
```

The API and ENGINE layers above are integration dependencies, not live adapters implemented in this CORE package.

## Current behavior and limits

The public shared service currently checks capability registration and generic input mapping shape. Capability packages expose their own typed request validators and service facades. A future integration must explicitly dispatch requests to the relevant capability service and test that routing before live traffic is enabled.

No Cohere network calls, credentials, provider writes or persistence are enabled by this directory.
