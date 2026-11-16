# GLOBAL PEOPLE LIFE Storage Ecosystem Foundation

Storage foundation aligned to `GLOBAL_PEOPLE_LIFE_API_ECOSYSTEM`.

## Existing root modules retained
- `ecosystem_config.py` — runtime configuration without embedded secrets
- `ecosystem_models.py` — typed metadata record
- `ecosystem_registry.py` — thread-safe in-memory metadata registry
- `ecosystem_service.py` — provider-neutral foundation health contract
- `ecosystem_manifest.json` — governance and readiness state
- `api_namespace_index.json` — exact API-to-storage namespace mapping
- `tests/` — existing offline foundation tests retained

## Mapping
28 source API namespaces are mapped: 22 domain namespaces and 6 service tiers (Normal, Standard, Advanced, Premium, Enterprise and Supreme).

## Readiness
State: `FOUNDATION_SCAFFOLD_CREATED`. This is not a production people-data platform. No sensitive-data workflows, identity/age-verification, consent service, adult-content service, integrations or external storage operations are claimed as implemented. Production persistence belongs in the central database. Enforce least privilege, encryption, audit logs, strict retention/deletion, consent and safety controls. Do not store real personal data in source control.
