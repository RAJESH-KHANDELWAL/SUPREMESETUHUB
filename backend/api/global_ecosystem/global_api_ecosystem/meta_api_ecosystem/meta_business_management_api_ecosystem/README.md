# META BUSINESS MANAGEMENT API ECOSYSTEM

Canonical Meta service-family catalog under `META API ECOSYSTEM`.

## Scope

Business Portfolio assets, system users, partner access, roles and asset assignments.

## Integration boundary

This directory is a catalog and implementation boundary, not proof of a live API integration. Use official Meta developer documentation and verify the exact product API, version, permissions, app mode, account eligibility and review requirements before implementing operations.

## Required implementation layers

- Typed catalog metadata and stable family identifiers.
- Provider adapter/client calls through shared backend integration infrastructure.
- Tenant-scoped authorization and encrypted credential handling.
- Request/response schemas, validation, bounded timeouts and rate-limit handling.
- Webhook verification where the service uses webhooks.
- Unit tests, mocked provider tests and deployment-level smoke tests.

## Security

Never commit app secrets or access tokens. Do not expose tokens to browser clients or logs. Apply least privilege, tenant isolation, revocation/disconnect handling and audit logging.

## Status

`CATALOG_ONLY` — service-family documentation exists; no live connection is asserted.
