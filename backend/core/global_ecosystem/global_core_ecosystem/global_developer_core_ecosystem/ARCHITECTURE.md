# GLOBAL DEVELOPER CORE — ARCHITECTURE

## Request boundary

Authenticated Application Context
-> Developer Core provider/domain discovery and metadata policy
-> Developer API adapter (authentication, authorization, secret resolution and transport)
-> Developer Engine (build, test, execution, deployment or automation)
-> Database / Storage (only when required)
-> Application response

## Ownership

Core owns stable IDs, package parity, provider/domain classification, capability metadata, readiness and dependency discovery. API owns external protocol and transport. Engine owns execution. Database and Storage own persistence and artifacts. Security and Identity own enforcement and secrets.

## Registry rules

- The 29 provider-specific API ecosystem package directories are the current provider package inventory.
- The Developer runtime catalog supplies geographic, maturity, domain and prohibited-use-case taxonomies.
- Existing Core provider paths are preserved and standardized in place.
- `integrations/`, `services/` and `tools/` remain support namespaces, not providers.
- Provider aliases must resolve to canonical IDs; do not create duplicate provider identities.
- Catalog registration never implies API access or a live connection.

## Readiness

`CORE_CATALOG_ONLY` means registered metadata only. A future adapter scaffold or configured connection must have a distinct status and evidence from the owning API layer. Core reports `live_connection_verified=false` until a deployment-level verification result is supplied by the owning integration layer.

## Security

Core contracts accept opaque secret references only where a future boundary needs them; raw credentials and token material are rejected. Adult-only functionality is disabled by default and subject to age assurance, consent, moderation, privacy and legal review.
