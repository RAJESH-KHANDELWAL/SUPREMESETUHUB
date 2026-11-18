# Cloudflare Product Core Ecosystem Standard

Each canonical Cloudflare product package must contain:

1. `README.md` and `ecosystem_manifest.json`
2. `ecosystem_config.py` and `contracts.py`
3. Ten responsibility folders: `authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, `tests/`
4. A PHP authentication-context contract at `authentication/contract.php`

## Ownership

Core owns product identity, capability metadata, lifecycle contracts, policy metadata and readiness. API owns OAuth/token handling, HTTP transport, SDKs and Cloudflare endpoint adapters. ENGINE owns execution and orchestration. DATABASE and STORAGE own persistence. SECURITY and IDENTITY own authorization, tenant identity and secret management. APPLICATION owns sessions, consent and UI.

## Required package invariants

- Product IDs and capabilities must match the runtime Cloudflare catalog.
- `live_connection` remains false until a controlled account-level verification is recorded.
- API references must be explicit; do not invent API availability or endpoint support.
- No secrets, API tokens or authorization headers in source control or logs.
- Product folders are not proof of implementation.
- Destructive operations and live provider calls require separate API-layer authorization and tests.
