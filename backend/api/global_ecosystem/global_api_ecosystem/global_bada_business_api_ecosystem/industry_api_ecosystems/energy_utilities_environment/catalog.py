"""Category catalog for Energy, Utilities & Environment."""
from __future__ import annotations

CATEGORIES = (
    {"id": "renewable_energy", "name": "Renewable Energy", "subcategories": ["solar_power","wind_energy","hydropower","geothermal_energy","biomass_energy"]},
    {"id": "conventional_energy", "name": "Conventional Energy", "subcategories": ["oil_gas","coal","thermal_power","nuclear_energy"]},
    {"id": "power_generation", "name": "Power Generation", "subcategories": ["electricity_generation","distributed_generation","captive_power"]},
    {"id": "electricity_transmission_distribution", "name": "Electricity Transmission & Distribution", "subcategories": ["transmission_grids","distribution_networks","smart_grids","grid_storage"]},
    {"id": "energy_storage", "name": "Energy Storage", "subcategories": ["battery_storage","pumped_hydro_storage","hydrogen_storage"]},
    {"id": "oil_gas_services", "name": "Oil, Gas & Energy Services", "subcategories": ["exploration","refining","pipelines","oilfield_services"]},
    {"id": "water_utilities", "name": "Water Utilities", "subcategories": ["water_supply","water_treatment","desalination","wastewater"]},
    {"id": "waste_management", "name": "Waste Management", "subcategories": ["solid_waste","recycling","hazardous_waste","circular_economy"]},
    {"id": "environmental_services", "name": "Environmental Services", "subcategories": ["environmental_consulting","impact_assessment","remediation","compliance"]},
    {"id": "climate_sustainability", "name": "Climate & Sustainability", "subcategories": ["carbon_accounting","carbon_markets","esg_services","climate_adaptation"]},
    {"id": "clean_technology", "name": "Clean Technology", "subcategories": ["energy_efficiency","green_buildings","clean_cooking","pollution_control"]},
    {"id": "utilities_infrastructure", "name": "Utilities Infrastructure", "subcategories": ["district_cooling","gas_distribution","street_lighting","utility_maintenance"]},
)

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None
