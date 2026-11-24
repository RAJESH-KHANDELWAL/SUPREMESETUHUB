# Ecosystem Foundation

Reusable provider storage foundation. Existing unrelated provider-specific files are retained.

## Modules
- `ecosystem_service.py` — provider identity and truthful health contract
- `ecosystem_models.py` — typed metadata records
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_manifest.json` — Bharat-to-global scope and readiness state
- `platform_links.json` — Bada Business platform destination catalog
- `course_links.json` — Bada Business Community course destination catalog
- `links_catalog_README.md` — link catalog documentation
- `tests/test_foundation.py` — offline foundation tests

## Readiness
FOUNDATION_READY means local package code loads. Stored links are reference metadata, not a live provider connection or proof of account/course access. Production persistence belongs in the central database. Use least privilege, encryption, audit logs, retention controls and jurisdictional compliance. Never commit credentials or personal data.
