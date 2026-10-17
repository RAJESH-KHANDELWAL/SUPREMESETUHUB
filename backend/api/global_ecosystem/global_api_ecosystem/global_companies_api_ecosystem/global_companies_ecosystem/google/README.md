# GOOGLE API ECOSYSTEM

Canonical company-specific Google API ecosystem package under GLOBAL COMPANIES API ECOSYSTEM.

- Parent provider catalog: `backend/api/global_api_ecosystem_catalog.py`
- Shared readiness adapter: `backend/integrations/providers/google.py`
- Related existing platform packages include Google Workspace, Google Cloud and Google Play under GLOBAL PLATFORMS API ECOSYSTEM.
- AI runtime registration currently includes `google_veo` in `backend/engines/ai/manager.py`.

The shared adapter currently reports configuration readiness only. It does not prove OAuth consent, Gmail/Drive access or any live Google API operation. Implement and test each API/scope explicitly before claiming it is connected.
