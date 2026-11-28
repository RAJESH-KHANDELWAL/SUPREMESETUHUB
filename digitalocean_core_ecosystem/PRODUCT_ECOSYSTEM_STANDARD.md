# DigitalOcean Capability CORE Package Standard

DigitalOcean Core follows the provider-level Google Core architectural pattern while retaining DigitalOcean-specific capability names and contracts.

## Root-level files

The provider root owns `manager.py`, `manager.php`, `catalog.py`, `contracts.py`, `service.py`, `orchestrator.py`, `policy.py`, `README.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_STATUS.md`, `ecosystem_manifest.json` and `product_ecosystem_index.json`.

## Capability packages

Five capability packages remain separate: Cloud, Hosting, Server, Storage and VPS. Each package keeps its existing ten-folder layout and only the files required for its real Core responsibilities. Do not duplicate provider managers inside capability packages.

## Shared packages

Every shared package uses `digitalocean_shared_<responsibility>_core_ecosystem`. Shared concerns are centralized and reused; capability-specific request validation stays in its own capability package.

## Layer boundaries

API transport and provider SDK clients belong in the DigitalOcean API ecosystem. Retries, timeouts, queues and scheduling belong in ENGINE. Durable records belong in DATABASE/STORAGE. Core performs metadata and request-contract validation only; it never resolves credentials or makes live provider calls.
