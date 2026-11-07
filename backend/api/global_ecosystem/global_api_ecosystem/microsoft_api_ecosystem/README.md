# Microsoft API Ecosystem

Canonical provider-owned Microsoft ecosystem catalog and shared backend adapter.

- Provider ID: `microsoft`
- Service-family directories: 16
- Shared live-verification adapter: `backend/integrations/providers/microsoft.py`
- Verification route: `POST /api/v1/integrations/providers/microsoft/verify` (authenticated)
- Authentication mode implemented: Entra ID OAuth 2.0 client credentials (application permissions)
- Live connection: verified only when the verification route successfully obtains a token and calls Microsoft Graph.

## One-time platform-owner setup

Set these server-side environment variables in the deployment secret manager:

- `MICROSOFT_TENANT_ID` — tenant GUID or verified tenant domain (not `common`)
- `MICROSOFT_CLIENT_ID` — Entra application/client ID
- `MICROSOFT_CLIENT_SECRET` — client secret value; never commit it

In Microsoft Entra:
1. Register an application in the target tenant.
2. Add Microsoft Graph **Application** permission `Organization.Read.All` and grant tenant admin consent.
3. Create a client secret or preferably configure certificate/workload identity for production.
4. Deploy the values as server-side secrets and call the authenticated verification route.

The verifier requests a short-lived token and calls `GET https://graph.microsoft.com/v1.0/organization?$select=id,displayName`. A 403 usually indicates missing Graph application permission or admin consent.

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

## Verification and security boundary

The current live verifier uses deployment-managed application credentials, verifies tenant-level Graph access, and discards the access token after the request. It does **not** persist credentials or create per-customer OAuth connections. Each service family still requires its own least-privilege permissions, adapter operations, tests, and product entitlement checks. Never mark every Microsoft service connected based on the tenant-level probe.
