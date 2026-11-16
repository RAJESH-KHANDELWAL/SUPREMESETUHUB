# NameSilo Domain Core

Provider identity and metadata contracts for NameSilo within Global Domain Core.

- Provider ID: `namesilo`
- Source scope: Domain registrar API
- Official reference: https://www.namesilo.com/api_reference.php
- API package reference: `namesilo_domain_api_ecosystem/namesilo_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
