# BADA BUSINESS DNS ECOSYSTEM

Tenant-aware DNS facade for Bada Business-owned domains.

## Responsibilities
- Resolve a tenant/domain binding through an injected binding repository.
- Enforce tenant, domain, provider and zone consistency before dispatch.
- Delegate record reads and approved record changes to the shared GLOBAL DNS
  service rather than reimplementing provider execution.
- Report provider connectivity as unverified unless a separate health-check
  mechanism proves otherwise.

## Architecture boundaries
- This package is a Bada Business domain facade, not a DNS provider.
- Cloudflare, Google Cloud DNS, Hostinger, Namecheap and Route 53 remain the
  actual DNS providers.
- Tenant/domain binding persistence belongs to the injected repository.
- Subscription eligibility, domain purchase, tenant onboarding and business
  policies belong to Bada Business CORE; HTTP endpoints belong to API.
- Provider SDKs, credentials and network calls remain behind shared DNS
  provider adapters.
- Canonical Bada Business programs, prices and links remain in
  `backend/bada_business_ecosystem/`; no catalog facts are copied here.

## Integration contract
Provide a repository implementing
`get_binding(tenant_id, normalized_domain)`. The returned binding must expose
`tenant_id`, `domain`, `provider_id`, `zone_id`, and `enabled`.
Pass a configured shared `GlobalDNSService` with injected provider clients
when actual DNS operations are required.

No provider credentials, live DNS client, domain purchase flow or persistent
tenant binding repository is included in this package.
