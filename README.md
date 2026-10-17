# SUPREMESETUHUB — MAIN BASE FOUNDATION

SUPREMESETUHUB is the central foundation for the SUPREME owner-controlled digital ecosystem.

## Architecture

- `backend/` — primary FastAPI backend and all runtime services.
- `backend/core/global_ecosystem/global_core_ecosystem/catalog.py` — canonical `GLOBAL ECOSYSTEM → GLOBAL CORE ECOSYSTEM` hierarchy, with business, server, database, storage, security, API, AI, search, backup, logging, notifications, and settings core ecosystems registered beneath the core root.
- `backend/api/global_ecosystem/global_api_ecosystem.py` — parallel API hierarchy; API-layer ecosystems remain separate from core-service ecosystems.
- `backend/api/global_freelancer_ecosystem.py`, `backend/engines/freelancer_ecosystem/manager.py`, and `backend/database/freelancer_ecosystem.py` — authenticated freelancer ecosystem API, orchestration engine, and owner-scoped central-database records; file bytes remain in the shared storage engine.
- `backend/supreme/` — SUPREME core package and configuration.
- `backend/supreme/supreme_ecosystem/` — SUPREME ECOSYSTEM modules, connectors, integrations, vault and ownership.
- `backend/supreme/config.py` — backend-side SUPREME configuration; private IDs and email values come from deployment environment variables.
- `backend/supreme/identity_service.py` — backend-side SUPREME profile helpers.
- `backend/api/supreme.py` — authenticated SUPREME API routes.
- `backend/start.py` — primary API startup entry point.
- `frontend/supreme/` — SUPREME interface assets served by the backend.

Root-level SUPREME Python application/configuration files have been removed in favor of the backend package. The production Procfile starts the FastAPI backend.

## Run locally

From the repository root:

```bash
python -m pip install -r backend/requirements.txt
python -m backend.start
```

API docs: `http://127.0.0.1:8000/docs`  
Health: `http://127.0.0.1:8000/health`

## Private environment setup

Copy `backend/.env.example` into your private deployment environment and set the owner identifiers and provider credentials there. Do not commit real emails, OAuth client secrets, WhatsApp tokens, webhook secrets, or AI API keys to GitHub.

## SUPREME owner/admin Google identities

SUPREME supports two separate private owner/admin Gmail identities and a separate security-recovery email through deployment environment variables. Configure `SUPREME_OWNER_PRIMARY_EMAIL`, `SUPREME_OWNER_SECONDARY_EMAIL`, and `SUPREME_OWNER_RECOVERY_EMAIL` in the private Render/service environment. Use the two owner Gmail addresses and the separately designated recovery address already supplied by the owner when configuring those variables. Do not publish these in frontend HTML, public APIs, logs, or Git-tracked environment files. The two owner/admin identities are contact/identity records only and do not independently grant login, owner permissions, or access to Google data.

## External integrations

The SUPREME ECOSYSTEM is the control plane for authorized Google/Gmail, Microsoft Graph and WhatsApp Business integrations. A provider is not connected merely because it appears in configuration: each requires provider-side registration, OAuth/permissions, secure deployment secrets, and end-to-end tests. WhatsApp automated replies additionally require a verified Meta webhook, valid signature verification, approved messaging permissions and a configured AI responder.

## Deployment

Root `render.yaml` and `backend/render.yaml` are retained for compatibility; configure only one Blueprint file per Render service to avoid duplicate services.

## Global platform compatibility

Read [Global Platform Compatibility Standard](docs/GLOBAL_PLATFORM_COMPATIBILITY.md) for the cross-browser, security, accessibility, deployment and release gates. The iOS folder documents the native App Store work still required; it is not a claim that a signed iOS app already exists.

The Android release workflow runs on pushes to `main`, pull requests targeting `main`, and manual dispatch. Passing CI is necessary but does not guarantee app-store approval or prove all live integrations work.

## Provider-neutral hosting and storage

GitHub is the source of truth for code and CI. Render is a temporary runtime, not permanent storage. See [Hosting and Storage Architecture](docs/HOSTING_STORAGE_ARCHITECTURE.md) and [provider status registry](backend/storage/provider_registry.py). The provider catalog records intended targets, but Google Drive, Microsoft Graph/OneDrive, MEGA, AWS S3 and Hostinger-specific storage are not treated as connected until their adapters and end-to-end tests exist.
