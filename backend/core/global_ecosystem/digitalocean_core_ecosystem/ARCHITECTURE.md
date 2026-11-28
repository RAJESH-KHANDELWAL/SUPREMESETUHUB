# DigitalOcean CORE Architecture

## Control-plane flow

1. `catalog.py` declares the DigitalOcean provider and five capability packages.
2. `manager.py` exposes the stable consumer-facing interface.
3. `orchestrator.py` provides discovery, health and dependency metadata.
4. `service.py` dispatches requests to capability-specific validators.
5. Each capability package validates its request shape and rejects secret-like fields.
6. `policy.py` enforces Core metadata and tenant-context boundaries.

## Capability packages

- `digitalocean_cloud_core_ecosystem`
- `digitalocean_hosting_core_ecosystem`
- `digitalocean_server_core_ecosystem`
- `digitalocean_storage_core_ecosystem`
- `digitalocean_vps_core_ecosystem`

Each package owns its own capability contract, service facade, configuration, manifest and tests.

## Shared packages

Shared package names use `digitalocean_shared_<responsibility>_core_ecosystem`. Shared concerns are centralized; capability-specific validation remains inside each capability package.

## Boundaries

API transport, token exchange and provider SDK clients belong to the DigitalOcean API layer. Retries, queues, timeouts and scheduling belong to ENGINE. Persistence belongs to DATABASE/STORAGE. Core never resolves credentials or makes provider network calls.
