# Let's Encrypt Domain Core

Provider identity and metadata contracts for Let's Encrypt within Global Domain Core.

- Provider ID: `letsencrypt`
- Source scope: Automated TLS certificate issuance for domains
- Official reference: https://letsencrypt.org/docs/
- API package reference: `letsencrypt_domain_api_ecosystem/letsencrypt_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
