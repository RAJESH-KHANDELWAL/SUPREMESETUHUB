# GOOGLE Storage Ecosystem

Storage-owned taxonomy and metadata foundation for Google-related product, service, content and technology categories from Bharat to global scope.

## Structure
- `taxonomy/google_storage_taxonomy.json` — canonical shared catalog.
- `ecosystem_taxonomy.py` — Python loader, listing and lookup.
- `catalog_api.py` — read-only provider-neutral Python API.
- `php/GoogleStorageCatalog.php` — PHP reader using the same JSON source.
- Existing models, registry, service and config remain the metadata foundation.

Every normalized category follows `GOOGLE_<CATEGORY>_STORAGE_ECOSYSTEM`.

This is a storage-side taxonomy, not a list of one-to-one Google products. Some entries are topics or internal namespaces, not Google services. Entries remain `CATALOG_ONLY` and `provider_product_verified=false` until independently validated.

Adult-related entries are classification labels only. Apply age/access controls, consent, privacy, retention and applicable law. Prohibited categories include child sexual abuse material, non-consensual intimate imagery, sexual exploitation, trafficking-related content and other unlawful material.

No Google account connection, OAuth flow, provider API call, upload, download or delete is performed. Mark a provider connected only after authorized credentials, live health checks and end-to-end read/write tests pass. Store secrets in an approved secret manager; never commit tokens or personal data.
