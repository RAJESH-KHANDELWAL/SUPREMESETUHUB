"""Category and business-domain catalog for Energy, Utilities & Environment."""
from __future__ import annotations

CATEGORIES = (
    {"id": "renewable_energy", "name": "Renewable Energy", "subcategories": ["solar_power", "wind_energy", "hydropower", "geothermal_energy", "biomass_energy", "renewable_project_development"]},
    {"id": "conventional_energy", "name": "Conventional Energy", "subcategories": ["oil_gas", "coal", "thermal_power", "nuclear_energy", "fuel_supply"]},
    {"id": "power_generation", "name": "Power Generation", "subcategories": ["electricity_generation", "distributed_generation", "captive_power", "independent_power_producers"]},
    {"id": "electricity_transmission_distribution", "name": "Electricity Transmission & Distribution", "subcategories": ["transmission_grids", "distribution_networks", "smart_grids", "grid_modernisation", "microgrids"]},
    {"id": "energy_storage", "name": "Energy Storage", "subcategories": ["battery_storage", "pumped_hydro_storage", "hydrogen_storage", "grid_scale_storage", "battery_recycling"]},
    {"id": "oil_gas_services", "name": "Oil, Gas & Energy Services", "subcategories": ["exploration", "refining", "pipelines", "oilfield_services", "lng_services"]},
    {"id": "water_utilities", "name": "Water Utilities", "subcategories": ["water_supply", "water_treatment", "desalination", "wastewater", "water_reuse"]},
    {"id": "waste_management", "name": "Waste Management", "subcategories": ["solid_waste", "recycling", "hazardous_waste", "circular_economy", "resource_recovery"]},
    {"id": "environmental_services", "name": "Environmental Services", "subcategories": ["environmental_consulting", "impact_assessment", "remediation", "environmental_monitoring", "compliance"]},
    {"id": "climate_sustainability", "name": "Climate & Sustainability", "subcategories": ["carbon_accounting", "carbon_markets", "esg_services", "climate_adaptation", "decarbonisation"]},
    {"id": "clean_technology", "name": "Clean Technology", "subcategories": ["energy_efficiency", "green_buildings", "clean_cooking", "pollution_control", "green_hydrogen", "industrial_efficiency"]},
    {"id": "utilities_infrastructure", "name": "Utilities Infrastructure", "subcategories": ["district_cooling", "gas_distribution", "street_lighting", "utility_maintenance", "utility_asset_management"]},
)

BUSINESS_DOMAINS = (
    {"id": "solar_energy", "name": "Solar Energy", "category_id": "renewable_energy", "description": "Solar generation, EPC, rooftop systems and project operations."},
    {"id": "wind_energy", "name": "Wind Energy", "category_id": "renewable_energy", "description": "Onshore and offshore wind projects, equipment and operations."},
    {"id": "hydropower", "name": "Hydropower", "category_id": "renewable_energy", "description": "Hydroelectric generation, small hydro and pumped-hydro projects."},
    {"id": "biomass_bioenergy", "name": "Biomass & Bioenergy", "category_id": "renewable_energy", "description": "Biomass power, biogas, biofuels and waste-to-energy feedstocks."},
    {"id": "oil_gas", "name": "Oil & Gas", "category_id": "oil_gas_services", "description": "Upstream, midstream, downstream and supporting energy services."},
    {"id": "nuclear_energy", "name": "Nuclear Energy", "category_id": "conventional_energy", "description": "Nuclear power generation, engineering and approved supply-chain services."},
    {"id": "electricity_generation", "name": "Electricity Generation", "category_id": "power_generation", "description": "Thermal, renewable, captive and distributed electricity generation."},
    {"id": "power_transmission_distribution", "name": "Power Transmission & Distribution", "category_id": "electricity_transmission_distribution", "description": "Grid networks, substations, distribution and grid maintenance."},
    {"id": "smart_grid_technology", "name": "Smart Grid Technology", "category_id": "electricity_transmission_distribution", "description": "Grid automation, metering, demand response and grid software."},
    {"id": "battery_energy_storage", "name": "Battery & Energy Storage", "category_id": "energy_storage", "description": "Battery systems, grid storage, storage integration and lifecycle services."},
    {"id": "green_hydrogen", "name": "Green Hydrogen", "category_id": "clean_technology", "description": "Renewable hydrogen production, electrolyzers, storage and distribution."},
    {"id": "water_supply_utilities", "name": "Water Supply & Utilities", "category_id": "water_utilities", "description": "Municipal, rural, industrial and bulk water supply services."},
    {"id": "water_treatment_desalination", "name": "Water Treatment & Desalination", "category_id": "water_utilities", "description": "Drinking-water treatment, industrial treatment and desalination."},
    {"id": "wastewater_management", "name": "Wastewater Management", "category_id": "water_utilities", "description": "Sewerage, wastewater collection, treatment and reuse."},
    {"id": "waste_management_recycling", "name": "Waste Management & Recycling", "category_id": "waste_management", "description": "Collection, sorting, recycling, recovery and compliant disposal."},
    {"id": "environmental_consulting", "name": "Environmental Consulting", "category_id": "environmental_services", "description": "Environmental assessments, monitoring, remediation and advisory."},
    {"id": "climate_sustainability", "name": "Climate Change & Sustainability", "category_id": "climate_sustainability", "description": "Climate risk, adaptation, mitigation and sustainability programmes."},
    {"id": "carbon_markets_esg", "name": "Carbon Markets & ESG", "category_id": "climate_sustainability", "description": "Carbon accounting, market services, ESG reporting and assurance support."},
    {"id": "clean_technology_efficiency", "name": "Clean Technology & Energy Efficiency", "category_id": "clean_technology", "description": "Efficiency technologies, electrification and pollution-control solutions."},
    {"id": "utility_infrastructure_maintenance", "name": "Utility Infrastructure & Maintenance", "category_id": "utilities_infrastructure", "description": "Utility asset operations, maintenance, district systems and infrastructure."},
)

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None

def list_business_domains():
    return [dict(item) for item in BUSINESS_DOMAINS]

def get_business_domain(domain_id: str):
    for item in BUSINESS_DOMAINS:
        if item["id"] == domain_id:
            return dict(item)
    return None
