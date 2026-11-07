# Salesforce API Ecosystem

Canonical provider-owned Salesforce ecosystem catalog.

- Provider ID: `salesforce`
- Main module: `salesforce_api_ecosystem.py`
- Service-family directories: 14
- Authentication foundation: Salesforce Connected App / OAuth 2.0, org-specific domain, scopes, and integration-user permissions.
- Status: catalog and service-family setup scaffolds are present; live connectivity is not verified.

## Service families
- Identity and OAuth
- REST API
- SOAP API
- Composite API
- Bulk API 2.0
- Platform Events and Pub/Sub
- Streaming API
- Metadata and Tooling APIs
- Apex APIs
- Files and Content
- Service Cloud
- Marketing Cloud
- Data Cloud
- Analytics and CRM Analytics

## Deployment requirements
Create/configure a Connected App, select least-privilege OAuth scopes, use a dedicated API-enabled integration user, and grant only required object/field permissions. Marketing Cloud and Data Cloud require their own entitlements and tenant-specific configuration. Store secrets in a managed secret store; use sandbox-first validation.

## Verification boundary
Service-family directories are catalog/setup scaffolds. Do not display a persistent Connected status until a real org credential has passed a live test. Production credential persistence and live API connectivity are not claimed by this scaffold.
