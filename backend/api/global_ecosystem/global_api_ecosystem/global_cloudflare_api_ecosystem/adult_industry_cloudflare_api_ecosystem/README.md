# Adult Industry — Cloudflare API Mapping

This folder maps Cloudflare's existing products/APIs that may be relevant to a website or service operating in the adult industry. **It is not a claim that Cloudflare offers a dedicated adult-industry API.**

## Relevant Cloudflare product areas

- **Zones and DNS** — domain-zone configuration and DNS records, when the account is authorized.
- **Security / WAF / API Shield** — available website and API security controls, subject to plan and product eligibility.
- **SSL/TLS** — certificate and encryption settings supported by Cloudflare.
- **R2 Storage** — object storage APIs where the account and use case are permitted.
- **Stream / Images** — media-related services only where the provider's current policies, terms, account eligibility, and content rules permit the intended use.
- **Workers / Pages** — application and website infrastructure, subject to current terms and product restrictions.
- **Analytics / Logpush** — supported measurement and log-export capabilities.

## Integration boundary

Adult-industry provider records (platforms, studios, creator services, hosting, payment/payout and affiliate providers) belong in the separate `global_adult_industry_api_ecosystem` catalog. This mapping only identifies Cloudflare services that might be relevant; it does not create a connection between Cloudflare and any named adult provider.

Before implementation, verify the current official API docs, account eligibility, acceptable-use terms, applicable law, privacy, consent and age-gating obligations. Store credentials in environment variables or a managed secret store. No API key is stored here.

## Status

- Catalog status: `CATALOG_ONLY`
- Live connection verified: `false`
- Dedicated Cloudflare adult-industry API confirmed: `false`

Official references:
- https://developers.cloudflare.com/api/
- https://developers.cloudflare.com/directory/
- https://www.cloudflare.com/service-specific-terms/
