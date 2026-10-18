# CRM — People CRM Ecosystem

This module is for **people records only**. The owner's private CRM must remain a
separate module with its own records and access rules. Do not merge private notes,
private leads, personal tasks, or owner-only business records into this ecosystem.

## Current foundation

- Provider-neutral PeopleContact model.
- Validation for required IDs/names and contact status.
- A DO_NOT_CONTACT record cannot be marked as consented to contact.
- Mapping helpers for Google Contacts-style records and explicitly mapped Google
  Sheets rows.
- Honest connector status: both providers are currently NOT_CONNECTED and live
  API synchronization is not implemented by this scaffold.

## Planned data flow

    Google Contacts ─┐
                     ├─> Provider adapters ─> People CRM normalized contact model
    Google Sheets ───┘                               │
                                                     └─> CRM-owned storage/API (separate task)

## Google Contacts and Sheets

The mapping layer prepares external records for normalization; it does not authenticate
with Google, read or write any account, or sync data. Before live integration, implement
OAuth 2.0 authorization and state validation, minimal scopes, secure token storage,
explicit account/user consent, duplicate detection, field-level mapping, sync direction,
conflict handling, deletion policy, audit logs, and tests. Never commit OAuth secrets or
access/refresh tokens. Start with read-only import and a preview/dry-run; enable writes
only as a separately reviewed feature.

For Sheets, configure the spreadsheet and column mapping explicitly. Do not assume every
spreadsheet has the same headings or treat an arbitrary row as consent to contact.
Google Contacts/Sheets data should not automatically trigger messages. Contact consent
must remain an explicit CRM field and DO_NOT_CONTACT must take precedence.

## Layer boundaries

- models.py: normalized data contract.
- service.py: provider-neutral validation, mapping, readiness status.
- Future connector adapters: Google auth and API calls only.
- Future storage/API modules: persistence and authorization; they must not reuse the
  owner's private CRM storage without a deliberate, reviewed boundary.

Existing backend/api/people.py and the existing referral engine are not silently
replaced by this scaffold. Route registration, persistent People CRM storage, Google
OAuth, and live sync are not part of this initial foundation.
