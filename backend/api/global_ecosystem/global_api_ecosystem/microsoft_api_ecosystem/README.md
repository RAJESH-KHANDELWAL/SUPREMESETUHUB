# Microsoft API Ecosystem

Canonical provider-owned Microsoft ecosystem catalog.

- Provider ID: `microsoft`
- Main module: `microsoft_api_ecosystem.py`
- Service-family directories: 16
- Authentication foundation: Microsoft Entra ID, OAuth 2.0 / OpenID Connect, Microsoft Graph permissions, and Azure RBAC as applicable.
- Status: catalog and service-family setup scaffolds are present; live connectivity is not verified.

## Service families
- Microsoft Graph
- Entra Identity and OAuth
- Outlook Mail and Calendar
- Teams
- OneDrive and SharePoint
- Office Documents
- Planner and Tasks
- Azure Compute
- Azure App Service and Functions
- Azure Storage
- Azure Database Services
- Azure Networking and DNS
- Azure AI Services
- Security and Defender
- Azure DevOps
- Power Platform

## Deployment requirements
Register an application in Microsoft Entra, configure only required delegated/application permissions, obtain tenant admin consent where required, and assign least-privilege Azure RBAC roles. Keep credentials in a managed secret store. Each service adapter must implement tenant isolation, token refresh/revocation, retries, rate limits, audit logs, and explicit connection tests.

## Verification boundary
Service-family directories are catalog/setup scaffolds. Do not display a persistent Connected status until a real deployment credential has passed a live test. Production credential persistence and live API connectivity are not claimed by this scaffold.
