# Root-level Industry Ecosystem Entry Points

This directory exposes industry packages directly under
`global_bada_business_api_ecosystem/`. Most industry implementations are
maintained under `industry_api_ecosystems/`; Agriculture, Food & Natural
Resources is consolidated under
`global_agriculture_food_natural_resources_api_ecosystem/`.
Beauty, Fashion & Lifestyle and Mining, Metals & Minerals are maintained directly at this root as explicit layout exceptions. Energy, Utilities & Environment is consolidated under its global API ecosystem package. Finance, Banking & Insurance exposes a global API ecosystem entry point while its maintained implementation remains under industry_api_ecosystems/.

Legacy paths for `media_entertainment_creative_industries` and
`family_relationships_parenting` are retained as aliases to their consolidated
canonical ecosystems. Adult sexual-wellness compatibility exports are now
included inside the consolidated global Kamasutra ecosystem. Do not create
duplicate source trees for compatibility entry points.

## Industry packages and consolidated entry points (35 root-level packages; 37 registered industry IDs)

- `global_agriculture_food_natural_resources_api_ecosystem/` — sole canonical Agriculture, Food & Natural Resources package; the former root-level `agriculture_food_natural_resources/` folder has been removed.
- `international_trade_import_export_customs_global_commerce/` — International Trade, Import-Export, Customs & Global Commerce.
- `arts_culture_heritage_creative_economy/` — Arts, Culture, Heritage & Creative Economy.
- `automotive_mobility/` — parent entry point containing the consolidated Transport, Mobility, Logistics & Supply Chain ecosystem and its nested Aviation/Aerospace entry point.
- `beauty_fashion_lifestyle/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `business_companies_corporates/`
- `digital_infrastructure_telecommunications/`
- `global_education_learning_training_api_ecosystem/` — consolidated Education, Learning & Training entry point; its nested `education_learning_training/` compatibility package points to the canonical industry implementation.
- `education_learning_training/` — retained root compatibility facade; do not delete while legacy imports depend on it.
- `global_energy_utilities_environment_api_ecosystem/` — consolidated Energy, Utilities & Environment package.
- `global_fashion_textiles_apparel_api_ecosystem/` — canonical Fashion, Textiles & Apparel implementation; former root and industry paths remain compatibility facades only.
- `global_finance_banking_insurance_api_ecosystem/` — consolidated public entry point; implementation remains under `industry_api_ecosystems/finance_banking_insurance/`.
- `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` — sole canonical root-level Hotels, Resorts, Restaurants & Hospitality entry point; legacy root-level Hospitality facades have been removed.
- `government_public_services_social_impact/`
- `healthcare_life_sciences/`
- `healthcare_wellness_fitness/` — canonical gym, fitness, spa and massage taxonomy.
- `home_services_property_maintenance_facility_management/` — Home Services, Property Maintenance & Facility Management.
- `jobs_careers_employment/`
- `global_legal_services_api_ecosystem/` — consolidated Legal Services taxonomy and API-ecosystem documentation entry point; runtime implementation remains explicitly separate until built and registered.
- `legal_consulting_professional_services/`
- `manufacturing_industrial_services/` — Manufacturing, Industrial & Industries API Ecosystem; maintained directly at this root (not inside `industry_api_ecosystems/`).
- `marketing_media_entertainment/`
- `mining_metals_minerals/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `personal_lifestyle_wellness/`
- `professional_legal_business_services/`
- `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem/` — consolidated Real Estate, Construction, Infrastructure & Property Business entry point.
- `retail_ecommerce_consumer_goods/`
- `science_research_innovation/`
- `security_defence_safety_services/`
- `sports_recreation_community/`
- `startups_entrepreneurship/`
- `technology_it_telecommunications/`
- `technology_software_ai_cloud/`
- `automotive_mobility/global_transport_mobility_logistics_supply_chain_business_api_ecosystem/` — consolidated Transport, Mobility, Logistics & Supply Chain entry point nested under Automotive & Mobility.
- `automotive_mobility/global_transport_mobility_logistics_supply_chain_business_api_ecosystem/global_aviation_aerospace_space_technology_api_ecosystem/` — Aviation, Aerospace & Space Technology entry point nested under Transport.
- `travel_tourism_hospitality/`
- `global_water_resources_marine_industries_industrial_business_api_ecosystem/` — sole canonical Global Water Resources & Marine Industries implementation and business-facing API entry point; the former `industry_api_ecosystems/water_resources_marine_industries/` package has been removed.

## Maintenance rules

- Unless explicitly documented as an exception, modify industry implementation files in `industry_api_ecosystems/<package>/`. Agriculture, Food & Natural Resources is maintained directly under `global_agriculture_food_natural_resources_api_ecosystem/`; food processing and food safety/testing/compliance belong there. Do not recreate the former root-level `agriculture_food_natural_resources/` folder.
- Beauty, Fashion & Lifestyle; Mining, Metals & Minerals; and Manufacturing, Industrial & Industries implementation files live directly at the Bada Business root. Energy, Utilities & Environment lives in `global_energy_utilities_environment_api_ecosystem/`; Finance, Banking & Insurance implementation remains in `industry_api_ecosystems/finance_banking_insurance/` with a consolidated global entry point. Water Resources & Marine Industries is now maintained directly in its consolidated global package. Real Estate and Transport also have consolidated global root entry points that expose their underlying industry packages without duplicating API implementations.
- Importers must use `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` as the sole root-level Hospitality entry point. The maintained implementation remains under `industry_api_ecosystems/food_hospitality_restaurants/`; the duplicate root-level legacy facades have been removed. Food safety/testing is maintained under Agriculture & Food.
- New industry packages must be registered in the industry ecosystem registry and covered by route, schema and integrity tests.
- These packages are taxonomy/API modules, not proof of verified businesses, live providers or exhaustive country coverage.

## Standalone adult intimacy ecosystem

- `global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem/` — consolidated adult-only (18+), consent-first Kamasutra, intimacy, relationship, lawful wellness, adult-industry provider catalog and professional-services ecosystem. The former adult 18+ lawful-industry, adult-business and adult-sexual-wellness root folders have been merged into this single package. Its current main-branch scope and implementation status are documented in that folder's `README.md`.
