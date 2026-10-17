# MICROSOFT API ECOSYSTEM

Canonical company-specific Microsoft API ecosystem package under GLOBAL COMPANIES API ECOSYSTEM.

- Parent provider catalog: `backend/api/global_api_ecosystem_catalog.py`
- Shared readiness adapter: `backend/integrations/providers/microsoft.py`
- Related existing platform package: Microsoft 365 under GLOBAL PLATFORMS API ECOSYSTEM.

The shared adapter currently reports configuration readiness only. Microsoft Graph, Outlook, OneDrive, SharePoint and Azure API operations require feature-specific permissions, consent, token handling and live tests before being considered connected.
