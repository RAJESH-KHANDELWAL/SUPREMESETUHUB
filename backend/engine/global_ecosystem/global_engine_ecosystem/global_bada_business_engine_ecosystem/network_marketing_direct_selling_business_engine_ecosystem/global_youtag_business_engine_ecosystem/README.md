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
