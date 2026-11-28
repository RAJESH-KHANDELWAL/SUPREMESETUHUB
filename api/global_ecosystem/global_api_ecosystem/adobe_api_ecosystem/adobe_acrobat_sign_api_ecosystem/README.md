# Acrobat Sign API

Adobe API family catalog for SUPREMESETUHUB.

## Scope
E-signature agreements, participants, signing status and document workflows subject to account entitlement and OAuth scopes.

## Integration rules
- Use the shared Adobe OAuth provider and server-side secret store.
- Request only the minimum product-specific OAuth scopes and permissions.
- Validate organization, product profile, ownership and user authorization before each operation.
- Apply rate limits, timeouts, retries, audit logging and secret redaction.
- Do not advertise desktop application features as API capabilities unless Adobe documents an API for them.

## Status
This folder is a **catalog/documentation scaffold**, not a completed live connector. Implement and test its API operations separately.
