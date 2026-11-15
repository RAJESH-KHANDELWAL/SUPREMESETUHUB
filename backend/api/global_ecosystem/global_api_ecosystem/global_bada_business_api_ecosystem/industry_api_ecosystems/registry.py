"""Master registry for India + Global business industry domains."""
from __future__ import annotations

INDUSTRY_ECOSYSTEMS = (
    {"id": "agriculture_food_natural_resources", "name": "Agriculture, Food & Natural Resources", "package": "agriculture_food_natural_resources", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "education_learning_training", "name": "Education, Learning & Training", "package": "global_education_learning_training_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "startups_entrepreneurship", "name": "Startups & Entrepreneurship", "package": "global_entrepreneurs_entrepreneurship_msme_sme_startups_solo_women_digital_ai_technology_innovation_business_creation_development_growth_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "business_companies_corporates", "name": "Businesses, Companies & Corporates", "package": "global_business_companies_corporates_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "finance_banking_insurance", "name": "Finance, Banking & Insurance", "package": "global_finance_banking_insurance_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "technology_software_ai_cloud", "name": "Technology, Software, AI & Cloud", "package": "global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem.technology_software_ai_cloud", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "international_trade_import_export_customs_global_commerce", "name": "International Trade, Import-Export, Customs & Global Commerce API Ecosystem", "package": "international_trade_import_export_customs_global_commerce", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "arts_culture_heritage_creative_economy", "name": "Arts, Culture, Heritage & Creative Economy API Ecosystem", "package": "arts_culture_heritage_creative_economy", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "marketing_media_entertainment", "name": "Marketing, Media & Entertainment", "package": "marketing_media_entertainment", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "real_estate_construction_infrastructure", "name": "Real Estate, Construction & Infrastructure", "package": "global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem.real_estate_construction_infrastructure", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "real_estate_construction", "name": "Real Estate & Construction", "package": "global_real_estate_construction_infrastructure_PROPERTY_BUSINESS_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "healthcare_wellness_fitness", "name": "Healthcare, Wellness & Fitness", "package": "healthcare_wellness_fitness", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "healthcare_life_sciences", "name": "Healthcare & Life Sciences", "package": "healthcare_life_sciences", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "beauty_fashion_lifestyle", "name": "Beauty, Fashion & Lifestyle", "package": "beauty_fashion_lifestyle", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "travel_tourism_hospitality", "name": "Travel, Tourism & Hospitality", "package": "global_travel_tourism_hospitality_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "legal_consulting_professional_services", "name": "Legal, Consulting & Professional Services", "package": "global_professional_business_services_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "retail_ecommerce_consumer_goods", "name": "Retail, E-commerce & Consumer Goods", "package": "retail_ecommerce_consumer_goods", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "transport_mobility_logistics", "name": "Transport, Mobility & Logistics", "package": "automotive_mobility.global_transport_mobility_logistics_supply_chain_business_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "sports_recreation_community", "name": "Sports, Recreation & Community", "package": "sports_recreation_community", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "technology_it_telecommunications", "name": "Technology, IT & Telecommunications", "package": "global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem.technology_it_telecommunications", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "manufacturing_industrial_services", "name": "Manufacturing, Industrial & Industries API Ecosystem", "package": "manufacturing_industrial_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "transport_logistics_supply_chain", "name": "Transport, Logistics & Supply Chain", "package": "transport_logistics_supply_chain", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "energy_utilities_environment", "name": "Energy, Utilities & Environment", "package": "energy_utilities_environment", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "professional_legal_business_services", "name": "Professional Services", "package": "global_professional_business_services_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "government_public_services_social_impact", "name": "Government, Public Services & Social Impact API Ecosystem", "package": "government_public_services_social_impact", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "automotive_mobility", "name": "Automotive, Vehicles, Mobility & Transport Services", "package": "automotive_mobility", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "personal_lifestyle_wellness", "name": "Personal, Couple, Family, Friends, Relationships, Health & Lifestyle", "package": "personal_lifestyle_wellness", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "home_services_property_maintenance_facility_management", "name": "Home Services, Property Maintenance & Facility Management API Ecosystem", "package": "home_services_property_maintenance_facility_management", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "food_hospitality_restaurants", "name": "Food Services, Restaurants & Hospitality", "package": "global_hospitality_hotels_resorts_restaurants_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "security_defence_safety_services", "name": "Security, Defence & Safety Services", "package": "security_defence_safety_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "science_research_innovation", "name": "Science, Research, Innovation & Technology API Ecosystem", "package": "science_research_innovation", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "mining_metals_minerals", "name": "Mining, Metals & Minerals", "package": "mining_metals_minerals", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "digital_infrastructure_telecommunications", "name": "Telecommunications, Internet & Digital Infrastructure", "package": "global_digital_infrastructure_telecommunications_technology_it_ai_business_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "aviation_aerospace_space_technology", "name": "Aviation, Aerospace & Space Technology", "package": "aviation_aerospace_space_technology", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "water_resources_marine_industries", "name": "Water Resources & Marine Industries", "package": "global_water_resources_marine_industries_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "fashion_textiles_apparel", "name": "Fashion, Textiles & Apparel", "package": "global_fashion_textiles_apparel_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "jobs_careers_employment", "name": "Jobs, Careers & Employment", "package": "global_jobs_careers_employment_api_ecosystem", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
)

def list_industry_ecosystems(*, include_adult: bool = False) -> list[dict[str, object]]:
    """Return industry domains; the 18+ taxonomy is hidden unless requested."""
    return [item for item in INDUSTRY_ECOSYSTEMS if include_adult or item["id"] != "adult_sexual_wellness"]

def get_industry_ecosystem(industry_id: str, *, include_adult: bool = False):
    """Return a domain or None when unknown/restricted by default."""
    for item in INDUSTRY_ECOSYSTEMS:
        if item["id"] == industry_id:
            if industry_id == "adult_sexual_wellness" and not include_adult:
                return None
            return item
    return None
