# Salesforce REST API API Ecosystem

Provider: **SALESFORCE**  
Service family: `salesforce_rest_api`

## Scope
SObjects, records, queries, describe resources, and REST resources.

## Connection setup
Connected App OAuth and API-enabled user with object/field permissions.

## Integration contract
- Use the provider's official API and current supported SDK/protocol.
- Keep secrets in a managed secret store; never commit credentials or expose them to browser code.
- Enforce tenant/user isolation, least-privilege permissions, request validation, rate limits, audit logging, and safe error handling.
- Implement explicit connection testing and token expiry/revocation handling before showing a persistent Connected state.

## Implementation status
- Service-family catalog and setup specification: scaffolded.
- Live API connection: **not verified**.
- Production credential persistence: **not implemented by this catalog scaffold**.
- Before production use, add a tested provider adapter, integration tests, and deployment-specific secret-store wiring.
