# GLOBAL AI Storage Ecosystem

Parent namespace for 13 independent AI storage category packages, aligned to the Google Storage Ecosystem package hierarchy.

- `taxonomy/global_ai_storage_taxonomy.json`: canonical grouped taxonomy.
- `category_index.json`: category folders, groups and paths.
- Each category contains Python foundation modules, API routes, models, JSON schema, PHP metadata reader, offline tests, README and manifest.
- Root PHP catalog reads the same taxonomy JSON used by Python.

These are catalog scaffolds, not official provider-product claims. All categories remain NOT_CONFIGURED. No live model API, inference, upload, download or delete operation is enabled. Provider API clients/authentication belong in integration layers; production persistence belongs in the central database layer. Never commit credentials or personal data.
