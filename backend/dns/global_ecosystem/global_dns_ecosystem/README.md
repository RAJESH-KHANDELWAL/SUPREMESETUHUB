# GLOBAL DNS ECOSYSTEM

Provider-neutral DNS discovery and orchestration for Cloudflare, Google Cloud
DNS, Hostinger, Namecheap and Amazon Route 53.

## Responsibilities
- Provider metadata registry and capability discovery.
- Shared DNS record and change-request contracts.
- Read-only record listing through explicitly injected provider clients.
- DNS mutations only through an injected client and explicit approval.
- Consistent status reporting without inferring connectivity from configuration.

## Bada Business boundary
Bada Business is not a DNS provider and must not be added as a provider
implementation here. DNS records for a Bada Business-owned domain use the
selected DNS registrar/host provider (for example Hostinger or Cloudflare).
Any Bada Business-specific domain policy, tenant ownership, onboarding,
subscription, or product workflow belongs to the appropriate Bada Business
domain package (CORE/API); this DNS package only handles DNS record contracts
and provider dispatch. Canonical Bada Business program/catalog facts stay in
`backend/bada_business_ecosystem/`.

## Boundaries
- Provider SDKs, credentials, signing, transport and API-version details belong
  in provider adapter/integration implementations.
- Registry metadata or injected client presence does not prove live connectivity.
- API owns HTTP routes and request/response validation.
- Secrets must come from secure configuration/secret management, never source
  files or logs.
- An approved request is not a persisted audit event; audit persistence must be
  supplied by the owning application workflow.

## Current status
The provider modules are metadata stubs. No SDKs, credentials or live clients
are configured. Service methods accept injected clients for future integration.
Connectivity is deliberately reported as unverified.
