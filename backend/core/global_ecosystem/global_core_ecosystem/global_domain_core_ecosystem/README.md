# GLOBAL DOMAIN CORE ECOSYSTEM

Canonical name: **GLOBAL DOMAIN CORE ECOSYSTEM**  
ID: `GLOBAL-DOMAIN-CORE-ECOSYSTEM`  
Parent: `GLOBAL-CORE-ECOSYSTEM`

## Ecosystem naming rule
Sector ecosystem display names follow **GLOBAL + SUBJECT + CORE ECOSYSTEM**. IDs follow `GLOBAL-SUBJECT-CORE-ECOSYSTEM`. The 39 sector entries are integrated into the canonical catalog and exposed through the manager.

## Modules
- `catalog.py`: canonical root catalog, legacy directory list, domain responsibility catalog and sector ecosystem registration.
- `sector_catalog.py`: 39 sector definitions, standardized display names and IDs.
- `provider_registry.py`: curated discovery references with explicit catalog-only status.
- `manager.py`: canonical manager exposing status, sectors and sector lookup.
- `domain_runtime.py`: read-only metadata runtime.
- `manager.php`: PHP interoperability facade.
- `test_global_domain_core.py`: naming, catalog registration and safety checks.

Provider entries are references, not verified live integrations or a complete global provider census. No API transport or operational domain/DNS actions are enabled in Core.
