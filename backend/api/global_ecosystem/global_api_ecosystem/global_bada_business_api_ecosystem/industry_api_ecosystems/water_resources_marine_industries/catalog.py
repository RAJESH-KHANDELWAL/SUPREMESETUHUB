CATEGORIES=(
    {"id":"water_resources","name":"Water Resources Management","subcategories":["river_basin_management","watershed_management","groundwater_management","water_allocation"]},
    {"id":"water_supply","name":"Water Supply Services","subcategories":["municipal_water","rural_water_supply","industrial_water_supply","bulk_water_supply"]},
    {"id":"water_treatment","name":"Water Treatment","subcategories":["drinking_water_treatment","industrial_effluent_treatment","desalination","water_reuse"]},
    {"id":"wastewater_services","name":"Wastewater & Sanitation","subcategories":["sewerage_systems","wastewater_collection","sewage_treatment","fecal_sludge_management"]},
    {"id":"irrigation_water","name":"Irrigation & Agricultural Water","subcategories":["micro_irrigation","canal_irrigation","farm_water_management","irrigation_equipment"]},
    {"id":"water_technology","name":"Water Technology & Monitoring","subcategories":["smart_metering","water_quality_sensors","leak_detection","hydrology_software"]},
    {"id":"marine_transport","name":"Marine Transport & Ports","subcategories":["shipping","port_operations","inland_waterways","marine_terminals"]},
    {"id":"fisheries_aquaculture","name":"Fisheries & Aquaculture","subcategories":["marine_fisheries","inland_fisheries","aquaculture_farms","seafood_handling"]},
    {"id":"marine_services","name":"Marine Services","subcategories":["vessel_services","marine_surveys","underwater_inspection","marine_equipment"]},
    {"id":"coastal_management","name":"Coastal & Ocean Management","subcategories":["coastal_protection","shoreline_management","ocean_observation","marine_spatial_planning"]},
    {"id":"marine_conservation","name":"Marine Conservation","subcategories":["coral_reef_protection","mangrove_restoration","marine_biodiversity","protected_marine_areas"]},
    {"id":"blue_economy","name":"Blue Economy & Offshore Industries","subcategories":["offshore_wind_support","ocean_energy","marine_biotechnology","sustainable_seafood"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for x in CATEGORIES:
  if x["id"]==category_id: return dict(x)
 return None
