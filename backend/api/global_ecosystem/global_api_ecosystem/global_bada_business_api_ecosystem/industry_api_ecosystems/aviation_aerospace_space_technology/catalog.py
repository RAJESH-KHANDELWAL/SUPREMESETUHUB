CATEGORIES=(
    {"id":"commercial_aviation","name":"Commercial Aviation","subcategories":["airlines","scheduled_passenger_services","charter_services","regional_aviation"]},
    {"id":"airport_operations","name":"Airport Operations","subcategories":["airport_management","ground_handling","terminal_services","airport_retail"]},
    {"id":"aircraft_manufacturing","name":"Aircraft Manufacturing","subcategories":["airframe_manufacturing","aircraft_assembly","interiors","avionics"]},
    {"id":"aircraft_maintenance","name":"Aircraft Maintenance & Repair","subcategories":["line_maintenance","heavy_maintenance","component_repair","airworthiness_support"]},
    {"id":"aviation_services","name":"Aviation Support Services","subcategories":["flight_planning","aviation_training","aircraft_leasing","aviation_consulting"]},
    {"id":"air_cargo","name":"Air Cargo & Freight","subcategories":["air_freight","cargo_handling","express_logistics","temperature_controlled_air_cargo"]},
    {"id":"aerospace_engineering","name":"Aerospace Engineering","subcategories":["propulsion_systems","aerostructures","materials_engineering","systems_design"]},
    {"id":"space_launch","name":"Space Launch Services","subcategories":["launch_vehicles","launch_sites","payload_integration","mission_operations"]},
    {"id":"satellite_systems","name":"Satellite Systems","subcategories":["satellite_manufacturing","earth_observation","communications_satellites","navigation_satellites"]},
    {"id":"space_data_services","name":"Space Data & Applications","subcategories":["geospatial_analytics","remote_sensing","satellite_imagery","space_weather_services"]},
    {"id":"space_research","name":"Space Research & Exploration","subcategories":["planetary_science","astronomy_missions","microgravity_research","space_science_instruments"]},
    {"id":"aviation_safety","name":"Aviation Safety & Compliance","subcategories":["flight_safety","safety_management","aviation_security","regulatory_advisory"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for x in CATEGORIES:
  if x["id"]==category_id: return dict(x)
 return None
