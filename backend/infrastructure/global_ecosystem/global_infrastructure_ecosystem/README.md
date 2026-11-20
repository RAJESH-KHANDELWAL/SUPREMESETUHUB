# GLOBAL INFRASTRUCTURE ECOSYSTEM

Canonical ownership for Infrastructure control-plane modules and 21 infrastructure domain implementations.

## Canonical modules
The canonical implementations are stored under `modules/`:
- `controller.py`
- `repository.py`
- `service.py`
- `hostinger_catalog.py`

The parent `backend/infrastructure/` files with these names are compatibility shims only. The module registry in `modules/__init__.py` points directly to the canonical ecosystem implementations.

## Domain structure
All 21 domain folders live directly inside this ecosystem root. There is no intermediate `domains/` wrapper:
- `backup/`, `billing/`, `cdn/`, `containers/`, `database/`, `dns/`, `domains/`
- `email/`, `firewall/`, `ftp/`, `hosting/`, `ipam/`, `load_balancer/`, `model/`
- `monitoring/`, `network/`, `object_storage/`, `security/`, `server/`, `ssl/`, `storage/`

## Supporting structure
- `integrations/`: CORE and Global CORE integration entry points.
- `structure.py`: canonical ownership and package path registry.
- `manager.py` / `manager.php`: structural domain health checks.
- Hostinger API and NSFWinfra provider adapters are owned by `backend/global_ecosystem/` in `global_hosting_ecosystem/` and `nsfwinfra_ecosystem/`; this infrastructure ecosystem references them through the provider module registry.

## Cross-layer boundaries
CORE stays in `backend/core/`; database persistence in `backend/database/`; storage runtime in `backend/storage/`; server ecosystem in `backend/server/`; provider execution in ENGINE; HTTP orchestration in API.

A catalog or manager result is not evidence of live provider connectivity. Live provider operations require documented APIs, credentials managed outside source, scoped authorization, audit logging, tests and verified connectivity.
