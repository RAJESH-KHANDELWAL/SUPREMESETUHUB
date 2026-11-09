# Global Setu — Compatibility Namespace

This path is intentionally provided alongside `backend/global_hub/global_setu/`
to support the shorter backend namespace requested by the project.

## Canonical ownership

- Canonical Global Hub location: `backend/global_hub/global_setu/`
- Compatibility import location: `backend/global_setu/`
- Domain services remain in their own packages; neither path duplicates or
  replaces Business, Bada Business, Company, Platform, Person/Freelancer or
  other domain implementations.

## Import compatibility

The Python package at this path delegates to
`backend.global_hub.global_setu`. New Global Setu implementation modules
should be authored in the canonical package, not copied into both locations.

## Current status

This is a namespace and import-compatibility layer only. It does not yet
provide a live service registry, API gateway, service discovery, health
monitoring or production integration. Those capabilities require separately
implemented contracts, route wiring and tests.
