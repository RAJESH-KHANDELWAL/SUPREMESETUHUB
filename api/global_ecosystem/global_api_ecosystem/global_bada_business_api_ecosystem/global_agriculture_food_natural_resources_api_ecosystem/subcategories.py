"""Canonical domain identifiers for the agriculture and food ecosystem."""
DOMAINS = (
    {"id": "agriculture_farming_primary_production", "name": "Agriculture & Farming", "folder": "agriculture_farming_primary_production"},
    {"id": "seeds_soil_fertilizers_crop_inputs", "name": "Seeds, Soil & Crop Inputs", "folder": "seeds_soil_fertilizers_crop_inputs"},
    {"id": "farm_machinery_agritech_iot_ai", "name": "Farm Machinery & AgriTech", "folder": "farm_machinery_agritech_iot_ai"},
    {"id": "irrigation_water_management", "name": "Irrigation & Water Management", "folder": "irrigation_water_management"},
    {"id": "dairy_livestock_animal_husbandry", "name": "Dairy & Animal Husbandry", "folder": "dairy_livestock_animal_husbandry"},
    {"id": "fisheries_aquaculture", "name": "Fisheries & Aquaculture", "folder": "fisheries_aquaculture"},
    {"id": "food_processing_manufacturing", "name": "Food Processing & Manufacturing", "folder": "food_processing_manufacturing"},
    {"id": "food_safety_testing_compliance", "name": "Food Safety & Compliance", "folder": "food_safety_testing_compliance"},
    {"id": "organic_natural_products", "name": "Organic & Natural Products", "folder": "organic_natural_products"},
    {"id": "agri_supply_chain_storage_logistics", "name": "Agri Supply Chain & Logistics", "folder": "agri_supply_chain_storage_logistics"},
    {"id": "agri_trade_marketplace_exports", "name": "Agri Trade & Marketplaces", "folder": "agri_trade_marketplace_exports"},
    {"id": "forestry_mining_natural_resources", "name": "Forestry & Natural Resources", "folder": "forestry_mining_natural_resources"},
    {"id": "agri_finance_insurance_investment", "name": "Agri Finance & Insurance", "folder": "agri_finance_insurance_investment"},
    {"id": "agri_research_education_extension", "name": "Research, Education & Extension", "folder": "agri_research_education_extension"},
    {"id": "agri_startups_msmes_enterprises", "name": "Agri Startups & Enterprises", "folder": "agri_startups_msmes_enterprises"},
    {"id": "global_bharat_agriculture_partnerships", "name": "Bharat & Global Partnerships", "folder": "global_bharat_agriculture_partnerships"},
)

def list_domains():
    return [dict(item) for item in DOMAINS]
