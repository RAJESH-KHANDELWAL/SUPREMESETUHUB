# Root-level Industry Ecosystem Entry Points

This directory exposes industry packages directly under
`global_bada_business_api_ecosystem/`. Most industry implementations are
maintained under `industry_api_ecosystems/`; Agriculture, Food & Natural
Resources is consolidated under
`global_agriculture_food_natural_resources_api_ecosystem/`.
Beauty, Fashion & Lifestyle and Mining, Metals & Minerals are maintained directly at this root as explicit layout exceptions. Fashion, Textiles & Apparel is maintained only in its canonical `global_fashion_textiles_apparel_api_ecosystem/` package; the redundant root compatibility directory has been removed. Energy, Utilities & Environment is consolidated under its global API ecosystem package. Finance, Banking & Insurance is maintained directly in `global_finance_banking_insurance_api_ecosystem/`; its payment-provider packages remain in the nested `global_payment_business_api_ecosystem/`.

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
- `global_business_companies_corporates_api_ecosystem/` — Global Businesses, Companies & Corporates taxonomy adapter backed by the canonical Global Company business-enterprise package.
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/` — canonical digital infrastructure, telecommunications, IT, technology and AI parent; its nested `digital_infrastructure_telecommunications/` folder owns the industry API implementation.
- `global_education_learning_training_api_ecosystem/` — canonical Education, Learning & Training entry point and implementation; student/learner skills remain in its separate child package.
- `global_energy_utilities_environment_api_ecosystem/` — consolidated Energy, Utilities & Environment package.
- `global_fashion_textiles_apparel_api_ecosystem/` — sole canonical Fashion, Textiles & Apparel implementation; the redundant root-level compatibility facade has been removed.
- `global_finance_banking_insurance_api_ecosystem/` — sole canonical Finance, Banking & Insurance implementation and public entry point; payment-provider packages remain nested under its Global Payment child ecosystem.
- `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` — sole canonical Hotels, Resorts, Restaurants & Hospitality implementation and public entry point; the former root-level `food_hospitality_restaurants/` package has been moved here.
- `government_public_services_social_impact/`
- `healthcare_life_sciences/`
- `healthcare_wellness_fitness/` — canonical gym, fitness, spa and massage taxonomy.
- `home_services_property_maintenance_facility_management/` — Home Services, Property Maintenance & Facility Management.
- `global_jobs_careers_employment_api_ecosystem/` — canonical 15-category Jobs, Careers & Employment industry/service taxonomy; distinct from the 24-category Work & Careers classification under the Global Freelancer ecosystem.
- `global_legal_services_api_ecosystem/` — consolidated Legal Services taxonomy and API-ecosystem documentation entry point; runtime implementation remains explicitly separate until built and registered.
- `legal_consulting_professional_services/`
- `manufacturing_industrial_services/` — Manufacturing, Industrial & Industries API Ecosystem; maintained directly at this root (not inside `industry_api_ecosystems/`).
- `marketing_media_entertainment/`
- `mining_metals_minerals/` — maintained directly at this root (not inside `industry_api_ecosystems/`).
- `personal_lifestyle_wellness/`
- `global_professional_business_services_api_ecosystem/` — canonical non-legal Professional Services implementation; kept separate from Legal Services.
- `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem/` — sole canonical Real Estate & Construction implementation and Property Business entry point; the separate infrastructure identity is nested within it.
- `retail_ecommerce_consumer_goods/`
- `science_research_innovation/`
- `security_defence_safety_services/`
- `sports_recreation_community/`
- `global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem/`
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_it_telecommunications/` — Technology, IT & Telecommunications industry API implementation.
- `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_software_ai_cloud/` — Technology, Software, AI & Cloud domain identity.
- `automotive_mobility/global_transport_mobility_logistics_supply_chain_business_api_ecosystem/` — consolidated Transport, Mobility, Logistics & Supply Chain entry point nested under Automotive & Mobility.
- `automotive_mobility/global_transport_mobility_logistics_supply_chain_business_api_ecosystem/global_aviation_aerospace_space_technology_api_ecosystem/` — Aviation, Aerospace & Space Technology entry point nested under Transport.
- `global_travel_tourism_hospitality_api_ecosystem/`
- `global_water_resources_marine_industries_api_ecosystem/`

- `global_universal_work_business_taxonomy_api_ecosystem/` — canonical A–Z India + Global work/business sector taxonomy.

## Maintenance rules

- Unless explicitly documented as an exception, modify industry implementation files in their documented canonical packages, including `global_education_learning_training_api_ecosystem/education_learning_training/` for Education. Travel, Tourism & Hospitality and Water Resources & Marine Industries are now maintained in their consolidated global API ecosystem folders. Startups & Entrepreneurship is owned by the consolidated Global Entrepreneurs ecosystem. Agriculture, Food & Natural Resources is maintained directly under `global_agriculture_food_natural_resources_api_ecosystem/`; food processing and food safety/testing/compliance belong there. Do not recreate the former root-level `agriculture_food_natural_resources/` folder. Jobs, Careers & Employment industry/service implementation is maintained in `global_jobs_careers_employment_api_ecosystem/`; its separate 24-category Work & Careers classification remains under the Global Freelancer ecosystem.
- Beauty, Fashion & Lifestyle; Mining, Metals & Minerals; and Manufacturing, Industrial & Industries implementation files live directly at the Bada Business root. Energy, Utilities & Environment lives in `global_energy_utilities_environment_api_ecosystem/`; Finance, Banking & Insurance implementation remains in `industry_api_ecosystems/finance_banking_insurance/` with a consolidated global entry point. Real Estate and Transport now also have consolidated global root entry points that expose their underlying industry packages without duplicating API implementations.
- Importers must use `global_hospitality_hotels_resorts_restaurants_api_ecosystem/` as the sole root-level Hospitality entry point. The maintained implementation remains under `industry_api_ecosystems/food_hospitality_restaurants/`; the duplicate root-level legacy facades have been removed. Food safety/testing is maintained under Agriculture & Food.
- New industry packages must be registered in the industry ecosystem registry and covered by route, schema and integrity tests.
- These packages are taxonomy/API modules, not proof of verified businesses, live providers or exhaustive country coverage.

## Standalone adult intimacy ecosystem

- The adult-only Kamasutra and adult-industry ecosystem is maintained in BOTH `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem/` and `backend/api/global_ecosystem/global_api_ecosystem/global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem/`. Both locations use the exact same folder name and remain active.
