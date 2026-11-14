# Global Infrastructure Ecosystem

Central, provider-neutral catalog and governance boundary for the platform's infrastructure domains.

## Ownership
- This package owns cross-domain infrastructure catalogs, provider metadata, capability definitions, integration contracts, registry metadata, and read-only discovery.
- Existing domain implementations remain canonical in `backend/infrastructure/<domain>/`.
- The canonical server ecosystem remains in `backend/server/global_ecosystem/global_server_ecosystem/`.
- Database persistence remains owned by `backend/database/`; storage implementation remains owned by `backend/storage/`.
- CORE validates platform identity and policy; ENGINE owns executable operations; API owns HTTP orchestration.

## Safety and status
Catalog entries describe possible providers and capabilities only. A provider is not connected merely because it appears in a catalog. Live operations require an explicit adapter, configured credentials, authorization, tests, and verified connectivity. This package performs no provisioning, billing, DNS mutation, deployment, backup, or destructive provider action.

## Package map
- `catalog.py`: combined catalog interface
- `providers.py`: provider directory and connection states
- `capabilities.py`: provider-neutral infrastructure capabilities
- `models.py` and `schemas.py`: catalog contracts
- `integrations.py`: integration declarations and verification states
- `services.py`: domain ownership map
- `registry.py`: in-memory metadata registry
- `service.py`: read-only ecosystem facade
- `governance.py`: safety and lifecycle policy metadata
- `structure.py`: canonical domain map

Status: catalog foundation; provider connectivity is not asserted or enabled.
