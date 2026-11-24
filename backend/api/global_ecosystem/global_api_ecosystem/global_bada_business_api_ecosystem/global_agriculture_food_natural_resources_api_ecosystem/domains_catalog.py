"""Descriptions and coverage notes for registered ecosystem domains."""
DOMAIN_DETAILS = {
    "agriculture_farming_primary_production": {"name": "Agriculture & Farming", "description": "Crop production, farm operations, horticulture, protected cultivation and farm services."},
    "seeds_soil_fertilizers_crop_inputs": {"name": "Seeds, Soil & Crop Inputs", "description": "Seed systems, nurseries, soil health, fertilizers, bio-inputs and crop protection."},
    "farm_machinery_agritech_iot_ai": {"name": "Farm Machinery & AgriTech", "description": "Mechanisation, precision agriculture, sensors, drones, farm software and AI."},
    "irrigation_water_management": {"name": "Irrigation & Water Management", "description": "Irrigation infrastructure, water-use efficiency, watershed and farm water systems."},
    "dairy_livestock_animal_husbandry": {"name": "Dairy & Animal Husbandry", "description": "Dairy, livestock, poultry, animal nutrition, veterinary and allied services."},
    "fisheries_aquaculture": {"name": "Fisheries & Aquaculture", "description": "Inland and marine fisheries, aquaculture, hatcheries, feed and cold-chain."},
    "food_processing_manufacturing": {"name": "Food Processing & Manufacturing", "description": "Food transformation, packaging, quality systems and food manufacturing."},
    "food_safety_testing_compliance": {"name": "Food Safety & Compliance", "description": "Food testing, traceability, standards, licensing and regulatory workflows."},
    "organic_natural_products": {"name": "Organic & Natural Products", "description": "Organic farming, natural produce, regenerative practices and certification."},
    "agri_supply_chain_storage_logistics": {"name": "Agri Supply Chain & Logistics", "description": "Warehousing, grading, aggregation, cold-chain, transport and market linkage."},
    "agri_trade_marketplace_exports": {"name": "Agri Trade & Marketplaces", "description": "Wholesale, retail, commodity markets, exports, imports and B2B/B2C trade."},
    "forestry_mining_natural_resources": {"name": "Forestry & Natural Resources", "description": "Forestry, biodiversity-linked enterprise, land resources and responsible extraction."},
    "agri_finance_insurance_investment": {"name": "Agri Finance & Insurance", "description": "Agricultural credit, insurance, risk products, investment and financial inclusion."},
    "agri_research_education_extension": {"name": "Research, Education & Extension", "description": "Research institutions, training, extension services, skills and certifications."},
    "agri_startups_msmes_enterprises": {"name": "Agri Startups & Enterprises", "description": "Agri startups, MSMEs, cooperatives, FPOs, enterprise operations and consulting."},
    "global_bharat_agriculture_partnerships": {"name": "Bharat & Global Partnerships", "description": "Cross-border collaboration, development programmes and international market access."},
}

def get_domain_details(domain_id):
    item = DOMAIN_DETAILS.get(domain_id)
    return dict(item) if item else None
