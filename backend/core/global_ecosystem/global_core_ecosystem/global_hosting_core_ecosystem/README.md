# GLOBAL HOSTING CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem/`

## Mission

Canonical read-only inventory and governance layer for hosting providers, capability metadata and readiness. It does not provision servers, modify DNS, deploy applications, manage billing or call provider APIs.

## Architecture

- `catalog.py`: canonical inventory of 118 provider packages.
- `registry.py`: deterministic lookup and duplicate-ID protection.
- `manager.py`: public Python manager and provider tree.
- `manager.php`: PHP metadata facade.
- `models.py`: typed provider metadata contract.
- `tests/test_hosting_core.py`: structural and behavior tests.
- Each provider package contains Python/PHP managers, exports and README.

API clients belong in API; durable state belongs in Storage/Database; provisioning belongs in Engine/Infrastructure. Catalog presence is not proof of account ownership, entitlement, credentials or live connectivity. Never store secrets in Core metadata.
