"""India and global automotive, vehicle and mobility taxonomy."""

CATEGORIES = (
    {"id":"passenger_vehicles","name":"Passenger Cars & SUVs","subcategories":["hatchbacks","sedans","suvs","muvs_mpvs","vans","used_passenger_vehicles"]},
    {"id":"commercial_vehicles","name":"Commercial Vehicles","subcategories":["light_commercial_vehicles","heavy_trucks","buses_and_coaches","special_purpose_vehicles","used_commercial_vehicles"]},
    {"id":"two_three_wheelers","name":"Two-Wheelers & Three-Wheelers","subcategories":["motorcycles","scooters","electric_two_wheelers","auto_rickshaws","electric_three_wheelers"]},
    {"id":"electric_mobility","name":"Electric Vehicles & EV Mobility","subcategories":["electric_cars","electric_commercial_vehicles","electric_buses","electric_two_three_wheelers","hybrid_vehicles"]},
    {"id":"automotive_parts","name":"Auto Parts & Components","subcategories":["engine_components","transmission_components","braking_and_suspension","electrical_electronic_components","spare_parts_wholesale"]},
    {"id":"automotive_manufacturing","name":"Automotive Manufacturing","subcategories":["vehicle_assembly","component_manufacturing","powertrain_manufacturing","automotive_electronics_manufacturing","contract_manufacturing"]},
    {"id":"auto_retail_dealerships","name":"Vehicle Dealerships & Showrooms","subcategories":["new_vehicle_dealers","used_vehicle_dealers","multi_brand_showrooms","vehicle_marketplaces","commercial_vehicle_dealers"]},
    {"id":"vehicle_rental_leasing","name":"Vehicle Rental & Leasing","subcategories":["self_drive_car_rental","chauffeur_driven_rental","two_wheeler_rental","commercial_vehicle_leasing","vehicle_subscription"]},
    {"id":"maintenance_repair","name":"Vehicle Repair & Maintenance","subcategories":["periodic_vehicle_servicing","engine_and_transmission_repair","body_and_collision_repair","vehicle_diagnostics","tyre_and_wheel_services"]},
    {"id":"vehicle_inspection_compliance","name":"Vehicle Inspection & Testing","subcategories":["roadworthiness_inspection","emissions_testing","vehicle_safety_testing","pre_purchase_inspection","vehicle_registration_support"]},
    {"id":"automotive_accessories_customisation","name":"Automotive Accessories & Customisation","subcategories":["interior_accessories","exterior_accessories","infotainment_and_audio","vehicle_wraps_and_paint","approved_vehicle_modifications"]},
    {"id":"fleet_management","name":"Vehicle Fleet Management","subcategories":["fleet_asset_management","vehicle_maintenance_planning","vehicle_telematics","driver_and_vehicle_safety","fleet_utilisation_analytics"]},
    {"id":"vehicle_finance_insurance","name":"Vehicle Finance & Insurance","subcategories":["vehicle_loans","vehicle_leasing_finance","motor_insurance","commercial_fleet_insurance","vehicle_warranty_products"]},
    {"id":"charging_battery_services","name":"EV Charging & Battery Services","subcategories":["public_ev_charging","private_charging_installation","battery_swapping","battery_diagnostics","battery_reuse_and_second_life"]},
    {"id":"vehicle_recycling_scrapping","name":"Vehicle Scrapping & Recycling","subcategories":["end_of_life_vehicle_collection","authorised_vehicle_scrapping","automotive_material_recycling","used_parts_recovery","ev_battery_recycling"]},
    {"id":"automotive_technology","name":"Automotive Technology & Software","subcategories":["connected_vehicle_platforms","adas_and_safety_technology","autonomous_vehicle_systems","automotive_software","vehicle_data_and_diagnostics"]},
    {"id":"public_private_mobility","name":"Public & Private Passenger Mobility","subcategories":["ride_hailing_and_taxi","carpooling_and_shared_cars","employee_transport_vehicles","school_transport_vehicles","micro_mobility_services"]},
    {"id":"roadside_assistance","name":"Roadside Assistance & Breakdown Services","subcategories":["vehicle_breakdown_recovery","on_road_repairs","emergency_towing","flat_tyre_assistance","battery_jump_start_services"]},
)

def list_categories():
    return [{**item, "subcategories": list(item["subcategories"])} for item in CATEGORIES]

def get_category(category_id):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return {**item, "subcategories": list(item["subcategories"])}
    return None
