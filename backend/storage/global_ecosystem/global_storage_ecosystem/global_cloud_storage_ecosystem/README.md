# GLOBAL_CLOUD_STORAGE_ECOSYSTEM

Provider-neutral global cloud storage taxonomy and metadata foundation.

## Google-style independent category architecture

This ecosystem uses the same direct-child package layout as `GOOGLE_STORAGE_ECOSYSTEM`: each category is an independent `global_cloud_<category>_storage_ecosystem/` folder at this root. Each package owns its README, manifest, Python configuration/models/services, API routes, model export, JSON schema, offline tests, and PHP metadata contract.

- **Independent category packages:** 38
- **Category index:** `category_index.json`
- **Provider catalog:** `provider_index.json`
- **Connection state:** `NOT_CONFIGURED`
- **Storage operations:** Disabled until provider authorization, health checks, and end-to-end tests are complete.

The existing `categories/` directory is retained for backward compatibility; the direct-child packages listed in `category_index.json` are the canonical Google-style category registry.
