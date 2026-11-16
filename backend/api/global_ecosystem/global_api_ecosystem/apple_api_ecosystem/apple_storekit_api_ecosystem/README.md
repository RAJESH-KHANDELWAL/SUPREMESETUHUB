# Apple StoreKit API Ecosystem

StoreKit integration boundary for in-app purchases and subscription entitlement workflows. Validate signed transaction data, product identifiers, environment and app ownership; do not treat client-side purchase claims as authoritative.

## Implementation status

Catalog and documentation scaffold only. No live API connector is claimed by this folder. Implement the provider-specific authentication, request signing, response validation, retries, rate limits, tenant authorization and deployment smoke tests before enabling operations.

## Security

Store credentials, signing keys and certificates only in server-side environment configuration or a managed secret store. Never commit secrets, expose them in browser code, or write them to logs. Apply least privilege and audit sensitive actions.

## Canonical provider

See the parent [Apple API Ecosystem](../README.md) and shared adapter `backend/integrations/providers/apple.py`.
