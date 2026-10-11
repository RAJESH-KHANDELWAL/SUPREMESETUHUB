# SUPREMESETUHUB Backend

This directory contains the primary FastAPI backend and all SUPREME runtime modules.

## SUPREME structure

- `supreme/` — SUPREME core, config and owner identity helpers.
- `supreme/ecosystem/` — ecosystem services, ownership, vault and external provider connector framework.
- `api/supreme.py` — private SUPREME endpoints.
- `api/app.py` — central FastAPI app and security middleware.
- `start.py` — production startup wrapper.

## Run from repository root

```bash
python -m pip install -r backend/requirements.txt
python -m backend.start
```

Use `backend/.env.example` as a checklist for deployment variables. Put actual values in private local or hosting environment settings, never in Git commits.

Google/Gmail, Microsoft and WhatsApp integrations remain `NOT_CONFIGURED` until their official provider apps, authorization, secrets and callbacks/webhooks have been configured and tested.
