# Global Business Governance, Compliance & Standards API Ecosystem

This is the consolidated ownership folder for four distinct API domains:

- `governance/` — governance policy, approved scope decisions, validation and governance routes.
- `government_public_services_social_impact/` — compatibility facade to the canonical implementation in `../industry_api_ecosystems/government_public_services_social_impact/`.
- `global_business_compliance_api_ecosystem/` — cross-industry business compliance discovery and jurisdictional compliance metadata.
- `global_classification_standards_business_api_ecosystem/` — economic activity classifications, standards metadata and crosswalks.

## Architecture rules

- Keep each domain's responsibility separate; this folder groups ownership, it does not merge their data models.
- Government/Public Services implementation remains canonical in `industry_api_ecosystems/`; the nested package is a compatibility facade.
- Old root import paths for `governance` and `government_public_services_social_impact` are retained as thin compatibility shims.
- Compliance discovery is informational and must not be represented as legal advice or a final applicability decision.
- Classification metadata is not a claim that every official code list has been ingested.
- Preserve jurisdiction, source, effective date, version and provenance for all external standards and compliance data.
- No live integrations, legal certification or complete global coverage are implied by folder placement.
