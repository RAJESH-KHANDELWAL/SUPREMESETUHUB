# GLOBAL HOSTING CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_hosting_core_ecosystem/`

## Purpose
A normalized, read-only global directory for hosting and hosting-adjacent providers. It separates actual service providers from developer platforms, control-panel software, generic category labels and regional tags.

## Taxonomy
See `hosting_categories.py` for the canonical service taxonomy: shared/WordPress, managed WordPress, cloud/VPS/dedicated compute, managed hosting, application platforms, CDN/edge, object/media storage, managed databases, email, domains/DNS, colocation/data centres, control panels and static/developer hosting.

## Data integrity
- `catalog.py` is the canonical provider inventory; provider IDs and ecosystem IDs are unique.
- `hosting_categories.py` adds explicit category and entity-type classification. Unclassified legacy records remain marked `UNCLASSIFIED`; category labels and software are not counted as provider companies.
- Each provider package exposes a consistent Python/PHP metadata contract.
- Catalog presence does not prove current trading status, service availability, account ownership, price, API access or live connectivity. Verify those separately before integration.
- No API calls, provisioning, DNS changes, deployment, billing, secrets or durable customer data are handled in Core.

## Structure
- `catalog.py`: canonical inventory and enriched lookups.
- `hosting_categories.py`: taxonomy and conservative classification.
- `registry.py`: deterministic lookup and duplicate-ID protection.
- `manager.py` / `manager.php`: read-only metadata facade.
- `models.py`: typed provider metadata contract.
- `tests/test_hosting_core.py`: inventory, classification and package-contract tests.
- Each provider package: `manager.py`, `manager.php`, `__init__.py`, `README.md`.

## Important
This is a maintained inventory baseline, not a claim that every hosting company worldwide has been identified. Add providers only with a verifiable brand identity and an actual hosting-related service. Keep software, service categories and regions as separate entity types.
