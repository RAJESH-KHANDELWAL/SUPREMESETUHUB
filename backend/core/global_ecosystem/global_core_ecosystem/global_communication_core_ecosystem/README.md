# Global Communication Core Ecosystem

Provider-neutral, metadata-first communication ecosystem for email, messaging, voice, video meetings, collaboration, communication APIs, notifications, privacy, trust and safety.

## Canonical structure
- `manager.py`: Python entry point.
- `manager.php`: PHP interoperability facade only.
- `product_catalog.py`: inventory of the 19 existing directory entries.
- `domain_catalog.py`: communication domain taxonomy.
- `orchestrator.py`: read-only catalog orchestration.
- `service.py`: service status and health facade.
- `policy.py`: authorization and restricted-domain boundaries.
- `test_global_communication_core.py`: unit tests.

## Master catalog
Reads `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` as the single master source. It does not copy, edit, or inflate the master catalog. Current counts are read dynamically.

## Implementation truth
The 19 listed entries correspond to existing directory placeholders. They are not 19 live integrations. Provider connectivity, OAuth, sending, calling, message storage and webhooks are not implemented or verified by this package. Credentials must remain in an external secret store.

## Run tests
`python -m unittest backend.core.global_ecosystem.global_core_ecosystem.global_communication_core_ecosystem.test_global_communication_core`
