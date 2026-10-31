"""Industries & Professional Services domain package; classification only, not verified live listings."""
DOMAIN_ID = "industries_professional_services"
DOMAIN_NAME = "Industries & Professional Services"
ADULT_RESTRICTED = false
DEFAULT_DISCOVERY_ENABLED = true
SUBCATEGORY_IDS: tuple[str, ...] = (
    "agriculture_forestry_fisheries",
    "mining_metals_minerals",
    "energy_utilities",
    "manufacturing_industrial",
    "construction_infrastructure",
    "real_estate_property",
    "retail_wholesale_distribution",
    "food_beverage_restaurants",
    "hospitality_tourism_travel",
    "transport_mobility_logistics",
    "automotive_ev_services",
    "technology_software_it",
    "ai_data_cloud_cybersecurity",
    "telecommunications",
    "finance_banking_insurance",
    "accounting_taxation",
    "legal_compliance",
    "consulting_advisory",
    "healthcare_life_sciences",
    "wellness_fitness",
    "beauty_personal_care",
    "fashion_textiles",
    "education_training",
    "media_entertainment",
    "arts_design_creative",
    "sports_recreation",
    "environment_sustainability",
    "water_marine",
    "aviation_aerospace",
    "security_safety",
    "government_public_services",
    "nonprofit_social_impact",
    "events_community_services",
    "repair_maintenance_home_services",
    "science_research_innovation",
    "supply_chain_warehousing",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
