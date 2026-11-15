# GLOBAL APP Storage Ecosystem

Parent namespace for 184 APP storage category packages across 18 classification groups, aligned to the Google Storage Ecosystem architecture.

- `taxonomy/global_app_storage_taxonomy.json`: canonical grouped taxonomy.
- `category_index.json`: category folders, groups and repository paths.
- Each category package contains Python foundation modules, API routes, models, PHP metadata reader, JSON schema, offline tests, README and manifest.
- Root PHP catalog reads the shared taxonomy JSON used by Python.

Catalog scaffolds only. App/vendor ownership and product support must be separately verified. Every integration remains NOT_CONFIGURED until authorized access, live health checks and end-to-end tests pass. This taxonomy does not enable app installation, distribution or data-transfer operations. Provider-specific APIs belong in integration layers; production persistence belongs in the central database layer. Never commit credentials, app binaries or personal data.
