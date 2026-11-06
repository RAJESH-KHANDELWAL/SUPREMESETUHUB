# Global Industry Ecosystems — Folder Ownership Index

This index records the consolidation of 22 matching root-level industry folders into their corresponding Global ecosystem packages.

## Canonical storage rule

Industry-specific source packages moved into:

`<global_ecosystem_package>/industry_domains/<original_industry_folder>/`

The existing Global ecosystem files were preserved. Files were moved by Git blob reference, so source contents were not overwritten by same-named files already present in a Global package. The old root-level source folders were removed after their contents were relocated.

## Consolidated mappings

| Former root folder | Global destination |
|---|---|
| `agriculture_food_natural_resources` | `global_agriculture_food_natural_resources_api_ecosystem` |
| `digital_infrastructure_telecommunications` | `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem` |
| `technology_it_telecommunications` | `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem` |
| `technology_software_ai_cloud` | `global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem` |
| `education_learning_training` | `global_education_learning_training_api_ecosystem` |
| `fashion_textiles_apparel` | `global_fashion_textiles_apparel_api_ecosystem` |
| `finance_banking_insurance` | `global_finance_banking_insurance_api_ecosystem` |
| `food_hospitality_restaurants` | `global_hospitality_hotels_resorts_restaurants_api_ecosystem` |
| `legal_consulting_professional_services` | `global_legal_services_api_ecosystem` |
| `professional_legal_business_services` | `global_legal_services_api_ecosystem` |
| `personal_lifestyle_wellness` | `global_beauty_fashion_lifestyle_api_ecosystem` |
| `real_estate_construction` | `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem` |
| `real_estate_construction_infrastructure` | `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem` |
| `family_relationships_parenting` | `global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem` |
| `jobs_careers_employment` | `global_freelancer_gig_independent_work_business_api_ecosystem` |
| `retail_ecommerce_consumer_goods` | `global_distribution_channels_api_ecosystem` |
| `international_trade_import_export_customs_global_commerce` | `global_distribution_channels_api_ecosystem` |
| `marketing_media_entertainment` | `global_affiliate_marketing_business_api_ecosystem` |
| `government_public_services_social_impact` | `global_business_governance_compliance_standards_api_ecosystem` |
| `home_services_property_maintenance_facility_management` | `global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem` |
| `healthcare_wellness_fitness` | `global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem` |
| `healthcare_life_sciences` | `global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_coach_consultant_advisor_professional_services_work_business_api_ecosystem` |

## Runtime and registry updates

- Industry router imports now resolve through the matching Global package's `industry_domains` subpackage.
- The industry registry package paths now point to the new canonical locations.
- Finance and Government/Public Services imports in the central domain registry now resolve through their Global destinations.
- Relative imports inside each moved industry package remain package-relative.

## Maintenance rules

- Add new industry-specific files under the owning Global package's `industry_domains/<industry_name>/` directory.
- Do not recreate the removed root-level industry folders.
- Do not overwrite existing Global package files when names overlap; compare and reconcile deliberately.
- Keep router imports, registry package paths, tests, and this index synchronized.
- These packages describe taxonomy and API structure; their presence does not prove verified businesses, live providers, or exhaustive country coverage.
