# Amazon Route 53 Domain Core

Provider identity and metadata contracts for Amazon Route 53 within Global Domain Core.

- Provider ID: `aws`
- Source scope: DNS hosting and domain registration transfer support
- Official reference: https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html
- API package reference: `aws_domain_api_ecosystem/aws_domain_api_ecosystem.py`
- Status: `CORE_CATALOG_ONLY`

This package does not authenticate, connect to the provider, purchase or transfer domains, change DNS, issue certificates, or perform any other external action. API transport belongs to API; runtime belongs to ENGINE; persistence belongs to DATABASE; secrets and authorization belong to IDENTITY / SECURITY.
