# Anthropic Storage Ecosystem Foundation

This directory follows the provider-catalog structure used by the Adobe Storage Ecosystem.

## Provider-level files
- `anthropic_storage_ecosystem.py` — canonical child catalog and manifest reader
- `ecosystem_manifest.json` — child modules, Bharat-to-global coverage, maturity levels, domain scope and readiness state
- `ecosystem_config.py` — runtime configuration; secrets must come from a secret manager or environment
- `ecosystem_models.py` — typed metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider-neutral service foundation
- `tests/` — offline foundation and catalog tests

## Child storage ecosystems

Each child module contains `domains/`, `geography/` and `maturity_levels/`:
- Bharat, regional and global geography
- Normal, Professional, Advanced, Enterprise and Supreme maturity classifications
- Broad domains, including lawful adult-only sexual wellness, adult sexual content, adult entertainment and pornography classification

## Architecture boundary

Anthropic API clients, authentication, endpoints, scopes and API operations belong to the API Ecosystem. This Storage Ecosystem owns storage-side taxonomy, metadata, lifecycle, mappings and health. It must not duplicate API clients or authentication.

## Readiness and governance

The folder structure is taxonomy/scaffolding only. It does not establish that any Anthropic product surface has a generic storage API or is connected. Verify product availability, account entitlements, permissions and supported operations before marking a child CONNECTED. Require authorized credentials, live health checks and end-to-end read/write tests.

Adult-only classifications require lawful adult contexts, age assurance, informed consent, privacy/security safeguards, retention and takedown controls, and jurisdiction-specific legal review. Prohibit minors, coercion, exploitation and non-consensual intimate imagery. Never commit credentials or personal data.
