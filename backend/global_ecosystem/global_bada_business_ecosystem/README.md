# GLOBAL BADA BUSINESS ECOSYSTEM

Canonical Bada Business ecosystem root:
`backend/global_ecosystem/global_bada_business_ecosystem/`

This directory is the single canonical home for Bada Business ecosystem identity, platform resources, course/event/product references, links, programs and referrals inside the Global Ecosystem.

## Structure

- `courses/` — course resource namespace
- `events/` — event and webinar resources
- `links/` — official and owner-provided referral destinations
- `platform/` — platform identity and profile
- `platform_resources/` — provider catalog and program snapshots
- `products/` — product resource namespace
- `referrals/` — referral metadata
- `registration/` — registration resources
- `course_resources/` — Bada Business Community course-link directory
- `global_network_marketing_direct_selling_business_ecosystem/` — direct-selling business families, including YOUTAG
- `provider_resources/` — provider-supplied resource references

## Canonical ownership and boundaries

All Bada Business ecosystem product/resource documentation and catalog files live here. The former `backend/bada_business_ecosystem/` package has been consolidated into this directory and is no longer a separate canonical root.

Architecture implementation remains separately owned:
- API: `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`
- CORE, ENGINE, DATABASE, AI, STORAGE, authentication and connection layers remain in their own architecture namespaces.
- Do not duplicate API transport logic, core business rules, engine orchestration, persistence schemas, credentials or live integrations here.

## Platform resources and claims

Provider URLs, program snapshots, course links, package details, pricing, commissions, event dates, instructor descriptions and promotional claims are reference data supplied by the repository owner or source documents. They do not establish current availability, official API access, partnership, entitlement, accreditation, income guarantees or live connectivity. Verify current commercial terms and access directly with the provider.

## Related business families

YOUTAG Wellness and YOUTAG Recharges remain separate apps under the YOUTAG business ecosystem. iDigitalPreneur and LeadsGuru remain separately scoped platforms under the affiliate-marketing ecosystem. Do not merge their referral identities or source data into Bada Business.

## YOUTAG referral reference

The canonical owner-provided YOUTAG referral profile remains at:
`global_network_marketing_direct_selling_business_ecosystem/global_youtag_business_ecosystem/referral_profiles/rajesh_khandelwal.json`.
