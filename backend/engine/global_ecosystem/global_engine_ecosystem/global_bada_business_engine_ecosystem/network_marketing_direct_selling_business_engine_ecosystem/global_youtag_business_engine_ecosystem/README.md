# GLOBAL YOUTAG BUSINESS ENGINE ECOSYSTEM

Engine namespace for the single YOUTAG business ecosystem and its two app channels.

## Workflow boundaries

- Resolve both app channels to `GLOBAL-YOUTAG-BUSINESS-ECOSYSTEM`.
- Preserve app-specific context: `YOUTAG-WELLNESS-APP` or `YOUTAG-RECHARGES-APP`.
- Load the owner referral profile from the canonical global ecosystem path:
  `backend/global_ecosystem/global_bada_business_ecosystem/global_network_marketing_direct_selling_business_ecosystem/global_youtag_business_ecosystem/referral_profiles/rajesh_khandelwal.json`.
- Pass the exact owner-supplied referral URL to the appropriate presentation/redirect boundary without modifying its query string.
- Record a click only when an approved first-party event source exists; record a registration/conversion only from verified provider evidence.

The profile contains Referral ID `2043272` and the owner's name. It is not an authentication secret.

## Status

Workflow specification only. No live YOUTAG API, redirect handler, callback receiver, commission processor or transaction execution is implemented or verified here.

## Owner-provided YOUTAG referral link

- Owner: Rajesh Khandelwal
- Referral ID: `2043272`
- Registration link: [Install YOUTAG Business and register with referral ID 2043272](https://play.google.com/store/apps/details?id=com.youtagindia.business&referrer=utm_source%3Dgoogle%26utm_campaign%3D2043272)
- App package: `com.youtagindia.business`
- Owner-declared scope: YOUTAG WELLNESS and YOUTAG RECHARGES; separate app attribution is not independently verified.
- Canonical source of truth: `backend/global_ecosystem/global_bada_business_ecosystem/global_network_marketing_direct_selling_business_ecosystem/global_youtag_business_ecosystem/referral_profiles/rajesh_khandelwal.json`

Preserve the URL exactly. It is owner-provided public referral metadata, not an API credential or proof of registration, commission, provider partnership or live integration. Read the canonical profile rather than creating alternate referral records.
