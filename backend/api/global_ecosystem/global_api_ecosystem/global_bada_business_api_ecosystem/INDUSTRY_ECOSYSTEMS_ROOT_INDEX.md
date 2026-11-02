# Root-level Industry Ecosystem Entry Points

This directory exposes the industry packages directly under
`global_bada_business_api_ecosystem/` while preserving the established
implementation under `industry_api_ecosystems/`.

Each root-level package is a compatibility facade: its Python package path
resolves to the maintained nested implementation. This avoids copying the
same source files into two locations and keeps existing imports and API
routing stable. The nested implementation is still canonical for now.

## Industry packages (39)

- `adult_sexual_wellness/`
- `agriculture_food_natural_resources/`
- `automotive_mobility/`
- `aviation_aerospace_space_technology/`
- `beauty_fashion_lifestyle/`
- `business_companies_corporates/`
- `digital_infrastructure_telecommunications/`
- `education_learning_training/`
- `energy_utilities_environment/`
- `family_relationships_parenting/`
- `fashion_textiles_apparel/`
- `finance_banking_insurance/`
- `food_hospitality_restaurants/`
- `government_public_services_social_impact/`
- `healthcare_life_sciences/`
- `healthcare_wellness_fitness/`
- `jobs_careers_employment/`
- `legal_consulting_professional_services/`
- `manufacturing_industrial_services/`
- `manufacturing_trade_retail/`
- `marketing_media_entertainment/`
- `media_entertainment_creative_industries/`
- `mining_metals_minerals/`
- `personal_lifestyle_wellness/`
- `professional_legal_business_services/`
- `real_estate_construction/`
- `real_estate_construction_infrastructure/`
- `retail_ecommerce_consumer_goods/`
- `science_research_innovation/`
- `security_defence_safety_services/`
- `sports_recreation_community/`
- `startups_entrepreneurship/`
- `supply_chain_warehousing_distribution/`
- `technology_it_telecommunications/`
- `technology_software_ai_cloud/`
- `transport_logistics_supply_chain/`
- `transport_mobility_logistics/`
- `travel_tourism_hospitality/`
- `water_resources_marine_industries/`

## Maintenance rules

- Add or modify industry implementation files in `industry_api_ecosystems/<package>/`.
- Importers may use either the root-level package name or the legacy nested path.
- Do not create duplicate catalogs or services in both locations.
- New industry packages must be registered in the industry ecosystem registry and covered by route, schema, and integrity tests.
- These packages are taxonomy/API modules, not proof of verified businesses, live providers, or exhaustive country coverage.
