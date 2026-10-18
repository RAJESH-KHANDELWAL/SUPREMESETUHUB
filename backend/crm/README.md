# CRM

This backend module contains the shared, people-facing CRM domain only. It is not
the SUPREME ECOSYSTEM orchestration layer and is not the owner's private CRM.

- `models.py`: canonical contact record and contact-consent validation.
- `contact_service.py`: provider-neutral contact normalization for imported data.
- `backend/supreme/supreme_ecosystem/crm.py`: ecosystem readiness and provider orchestration.

Google Contacts and Google Sheets are **not connected** yet. The normalization
helpers do not authenticate, read or write Google data, persist records, or sync.
Live integration must use explicit OAuth consent, least-privilege scopes, secure
token storage, duplicate detection, conflict/deletion policies, audit logs, and
a read-only preview before any write operation.

A spreadsheet row is not proof of consent to contact. `DO_NOT_CONTACT` must
always take precedence. Never commit credentials or access/refresh tokens.
The owner's private CRM must keep its own storage and authorization boundary.
