"""Category and business-domain catalog for Mining, Metals & Minerals."""
from __future__ import annotations

CATEGORIES = (
    {"id": "metal_mining", "name": "Metal Mining", "subcategories": ["iron_ore", "copper", "aluminium_bauxite", "zinc_lead", "precious_metals", "manganese", "chromium"]},
    {"id": "nonmetal_mining", "name": "Non-metallic Minerals", "subcategories": ["limestone", "gypsum", "phosphate", "silica", "industrial_minerals", "potash", "clays"]},
    {"id": "critical_minerals", "name": "Critical & Strategic Minerals", "subcategories": ["lithium", "cobalt", "rare_earths", "graphite", "nickel", "vanadium", "tungsten"]},
    {"id": "coal_mining", "name": "Coal & Lignite Mining", "subcategories": ["thermal_coal", "coking_coal", "lignite", "mine_services", "coal_bed_methane"]},
    {"id": "quarrying_aggregates", "name": "Quarrying & Aggregates", "subcategories": ["granite", "marble", "sandstone", "construction_aggregates", "dimension_stone"]},
    {"id": "metal_processing", "name": "Metal Processing & Smelting", "subcategories": ["smelting", "refining", "ore_beneficiation", "mineral_processing", "pelletisation"]},
    {"id": "steel_iron", "name": "Iron & Steel Industry", "subcategories": ["steelmaking", "ironmaking", "rolled_products", "foundries", "steel_products", "recycling_scrap"]},
    {"id": "nonferrous_metals", "name": "Non-ferrous Metals", "subcategories": ["aluminium_products", "copper_products", "zinc_products", "specialty_alloys", "non_ferrous_metals"]},
    {"id": "mining_equipment", "name": "Mining Equipment & Technology", "subcategories": ["drilling_equipment", "excavation_machinery", "mining_automation", "mine_safety_systems", "mining_software"]},
    {"id": "mining_services", "name": "Mining Support Services", "subcategories": ["geological_survey", "mine_planning", "exploration_services", "contract_mining", "laboratory_services"]},
    {"id": "mineral_trade", "name": "Mineral Trade & Logistics", "subcategories": ["ore_trading", "mineral_exports", "bulk_handling", "mineral_transport", "commodity_brokering"]},
    {"id": "mine_environment", "name": "Mine Environment & Closure", "subcategories": ["mine_rehabilitation", "tailings_management", "water_management", "environmental_monitoring", "mine_closure"]},
)

BUSINESS_DOMAINS = (
    {"id": "iron_ore_mining", "name": "Iron Ore Mining", "category_id": "metal_mining", "description": "Iron ore exploration, extraction, beneficiation and mine operations."},
    {"id": "coal_lignite_mining", "name": "Coal & Lignite Mining", "category_id": "coal_mining", "description": "Thermal coal, coking coal and lignite extraction and related services."},
    {"id": "gold_silver_mining", "name": "Gold & Silver Mining", "category_id": "metal_mining", "description": "Precious-metal exploration, mining, processing and refining."},
    {"id": "copper_mining", "name": "Copper Mining", "category_id": "metal_mining", "description": "Copper ore extraction, concentration and primary processing."},
    {"id": "aluminium_bauxite", "name": "Aluminium & Bauxite", "category_id": "nonferrous_metals", "description": "Bauxite mining, alumina refining and aluminium production."},
    {"id": "critical_minerals", "name": "Critical & Rare Earth Minerals", "category_id": "critical_minerals", "description": "Lithium, cobalt, nickel, graphite and rare-earth mineral value chains."},
    {"id": "limestone_industrial_minerals", "name": "Limestone & Industrial Minerals", "category_id": "nonmetal_mining", "description": "Limestone, gypsum, silica, phosphate and industrial mineral operations."},
    {"id": "quarrying_dimension_stone", "name": "Quarrying & Dimension Stone", "category_id": "quarrying_aggregates", "description": "Granite, marble, sandstone and construction aggregate quarrying."},
    {"id": "mineral_exploration_geology", "name": "Mineral Exploration & Geology", "category_id": "mining_services", "description": "Geological surveys, exploration programmes, sampling and resource evaluation."},
    {"id": "drilling_blasting_services", "name": "Drilling & Blasting Services", "category_id": "mining_services", "description": "Specialist drilling, blasting and mine development services subject to permits."},
    {"id": "ore_beneficiation_processing", "name": "Ore Beneficiation & Processing", "category_id": "metal_processing", "description": "Crushing, grinding, separation, concentration and mineral processing."},
    {"id": "smelting_refining", "name": "Metal Smelting & Refining", "category_id": "metal_processing", "description": "Primary and secondary metal smelting, refining and recovery."},
    {"id": "iron_steel_manufacturing", "name": "Iron & Steel Manufacturing", "category_id": "steel_iron", "description": "Ironmaking, steelmaking, foundries and rolled steel products."},
    {"id": "nonferrous_metal_products", "name": "Non-ferrous Metal Products", "category_id": "nonferrous_metals", "description": "Copper, aluminium, zinc and specialty alloy products."},
    {"id": "mining_equipment_technology", "name": "Mining Equipment & Technology", "category_id": "mining_equipment", "description": "Mining machinery, drilling equipment, automation, sensors and software."},
    {"id": "contract_mining_operations", "name": "Contract Mining & Mine Operations", "category_id": "mining_services", "description": "Contract extraction, mine planning, operations and technical support."},
    {"id": "mineral_trading_exports", "name": "Mineral Trading & Exports", "category_id": "mineral_trade", "description": "Mineral procurement, trading, export services and commodity brokerage."},
    {"id": "mineral_transport_bulk_handling", "name": "Mineral Transport & Bulk Handling", "category_id": "mineral_trade", "description": "Bulk material handling, storage, rail, road and port-side logistics."},
    {"id": "mine_environment_rehabilitation", "name": "Mine Environment & Rehabilitation", "category_id": "mine_environment", "description": "Environmental monitoring, tailings, mine-water management and rehabilitation."},
    {"id": "mine_closure_safety_compliance", "name": "Mine Closure, Safety & Compliance Services", "category_id": "mine_environment", "description": "Mine closure planning, safety systems and environmental compliance support."},
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
