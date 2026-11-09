# GLOBAL CRM ECOSYSTEM

This folder is the CRM ecosystem facade. The canonical implementation stays
in `backend/crm/` (models, contact service, quality, repository, integrations
and CRM workflows). No second contact schema or repository is introduced.

## Exposed behavior

- Owner-scoped contact operations and reporting.
- Duplicate candidates, quality review and audit-backed workflows through
  the canonical service.
- Consent-aware follow-up and message drafts through the canonical service.
- Google Sheets / Google Contacts import preview and explicitly confirmed
  import through the canonical service.
- Provider connections and external AI remain disabled until separately
  configured and verified.

The facade never bypasses owner scoping. Callers must provide the owner and
actor identities supplied by the authenticated application context.
