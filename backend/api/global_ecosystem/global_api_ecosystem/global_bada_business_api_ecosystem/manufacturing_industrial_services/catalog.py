"""Manufacturing, industrial, industries and factory-services taxonomy."""

CATEGORIES = [
    {"id": "industrial_manufacturing", "name": "Industrial Manufacturing", "subcategories": ["discrete_manufacturing", "process_manufacturing", "contract_manufacturing", "precision_manufacturing"]},
    {"id": "factory_operations_management", "name": "Factory Operations & Production Management", "subcategories": ["factory_setup_and_layout", "production_planning", "plant_operations", "lean_manufacturing"]},
    {"id": "machinery_equipment_tools", "name": "Machinery, Equipment & Machine Tools", "subcategories": ["industrial_machinery", "machine_tools", "factory_equipment", "precision_engineering"]},
    {"id": "automotive_vehicle_manufacturing", "name": "Automotive & Vehicle Manufacturing", "subcategories": ["vehicle_assembly", "automotive_components", "electric_vehicle_components", "battery_pack_manufacturing"]},
    {"id": "electrical_electronics_manufacturing", "name": "Electrical & Electronics Manufacturing", "subcategories": ["electrical_equipment", "electronic_components", "pcb_assembly", "device_contract_manufacturing"]},
    {"id": "chemicals_materials_processing", "name": "Chemical, Polymer & Materials Processing", "subcategories": ["industrial_chemicals", "specialty_chemicals", "polymer_processing", "advanced_materials"]},
    {"id": "pharmaceutical_medical_manufacturing", "name": "Pharmaceutical & Medical Product Manufacturing", "subcategories": ["pharmaceutical_production", "api_and_formulations", "medical_devices", "medical_consumables"]},
    {"id": "food_beverage_processing", "name": "Food & Beverage Processing Industries", "subcategories": ["food_processing", "beverage_manufacturing", "dairy_processing", "industrial_food_packaging"]},
    {"id": "textile_technical_textile_manufacturing", "name": "Textile & Technical Textile Manufacturing", "subcategories": ["spinning_and_weaving", "technical_textiles", "fabric_processing", "industrial_garment_production"]},
    {"id": "metal_fabrication_foundry", "name": "Metal Fabrication, Foundry & Forging", "subcategories": ["metal_fabrication", "foundry_and_casting", "forging_and_forging_parts", "industrial_welding"]},
    {"id": "packaging_printing_converting", "name": "Packaging, Printing & Converting", "subcategories": ["flexible_packaging", "rigid_packaging", "labels_and_cartons", "industrial_printing"]},
    {"id": "industrial_automation_robotics", "name": "Industrial Automation & Robotics", "subcategories": ["factory_automation", "industrial_robotics", "plc_scada_control", "machine_vision_and_sensors"]},
    {"id": "quality_testing_inspection", "name": "Quality, Testing, Inspection & Calibration", "subcategories": ["quality_assurance", "product_testing", "industrial_inspection", "calibration_services"]},
    {"id": "plant_engineering_maintenance", "name": "Plant Engineering, Maintenance & Shutdown Services", "subcategories": ["plant_maintenance", "equipment_repair", "shutdown_turnaround", "reliability_engineering"]},
    {"id": "factory_utilities_environment", "name": "Factory Utilities, Environment & Resource Services", "subcategories": ["industrial_electrical_utilities", "industrial_water_and_effluent", "air_and_compressed_gas_systems", "waste_and_emissions_management"]},
    {"id": "industrial_facility_safety_support", "name": "Industrial Facility, Safety & Factory Support Services", "subcategories": ["factory_facility_management", "industrial_safety_and_fire_protection", "internal_material_handling", "industrial_project_engineering"]},
]

BUSINESS_DOMAINS = [
    {"id": "discrete_process_manufacturing", "name": "Discrete & Process Manufacturing", "category_id": "industrial_manufacturing", "description": "Factories producing discrete goods or process-based outputs, including batch, continuous and assembly production."},
    {"id": "contract_manufacturing", "name": "Contract, OEM & Private-Label Manufacturing", "category_id": "industrial_manufacturing", "description": "Third-party production, OEM supply, private-label manufacturing and job-work arrangements."},
    {"id": "factory_setup_layout_expansion", "name": "Factory Setup, Layout & Expansion", "category_id": "factory_operations_management", "description": "Factory planning, plant layout, production-line setup, capacity expansion and commissioning support."},
    {"id": "production_operations_management", "name": "Production Planning & Factory Operations Management", "category_id": "factory_operations_management", "description": "Production planning, shop-floor operations, workflow optimization, inventory coordination and lean operations."},
    {"id": "industrial_machinery_equipment", "name": "Industrial Machinery & Equipment Manufacturing", "category_id": "machinery_equipment_tools", "description": "Manufacture, assembly and servicing of industrial machines, plant equipment and production systems."},
    {"id": "machine_tools_precision_engineering", "name": "Machine Tools & Precision Engineering", "category_id": "machinery_equipment_tools", "description": "CNC machinery, tooling, precision components, dies, moulds and engineering fabrication."},
    {"id": "automotive_vehicle_component_manufacturing", "name": "Automotive, Vehicle & Component Manufacturing", "category_id": "automotive_vehicle_manufacturing", "description": "Vehicle assembly and OEM component production; excludes dealerships, vehicle rentals and general aftermarket services."},
    {"id": "ev_battery_component_manufacturing", "name": "EV, Battery & Charging-Hardware Manufacturing", "category_id": "automotive_vehicle_manufacturing", "description": "Electric-vehicle components, battery packs, power electronics and charging hardware production."},
    {"id": "electrical_electronics_pcb_manufacturing", "name": "Electrical, Electronics & PCB Manufacturing", "category_id": "electrical_electronics_manufacturing", "description": "Electrical equipment, electronic components, printed circuit boards, assemblies and contract electronics production."},
    {"id": "chemical_materials_processing", "name": "Chemical, Polymer & Advanced-Materials Processing", "category_id": "chemicals_materials_processing", "description": "Industrial and specialty chemical production, polymer conversion and advanced-material processing; excludes extraction and mining."},
    {"id": "pharmaceutical_medical_device_manufacturing", "name": "Pharmaceutical & Medical-Device Manufacturing", "category_id": "pharmaceutical_medical_manufacturing", "description": "Manufacturing of APIs, formulations, medical devices and regulated medical consumables; excludes clinical treatment and pharmacies."},
    {"id": "food_beverage_processing", "name": "Food, Beverage & Dairy Processing", "category_id": "food_beverage_processing", "description": "Industrial food processing, beverage production, dairy processing and packaged-food manufacturing; excludes restaurants and catering."},
    {"id": "textile_technical_textile_manufacturing", "name": "Textile, Fabric & Technical-Textile Manufacturing", "category_id": "textile_technical_textile_manufacturing", "description": "Industrial spinning, weaving, fabric finishing, technical textiles and garment production; excludes fashion retail."},
    {"id": "metal_fabrication_foundry_forging", "name": "Metal Fabrication, Foundry, Casting & Forging", "category_id": "metal_fabrication_foundry", "description": "Fabrication, casting, forging, welding and manufactured metal components; excludes mining and primary mineral extraction."},
    {"id": "packaging_printing_label_manufacturing", "name": "Packaging, Printing, Labels & Cartons Manufacturing", "category_id": "packaging_printing_converting", "description": "Flexible and rigid packaging, industrial printing, labels, cartons and converting operations."},
    {"id": "industrial_automation_robotics_integration", "name": "Industrial Automation, Robotics & Controls", "category_id": "industrial_automation_robotics", "description": "Factory automation, robotics, PLC/SCADA, industrial controls, sensors and machine-vision integration."},
    {"id": "quality_inspection_testing_calibration", "name": "Industrial Quality, Inspection, Testing & Calibration", "category_id": "quality_testing_inspection", "description": "Product and process quality systems, inspection, testing laboratories and equipment calibration services."},
    {"id": "plant_maintenance_repair_shutdown", "name": "Plant Maintenance, Equipment Repair & Shutdown Services", "category_id": "plant_engineering_maintenance", "description": "Preventive and corrective maintenance, industrial repair, reliability work and planned shutdown or turnaround support."},
    {"id": "factory_utilities_environmental_services", "name": "Factory Utilities, Water, Effluent & Environmental Services", "category_id": "factory_utilities_environment", "description": "Factory utility systems, industrial water and effluent treatment, compressed air, emissions and waste-management services."},
    {"id": "factory_facility_safety_support_services", "name": "Factory Facility, Industrial Safety & Support Services", "category_id": "industrial_facility_safety_support", "description": "Factory facility management, industrial fire and safety systems, internal material handling and industrial project-engineering support."},
]

def list_categories():
    return [dict(item, subcategories=list(item["subcategories"])) for item in CATEGORIES]

def get_category(category_id: str):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None

def list_business_domains():
    return [dict(item) for item in BUSINESS_DOMAINS]

def get_business_domain(domain_id: str):
    for item in BUSINESS_DOMAINS:
        if item["id"] == domain_id:
            return dict(item)
    return None

def validate_catalog():
    category_ids = [item["id"] for item in CATEGORIES]
    domain_ids = [item["id"] for item in BUSINESS_DOMAINS]
    known_categories = set(category_ids)
    invalid_mappings = sorted(item["id"] for item in BUSINESS_DOMAINS if item["category_id"] not in known_categories)
    return {
        "category_count": len(CATEGORIES),
        "business_domain_count": len(BUSINESS_DOMAINS),
        "duplicate_category_ids": sorted({value for value in category_ids if category_ids.count(value) > 1}),
        "duplicate_business_domain_ids": sorted({value for value in domain_ids if domain_ids.count(value) > 1}),
        "invalid_category_mappings": invalid_mappings,
        "structurally_valid": len(category_ids) == len(set(category_ids)) and len(domain_ids) == len(set(domain_ids)) and not invalid_mappings,
        "live_data_verified": False,
    }
