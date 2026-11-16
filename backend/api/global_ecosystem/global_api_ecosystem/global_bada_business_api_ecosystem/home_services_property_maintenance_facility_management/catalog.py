"""Home-services taxonomy; gym/spa/massage remain canonical in healthcare_wellness_fitness."""
from __future__ import annotations

CATEGORIES = [
 {"id":"cleaning_and_housekeeping","name":"Cleaning & Housekeeping","channels":["online","offline","hybrid"],"subcategories":["deep_home_cleaning","regular_housekeeping","kitchen_cleaning","bathroom_cleaning","move_in_move_out_cleaning"]},
 {"id":"plumbing_and_water_services","name":"Plumbing & Water Services","channels":["offline","hybrid"],"subcategories":["plumbing_repairs","pipe_installation","water_tank_cleaning","water_pump_services","leak_detection"]},
 {"id":"electrical_and_power_services","name":"Electrical & Power Services","channels":["offline","hybrid"],"subcategories":["electrical_repairs","wiring_and_rewiring","lighting_installation","inverter_and_backup_services","electrical_safety_inspection"]},
 {"id":"appliance_repair_and_installation","name":"Appliance Repair & Installation","channels":["offline","hybrid"],"subcategories":["refrigerator_repair","washing_machine_repair","air_conditioner_repair","kitchen_appliance_installation","small_appliance_repair"]},
 {"id":"carpentry_and_furniture_services","name":"Carpentry & Furniture Services","channels":["offline","hybrid"],"subcategories":["furniture_repair","custom_carpentry","door_and_window_repairs","modular_furniture_installation","furniture_assembly"]},
 {"id":"painting_and_wall_finishing","name":"Painting & Wall Finishing","channels":["offline","hybrid"],"subcategories":["interior_painting","exterior_painting","wallpaper_installation","waterproofing","surface_finishing"]},
 {"id":"pest_control_and_sanitation","name":"Pest Control & Sanitation","channels":["offline","hybrid"],"subcategories":["general_pest_control","termite_treatment","rodent_control","mosquito_management","sanitation_services"]},
 {"id":"home_renovation_and_minor_repairs","name":"Home Renovation & Minor Repairs","channels":["offline","hybrid"],"subcategories":["minor_civil_repairs","tile_and_floor_repairs","false_ceiling_repairs","kitchen_bathroom_renovation","home_inspection_coordination"]},
 {"id":"interior_design_and_home_setup","name":"Interior Design & Home Setup","channels":["online","offline","hybrid"],"subcategories":["space_planning","interior_design_consultation","home_styling","furniture_and_fixture_coordination","smart_home_setup"]},
 {"id":"laundry_and_garment_care","name":"Laundry & Garment Care","channels":["online","offline","hybrid"],"subcategories":["wash_and_fold","dry_cleaning","ironing_services","garment_repairs","pickup_and_delivery_coordination"]},
 {"id":"gardening_and_landscape_maintenance","name":"Gardening & Landscape Maintenance","channels":["offline","hybrid"],"subcategories":["garden_maintenance","lawn_care","plant_care","landscape_installation","irrigation_maintenance"]},
 {"id":"moving_packing_and_storage","name":"Moving, Packing & Storage","channels":["online","offline","hybrid"],"subcategories":["household_shifting","packing_and_unpacking","local_movers","short_term_storage","furniture_relocation"]},
 {"id":"residential_property_maintenance","name":"Residential Property Maintenance","channels":["online","offline","hybrid"],"subcategories":["preventive_maintenance","property_inspection_scheduling","maintenance_work_orders","tenant_move_in_move_out_support","vendor_coordination"]},
 {"id":"commercial_facility_management","name":"Commercial Facility Management","channels":["online","offline","hybrid"],"subcategories":["facility_operations","building_maintenance","soft_services_coordination","hard_services_coordination","service_level_monitoring"]},
 {"id":"society_and_community_property_management","name":"Housing Society & Community Property Management","channels":["online","offline","hybrid"],"subcategories":["residential_society_maintenance","common_area_management","resident_service_requests","vendor_contract_coordination","community_asset_registers"]},
 {"id":"workplace_and_retail_facility_services","name":"Workplace & Retail Facility Services","channels":["online","offline","hybrid"],"subcategories":["office_facility_support","retail_site_maintenance","workplace_service_desk","multi_site_facility_coordination","business_continuity_maintenance"]},
 {"id":"pool_water_feature_and_specialist_maintenance","name":"Pool, Water Feature & Specialist Maintenance","channels":["offline","hybrid"],"subcategories":["swimming_pool_maintenance","water_feature_cleaning","pump_and_filtration_maintenance","pool_water_quality_checks","specialist_equipment_servicing"]},
 {"id":"home_service_booking_and_vendor_management","name":"Home Service Booking & Vendor Management","channels":["online","hybrid"],"subcategories":["service_request_intake","provider_dispatch","appointment_scheduling","quotation_and_estimate_workflows","work_order_tracking"]}
]

CROSS_ECOSYSTEM_LINKS = {
 "healthcare_wellness_fitness":{"canonical_categories":["gym_and_fitness_centres","spa_and_massage_services","personal_training_and_coaching","yoga_and_meditation"],"relationship":"Wellness provider taxonomy remains canonical in healthcare_wellness_fitness; this package can reference it for home-visit fulfilment and facility coordination."},
 "real_estate_construction":{"canonical_categories":["property_development","construction_and_renovation"],"relationship":"Property transactions, development and major construction remain in real_estate_construction."},
 "security_defence_safety_services":{"canonical_categories":["security_services","safety_services"],"relationship":"Licensed security and specialist safety provider taxonomies remain in security_defence_safety_services."}
}

def list_categories():
 return [dict(x,channels=list(x["channels"]),subcategories=list(x["subcategories"])) for x in CATEGORIES]

def get_category(category_id: str):
 for x in CATEGORIES:
  if x["id"] == category_id: return dict(x,channels=list(x["channels"]),subcategories=list(x["subcategories"]))
 return None

def validate_catalog():
 ids=[x["id"] for x in CATEGORIES]
 duplicates=sorted({x for x in ids if ids.count(x)>1})
 return {"valid":not duplicates,"category_count":len(CATEGORIES),"duplicate_ids":duplicates}
