"""Manufacturing and industrial services taxonomy."""
CATEGORIES = [
  {
    "id": "industrial_manufacturing",
    "name": "Industrial Manufacturing",
    "subcategories": [
      "discrete_manufacturing",
      "process_manufacturing",
      "precision_engineering",
      "contract_manufacturing"
    ]
  },
  {
    "id": "machinery_and_equipment",
    "name": "Machinery & Equipment",
    "subcategories": [
      "industrial_machinery",
      "machine_tools",
      "automation_equipment",
      "plant_equipment"
    ]
  },
  {
    "id": "automotive_and_components",
    "name": "Automotive & Components",
    "subcategories": [
      "vehicle_assembly",
      "auto_components",
      "electric_vehicle_components",
      "aftermarket_parts"
    ]
  },
  {
    "id": "chemicals_and_materials",
    "name": "Chemicals & Advanced Materials",
    "subcategories": [
      "specialty_chemicals",
      "industrial_gases",
      "polymers",
      "advanced_materials"
    ]
  },
  {
    "id": "metals_and_minerals",
    "name": "Metals, Minerals & Mining Services",
    "subcategories": [
      "steel_products",
      "non_ferrous_metals",
      "mineral_processing",
      "mining_equipment"
    ]
  },
  {
    "id": "textiles_and_apparel_manufacturing",
    "name": "Textiles & Apparel Manufacturing",
    "subcategories": [
      "spinning_and_weaving",
      "technical_textiles",
      "garment_manufacturing",
      "dyeing_and_finishing"
    ]
  },
  {
    "id": "electronics_manufacturing",
    "name": "Electronics Manufacturing",
    "subcategories": [
      "pcb_assembly",
      "electronic_components",
      "consumer_electronics_manufacturing",
      "testing_and_assembly"
    ]
  },
  {
    "id": "industrial_automation",
    "name": "Industrial Automation & Robotics",
    "subcategories": [
      "factory_automation",
      "industrial_robotics",
      "control_systems",
      "machine_vision"
    ]
  },
  {
    "id": "quality_testing_certification",
    "name": "Quality, Testing & Certification",
    "subcategories": [
      "product_testing",
      "inspection_services",
      "calibration_labs",
      "quality_management"
    ]
  },
  {
    "id": "industrial_maintenance",
    "name": "Industrial Maintenance & Plant Services",
    "subcategories": [
      "plant_maintenance",
      "equipment_repair",
      "shutdown_services",
      "reliability_engineering"
    ]
  },
  {
    "id": "packaging_and_printing",
    "name": "Packaging & Printing",
    "subcategories": [
      "industrial_packaging",
      "flexible_packaging",
      "commercial_printing",
      "labels_and_cartons"
    ]
  },
  {
    "id": "industrial_safety_environment",
    "name": "Industrial Safety & Environment",
    "subcategories": [
      "occupational_safety",
      "environmental_services",
      "industrial_waste",
      "emissions_management"
    ]
  }
]
def list_categories(): return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
