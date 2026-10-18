# CRM

The people-facing CRM domain lives directly in this module. CRM Ecosystem
orchestration belongs only under `backend/supreme/supreme_ecosystem/`. The
owner's private CRM must use a separate module, storage boundary, and permissions.

## Implemented foundation

- Canonical contact model with consent and DO_NOT_CONTACT validation.
- SQLite persistence through the central DatabaseService using namespaced
  `crm_contacts` and `crm_audit_log` tables; records are scoped by signed-in user.
- Authenticated API for contact CRUD, summary reports, duplicate candidates,
  category/follow-up suggestions, message drafts, and audit history.
- Duplicate detection only suggests matches; it never auto-merges.
- Category suggestions are transparent rules and require human approval.
- Outreach drafts are never sent automatically and require explicit contact consent.
- Google sync preview reports zero writes and makes no external API calls.

## API

- `/api/v1/crm/status`
- `/api/v1/crm/contacts` (GET/POST)
- `/api/v1/crm/contacts/{contact_id}` (GET/PATCH/DELETE)
- `/api/v1/crm/ai/duplicates`
- `/api/v1/crm/ai/categories`
- `/api/v1/crm/ai/follow-ups`
- `/api/v1/crm/reports/summary`
- `/api/v1/crm/contacts/{contact_id}/message-draft`
- `/api/v1/crm/audit` (OWNER/ADMIN)
- `/api/v1/crm/integrations/sync-preview`
- `/api/v1/crm/imports/preview` (normalizes and checks duplicates; no writes)
- `/api/v1/crm/imports/commit` (requires explicit `confirm_import: true`)

## Not yet live

The AI behavior currently uses deterministic, inspectable rules; an external AI
model is not connected. Google Contacts/Sheets OAuth and live sync are not
implemented. Sync preview is read-only and never persists incoming provider data.
Do not commit OAuth secrets or tokens. Before enabling live sync, implement OAuth
state validation, minimal scopes, encrypted token storage, per-user connection
ownership, duplicate/conflict/deletion policy, import preview, human approval,
audit logs, and integration tests. Hosted SQLite durability must be verified in
the deployment environment before relying on stored CRM records.


## Contact quality and daily work

- Extended profiles include WhatsApp number, address, city, pincode, designation, and verification status.
- `backend/crm/quality.py` flags missing fields, placeholder names, malformed Indian mobile formats, and malformed email formats with explainable reasons and a completeness score.
- A valid-looking phone/email format is **not** proof that the number is active or belongs to the named person. Real-world verification remains UNVERIFIED unless approved evidence is recorded.
- Contact quality endpoints:
  - `/api/v1/crm/quality/review-queue?limit=200`
  - `/api/v1/crm/contacts/{contact_id}/quality`
- Daily workflow endpoints:
  - `/api/v1/crm/daily/briefing`
  - `/api/v1/crm/daily/items` (GET/POST)
  - `/api/v1/crm/daily/items/{item_id}` (PATCH status)
- Daily work items support tasks, calls, meetings, follow-ups, notes, and personal items, with user scoping and audit events. Morning/workday/evening briefing prompts are suggestions, not automatic surveillance or calendar synchronization.
- Existing databases receive additive schema migrations for the new fields and daily items table.

## Remaining production work

- Run CI and review migrations against the actual deployment database before rollout.
- Build the front-end dashboard for color-coded flags, quality filters, and daily briefing; these changes add backend/API capability, not a finished UI.
- Connect a real AI provider only after choosing the provider and securely configuring deployment secrets. The current quality rules are deterministic and auditable.
- Implement provider-backed verification (if desired) with lawful consent, source/evidence, timestamps, and explicit distinction between syntax checks and verified ownership.
- Google Sheets/Contacts live OAuth and synchronization are still not connected.
