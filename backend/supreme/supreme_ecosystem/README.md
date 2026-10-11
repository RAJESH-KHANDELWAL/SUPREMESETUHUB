# SUPREME ECOSYSTEM

This is the child ecosystem of **SUPREME**. The hierarchy is:

`SUPREME → SUPREME ECOSYSTEM → SUPREME BUSINESS ECOSYSTEM → GLOBAL BUSINESS ECOSYSTEM`

`SUPREME → SUPREME ECOSYSTEM → SUPREME AI ECOSYSTEM → GLOBAL AI ECOSYSTEM`

The Global Business Ecosystem source now lives at:
`supreme_business_ecosystem/global_business_ecosystem/`

The existing Global AI API source tree remains under `backend/api/global_ecosystem/global_api_ecosystem/global_ai_api_ecosystem/` to avoid breaking legacy source paths. It is bridged by `/api/v1/global-ai-ecosystem`, while the existing Central AI and SUPREME PERSONAL AI APIs remain registered.

Private owner-control routes:
- `/api/v1/supreme-ecosystem/business/status`
- `/api/v1/supreme-ecosystem/ai/status`

Public API route registration does not imply public data access; the backend's owner-only middleware applies. Provider credentials and live runtime behavior still require deployment configuration and tests.
