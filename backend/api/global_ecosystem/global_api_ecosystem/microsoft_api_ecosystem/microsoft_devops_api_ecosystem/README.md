# Azure DevOps API Ecosystem

Provider: **MICROSOFT**  
Service family: `microsoft_devops_api`

## Scope
Organizations, projects, repositories, pipelines, builds, work items, and artifacts.

## Connection setup
Azure DevOps organization, scoped PAT or Entra OAuth, and project-level permissions.

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
