# DIGITALOCEAN Storage Ecosystem

Parent namespace for 21 DigitalOcean-related storage category packages.

- `taxonomy/digitalocean_storage_taxonomy.json`: canonical grouped storage taxonomy.
- `category_index.json`: category folder names, groups and repository paths.
- Each category package contains its own README, manifest and Python package entry point.

These packages are catalog and metadata scaffolds. They are not a claim that every category is a separate DigitalOcean product or that any account is connected. Provider API support, product availability, account entitlements, permissions, region availability and operational behavior must be verified independently.

## Architecture boundary
This STORAGE namespace owns storage taxonomy, metadata, lifecycle definitions and health contracts. DigitalOcean API clients, authentication, endpoint operations and external network calls belong in the corresponding API/integration layers. Production persistence belongs in the central database.

## Readiness
All categories start as `NOT_CONFIGURED`. Never mark a provider connected until authorized live health checks and end-to-end tests pass. No upload, download, overwrite or delete operation is enabled by this catalog. Never commit credentials or personal data.