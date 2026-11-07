# IBM API ECOSYSTEM

Provider-owned catalog entry for IBM enterprise APIs.

## Scope

This provider ecosystem is the IBM-specific catalog boundary. Shared capability families remain in their category directories and refer back to this provider catalog.

Current mapped areas:
- AI: watsonx and related IBM AI services
- Cloud: IBM Cloud APIs
- Database: Db2 and supported data-platform APIs
- Business: IBM enterprise/business platform references
- Security: IBM security and identity services
- VPS: IBM Cloud infrastructure inventory and operations references

## Repository structure

- `ibm_api_ecosystem.py` — provider metadata and ecosystem routing context
- AI, Cloud, Database, Business, Security and VPS category mappings live in their respective shared category folders
- IBM company profile discovery adapter lives in the companies ecosystem
- IBM Cloud hosting references live in the hosting ecosystem

## Integration status

This folder is a catalog and architecture boundary, not a claim of a live IBM API connection. No API credentials are stored in source control. Provider-specific adapters, official API/documentation verification, secret configuration and live integration tests are required before marking any IBM API capability as connected.

Use environment variables or a managed secret store for future credentials. Never commit API keys, access tokens, IAM API keys or service credentials.

## Reference

Official IBM website: https://www.ibm.com/
