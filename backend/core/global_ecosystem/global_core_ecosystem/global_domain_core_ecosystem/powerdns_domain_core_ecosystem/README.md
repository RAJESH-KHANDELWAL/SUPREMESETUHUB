# PowerDNS Domain Core

Provider identity and metadata contracts for PowerDNS within Global Domain Core.

- Provider ID: `powerdns`
- Source scope: Authoritative DNS API/software
- Official reference: https://doc.powerdns.com/authoritative/http-api/
- API package reference: `powerdns_domain_api_ecosystem/powerdns_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
