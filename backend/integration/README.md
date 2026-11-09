# Bada Business integration

The Bada Business integration is currently a **read-only resource-catalog integration**.

## Architecture

- Provider: `backend/integration/provider/bada_business.py`
- Connector: `backend/integration/connector/bada_business.py`
- Connector registry: `backend/integration/connector/registry.py`
- API: `backend/api/bada_business_integration.py`
- Canonical resource data: `backend/bada_business_ecosystem/platform_resources/`
- Tests: `backend/tests/test_bada_business_integration.py`

The canonical ecosystem remains the single source of truth for referral links and program metadata. The provider and connector expose that data without maintaining duplicate catalogs.

## API routes

These routes are mounted in the FastAPI application and follow the application's default owner-authentication policy:

- `GET /api/v1/bada-business-integration/status`
- `GET /api/v1/bada-business-integration/catalog`
- `GET /api/v1/bada-business-integration/links`
- `GET /api/v1/bada-business-integration/links/{link_id}`
- `GET /api/v1/bada-business-integration/programs`
- `GET /api/v1/bada-business-integration/programs/{program_id}`

## Current connection boundary

- Resource catalog: available
- Referral link and program lookup: available
- Provider authentication: not configured
- Official public developer API: not verified
- Live provider connection: not connected
- Purchase, enrollment, payment, lead submission, and account actions: not implemented

Do not interpret catalog availability as a live Bada Business account connection. Do not add undocumented endpoints or collect provider credentials until an official supported integration contract is available.
