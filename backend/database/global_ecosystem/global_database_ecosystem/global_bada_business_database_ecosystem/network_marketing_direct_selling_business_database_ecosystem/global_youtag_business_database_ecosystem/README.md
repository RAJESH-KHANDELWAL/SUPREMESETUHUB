# GLOBAL YOUTAG BUSINESS DATABASE ECOSYSTEM

Database namespace for the single YOUTAG business identity and its two app channels.

## Logical records

- `youtag_business`: one canonical YOUTAG business identity.
- `youtag_apps`: distinct app records for YOUTAG WELLNESS and YOUTAG RECHARGES, both referencing the same business ID.
- `youtag_referral_profiles`: owner-supplied referral metadata, including profile ID, owner display name, referral ID, exact URL, app scope, verification status and timestamps.
- `youtag_referral_events`: optional event records only when a provider-confirmed callback or verified event source exists.

## Seed/reference profile

Canonical public profile:
`backend/global_ecosystem/global_bada_business_ecosystem/global_network_marketing_direct_selling_business_ecosystem/global_youtag_business_ecosystem/referral_profiles/rajesh_khandelwal.json`

Referral ID: `2043272`; owner display name: `Rajesh Khandelwal`.

## Data integrity

Use one business foreign key for both app records. Never store the referral ID as a password/token. Do not create successful registration or commission events from a click alone. No production migration or live database table is created by this documentation.
