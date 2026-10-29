# CLOUDFLARE SECURITY AND WAF API ECOSYSTEM

- Provider: Cloudflare
- Product area: Security and WAF
- Status: `CATALOG_ONLY`
- Live connection verified: `False`

## Scope

Security rules and rulesets exposed by Cloudflare APIs.

## Official documentation

https://developers.cloudflare.com/api/resources/rulesets/

## API boundary

Rulesets API resources

Use only endpoints, permissions and request schemas currently documented by Cloudflare. The path above is a product/API reference, not a promise that every operation is available to every account or plan.

## Implementation rules

- Use a least-privilege Cloudflare API token with only the permissions required for the selected account, zone and product.
- Keep credentials in environment variables or a managed secret store; never commit tokens.
- Validate account/zone IDs and request schemas before sending requests.
- Add mocked unit tests and authenticated integration tests before changing status from `CATALOG_ONLY`.
- Require explicit confirmation, audit logs and idempotency for destructive or production-changing operations.
