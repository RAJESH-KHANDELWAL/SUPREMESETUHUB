"""Taxonomy catalog for Automotive & Mobility."""
CATEGORIES=(
    {"id": "passenger_vehicles", "name": "Passenger Vehicles", "subcategories": ["cars","suvs","vans","used_cars"]},
    {"id": "commercial_vehicles", "name": "Commercial Vehicles", "subcategories": ["trucks","buses","light_commercial_vehicles"]},
    {"id": "two_three_wheelers", "name": "Two & Three Wheelers", "subcategories": ["motorcycles","scooters","electric_two_wheelers"]},
    {"id": "electric_mobility", "name": "Electric Mobility", "subcategories": ["electric_cars","electric_buses","charging_networks","battery_swapping"]},
    {"id": "automotive_manufacturing", "name": "Automotive Manufacturing", "subcategories": ["vehicle_assembly","components","powertrain","electronics"]},
    {"id": "auto_retail_dealerships", "name": "Auto Retail & Dealerships", "subcategories": ["new_vehicle_dealers","used_vehicle_dealers","vehicle_marketplaces"]},
    {"id": "maintenance_repair", "name": "Maintenance & Repair", "subcategories": ["vehicle_servicing","body_repair","diagnostics","roadside_assistance"]},
    {"id": "automotive_parts", "name": "Automotive Parts & Accessories", "subcategories": ["spare_parts","tyres","batteries","accessories"]},
    {"id": "vehicle_rental_leasing", "name": "Vehicle Rental & Leasing", "subcategories": ["car_rental","self_drive","leasing","subscription_fleets"]},
    {"id": "mobility_services", "name": "Mobility Services", "subcategories": ["ride_hailing","carpooling","micro_mobility","shared_mobility"]},
    {"id": "automotive_technology", "name": "Automotive Technology", "subcategories": ["telematics","autonomous_systems","connected_vehicles","fleet_software"]},
    {"id": "vehicle_inspection_compliance", "name": "Vehicle Inspection & Compliance", "subcategories": ["vehicle_testing","emissions_testing","roadworthiness","registration_support"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
