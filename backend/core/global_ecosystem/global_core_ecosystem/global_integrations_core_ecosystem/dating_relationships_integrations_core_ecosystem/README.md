# DATING RELATIONSHIPS INTEGRATIONS CORE ECOSYSTEM

Dating and relationship service provider references; sensitive profile and message data are not stored in CORE.

## CORE responsibilities
- Maintain provider-neutral capability identifiers and integration metadata.
- Define contract, policy and lifecycle expectations for the domain.
- Expose read-only discovery metadata to API and ENGINE consumers.

## Boundaries
- No credentials, access tokens, personal records or customer payloads in CORE.
- No provider SDK calls, HTTP transport, webhook processing or live operations here.
- Provider-specific execution belongs to adapter/integration runtime packages and requires tenant authorization, least-privilege scopes, auditability and secret-manager references.
- Status: `CORE_CATALOG_ONLY`; live provider connectivity is not verified.
