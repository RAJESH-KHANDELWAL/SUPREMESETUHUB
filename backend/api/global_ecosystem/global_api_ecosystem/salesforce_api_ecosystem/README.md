# Salesforce API Ecosystem

Provider-owned catalog metadata for Salesforce platform APIs.

- Provider ID: `salesforce`
- Main module: `salesforce_api_ecosystem.py`
- Scope: CRM objects, platform, identity, and business workflow APIs, subject to Salesforce org configuration and OAuth scopes.
- Status: catalog-only unless adapter tests pass; live connection is not verified.
- Store credentials in environment variables or a managed secret store. Configure a Salesforce Connected App, OAuth scopes, org/instance, and user or integration permissions before enabling integrations.

This is the canonical Salesforce provider catalog directory.
