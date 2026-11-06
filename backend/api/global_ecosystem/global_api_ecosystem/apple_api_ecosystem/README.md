# Apple API Ecosystem

Canonical provider-owned catalog for Apple's developer APIs and platform integrations.

## Catalog

- `apple_api_ecosystem.py` — provider metadata and `list_apple_api_ecosystems()`.

## API families

- App Store Connect
- Sign in with Apple
- Apple Push Notification service (APNs)
- StoreKit
- App distribution
- Apple Pay-eligible integrations
- Device management

## Integration boundary

The catalog is metadata, not a live API connection. Runtime authentication and provider readiness are handled separately by:

`backend/integrations/providers/apple.py`

Credentials must be stored in environment variables or a managed secret store. Do not commit private keys, API keys, or certificates.

Live connectivity remains unverified until provider-specific tests are run.
