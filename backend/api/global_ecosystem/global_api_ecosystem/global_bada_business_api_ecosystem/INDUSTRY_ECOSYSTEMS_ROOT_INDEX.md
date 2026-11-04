# Root-level Industry Ecosystem Entry Points

This directory exposes industry packages directly under
`global_bada_business_api_ecosystem/`. Most industry implementations are
maintained under `industry_api_ecosystems/`; Beauty, Fashion & Lifestyle,
Energy, Utilities & Environment, and Mining, Metals & Minerals are maintained
directly at this root as explicit layout exceptions.

Legacy paths for `media_entertainment_creative_industries`,
`family_relationships_parenting` and `adult_sexual_wellness` are retained as
aliases to their consolidated canonical ecosystems. Do not create duplicate
source trees for compatibility entry points.

## Industry packages (34)

- `agriculture_food_natural_resources/`
- `automotive_mobility/`
- `aviation_aerospace_space_technology/`
- `beauty_fashion_lifestyle/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `business_companies_corporates/`
- `digital_infrastructure_telecommunications/`
- `education_learning_training/`
- `energy_utilities_environment/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `fashion_textiles_apparel/`
- `finance_banking_insurance/`
- `food_hospitality_restaurants/`
- `government_public_services_social_impact/`
- `healthcare_life_sciences/`
- `healthcare_wellness_fitness/`
- `jobs_careers_employment/`
- `legal_consulting_professional_services/`
- `manufacturing_industrial_services/`
- `marketing_media_entertainment/`
- `mining_metals_minerals/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `personal_lifestyle_wellness/`
- `professional_legal_business_services/`
- `real_estate_construction/`
- `real_estate_construction_infrastructure/`
- `retail_ecommerce_consumer_goods/`
- `science_research_innovation/`
- `security_defence_safety_services/`
- `sports_recreation_community/`
- `startups_entrepreneurship/`
- `technology_it_telecommunications/`
- `technology_software_ai_cloud/`
- `transport_logistics_supply_chain/`
- `transport_mobility_logistics/`
- `travel_tourism_hospitality/`
- `water_resources_marine_industries/`

## Maintenance rules

- Unless explicitly documented as a root-level exception, modify industry implementation files in `industry_api_ecosystems/<package>/`.
- Beauty, Fashion & Lifestyle; Energy, Utilities & Environment; and Mining, Metals & Minerals implementation files live directly at the Bada Business root.
- Importers may use the documented root package names; avoid duplicate catalogs and services.
- New industry packages must be registered in the industry ecosystem registry and covered by route, schema and integrity tests.
- These packages are taxonomy/API modules, not proof of verified businesses, live providers or exhaustive country coverage.

## Standalone adult intimacy ecosystem

- `kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem/` — separate adult-only (18+), consent-first Kamasutra, intimacy, relationship, lawful wellness and professional-services ecosystem. Its current main-branch scope and implementation status are documented in that folder's `README.md`.
