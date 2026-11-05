# Root-level Industry Ecosystem Entry Points

This directory exposes industry packages directly under
`global_bada_business_api_ecosystem/` while preserving maintained
implementations under `industry_api_ecosystems/`.

Compatibility facades preserve established imports and avoid duplicate
catalogs and services. The hospitality domain is exposed through the
canonical `global_hospitality_hotels_resorts_restaurants_api_ecosystem/`
entry point while its maintained implementation remains under
`industry_api_ecosystems/food_hospitality_restaurants/`.

## Industry packages (39 registered industry IDs)

- `adult_sexual_wellness/`
- `agriculture_food_natural_resources/` — food processing and food safety/testing/compliance are maintained here.
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
- `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` — canonical entry point; legacy `food_hospitality_restaurants/` remains for compatibility.
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

- Modify industry implementation files in `industry_api_ecosystems/<package>/` unless a canonical consolidated package explicitly owns the implementation.
- Keep legacy facades for import compatibility; do not duplicate catalogs or services.
- Food production, processing, agricultural food supply chains, food testing and food-safety compliance belong to Agriculture & Food.
- Hotels, resorts, restaurants, dhabas, cafes, catering, prepared-food delivery, accommodation, event venues and restaurant operations belong to Hospitality.
- Restaurant suppliers, commercial kitchens, food equipment and restaurant technology remain in Hospitality when they directly support hospitality operators.
- New industry packages must be registered and covered by route, schema and integrity tests.
- These packages are taxonomy/API modules, not proof of verified businesses, live providers or exhaustive country coverage.

## Standalone industry-domain exception

The Kamasutra / Adult Sexual Health & Wellness API Ecosystem is maintained as a standalone sibling package directly under `global_bada_business_api_ecosystem/`, not inside `industry_api_ecosystems/`:

`kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem/`

Its API router is mounted independently by the parent `global_bada_business_api_ecosystem/routes.py`. The old nested package is a temporary compatibility location only; do not add new implementation files there.
