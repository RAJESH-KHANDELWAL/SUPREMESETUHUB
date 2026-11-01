# GLOBAL COMPANY / COMPANIES API ECOSYSTEM

## Scope and canonical records
This ecosystem classifies and discovers organizations operating in Bharat and other jurisdictions.

- **Company:** legally constituted entity or formally registered organization.
- **Enterprise:** operating economic organization, including sole proprietorships, MSMEs, startups and franchises.
- **Corporate Group:** parent, holding, subsidiary and affiliated corporate structures.
- **Freelancer:** independent person/professional; retained only for legacy compatibility and not a canonical company class.

A brand, product, platform, company and individual are separate entity types. Do not create duplicate company profiles to represent platforms or brands.

## Package architecture
- Root API, schemas and read-only canonical registry: `routes.py`, `schemas.py`, `service.py`.
- Dedicated class packages: `company_legal_entities_api_ecosystem/`, `business_enterprises_api_ecosystem/`, `corporate_groups_api_ecosystem/`.
- Independent classification dimensions: `industry_api_ecosystems/`, `country_api_ecosystems/`, `company_classification_standards_api_ecosystem/`.
- Provider discovery packages: Apple, AWS, Google and Microsoft; these are catalog metadata unless separately verified and integrated.
- Company-domain relationship extension point: `company_relationships_api_ecosystem/`.
- Shared ownership/operator/parent-subsidiary relationship records are maintained centrally by `global_entity_relationships_api_ecosystem/`, not duplicated here.
- Supporting areas: `data/`, `integrations/`, `services/`, `tools/`, `tests/`.

## Evidence and verification
The local profile registry is read-only and currently empty. Country source entries are source-directory metadata, not live government connections. Provider product APIs and official websites are not automatically company-registration authorities. Verified records require traceable evidence and source URLs. No complete worldwide company coverage is claimed.

## Adult-industry classification
Adult-industry companies may be classified as a lawful industry segment with jurisdiction, minimum-age, licensing/compliance and safety attributes. Classification does not override local law or verify any company.

## Reference boundary
The Global Bada Business API ecosystem is a structural package-layout reference only. Its business-specific catalogues, categories and data are not imported into this Company ecosystem.
