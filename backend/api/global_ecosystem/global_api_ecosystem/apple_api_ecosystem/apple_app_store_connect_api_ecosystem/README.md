# Apple App Store Connect API Ecosystem

App Store Connect API resources for apps, app metadata, users, roles, builds, TestFlight and reporting. Use App Store Connect API keys with issuer ID, key ID and private key; restrict roles and store private keys server-side.

## Implementation status

Catalog and documentation scaffold only. No live API connector is claimed by this folder. Implement the provider-specific authentication, request signing, response validation, retries, rate limits, tenant authorization and deployment smoke tests before enabling operations.

## Security

Store credentials, signing keys and certificates only in server-side environment configuration or a managed secret store. Never commit secrets, expose them in browser code, or write them to logs. Apply least privilege and audit sensitive actions.

## Canonical provider

See the parent [Apple API Ecosystem](../README.md) and shared adapter `backend/integrations/providers/apple.py`.
