# 👑 SUPREME DASHBOARD

This folder is the architecture/catalog location for the MAIN SUPREME Dashboard.

## Existing runtime source

- API router: `backend/api/supreme.py`
- Owner configuration: `backend/supreme/config.py`
- Identity and profile services: `backend/supreme/identity_service.py`
- SUPREME control services: `backend/supreme/control.py` and `backend/supreme/controller.py`

The existing router exposes the owner-protected SUPREME dashboard, identities, status, health, profile, and related endpoints. Keep its live router in `backend/api/supreme.py` until imports, router registration, tests, and deployment wiring are migrated together. This folder documents the dashboard domain; it does not duplicate or relocate live API code.
