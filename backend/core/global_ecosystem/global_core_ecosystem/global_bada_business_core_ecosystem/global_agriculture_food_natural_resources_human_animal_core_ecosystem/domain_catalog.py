"""Business-facing domain inventory; IDs align to the canonical global CORE."""
from __future__ import annotations

BUSINESS_DOMAINS = (
    {"domain_id": "agriculture_farming_primary_production", "name": "Agriculture and Farming — Primary Production", "business_type": "FARMING", "description": "Production planning, crop operations, farm services and producer networks.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "seeds_soil_fertilizers_crop_inputs", "name": "Seeds, Soil, Fertilizers and Crop Inputs", "business_type": "INPUTS", "description": "Seed systems, soil services, nutrient management and compliant crop inputs.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "irrigation_water_management", "name": "Irrigation and Water Management", "business_type": "WATER", "description": "Irrigation services, water efficiency, watershed and equipment operations.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "farm_machinery_agritech_iot_ai", "name": "Farm Machinery and AgriTech", "business_type": "TECHNOLOGY", "description": "Machinery, precision agriculture, IoT, AI and equipment maintenance.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "agri_supply_chain_storage_logistics", "name": "Agriculture Supply Chain and Logistics", "business_type": "SUPPLY_CHAIN", "description": "Aggregation, warehousing, cold chain, transport and traceability.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "food_processing_manufacturing", "name": "Food Processing and Manufacturing", "business_type": "PROCESSING", "description": "Food manufacturing, packaging, processing and value addition.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "food_safety_testing_compliance", "name": "Food Safety and Compliance", "business_type": "COMPLIANCE", "description": "Testing, quality assurance, certifications and regulatory services.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "dairy_livestock_animal_husbandry", "name": "Dairy and Animal Husbandry", "business_type": "ANIMAL", "description": "Dairy, livestock, animal care, feed and veterinary service businesses.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "fisheries_aquaculture", "name": "Fisheries and Aquaculture", "business_type": "AQUATIC", "description": "Aquaculture operations, fisheries services, processing and distribution.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "forestry_mining_natural_resources", "name": "Forestry and Natural Resources", "business_type": "RESOURCES", "description": "Sustainable forestry, resource mapping, restoration and licensed resource services.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "organic_natural_products", "name": "Organic and Natural Products", "business_type": "NATURAL_PRODUCTS", "description": "Organic production, certification, natural products and responsible sourcing.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "agri_research_education_extension", "name": "Agriculture Research and Education", "business_type": "KNOWLEDGE", "description": "Research services, training, extension and technical advisory.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "agri_finance_insurance_investment", "name": "Agriculture Finance and Insurance", "business_type": "FINANCE", "description": "Agricultural finance, insurance, risk assessment and investment services.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "agri_trade_marketplace_exports", "name": "Agriculture Trade and Exports", "business_type": "TRADE", "description": "Marketplaces, procurement, export readiness and trade facilitation.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "agri_startups_msmes_enterprises", "name": "Agriculture Startups and MSMEs", "business_type": "ENTERPRISE", "description": "Agri-startups, MSMEs, enterprise development and business support.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
    {"domain_id": "global_bharat_agriculture_partnerships", "name": "Bharat and Global Agriculture Partnerships", "business_type": "PARTNERSHIPS", "description": "Producer partnerships, institutional collaboration and international programs.", "capabilities": ["SERVICE", "WORK", "BUSINESS"]},
)

def list_business_domains():
    return [dict(item) for item in BUSINESS_DOMAINS]

def get_business_domain(domain_id: str):
    key = domain_id.strip().casefold()
    return next((dict(item) for item in BUSINESS_DOMAINS if item["domain_id"].casefold() == key), None)
