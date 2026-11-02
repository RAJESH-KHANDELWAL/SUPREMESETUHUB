CATEGORIES=(
    {"id": "metal_mining", "name": "Metal Mining", "subcategories": ["iron_ore","copper","aluminium_bauxite","zinc_lead","precious_metals"]},
    {"id": "nonmetal_mining", "name": "Non-metallic Minerals", "subcategories": ["limestone","gypsum","phosphate","silica","industrial_minerals"]},
    {"id": "critical_minerals", "name": "Critical & Strategic Minerals", "subcategories": ["lithium","cobalt","rare_earths","graphite","nickel"]},
    {"id": "coal_mining", "name": "Coal & Lignite Mining", "subcategories": ["thermal_coal","coking_coal","lignite","mine_services"]},
    {"id": "quarrying_aggregates", "name": "Quarrying & Aggregates", "subcategories": ["granite","marble","sandstone","construction_aggregates"]},
    {"id": "metal_processing", "name": "Metal Processing & Smelting", "subcategories": ["smelting","refining","ore_beneficiation","mineral_processing"]},
    {"id": "steel_iron", "name": "Iron & Steel Industry", "subcategories": ["steelmaking","ironmaking","rolled_products","foundries"]},
    {"id": "nonferrous_metals", "name": "Non-ferrous Metals", "subcategories": ["aluminium_products","copper_products","zinc_products","specialty_alloys"]},
    {"id": "mining_equipment", "name": "Mining Equipment & Technology", "subcategories": ["drilling_equipment","excavation_machinery","mining_automation","mine_safety_systems"]},
    {"id": "mining_services", "name": "Mining Support Services", "subcategories": ["geological_survey","mine_planning","exploration_services","contract_mining"]},
    {"id": "mineral_trade", "name": "Mineral Trade & Logistics", "subcategories": ["ore_trading","mineral_exports","bulk_handling","mineral_transport"]},
    {"id": "mine_environment", "name": "Mine Environment & Closure", "subcategories": ["mine_rehabilitation","tailings_management","water_management","environmental_monitoring"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
