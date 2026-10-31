"""Master registry for India + Global business industry domains."""
from __future__ import annotations

INDUSTRY_ECOSYSTEMS = (
    {"id": "agriculture_food_natural_resources", "name": "Agriculture, Food & Natural Resources", "package": "agriculture_food_natural_resources", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "education_learning_training", "name": "Education, Learning & Training", "package": "education_learning_training", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "jobs_careers_employment", "name": "Jobs, Careers & Employment", "package": "jobs_careers_employment", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "startups_entrepreneurship", "name": "Startups & Entrepreneurship", "package": "startups_entrepreneurship", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "business_companies_corporates", "name": "Businesses, Companies & Corporates", "package": "business_companies_corporates", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "finance_banking_insurance", "name": "Finance, Banking & Insurance", "package": "finance_banking_insurance", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "technology_software_ai_cloud", "name": "Technology, Software, AI & Cloud", "package": "technology_software_ai_cloud", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "marketing_media_entertainment", "name": "Marketing, Media & Entertainment", "package": "marketing_media_entertainment", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "real_estate_construction_infrastructure", "name": "Real Estate, Construction & Infrastructure", "package": "real_estate_construction_infrastructure", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "real_estate_construction", "name": "Real Estate & Construction", "package": "real_estate_construction", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "healthcare_wellness_fitness", "name": "Healthcare, Wellness & Fitness", "package": "healthcare_wellness_fitness", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "healthcare_life_sciences", "name": "Healthcare & Life Sciences", "package": "healthcare_life_sciences", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "beauty_fashion_lifestyle", "name": "Beauty, Fashion & Lifestyle", "package": "beauty_fashion_lifestyle", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "family_relationships_parenting", "name": "Family, Relationships & Parenting", "package": "family_relationships_parenting", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "adult_sexual_wellness", "name": "Adult & Sexual Wellness (18+)", "package": "adult_sexual_wellness", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "travel_tourism_hospitality", "name": "Travel, Tourism & Hospitality", "package": "travel_tourism_hospitality", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "legal_consulting_professional_services", "name": "Legal, Consulting & Professional Services", "package": "legal_consulting_professional_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "manufacturing_trade_retail", "name": "Manufacturing, Trade & Retail", "package": "manufacturing_trade_retail", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "retail_ecommerce_consumer_goods", "name": "Retail, E-commerce & Consumer Goods", "package": "retail_ecommerce_consumer_goods", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "transport_mobility_logistics", "name": "Transport, Mobility & Logistics", "package": "transport_mobility_logistics", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "sports_recreation_community", "name": "Sports, Recreation & Community", "package": "sports_recreation_community", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "technology_it_telecommunications", "name": "Technology, IT & Telecommunications", "package": "technology_it_telecommunications", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "manufacturing_industrial_services", "name": "Manufacturing & Industrial Services", "package": "manufacturing_industrial_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "transport_logistics_supply_chain", "name": "Transport, Logistics & Supply Chain", "package": "transport_logistics_supply_chain", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "media_entertainment_creative_industries", "name": "Media, Entertainment & Creative Industries", "package": "media_entertainment_creative_industries", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "energy_utilities_environment", "name": "Energy, Utilities & Environment", "package": "energy_utilities_environment", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "professional_legal_business_services", "name": "Professional, Legal & Business Services", "package": "professional_legal_business_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "government_public_services_social_impact", "name": "Government, Public Services & Social Impact", "package": "government_public_services_social_impact", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "automotive_mobility", "name": "Automotive & Mobility", "package": "automotive_mobility", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "personal_lifestyle_wellness", "name": "Personal, Lifestyle & Wellness Services", "package": "personal_lifestyle_wellness", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "food_hospitality_restaurants", "name": "Food Services, Restaurants & Hospitality", "package": "food_hospitality_restaurants", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "security_defence_safety_services", "name": "Security, Defence & Safety Services", "package": "security_defence_safety_services", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "science_research_innovation", "name": "Science, Research & Innovation", "package": "science_research_innovation", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
    {"id": "mining_metals_minerals", "name": "Mining, Metals & Minerals", "package": "mining_metals_minerals", "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "status": "taxonomy_scaffold"},
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
