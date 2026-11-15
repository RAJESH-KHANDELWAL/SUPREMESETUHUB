# Atlassian Ecosystem Foundation

- `atlassian_storage_ecosystem.py` — provider catalog and manifest validation
- `ecosystem_service.py` — provider-neutral identity and health contract
- `ecosystem_models.py` — typed storage metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration; no secrets in source
- `ecosystem_manifest.json` — product catalog, geographic scope and connection state

Each product ecosystem contains a README and three classification namespaces: domains, geography and maturity levels. These are taxonomy folders, not duplicated API implementations.

FOUNDATION_READY means only that local metadata code loads. A product is CONNECTED only after authorized authentication, live health checks, required permissions and end-to-end tests pass. Production records belong in central database/object-storage services, not the in-memory registry. Never commit credentials or private customer content.
