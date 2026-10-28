# MICROSOFT API ECOSYSTEM

This is the provider-owned Microsoft ecosystem within GLOBAL API ECOSYSTEM. It groups Microsoft's company identity, official platforms, products, developer APIs and service families under one provider-specific boundary.

## Microsoft-owned / Microsoft-operated areas
- **Platforms:** Microsoft 365, Azure Portal, Microsoft Entra admin center, Microsoft Graph, Power Platform and Microsoft Store.
- **API families:** Microsoft Graph, identity/OAuth, Outlook/Mail, Calendar, Teams, OneDrive, SharePoint, Excel, Word, Planner and supported device/tenant administration APIs.
- **Cloud and hosting:** Azure Virtual Machines, App Service, Functions, Blob Storage, Azure SQL, Cosmos DB, Azure DNS, Azure AI services and supported networking/security APIs.
- **Developer ecosystem:** Azure SDKs, Microsoft Graph SDKs, DevOps APIs and application registration.
- **Security and identity:** Microsoft Entra ID, permissions/consent, role-based access, Defender APIs where licensed and authorized.
- **Business ecosystem:** Microsoft 365 and Power Platform APIs subject to tenant licensing and administrator consent.

## Integration rules
1. This directory is a catalog/architecture boundary, not proof of live connectivity.
2. Register applications in the correct tenant, use least-privilege delegated/application permissions and obtain required admin consent.
3. Keep client secrets, certificates and tokens outside Git in environment variables or a managed secret store.
4. Respect tenant licensing, data residency, API throttling and product-specific permissions.
5. Azure DNS is a DNS service; do not imply domain registration unless a separately supported registrar workflow exists.

## Canonical cross-links
- Provider adapter: `backend/integrations/providers/microsoft.py`
- Central registry: `backend/api/global_api_ecosystem_catalog.py`
- Related platform index: `../global_platforms_api_ecosystem/`
- Related families: AI, App, Business, Cloud, Communication, Database, Developer, Hosting, Security, Server, Storage, Web and Website.
