# Commercial Terms and Finance Controls

**Namespace:** `finance_commercial/`

Fee schedules, commission disclosures, invoicing, payout responsibilities, refund rules, tax review and reconciliation requirements. No payment processing or secrets.

## Required controls
- Stable record ID and accountable owner.
- Source evidence, provenance and verification status where relevant.
- Created, updated and review timestamps with lifecycle status.
- Permission, license, consent and retention notes where relevant.
- Public/private field separation and access requirements.
- Correction, suspension, archival and audit procedures.

## Architecture boundary
Business-domain records and requirements only. API, CORE, ENGINE, AI, DATABASE, STORAGE, authentication, payments and APP implementation remain in their respective layers. Never store secrets or sensitive personal data here.
