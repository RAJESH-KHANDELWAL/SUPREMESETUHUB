# DeepSeek Core Package Standard

DeepSeek Core follows the provider-level Google Core architectural pattern while retaining DeepSeek-specific capability names and contracts.

## Root-level files

The provider root owns `manager.py`, `manager.php`, `catalog.py`, `contracts.py`, `service.py`, `orchestrator.py`, `policy.py`, `README.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_STATUS.md`, `ecosystem_manifest.json` and `product_ecosystem_index.json`.

## Capability packages

Each capability package owns only its actual contract, service facade, configuration, manifest, tests and documentation. Do not create fixed empty folders or duplicate shared managers in each capability package.

## Shared packages

Every shared package uses the form `deepseek_shared_<responsibility>_core_ecosystem`. Shared concerns are centralized and reused; capability-specific request validation stays in its own capability package.

## Layer boundaries

API transport and provider SDK clients belong in the DeepSeek API ecosystem. Retries, timeouts, queues and scheduling belong in ENGINE. Durable records belong in DATABASE/STORAGE. Core performs metadata and request-contract validation only; it never resolves credentials or makes live provider calls.
