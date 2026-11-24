# APPLE API ECOSYSTEM

Canonical provider root for Apple developer APIs and platform integrations in SUPREMESETUHUB.

## Provider structure

- `apple_api_ecosystem.py` — provider registry, API-family metadata and safe catalog listing.
- `apple_app_store_connect_api_ecosystem/` — App Store Connect API.
- `apple_sign_in_with_apple_api_ecosystem/` — Sign in with Apple.
- `apple_push_notification_api_ecosystem/` — Apple Push Notification service (APNs).
- `apple_storekit_api_ecosystem/` — StoreKit and in-app purchase integration boundary.
- `apple_app_store_server_api_ecosystem/` — App Store Server API and server notifications.
- `apple_pay_api_ecosystem/` — Apple Pay integration boundary, subject to merchant and processor eligibility.
- `apple_device_management_api_ecosystem/` — device management and MDM protocol boundary.
- `apple_icloud_cloudkit_api_ecosystem/` — CloudKit and supported iCloud app-data services.

Shared provider adapter: `backend/integrations/providers/apple.py`.

Shared integration registration: `backend/integrations/registry.py` (provider key: `APPLE`).

## API family overview

| Family | Main purpose | Typical authentication boundary |
|---|---|---|
| App Store Connect | App metadata, users, builds, TestFlight and reporting | App Store Connect API key |
| Sign in with Apple | User authentication and identity | Services ID / app identifier and signed client secret |
| APNs | Push notifications | Token-based provider authentication |
| StoreKit | In-app purchases and subscriptions | App-side StoreKit plus server verification |
| App Store Server API | Transaction history and subscription status | App Store Server API JWT |
| Apple Pay | Eligible payment flows | Merchant validation and payment processor |
| Device Management | Managed Apple device lifecycle | MDM enrollment, certificates and protocol |
| CloudKit | App data and cloud records | Container and user/server-scoped authentication |

## Authentication and setup

Apple APIs do not share one universal credential. Select the credential model for the exact API family:

- App Store Connect: issuer ID, key ID and private key.
- Sign in with Apple: Team ID, Services ID or app identifier, Key ID, private key and registered redirect URI.
- APNs: team/key identifiers and APNs signing key, with the correct topic and environment.
- Server APIs: use the API-specific signed JWT and verify all signed responses/notifications.

Configure secrets only in the deployment secret manager. The current readiness adapter checks configuration presence for Sign in with Apple or App Store Connect; it does not perform token generation, key validation or a live API request.

## Security and operational requirements

- Never commit Apple private keys, certificates, tokens or API credentials.
- Keep signing and merchant credentials server-side; never expose them in browser code or logs.
- Apply least-privilege roles, app/container scoping and tenant authorization.
- Validate OAuth state and nonce; verify identity tokens, signed transactions and server notifications.
- Use idempotent handling for purchase events and webhook/server notifications.
- Add request timeouts, bounded retries, rate-limit handling, audit logs and key rotation.
- Require explicit authorization and confirmation for sensitive device-management or account operations.

## Status semantics

- `NEEDS_CONFIGURATION`: required settings are absent.
- `CONFIGURED_NOT_VERIFIED`: settings are present; no successful Apple API operation is implied.
- `CONNECTED`: use only after deployment-level authentication and an API-family smoke test have succeeded.

## Non-duplication rule

Apple-owned API catalogs remain canonical under this provider root. Shared AI, App, Business, Companies, Developer, Integrations, Payment, Platforms, Security, Software and System ecosystems should reference these catalogs rather than duplicate provider implementations.

## Implementation status

The family directories are documentation/catalog scaffolds. They are not eight completed live connectors. Implement and test each API family separately, subject to Apple's current developer program requirements, product entitlements and documented API availability.
