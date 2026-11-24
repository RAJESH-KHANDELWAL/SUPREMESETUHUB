"""Transport, logistics and supply chain taxonomy."""
CATEGORIES = [
  {
    "id": "road_transport",
    "name": "Road Transport & Trucking",
    "subcategories": [
      "full_truckload",
      "less_than_truckload",
      "fleet_operators",
      "last_mile_road_delivery"
    ]
  },
  {
    "id": "rail_and_freight",
    "name": "Rail & Freight Services",
    "subcategories": [
      "rail_freight",
      "container_rail",
      "intermodal_services",
      "freight_terminals"
    ]
  },
  {
    "id": "air_cargo",
    "name": "Air Cargo & Aviation Logistics",
    "subcategories": [
      "air_freight",
      "cargo_handling",
      "charter_cargo",
      "express_air_services"
    ]
  },
  {
    "id": "ocean_and_shipping",
    "name": "Ocean Freight & Shipping",
    "subcategories": [
      "container_shipping",
      "bulk_shipping",
      "freight_forwarding",
      "port_services"
    ]
  },
  {
    "id": "warehousing_and_fulfilment",
    "name": "Warehousing & Fulfilment",
    "subcategories": [
      "distribution_centres",
      "cold_chain_warehousing",
      "inventory_handling",
      "order_fulfilment"
    ]
  },
  {
    "id": "courier_and_parcel",
    "name": "Courier, Express & Parcel",
    "subcategories": [
      "domestic_courier",
      "international_parcel",
      "same_day_delivery",
      "document_delivery"
    ]
  },
  {
    "id": "supply_chain_management",
    "name": "Supply Chain Management",
    "subcategories": [
      "supply_chain_consulting",
      "demand_planning",
      "procurement_operations",
      "control_tower_services"
    ]
  },
  {
    "id": "customs_and_trade",
    "name": "Customs, Trade & Border Services",
    "subcategories": [
      "customs_brokerage",
      "trade_documentation",
      "duties_and_tariffs_support",
      "border_compliance"
    ]
  },
  {
    "id": "fleet_and_vehicle_services",
    "name": "Fleet & Vehicle Services",
    "subcategories": [
      "fleet_leasing",
      "fleet_maintenance",
      "telematics",
      "driver_management"
    ]
  },
  {
    "id": "cold_chain_and_perishables",
    "name": "Cold Chain & Perishable Logistics",
    "subcategories": [
      "refrigerated_transport",
      "pharma_logistics",
      "fresh_food_logistics",
      "temperature_monitoring"
    ]
  },
  {
    "id": "moving_and_relocation",
    "name": "Moving, Packing & Relocation",
    "subcategories": [
      "household_moving",
      "office_relocation",
      "industrial_moving",
      "packing_services"
    ]
  },
  {
    "id": "mobility_and_passenger",
    "name": "Passenger Mobility & Transit",
    "subcategories": [
      "public_transport",
      "ride_hailing",
      "employee_transport",
      "school_transport"
    ]
  }
]
def list_categories(): return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
