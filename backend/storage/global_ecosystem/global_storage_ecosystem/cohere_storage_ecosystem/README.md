# COHERE Storage Ecosystem

Parent namespace for 94 proposed Cohere-related storage taxonomy categories.

- `taxonomy/cohere_storage_taxonomy.json`: canonical category taxonomy and classification groups.
- `category_index.json`: category folder names, intended paths and scaffold status.
- `catalog_api.py`: read-only taxonomy catalog API.
- `ecosystem_taxonomy.py`: taxonomy loader, listing and lookup helpers.
- `ecosystem_manifest.json`: package scope, interfaces and readiness contract.
- `ecosystem_config.py`, `ecosystem_models.py`, `ecosystem_registry.py`, `ecosystem_service.py`: provider storage foundation.

Category entries are organizational namespaces, not claims that Cohere offers each as a distinct product or data-storage service. The index currently records proposed folders as `PLANNED_NOT_CREATED`; it does not claim their scaffolds exist. Provider API support, authorized credentials, live health checks and end-to-end tests are required before enabling integrations or storage operations.
