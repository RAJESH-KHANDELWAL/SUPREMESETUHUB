# 👑 SUPREME ECOSYSTEM — Runtime Registry

This directory organizes the existing SUPREME capabilities into separate functional ecosystems without moving live implementation modules or breaking imports.

## Runtime source of truth

- API entry point and router registration: `backend/api/app.py`
- SUPREME owner/control domain: `backend/supreme/`
- Global Business Ecosystem API: `backend/api/global_business_ecosystem.py`
- Global AI Ecosystem API: `backend/api/global_ai_ecosystem.py`

## Functional ecosystems

- `SUPREME-API-ECOSYSTEM/` — API routing, authentication boundaries, health and frontend delivery.
- `SUPREME-BUSINESS-ECOSYSTEM/` — business, project, opportunity, matching, work/income and marketplace workflows.
- `SUPREME-CLOUD-ECOSYSTEM/` — infrastructure, cloud, storage, database, DNS, connectors and service integration.
- `SUPREME-AI-ECOSYSTEM/` — AI, language services, personal AI, WhatsApp AI and global AI workflows.
- `global-business-ecosystem/GLOBAL-BUSINESS-ECOSYSTEM/` — the dedicated Global Business Ecosystem layer.

The registries are architecture/catalog metadata. They do not claim a capability is deployed, connected, or enabled merely because it is listed. Existing runtime files remain in their current locations until imports, tests and deployment paths can be migrated safely. SUPREME, SUPREME ECOSYSTEM and GLOBAL BUSINESS ECOSYSTEM remain separate systems.
