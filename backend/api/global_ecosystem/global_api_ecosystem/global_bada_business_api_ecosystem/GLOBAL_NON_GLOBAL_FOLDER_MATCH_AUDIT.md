# Global vs Non-Global Folder Audit

Repository: `RAJESH-KHANDELWAL/SUPREMESETUHUB`  
Branch: `main`  
Scope: direct child folders of `backend/api/global_ecosystem/global_api_ecosystem/global_bada_business_api_ecosystem/`  
Audit date: 2026-11-06

## 1. Folders WITH the `global_` prefix (22)

- global_affiliate_marketing_business_api_ecosystem
- global_agriculture_food_natural_resources_api_ecosystem
- global_beauty_fashion_lifestyle_api_ecosystem
- global_business_companies_corporates_api_ecosystem
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
- global_jobs_careers_employment_api_ecosystem
- global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem
- global_legal_services_api_ecosystem
- global_professional_business_services_api_ecosystem
- global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem
- global_travel_tourism_hospitality_api_ecosystem
- global_universal_work_business_taxonomy_api_ecosystem
- global_water_resources_marine_industries_api_ecosystem

## 2. Folders WITHOUT the `global_` prefix (39)

- arts_culture_heritage_creative_economy
- automotive_mobility
- aviation_aerospace_space_technology
- business_capabilities
- exoclick_business_api_ecosystem
- family_relationships_parenting
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
- legal_coach_consultant_advisor_education_learning_training_professional_services_api_ecosystem
- manufacturing_industrial_services
- marketing_media_entertainment
- media_entertainment_creative_industries
- mining_metals_minerals
- network_marketing_direct_selling_business_api_ecosystem
- personal_lifestyle_wellness
- public_nonprofit_social_impact_business_api_ecosystem
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
- tools
- trafficjunky_business_api_ecosystem
- transport_logistics_supply_chain

## 3. Verified consolidations completed on 2026-11-06

- Adult Kamasutra and lawful adult-industry taxonomy is maintained in BOTH the Bada Business subtree and the Global API root, using the exact same folder name. Both locations remain active; no move or source deletion is intended.

- `agriculture_food_natural_resources` → `global_agriculture_food_natural_resources_api_ecosystem`: obsolete compatibility files removed after confirming the canonical implementation existed in the Global package.
- `education_learning_training` → `global_education_learning_training_api_ecosystem/education_learning_training`: implementation moved; router, registry and dependent imports updated; old root folder removed.
- `fashion_textiles_apparel` → `global_fashion_textiles_apparel_api_ecosystem`: redundant compatibility shim removed; router, registry and service test updated.
- `finance_banking_insurance` → `global_finance_banking_insurance_api_ecosystem`: implementation moved; router, industry registry, domain registry and related facades updated; old root folder removed.
- `food_hospitality_restaurants` → `global_hospitality_hotels_resorts_restaurants_api_ecosystem`: implementation moved; router, registry and test updated; old root folder removed.
- `governance` → `global_business_governance_compliance_standards_api_ecosystem/governance`: compatibility shims removed after routes and tests were redirected to the canonical package.
- `real_estate_construction` and `real_estate_construction_infrastructure` → `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem`: implementation and identity files moved; router, registry and tests updated; old root folders removed.
- `digital_infrastructure_telecommunications` → `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/digital_infrastructure_telecommunications`: implementation moved; router, registry and test updated; old root folder removed.
- `jobs_careers_employment` → `global_jobs_careers_employment_api_ecosystem`: 843 preserved files moved; industry router and registry updated. This 15-category Jobs industry/service taxonomy remains distinct from the 24-category Work & Careers taxonomy under Global Freelancer.
- `professional_legal_business_services` → `global_professional_business_services_api_ecosystem`: non-legal Professional Services implementation moved; router, registry and service test updated; old root implementation and obsolete `legal_consulting_professional_services` alias removed. It was deliberately NOT merged into Legal Services because the scopes differ.
- `business_companies_corporates` → `global_business_companies_corporates_api_ecosystem`: domain metadata and category adapter consolidated into the Global package; the adapter reuses the canonical Global Company business-enterprise taxonomy.
- Flat Universal Work & Business Taxonomy modules → `global_universal_work_business_taxonomy_api_ecosystem`: catalog, model, service and routes moved; root router and tests updated; old flat source modules removed.
- `technology_it_telecommunications` → `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_it_telecommunications`: implementation moved; industry router, registry and service test updated; old root folder removed.
- `technology_software_ai_cloud` → `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem/technology_software_ai_cloud`: domain identity moved; registry package path updated; old root identity file removed.

- `transport_mobility_logistics` → `automotive_mobility/global_transport_mobility_logistics_supply_chain_business_api_ecosystem`: its single-file industry identity shim was consolidated into the Global entry point; the registry now resolves the stable industry ID there. The separate `transport_logistics_supply_chain` API implementation remains intact.

## 4. Related folders that must remain separate

- International Trade is broader than distribution channels; it is not a duplicate of `global_distribution_channels_api_ecosystem`.
- Automotive, aviation, transport/logistics and transport/mobility have distinct domain boundaries and nested transport/aviation entry points. Do not collapse them solely by name.
- Government/Public Services and Nonprofit/Social Impact are not equivalents of governance/compliance.
- Healthcare, life sciences and wellness folders remain separate scopes; the adult-only Global Kamasutra ecosystem is not a general healthcare replacement.
- Family/parenting is not interchangeable with the broader adult-industry Global Kamasutra ecosystem.
- Marketing/media/entertainment folders have distinct content and commercial-media boundaries.
- Platform-specific folders such as Salesforce, Shopify, Slack, ExoClick and TrafficJunky are integrations/providers, not industry taxonomy duplicates.
- `global_legal_services_api_ecosystem` is a separate legal-services taxonomy/documentation scope. Non-legal Professional Services are maintained in `global_professional_business_services_api_ecosystem`.

## 5. Remaining migration policy

A non-global folder is not automatically obsolete because a similarly named Global folder exists. Before any further move or deletion:
1. compare source and destination file contents and collisions;
2. identify every import, route, registry, test, documentation and runtime reference;
3. move unique files without overwriting canonical implementations;
4. update dependent references in the same migration;
5. run relevant tests and inspect GitHub Actions results;
6. delete the old source only after the canonical destination is verified.

The 39 non-global folders above remain because they are separate domains, nested infrastructure, provider integrations, documentation layers, or have no verified one-to-one Global destination. Do not delete them based on naming alone.
