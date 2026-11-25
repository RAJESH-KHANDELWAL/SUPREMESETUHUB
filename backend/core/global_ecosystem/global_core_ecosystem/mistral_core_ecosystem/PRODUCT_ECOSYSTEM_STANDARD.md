# Mistral Product Ecosystem Standard

Each product family is represented once in the provider-level catalog and linked to its existing Core and API directories.

A product directory gains implementation files only when a distinct, testable Core responsibility exists. Do not copy shared managers, contracts, catalogs, policy or orchestration into every product directory.

Product metadata may describe capabilities and layer references. It must not claim that an API client, model entitlement, account configuration or live connection exists unless separately verified.

Provider authentication and HTTP transport belong to API; inference and job execution belong to ENGINE/runtime; durable persistence belongs to the shared DATABASE layer; artifacts belong to STORAGE.

The canonical master catalog at `backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json` is read-only. Provider-to-topic references do not create or increment master-catalog entries.
