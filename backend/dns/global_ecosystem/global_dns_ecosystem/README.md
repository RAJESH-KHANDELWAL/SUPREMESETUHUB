# GLOBAL DNS ECOSYSTEM

Provider-neutral DNS discovery and orchestration for Cloudflare, Google Cloud
DNS, Hostinger, Namecheap and Amazon Route 53.

## Responsibilities
- Provider metadata registry and capability discovery.
- Shared DNS record and change-request contracts.
- Read-only record listing through explicitly injected provider clients.
- DNS mutations only through an injected client and explicit approval.

## Boundaries
- Provider SDKs, credentials, signing, transport and API-version details belong
  in provider adapter/integration implementations.
- Registry metadata does not imply an authenticated or live connection.
- API owns HTTP routes and request/response validation.
- DNS owns DNS contracts and provider dispatch boundaries.
- Secrets must come from secure configuration/secret management, never source
  files or logs.

## Current status
The provider modules are metadata stubs. No SDKs, credentials or live clients
are configured. Service methods accept injected clients for future integration
and do not claim verified connectivity.
