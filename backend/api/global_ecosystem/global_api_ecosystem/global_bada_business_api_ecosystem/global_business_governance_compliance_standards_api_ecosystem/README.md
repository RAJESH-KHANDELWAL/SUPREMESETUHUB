# Global Business Governance, Compliance & Standards API Ecosystem

## Purpose

This directory is the umbrella index for four related but independently maintained API domains:

1. Governance
2. Government, Public Services & Social Impact
3. Global Business Compliance
4. Global Classification & Business Standards

The domains share governance and interoperability concerns, but they have different responsibilities and must not duplicate one another's implementation.

## Canonical ownership

| Domain | Responsibility | Implementation rule |
|---|---|---|
| Governance | Policies, approvals, decision records, lifecycle controls, auditability and cross-cutting API governance | Keep governance rules and control-plane logic here; do not place citizen-service catalogues here. |
| Government, Public Services & Social Impact | Public administration, citizen services, welfare, public programmes, nonprofit and social-impact services | The maintained implementation currently lives at `../global_bada_business_api_ecosystem/industry_api_ecosystems/government_public_services_social_impact/`. The root-level `government_public_services_social_impact/` is a compatibility entry point. |
| Global Business Compliance | Business obligations and compliance discovery across jurisdictions and industries | Keep compliance discovery separate from governance policy controls and industry classification. Do not represent discovery metadata as legal advice or a definitive legal determination. |
| Global Classification & Business Standards | Official economic-activity classifications, national/international code systems, metadata and crosswalks | Keep official classification systems distinct from internal product, service or industry discovery taxonomies. Registry metadata must not be described as a complete official code dataset unless the full dataset has been ingested and verified. |

## Architecture rules

- Maintain one canonical implementation for each domain.
- Compatibility facades may preserve old imports, routes or category identifiers; they must not become parallel implementations.
- Do not copy government/public-service implementation into this umbrella. Link to and preserve its canonical industry implementation.
- Keep compliance discovery, governance controls and classification standards as separate bounded contexts.
- Record jurisdiction, source authority, version, effective date and verification status for regulatory or classification data where applicable.
- Do not claim global completeness or live official integrations without verified source coverage.

## Current setup status

- Governance: existing implementation is under the sibling `governance/` directory.
- Government/Public Services/Social Impact: canonical implementation is under `industry_api_ecosystems/government_public_services_social_impact/`; the root-level folder is a compatibility facade.
- Business Compliance: place or link the single canonical implementation here when its exact current location is confirmed.
- Classification Standards: place or link the single canonical implementation here when its exact current location is confirmed.

This README is an architectural index. It does not move files, change import paths, or create duplicate implementations.
