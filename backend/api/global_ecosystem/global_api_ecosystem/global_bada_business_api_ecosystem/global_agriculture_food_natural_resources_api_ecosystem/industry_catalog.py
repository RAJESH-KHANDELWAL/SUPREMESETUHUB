"""Agriculture, Food & Natural Resources category taxonomy."""
from __future__ import annotations

AGRICULTURE_CATEGORIES = (
    {"id": "crop_farming", "name": "Crop Farming & Field Agriculture", "subcategories": ["cereals_and_grains", "pulses_and_legumes", "oilseeds", "cotton_and_fibre_crops", "sugarcane_and_commercial_crops", "medicinal_and_aromatic_crops"]},
    {"id": "horticulture", "name": "Horticulture, Fruits & Vegetables", "subcategories": ["fruit_cultivation", "vegetable_cultivation", "floriculture", "plant_nurseries", "protected_cultivation", "landscaping_and_gardening"]},
    {"id": "organic_and_natural_farming", "name": "Organic, Natural & Regenerative Farming", "subcategories": ["certified_organic_farming", "natural_farming", "permaculture", "regenerative_agriculture", "soil_health_and_composting"]},
    {"id": "livestock_and_dairy", "name": "Livestock, Dairy & Animal Husbandry", "subcategories": ["dairy_farming", "poultry_farming", "goat_and_sheep_farming", "cattle_and_buffalo", "animal_feed", "veterinary_services"]},
    {"id": "fisheries_and_aquaculture", "name": "Fisheries & Aquaculture", "subcategories": ["inland_fisheries", "marine_fisheries", "fish_farming", "shrimp_and_prawn_farming", "aquaculture_equipment"]},
    {"id": "forestry_and_plantation", "name": "Forestry, Plantations & Natural Resources", "subcategories": ["agroforestry", "timber_and_wood", "bamboo_and_rattan", "plantation_crops", "forest_products_and_services"]},
    {"id": "agri_inputs_and_seeds", "name": "Agricultural Inputs, Seeds & Crop Protection", "subcategories": ["seeds_and_seedlings", "fertilisers_and_nutrients", "biofertilisers", "crop_protection", "pesticide_application_services"]},
    {"id": "farm_machinery_and_equipment", "name": "Farm Machinery, Tools & Equipment", "subcategories": ["tractors_and_power_tillers", "harvesters_and_implements", "precision_farming_equipment", "irrigation_systems", "equipment_rental_and_repair"]},
    {"id": "irrigation_and_water_management", "name": "Irrigation & Water Management", "subcategories": ["drip_and_sprinkler", "water_pumps", "watershed_management", "rainwater_harvesting", "farm_water_efficiency"]},
    {"id": "food_processing_and_manufacturing", "name": "Food Processing & Manufacturing", "subcategories": ["grain_milling", "dairy_processing", "fruit_and_vegetable_processing", "meat_and_seafood_processing", "packaged_and_convenience_food", "food_quality_and_testing"]},
    {"id": "storage_cold_chain_and_logistics", "name": "Agricultural Storage, Cold Chain & Logistics", "subcategories": ["warehousing_and_silos", "cold_storage", "reefer_transport", "packaging_and_grading", "agri_supply_chain_services"]},
    {"id": "agri_markets_and_trade", "name": "Agricultural Markets, Procurement & Trade", "subcategories": ["farmer_producer_organisations", "wholesale_and_commodity_markets", "agri_exports_and_imports", "commodity_trading", "market_linkage_services"]},
    {"id": "agritech_and_digital_services", "name": "AgriTech, Data & Digital Services", "subcategories": ["farm_management_software", "remote_sensing_and_drones", "precision_agriculture", "digital_marketplaces", "farm_advisory_and_analytics"]},
    {"id": "rural_finance_and_insurance", "name": "Rural Finance, Credit & Crop Insurance", "subcategories": ["agricultural_credit", "crop_and_livestock_insurance", "equipment_finance", "rural_banking_services", "risk_assessment"]},
    {"id": "bioenergy_and_agri_waste", "name": "Bioenergy, Biomass & Agricultural Waste", "subcategories": ["biogas_and_biomethane", "biomass_fuels", "biochar", "crop_residue_management", "agri_waste_recycling"]},
)

def list_agriculture_categories() -> list[dict[str, object]]:
    """Return a copy of the agriculture category catalog."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in AGRICULTURE_CATEGORIES]

def get_agriculture_category(category_id: str) -> dict[str, object] | None:
    """Return one category by its stable identifier."""
    for item in AGRICULTURE_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
