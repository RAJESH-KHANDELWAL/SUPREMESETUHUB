# CLOUDFLARE ANALYTICS AND LOGPUSH API ECOSYSTEM

- Provider: Cloudflare
- Product area: Analytics and Logpush
- Status: `CATALOG_ONLY`
- Live connection verified: `False`

## Scope

Analytics and supported Logpush configuration and observability resources.

## Official documentation

https://developers.cloudflare.com/api/

## API boundary

Product-specific analytics and Logpush endpoints in official API reference

Use only endpoints, permissions and request schemas currently documented by Cloudflare. The path above is a product/API reference, not a promise that every operation is available to every account or plan.

## Implementation rules

- Use a least-privilege Cloudflare API token with only the permissions required for the selected account, zone and product.
- Keep credentials in environment variables or a managed secret store; never commit tokens.
- Validate account/zone IDs and request schemas before sending requests.
- Add mocked unit tests and authenticated integration tests before changing status from `CATALOG_ONLY`.
- Require explicit confirmation, audit logs and idempotency for destructive or production-changing operations.
