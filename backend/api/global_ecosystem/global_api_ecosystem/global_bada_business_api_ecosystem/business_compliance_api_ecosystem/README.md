# Business Registration & Compliance API Ecosystem

Independent, cross-industry compliance-discovery API for business onboarding and operational screening.

**Package:** `business_compliance_api_ecosystem`  
**Scope:** India starter reference + global jurisdiction framework.  
**API prefix:** `/compliance`

## Purpose

Provide structured discovery topics for entity formation, tax, MSME, local trade permissions, premises safety, food licensing, product standards, regulated goods, import/export, labour, environment, data privacy, consumer and e-commerce obligations. The API is designed to help a business identify questions that need official verification; it does not decide legal applicability.

## Endpoints

- `GET /compliance/status`
- `GET /compliance/jurisdictions`
- `GET /compliance/jurisdictions/india/subdivisions`
- `GET /compliance/jurisdictions/india/subdivisions?subdivision_type=state`
- `GET /compliance/jurisdictions/india/subdivisions/{subdivision_code}`
- `GET /compliance/jurisdictions/india/subdivisions/{subdivision_code}/requirements` (returns HTTP 501 until verified state rules are curated)
- `GET /compliance/requirements?country_code=IN`
- `GET /compliance/requirements?country_code=IN&q=GST`
- `GET /compliance/requirements?country_code=IN&area=tax`
- `GET /compliance/requirements/{requirement_id}?country_code=IN`

These paths are relative to the parent Global Bada Business API router. The parent router currently uses `/api/v1/global-ecosystem/business`.

## Coverage status

- **India (IN):** starter topic catalogue across 12 compliance areas. Entries are screening topics and illustrative examples, not exhaustive statutory inventories.
- **GLOBAL:** jurisdiction framework only. Country-specific requirements are not yet curated; requests for uncurated countries return HTTP 501 rather than fabricated compliance data.
- **India subnational index:** all 28 States and 8 Union Territories are listed as jurisdiction profiles. This is an index only; it does not mean state-specific legal rules have been researched or verified.
- District and municipal requirements are not yet separately enumerated.
- The state-specific requirements endpoint deliberately returns HTTP 501 until primary-source research, applicability conditions and verification dates are added.

## Important applicability rules

GST, Udyam, FSSAI, BIS, IEC, fire approvals, labour registrations, pollution consents and other examples are not universal requirements. Applicability can depend on entity type, activity, product, turnover, employee count, premises, location, supply model and current law. The API intentionally uses conditional language and includes verification guidance.

Before acting, verify current rules, thresholds, exemptions, commencement dates and forms directly with the responsible official authority or a qualified professional. Do not use this catalogue as legal, tax or regulatory advice.

## Architecture boundaries

- Distribution Channels API describes channel participants and commercial hand-offs.
- This package describes compliance discovery topics across business activities and jurisdictions.
- Industry packages describe sector taxonomies. Product-specific approvals should be linked to the relevant sector and regulator rather than duplicated as universal rules.
- No provider verification, application submission, licence issuance, legal opinion or live government integration is provided.

## Extension policy

Add a country dataset only after identifying official primary sources, jurisdiction level, effective date, applicability conditions, exemptions, last-verified date and a review owner. Keep source URLs and version metadata with each future rule. Never label a rule current without checking its official source.
