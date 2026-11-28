# Oracle API Ecosystem

Canonical provider-owned Oracle Cloud Infrastructure (OCI) API catalog.

- Provider ID: `oracle`
- Provider metadata: `oracle_api_ecosystem.py`
- Service-family catalogs: 17
- Authentication: OCI Request Signature Version 1 (RSA-SHA256)
- Shared readiness adapter: `backend/integrations/providers/oracle.py`
- Live connection: **not verified**; configuration readiness is not proof of authenticated OCI access.

## Structure

Each service family has its own child directory and catalog module. Shared category mappings remain in the repository's `global_*_api_ecosystem` directories and are referenced by the provider catalog.

## Credentials and security

Configure OCI tenancy, user, fingerprint, region, and private-key material through deployment-managed environment variables or a secret manager. Never commit private keys, passphrases, authorization headers, or tenancy secrets.

Use least-privilege IAM policies, region- and service-specific endpoints, HTTPS, bounded timeouts, retries, and explicit opt-in live integration tests. A successful configuration check must never be represented as a live connection.

## Service-family status

All child entries currently describe catalog scope only. Each service requires its own documented operations, IAM policy review, tests, and authenticated live verification before it can be marked connected.
