CATEGORIES = (
    {"id": "procurement", "name": "Procurement", "subcategories": ["sourcing", "purchasing", "supplier_management"]},
    {"id": "warehousing", "name": "Warehousing", "subcategories": ["storage", "cold_storage", "bonded_warehousing"]},
    {"id": "inventory", "name": "Inventory Management", "subcategories": ["stock_control", "forecasting", "cycle_counting"]},
    {"id": "distribution", "name": "Distribution", "subcategories": ["regional_distribution", "last_mile", "fulfilment"]},
    {"id": "freight", "name": "Freight Forwarding", "subcategories": ["air_freight", "ocean_freight", "road_freight"]},
    {"id": "logistics", "name": "Logistics Services", "subcategories": ["third_party_logistics", "reverse_logistics", "contract_logistics"]},
    {"id": "cold_chain", "name": "Cold Chain", "subcategories": ["food_cold_chain", "pharma_cold_chain", "temperature_monitoring"]},
    {"id": "packaging", "name": "Packaging", "subcategories": ["industrial_packaging", "protective_packaging", "pallets"]},
    {"id": "customs", "name": "Customs & Trade Compliance", "subcategories": ["customs_brokerage", "import_export_docs", "trade_compliance"]},
    {"id": "supply_technology", "name": "Supply Chain Technology", "subcategories": ["warehouse_software", "transport_software", "analytics"]},
    {"id": "supply_strategy", "name": "Supply Chain Strategy", "subcategories": ["network_design", "demand_planning", "resilience"]},
    {"id": "returns", "name": "Returns & Circular Logistics", "subcategories": ["returns_management", "repair", "recycling_logistics"]},
)
def list_categories():
    return [dict(item) for item in CATEGORIES]
def get_category(category_id):
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item)
    return None
