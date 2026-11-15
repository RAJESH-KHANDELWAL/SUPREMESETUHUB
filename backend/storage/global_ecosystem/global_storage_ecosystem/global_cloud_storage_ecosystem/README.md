# GLOBAL_CLOUD_STORAGE_ECOSYSTEM

Provider-neutral global cloud storage taxonomy and metadata foundation.

## Google-style independent category architecture

Each storage category is an independent `global_cloud_<category>_storage_ecosystem/` package directly under this root, matching the direct-child architecture used by `GOOGLE_STORAGE_ECOSYSTEM`.

- **Independent category packages:** 38
- **Category index:** `category_index.json`
- **Provider catalog:** `provider_index.json` (metadata only; no provider package directories in this ecosystem root)
- **Taxonomy:** `taxonomy/`
- **Connection state:** `NOT_CONFIGURED`
- **Storage operations:** Disabled until provider authorization, health checks, and end-to-end tests are complete.

Category and provider package directories are not nested under this ecosystem. Provider records remain catalog metadata only.
