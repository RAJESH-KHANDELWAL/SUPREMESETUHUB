"""India and global aviation, aerospace and space technology taxonomy."""

BUSINESS_DOMAINS = (
    {"id":"commercial_aviation","name":"Commercial Aviation","category_id":"commercial_aviation"},
    {"id":"airlines_operations","name":"Airlines & Airline Operations","category_id":"commercial_aviation"},
    {"id":"airports_services","name":"Airports & Airport Services","category_id":"airport_operations"},
    {"id":"aircraft_manufacturing","name":"Aircraft Manufacturing","category_id":"aircraft_manufacturing"},
    {"id":"aircraft_mro","name":"Aircraft Maintenance, Repair & Overhaul","category_id":"aircraft_maintenance"},
    {"id":"aircraft_parts_components","name":"Aircraft Parts & Components","category_id":"aircraft_manufacturing"},
    {"id":"aviation_technology_software","name":"Aviation Technology & Software","category_id":"aviation_services"},
    {"id":"air_cargo_logistics","name":"Air Cargo & Aviation Logistics","category_id":"air_cargo"},
    {"id":"private_business_aviation","name":"Private & Business Aviation","category_id":"commercial_aviation"},
    {"id":"helicopter_services","name":"Helicopter Services","category_id":"aviation_services"},
    {"id":"drone_uav_technology","name":"Drone & UAV Technology","category_id":"aerospace_engineering"},
    {"id":"drone_services_operations","name":"Drone Services & Operations","category_id":"aviation_services"},
    {"id":"aerospace_manufacturing","name":"Aerospace Manufacturing","category_id":"aerospace_engineering"},
    {"id":"space_technology","name":"Space Technology","category_id":"space_research"},
    {"id":"satellite_manufacturing","name":"Satellite Manufacturing","category_id":"satellite_systems"},
    {"id":"satellite_communication","name":"Satellite Communication","category_id":"satellite_systems"},
    {"id":"space_launch_services","name":"Space Launch Services","category_id":"space_launch"},
    {"id":"space_research_exploration","name":"Space Research & Exploration","category_id":"space_research"},
    {"id":"aviation_training_certification","name":"Aviation Training & Certification","category_id":"aviation_services"},
    {"id":"aviation_safety_compliance","name":"Aviation Safety & Compliance","category_id":"aviation_safety"},
)

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

def list_categories():
    return [dict(item) for item in CATEGORIES]

def get_category(category_id):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None

def list_business_domains():
    return [dict(item) for item in BUSINESS_DOMAINS]

def get_business_domain(domain_id):
    for item in BUSINESS_DOMAINS:
        if item["id"] == domain_id:
            return dict(item)
    return None
