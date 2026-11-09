"""Catalog for Telecommunications, Internet & Digital Infrastructure."""
CATEGORIES=(
    {"id": "telecom_networks", "name": "Telecommunications Networks", "subcategories": ["mobile_networks","fixed_line_networks","5g_networks","network_infrastructure"]},
    {"id": "internet_services", "name": "Internet Services", "subcategories": ["broadband","fiber_internet","wireless_internet","internet_service_providers"]},
    {"id": "data_centres", "name": "Data Centres & Hosting", "subcategories": ["colocation","hyperscale_data_centres","web_hosting","edge_data_centres"]},
    {"id": "cloud_infrastructure", "name": "Cloud Infrastructure", "subcategories": ["cloud_platforms","infrastructure_as_a_service","platform_services","cloud_operations"]},
    {"id": "connectivity_iot", "name": "Connectivity & IoT", "subcategories": ["internet_of_things","machine_to_machine","private_networks","iot_connectivity"]},
    {"id": "submarine_satellite", "name": "Submarine & Satellite Connectivity", "subcategories": ["submarine_cables","satellite_internet","ground_stations","backhaul_networks"]},
    {"id": "network_equipment", "name": "Telecom Equipment", "subcategories": ["routers_switches","radio_access_equipment","optical_fiber_equipment","network_hardware"]},
    {"id": "digital_identity", "name": "Digital Identity & Trust", "subcategories": ["digital_certificates","identity_verification","trust_services","authentication"]},
    {"id": "cyber_infrastructure", "name": "Digital Infrastructure Security", "subcategories": ["network_security","ddos_protection","telecom_security","infrastructure_resilience"]},
    {"id": "managed_connectivity", "name": "Managed Connectivity Services", "subcategories": ["managed_networks","sd_wan","network_operations","connectivity_support"]},
    {"id": "digital_public_infrastructure", "name": "Digital Public Infrastructure", "subcategories": ["digital_payment_rails","identity_rails","data_exchange","public_digital_platforms"]},
    {"id": "internet_exchange", "name": "Internet Exchange & Peering", "subcategories": ["internet_exchange_points","ip_transit","peering_services","content_delivery_networks"]},
)
def list_categories(): return [dict(x) for x in CATEGORIES]
def get_category(category_id):
 for item in CATEGORIES:
  if item["id"]==category_id: return dict(item)
 return None
