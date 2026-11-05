# Business Registration & Compliance API Ecosystem

Independent, cross-industry compliance-discovery API for business onboarding and operational screening.

**Package:** `business_compliance_api_ecosystem`  
**Scope:** India starter reference + global jurisdiction framework.  
**API prefix:** `/compliance`

## Purpose

Provide structured discovery topics for entity formation, tax, MSME, local trade permissions, premises safety, food licensing, product standards, regulated goods, import/export, labour, environment, data privacy, consumer and e-commerce obligations. The API is designed to help a business identify questions that need official verification; it does not decide legal applicability.

## Endpoints

- `GET /compliance/status`
- `GET /compliance/jurisdictions` (unified country master)
- `GET /compliance/jurisdictions/{country_code}`
- `GET /compliance/jurisdictions/{country_code}/subdivisions` (India index available; other country datasets return HTTP 501)
- `GET /compliance/jurisdictions/india/subdivisions`
- `GET /compliance/jurisdictions/india/subdivisions?subdivision_type=state`
- `GET /compliance/jurisdictions/india/subdivisions/{subdivision_code}`
- `GET /compliance/jurisdictions/india/subdivisions/{subdivision_code}/requirements` (returns HTTP 501 until verified state rules are curated)
- `GET /compliance/rules?country_code=IN`
- `GET /compliance/rules?country_code=IN&area=tax`
- `GET /compliance/rules?country_code=IN&subdivision_code=RJ` (central India records plus Rajasthan-specific records)
- `GET /compliance/rules/{rule_id}?country_code=IN&subdivision_code=RJ`
- `GET /compliance/rules/{rule_id}?country_code=IN`
- `GET /compliance/requirements?country_code=IN`
- `GET /compliance/requirements?country_code=IN&q=GST`
- `GET /compliance/requirements?country_code=IN&area=tax`
- `GET /compliance/requirements/{requirement_id}?country_code=IN`

These paths are relative to the parent Global Bada Business API router. The parent router currently uses `/api/v1/global-ecosystem/business`.

## Coverage status

- **India (IN):** 12 national-level discovery records across 12 areas, linked to official starting portals where identified.
- **Rajasthan (IN-RJ):** 6 state/local discovery records covering Shops and Establishments, contract labour, municipal trade permissions, fire NOC, factory approvals and pollution/waste authorisations. These are conditional discovery records, not a claim that every business needs every approval.
- **Unified country master:** India plus 13 additional priority country profiles (AE, AU, BD, CA, DE, FR, GB, JP, NZ, PK, SA, SG, US) are in one registry. This starter index is not claimed to be the exhaustive ISO country list.
- **India (IN):** the only country with a starter compliance topic dataset at this stage.
- **Other indexed countries:** jurisdiction profiles only; country-specific requirements and subnational data are not yet curated. Requests return HTTP 501 rather than fabricated compliance data.
- **India subnational index:** all 28 States and 8 Union Territories are listed in the same jurisdiction hierarchy. This is an index only; it does not mean state-specific legal rules have been researched or verified.
- District and municipal requirements are not yet separately enumerated.
- The state-specific requirements endpoint returns discovery records for subdivisions with records (currently Rajasthan, RJ); other States and UTs return HTTP 501 until researched.

## Important applicability rules

GST, Udyam, FSSAI, BIS, IEC, fire approvals, labour registrations, pollution consents and other examples are not universal requirements. Applicability can depend on entity type, activity, product, turnover, employee count, premises, location, supply model and current law. The API intentionally uses conditional language and includes verification guidance.

Each rule record includes applicability status, trigger factors, jurisdiction level, official source links where identified, source verification status, source-link-added date, last-source-verified placeholder, effective-date placeholder and legal-review status. A portal link is not proof that a particular rule is current or applies. The `last_source_checked_on` and `last_source_verified_on` fields remain empty until the operative rule text and applicability are checked. Rajasthan entries link official government portals and statutory/procedure sources, but full rule-text and legal review remain pending. Records marked `official_portal_linked_rule_text_not_fully_reviewed` have an official starting portal but have not undergone full rule-text/legal review; records marked `official_jurisdiction_source_required` still need a precise authority/source. Effective dates and filing frequencies remain unset until individually researched. Before acting, verify current rules, thresholds, exemptions, commencement dates and forms directly with the responsible official authority or a qualified professional. Do not use this catalogue as legal, tax or regulatory advice.

## Architecture boundaries

- Distribution Channels API describes channel participants and commercial hand-offs.
- This package describes compliance discovery topics across business activities and jurisdictions.
- Industry packages describe sector taxonomies. Product-specific approvals should be linked to the relevant sector and regulator rather than duplicated as universal rules.
- No provider verification, application submission, licence issuance, legal opinion or live government integration is provided.

## Extension policy

Add a country dataset only after identifying official primary sources, jurisdiction level, effective date, applicability conditions, exemptions, last-verified date and a review owner. Keep source URLs and version metadata with each future rule. Never label a rule current without checking its official source.
