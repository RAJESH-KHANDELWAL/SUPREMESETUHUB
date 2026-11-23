# Adobe Firefly — Core Ecosystem

Generative AI capabilities, model metadata, provenance and usage policy.

## Core ownership

This package owns product identity, capability metadata, lifecycle state, policy metadata, readiness and stable contracts. Provider HTTP/OAuth clients belong to the API layer; persistence belongs to Storage/Database; jobs belong to Runtime/Engine; user-facing journeys belong to Application/UI.

## Package state

- Package scaffold: present
- Product-specific capability definitions: pending verification and implementation
- Live Adobe connection: not configured or verified
- Credentials and entitlements: never stored in this package

## Standard directories

- `authentication/`
- `capabilities/`
- `docs/`
- `events/`
- `lifecycle/`
- `models/`
- `schemas/`
- `security/`
- `services/`
- `tests/`

See `ecosystem_manifest.json` for machine-readable metadata.
