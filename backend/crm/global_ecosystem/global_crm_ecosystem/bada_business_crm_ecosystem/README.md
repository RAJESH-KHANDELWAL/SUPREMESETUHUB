# BADA BUSINESS CRM ECOSYSTEM

Bada Business-specific CRM workflow facade over the shared `backend.crm`
domain. It does not create a second contact table or duplicate provider catalog.

## Features

- Business lead listing and creation.
- Lead-category suggestion with human approval.
- Follow-up preparation, respecting contact status and consent.
- Outreach draft generation through the canonical consent-aware CRM service.

## Boundaries

- CRM records and database operations remain in `backend.crm`.
- Bada Business programs, prices, registration URLs and course facts remain in
  `backend.global_ecosystem.global_bada_business_ecosystem`.
- No automatic WhatsApp/email outreach, provider API connection or payments
  are enabled.
- The authenticated application must supply owner and actor IDs.
