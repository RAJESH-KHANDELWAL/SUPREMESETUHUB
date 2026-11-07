# IBM API ECOSYSTEM

Provider-owned catalog entry for IBM enterprise APIs.

## Scope and provider boundaries

This directory is the canonical IBM-specific provider catalog. Shared capability-family directories remain separate and reusable across providers. Each IBM category mapping points back to this provider directory.

## Mapped capability families

- **AI** — watsonx and other IBM AI services, subject to product, account and region availability.
- **Cloud** — IBM Cloud platform and resource-management APIs.
- **Database** — Db2 and supported IBM data-platform APIs.
- **Language** — language, speech, translation or related capabilities only where IBM currently documents and offers an applicable API.
- **Business** — IBM enterprise and business-platform references.
- **Security** — IBM security, identity and access-related services.
- **VPS** — IBM Cloud infrastructure inventory and operations references where applicable. This is an infrastructure category mapping, not a claim that IBM exposes a product named VPS.

## Repository structure

- `ibm_api_ecosystem.py` — canonical provider metadata and mapped-family declaration.
- Shared AI, Cloud, Database, Language, Security and VPS mappings are maintained in their corresponding category directories.
- The IBM Business mapping is maintained under the business ecosystem taxonomy.
- IBM company-profile discovery code is maintained under the companies ecosystem.
- IBM Cloud hosting references are maintained under the hosting ecosystem.

## Integration and verification status

**Current status: catalog-only. Live IBM API connectivity is not verified.**

The metadata files describe repository scope and routing only. They do not authenticate to IBM, make API requests, verify entitlement, or prove that a given IBM product/API is enabled for an account or region.

Before any capability is marked connected:
1. Identify the exact IBM product and its current official API documentation.
2. Confirm account, region, plan, entitlement and required IAM permissions.
3. Implement a provider-specific adapter for the documented API.
4. Store credentials only in deployment environment variables or a managed secret store.
5. Run authenticated health checks and capability-specific integration tests.
6. Set live-connection status to true only after those checks pass.

Never commit IBM Cloud API keys, IAM API keys, access tokens, service credentials or other secrets to this repository.

## Official references

- IBM: https://www.ibm.com/
- IBM Cloud: https://www.ibm.com/cloud
- IBM Documentation: https://www.ibm.com/docs/
- IBM Cloud API documentation: https://cloud.ibm.com/apidocs
