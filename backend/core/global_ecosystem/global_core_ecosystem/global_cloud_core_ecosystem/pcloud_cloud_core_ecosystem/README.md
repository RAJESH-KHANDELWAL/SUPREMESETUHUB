# Provider-specific Cloud Core scaffold

**Status:** `scaffold_only` — no live provider integration is enabled.

This directory represents a canonical provider package. Its folder name is derived from the provider ID in the authoritative runtime catalog at `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`.

The ten responsibility folders follow the Google Cloud Core reference layout:
`authentication/`, `capabilities/`, `docs/`, `events/`, `lifecycle/`, `models/`, `schemas/`, `security/`, `services/`, and `tests/`.

Do not infer API support, authentication success, regional availability, production readiness or live connectivity from the existence of this scaffold.

## Implementation gates

1. Verify provider identity and official API documentation.
2. Document authentication, least-privilege scopes and secret handling.
3. Define typed models and strict schemas.
4. Map only capabilities supported by evidence.
5. Implement adapters behind Core policy and safety controls.
6. Add offline contract/security tests before any isolated live tests.

No credentials, SDK clients, network calls, provisioning, workload execution or persistence are included in this scaffold.
