# Complete India + Global Bada Business Taxonomy Index

**Repository:** `RAJESH-KHANDELWAL/SUPREMESETUHUB`  
**Branch:** `feat/global-complete-work-business-taxonomy`  
**Status:** taxonomy and API package architecture; not a live verified business directory.

This index separates the ecosystem into independent layers. The layers are intentionally not collapsed into one giant category list because an industry, a legal entity, an occupation, a product, a service and a job vacancy are different data concepts.

## 1. Core work and business domains — 10 canonical packages

- `global_freelancer_gig_independent_work_business_api_ecosystem/jobs_careers_employment_api_ecosystem/`
- `global_freelancer_gig_independent_work_business_api_ecosystem/`
- `global_education_learning_training_api_ecosystem/students_education_skills_business_api_ecosystem/`
- `business_companies_trade_business_api_ecosystem/`
- `global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem/`
- `home_homemaker_care_economy_business_api_ecosystem/`
- `industries_professional_services_business_api_ecosystem/`
- `family_relationships_community_business_api_ecosystem/`
- `adult_18_plus_lawful_industry_business_api_ecosystem/`
- `services_platforms_integrations_business_api_ecosystem/`


Each core domain follows its documented package convention. Finance, Banking & Insurance is implemented directly in `global_finance_banking_insurance_api_ecosystem/`, alongside its separate Global Payment child ecosystem. Government, Public Services & Social Impact remains under `industry_api_ecosystems/`.

- `global_universal_work_business_taxonomy_api_ecosystem/` — canonical A–Z India + Global work/business sector classification.

## 2. Industry vertical API ecosystems — 37 packages

- `agriculture_food_natural_resources/`
- `international_trade_import_export_customs_global_commerce/` — International Trade, Import-Export, Customs & Global Commerce.
- `arts_culture_heritage_creative_economy/` — Arts, Culture, Heritage & Creative Economy.
- `automotive_mobility/` — parent entry point for Automotive, Mobility, Transport, Logistics & Supply Chain.
  - `global_transport_mobility_logistics_supply_chain_business_api_ecosystem/` — nested transport and mobility ecosystem; canonical owner of the `transport_mobility_logistics` industry identity.
    - `global_aviation_aerospace_space_technology_api_ecosystem/` — nested Aviation, Aerospace & Space Technology entry point.
- `beauty_fashion_lifestyle/`
- `global_business_companies_corporates_api_ecosystem/`
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/digital_infrastructure_telecommunications/`
- `global_education_learning_training_api_ecosystem/education_learning_training/`
- `global_energy_utilities_environment_api_ecosystem/`
- `global_fashion_textiles_apparel_api_ecosystem/` — sole canonical Fashion, Textiles & Apparel implementation; the redundant root-level compatibility facade has been removed.
- `global_finance_banking_insurance_api_ecosystem/`
- `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` — canonical Hotels, Resorts, Restaurants & Hospitality ecosystem; food processing and food-safety compliance remain in Agriculture & Food.
- `government_public_services_social_impact/`
- `healthcare_life_sciences/`
- `healthcare_wellness_fitness/` — canonical gym, fitness, spa and massage taxonomy.
- `home_services_property_maintenance_facility_management/` — home services, property maintenance and facility operations.
- `global_jobs_careers_employment_api_ecosystem/` — 15 industry/service categories and 60 subcategories for recruitment, staffing, HR/payroll, career support and related services.
- `legal_consulting_professional_services/`
- `manufacturing_industrial_services/`
- `marketing_media_entertainment/`
- `mining_metals_minerals/`
- `personal_lifestyle_wellness/`
- `global_professional_business_services_api_ecosystem/`
- `retail_ecommerce_consumer_goods/`
- `science_research_innovation/` — Science, Research, Innovation & Technology, including AI/ML and Generative AI research.
- `security_defence_safety_services/`
- `sports_recreation_community/`
- `global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem/` — canonical Startups & Entrepreneurship ecosystem.
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_it_telecommunications/`
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_software_ai_cloud/`
- `transport_logistics_supply_chain/`
- `global_travel_tourism_hospitality_api_ecosystem/`
- `global_water_resources_marine_industries_api_ecosystem/`

International Trade, Import-Export, Customs & Global Commerce is a cross-sector trade lifecycle ecosystem; agriculture-specific commodity trade remains with Agriculture, Food & Natural Resources, and freight execution remains with Transport, Logistics & Supply Chain. The Arts, Culture, Heritage & Creative Economy ecosystem is distinct from commercial media/entertainment, travel inventory and general education. These remain 37 separately registered industry IDs. The former root-level Real Estate implementation is now maintained directly in `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem/`, with the infrastructure identity preserved as a nested package, and the former Transport pair through `global_transport_mobility_logistics_supply_chain_business_api_ecosystem/`; their underlying industry packages and IDs remain distinct. `manufacturing_industrial_services/` is maintained directly at the Bada Business root (outside `industry_api_ecosystems/`) as an explicit layout exception. Marketing, digital marketing, offline advertising, media and entertainment are consolidated under `marketing_media_entertainment/`; mining and metals are maintained under `mining_metals_minerals/`; personal lifestyle, family, parenting, couples, relationship support and restricted 18+ adult wellness/content categories are consolidated under `personal_lifestyle_wellness/` with adult categories excluded from default discovery. Manufacturing, Industrial & Industries are maintained at the Bada Business root under `manufacturing_industrial_services/`; factory services are one supporting component within this broad industrial ecosystem. Distribution-channel discovery is maintained separately in `distribution_channels_api_ecosystem/`, outside the industry vertical registry. Other adjacent verticals remain separate where their operational scope differs.

## 3. Provider/platform integrations — 21 packages

- `adult_business_api_ecosystem/`
- `apple_business_api_ecosystem/`
- `atlassian_business_api_ecosystem/`
- `aws_business_api_ecosystem/`
- `ccbill_business_api_ecosystem/`
- `crakrevenue_business_api_ecosystem/`
- `epoch_business_api_ecosystem/`
- `exoclick_business_api_ecosystem/`
- `google_business_api_ecosystem/`
- `ibm_business_api_ecosystem/`
- `microsoft_business_api_ecosystem/`
- `oracle_business_api_ecosystem/`
- `paxum_business_api_ecosystem/`
- `paypal_business_api_ecosystem/`
- `salesforce_business_api_ecosystem/`
- `segpay_business_api_ecosystem/`
- `shopify_business_api_ecosystem/`
- `slack_business_api_ecosystem/`
- `stripe_business_api_ecosystem/`
- `trafficjunky_business_api_ecosystem/`
- `verotel_business_api_ecosystem/`

A provider package is not proof of a live connection, current API credentials, commercial partnership or working payment flow.

## 4. Standards and classification registry — 8 entries

Package: `classification_standards_business_api_ecosystem/`

- India NIC 2025 — economic activities.
- UN ISIC Revision 5 — international economic activities.
- NAICS 2022 — North American economic activities (US, Canada, Mexico).
- EU NACE Rev. 2.1 — European economic activities.
- India NCO 2015 — occupations.
- ILO ISCO-08 — international occupations.
- EU ESCO 1.2.1 — occupations, skills and competences.
- UN CPC 3.0 draft structure — products and services.

The registry records publishers, jurisdictions, versions, source URLs and ingestion status. Most datasets are registered as sources only and still need import, normalization, code-level validation and versioned crosswalks. Do not treat registry metadata as a complete code database.

## 5. Required future classification layers

These must remain distinct and be added as versioned datasets with source provenance:

1. **Economic activities / industries:** NIC, ISIC, NAICS, NACE and national equivalents.
2. **Occupations / work:** NCO, ISCO, ESCO, national occupational classifications and emerging role catalogues.
3. **Products / goods / services:** CPC, national product classifications, HS/ITC-HS, GST HSN and SAC, with legal/tax applicability notes.
4. **Skills / qualifications:** ESCO, national skills frameworks, qualification packs, credentials and competency standards.
5. **Business/legal entities:** company, LLP, partnership, cooperative, sole proprietorship, nonprofit and jurisdiction-specific legal forms; legal sources and effective dates required.
6. **Business models / channels:** B2B, B2C, C2C, D2C, marketplace, subscription, franchise, licensing, online, offline and hybrid.
7. **Jobs / vacancies / engagements:** vacancy records, contract type, location, remote status, compensation, employer verification and freshness.
8. **Business services / providers:** service taxonomy, provider identity, service areas, delivery modes, credentials, pricing and availability.
9. **Government / public procurement / grants:** official agency and programme registries, procurement classifications, eligibility and jurisdiction.
10. **Geography / markets:** ISO country and subdivision codes, languages, currencies, time zones, trade blocs and market coverage.

## 6. Data and safety boundaries

- Taxonomy is not a verified business listing, employer, job vacancy, financial product, licence or legal opinion.
- Adult-industry taxonomy is separately restricted and excluded from default discovery; an inclusion flag is not age verification or legal authorization.
- Crosswalks may be many-to-many, partial or version-specific. Never assume code equivalence from similar labels.
- Country coverage must be evidenced by a named source and edition; “global” is a coverage goal, not proof of exhaustive worldwide completeness.
- Do not publish scraped personal data, credentials, private account information or unverified provider claims.
- Every ingested dataset needs provenance, checksum, schema validation, duplicate checks, source-version tracking and an update process.

## 7. Current implementation status

- 10 canonical core domain packages exist; Finance and Government/Public Services are maintained in the industry API ecosystem layer.
- 37 industry vertical packages are registered across the Bada Business industry ecosystem layer.
- 21 provider/platform packages exist.
- 8 classification standards are registered in the new classification package.
- NIC 2025 workbook importer extracts raw rows but requires reviewed column mapping before records can be published.
- Classification registry API routes are mounted under the existing Bada Business router.
- Full source datasets, complete code-level crosswalks, country-by-country official datasets, live provider integrations, verified businesses and live job listings are not yet complete.


## Consolidated Global domain folders

- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/` — Digital Infrastructure, Telecommunications, Technology, IT, AI, software, cloud and related technology-provider packages.
- `network_marketing_direct_selling_business_api_ecosystem/` — Bharat and international network-marketing and direct-selling companies, distributors, products and business models.
- `global_freelancer_gig_independent_work_business_api_ecosystem/` — freelancing, gig and independent work; its `jobs_careers_employment_api_ecosystem/` child owns the separate 24-category Work, Jobs & Careers employment classification. The 15-category Jobs, Careers & Employment industry/service taxonomy is maintained in `global_jobs_careers_employment_api_ecosystem/`.
- `global_finance_banking_insurance_api_ecosystem/global_payment_business_api_ecosystem/` — payment platforms and provider packages, including PayPal, Stripe, Epoch, Paxum, Segpay, Verotel and CCBill.

These consolidated folders are business-facing ownership boundaries. Existing canonical detailed industry implementations and stable API contracts are retained where needed; do not duplicate their catalogues.
