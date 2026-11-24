# APPLE CORE ECOSYSTEM

Provider-level control plane for Apple product identity, product-family catalog, domain classification, capability metadata, lifecycle policy and readiness.

## Product families
- App Store Connect — `apple_app_store_connect_core_ecosystem`
- App Store Server — `apple_app_store_server_core_ecosystem`
- Apple Device Management — `apple_device_management_core_ecosystem`
- iCloud CloudKit — `apple_icloud_cloudkit_core_ecosystem`
- Apple Pay — `apple_pay_core_ecosystem`
- Apple Push Notification Service — `apple_push_notification_core_ecosystem`
- Sign in with Apple — `apple_sign_in_with_apple_core_ecosystem`
- StoreKit — `apple_storekit_core_ecosystem`

## Layer boundaries
- **Core:** identity, capabilities, lifecycle, policy and readiness.
- **API:** Apple authentication/signing, API adapters and HTTP transport.
- **Storage/Database:** durable records, schemas, migrations and transactions.
- **Runtime/Engine:** jobs, queues, retries and execution.
- **Application/UI:** sessions, consent and product workflows.

Core does not store private keys, API keys, signing material, payment credentials or access tokens. Catalog registration is not proof of entitlement, authorization or live connectivity.
