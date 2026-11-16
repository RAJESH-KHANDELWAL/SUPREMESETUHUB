# Vercel Cloud Core Package

**Canonical runtime provider ID:** `vercel`

**Implementation status:** `scaffold_only`

This package reserves the provider-specific Cloud Core boundary and follows the ten-folder Google Cloud Core reference layout. It is not a working provider integration.

## Boundaries
- Runtime catalog metadata remains authoritative in `backend/global_ecosystem/global_cloud_ecosystem/catalog.py`.
- Shared orchestration and safe projections remain owned by Global Cloud Core.
- Provider authentication, SDK clients, network calls, provisioning, persistence and workload execution are **not implemented** here.
- Do not mark this provider live-verified without reproducible, reviewed connection evidence.

## Required implementation sequence
1. Verify official provider identity, auth model, API docs and regional/service availability.
2. Define least-privilege authentication and secret handling.
3. Add typed models and strict schemas.
4. Map only evidenced capabilities.
5. Implement lifecycle/events/services behind explicit policy gates.
6. Add offline contract/security tests; isolate any live tests.

Each responsibility folder contains its own scope note. Replace scaffold documentation with reviewed implementation artifacts as work progresses.
