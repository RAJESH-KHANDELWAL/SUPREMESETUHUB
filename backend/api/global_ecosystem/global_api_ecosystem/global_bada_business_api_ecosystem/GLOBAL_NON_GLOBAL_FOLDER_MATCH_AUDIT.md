# Global vs Non-Global Folder Audit

Repository: `RAJESH-KHANDELWAL/SUPREMESETUHUB`
Branch inspected: `main`
Parent: `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`
Audit basis: GitHub recursive tree at commit `03681882d4a06b9dad811d480053f88bc5c8a9fb`.

## 1. Folders WITH the `global_` prefix (18)

- global_affiliate_marketing_business_api_ecosystem
- global_agriculture_food_natural_resources_api_ecosystem
- global_beauty_fashion_lifestyle_api_ecosystem
- global_business_governance_compliance_standards_api_ecosystem
- global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem
- global_distribution_channels_api_ecosystem
- global_education_learning_training_api_ecosystem
- global_energy_utilities_environment_api_ecosystem
- global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem
- global_fashion_textiles_apparel_api_ecosystem
- global_finance_banking_insurance_api_ecosystem
- global_freelancer_gig_independent_work_business_api_ecosystem
- global_hospitality_hotels_resorts_restaurants_api_ecosystem
- global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem
- global_legal_services_api_ecosystem
- global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem
- global_travel_tourism_hospitality_api_ecosystem
- global_water_resources_marine_industries_api_ecosystem

## 2. Folders WITHOUT the `global_` prefix (55)

- agriculture_food_natural_resources
- arts_culture_heritage_creative_economy
- automotive_mobility
- aviation_aerospace_space_technology
- business_capabilities
- business_companies_corporates
- digital_infrastructure_telecommunications
- exoclick_business_api_ecosystem
- family_relationships_parenting
- fashion_textiles_apparel
- governance
- government_public_services_social_impact
- healthcare_life_sciences
- healthcare_medical_life_sciences_api_ecosystem
- healthcare_wellness_fitness
- healthcare_wellness_fitness_api_ecosystem
- home_homemaker_care_economy_business_api_ecosystem
- home_services_property_maintenance_facility_management
- industries_professional_services_business_api_ecosystem
- industry_api_ecosystems
- integrations
- international_trade_import_export_customs_global_commerce
- investment_finance_support_business_api_ecosystem
- jobs_careers_employment
- legal_coach_consultant_advisor_education_learning_training_professional_services_api_ecosystem
- legal_consulting_professional_services
- manufacturing_industrial_services
- marketing_media_entertainment
- media_entertainment_creative_industries
- mining_metals_minerals
- network_marketing_direct_selling_business_api_ecosystem
- personal_lifestyle_wellness
- professional_legal_business_services
- public_nonprofit_social_impact_business_api_ecosystem
- real_estate_construction
- real_estate_construction_infrastructure
- retail_ecommerce_consumer_goods
- salesforce_business_api_ecosystem
- science_research_innovation
- sectors
- security_defence_safety_services
- services
- services_platforms_integrations_business_api_ecosystem
- shopify_business_api_ecosystem
- slack_business_api_ecosystem
- sports_recreation_community
- technology_it_telecommunications
- technology_software_ai_cloud
- tools
- trafficjunky_business_api_ecosystem
- transport_logistics_supply_chain
- transport_mobility_logistics

## 3. Strong semantic matches (source -> existing global destination)

These are clear subject matches by folder name and existing destination structure:

| Non-global source | Global destination |
|---|---|
| agriculture_food_natural_resources | global_agriculture_food_natural_resources_api_ecosystem |
| digital_infrastructure_telecommunications | global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem |
| education_learning_training | global_education_learning_training_api_ecosystem |
| fashion_textiles_apparel | global_fashion_textiles_apparel_api_ecosystem |
| finance_banking_insurance | global_finance_banking_insurance_api_ecosystem |
| food_hospitality_restaurants | global_hospitality_hotels_resorts_restaurants_api_ecosystem |
| governance | global_business_governance_compliance_standards_api_ecosystem |
| real_estate_construction | global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem |
| real_estate_construction_infrastructure | global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem |
| legal_consulting_professional_services | global_legal_services_api_ecosystem |
| professional_legal_business_services | global_legal_services_api_ecosystem |
| jobs_careers_employment | global_freelancer_gig_independent_work_business_api_ecosystem (overlapping work/jobs scope; review subdomain boundaries before merge) |

## 4. Related but NOT safe to merge automatically

- international_trade_import_export_customs_global_commerce -> global_distribution_channels_api_ecosystem (trade/import-export is broader than distribution)
- family_relationships_parenting -> global_kamasutra... (the global destination has a family/relationships branch, but its wider adult-industry scope makes a blind merge inappropriate)
- healthcare_medical_life_sciences_api_ecosystem -> global_kamasutra... (not a valid general healthcare destination; do not merge)
- automotive_mobility, aviation_aerospace_space_technology, transport_logistics_supply_chain, transport_mobility_logistics -> some transport/aviation branches exist inside other ecosystems, but there is no clearly named standalone global transport/aviation root destination
- government_public_services_social_impact and public_nonprofit_social_impact_business_api_ecosystem -> no exact global public-services destination; do not assume governance is equivalent
- marketing_media_entertainment and media_entertainment_creative_industries -> no exact global media destination
- healthcare_life_sciences, healthcare_wellness_fitness, healthcare_wellness_fitness_api_ecosystem -> no suitable general global healthcare destination in the current 18-folder list
- all other non-global folders should remain separate until an explicit canonical destination is established

## 5. Why source folders have NOT been deleted in this audit

The live tree shows existing destination files with overlapping names. For example:
- agriculture source has `__init__.py` and `routes.py`; the global destination already has both.
- fashion source has `__init__.py`; the global destination already has one.
- finance source has `__init__.py`, `catalog.py`, `routes.py`, `schemas.py`, and `service.py`; some are already present in the global destination.
- education, digital infrastructure, hospitality, real estate, and legal/work destinations also contain existing package entry points or subtrees.
- jobs_careers_employment contains 843 files while the global freelancer destination contains 5,697 files; a direct overwrite/delete is unsafe.

A safe consolidation must compare conflicting file contents, merge unique subdirectories, reconcile Python imports and package exports, update registries/documentation/tests, then run the relevant test suite. This audit intentionally makes no destructive folder deletion.


## 6. Execution result on 2026-11-06

- The obsolete root-level `agriculture_food_natural_resources/` compatibility folder was removed. Its two files were only compatibility shims; the canonical implementation and routes already live in `global_agriculture_food_natural_resources_api_ecosystem/`.
- The global agriculture package remains intact.
- No other matched folder was deleted in this pass. Repository code confirms that several apparent matches are still active implementation packages or compatibility entry points used by registries, routes, tests, or global facade imports. Examples include Education, Digital Infrastructure, Finance, Hospitality, Real Estate, Jobs/Careers, and Governance.
- Moving or deleting those directories without first migrating their implementation and rewriting every dependent import would break the running API. In particular, the existing global Finance/Education/Hospitality/Real Estate packages deliberately expose or point to maintained implementation packages rather than containing independent copies.
- Therefore this commit performs only the verified safe deletion; the remaining mappings are retained as migration candidates, not reported as completed moves.


## 7. Additional verified consolidation on 2026-11-06

- Removed the root-level `fashion_textiles_apparel/` compatibility shim after switching the industry router, registry package path, and service test to the canonical `global_fashion_textiles_apparel_api_ecosystem/` package.
- Removed the root-level `governance/` compatibility shims after switching the Bada Business router and approved-requirements test to `global_business_governance_compliance_standards_api_ecosystem/governance/` directly.
- No canonical implementation files were discarded in these two cleanups; both removed directories contained only compatibility imports.
- Other matching directories remain subject to their documented implementation ownership and dependency requirements; they are not marked migrated merely because their names match.

- The complete `education_learning_training/` implementation (37 files) was moved into `global_education_learning_training_api_ecosystem/education_learning_training/`; the industry router and registry now point to that canonical package, and the old root directory was removed.

- The complete `finance_banking_insurance/` implementation (24 files) was moved into `global_finance_banking_insurance_api_ecosystem/`; the industry router, industry registry, domain registry, world catalogue and investment-finance compatibility facade now reference the canonical Global package. The old root directory was removed.

- The complete `food_hospitality_restaurants/` implementation (30 files) was moved into `global_hospitality_hotels_resorts_restaurants_api_ecosystem/`; the industry router, registry and service test now target that canonical package. The old root directory was removed.
