"""Technology, IT & Telecommunications taxonomy."""
from __future__ import annotations
CATEGORIES = [
{"id":"software_development","name":"Software Development","subcategories":["web_development","mobile_app_development","enterprise_software","custom_software"]},
{"id":"cloud_and_infrastructure","name":"Cloud & Infrastructure","subcategories":["cloud_hosting","cloud_migration","data_centres","infrastructure_management"]},
{"id":"artificial_intelligence","name":"Artificial Intelligence & Machine Learning","subcategories":["machine_learning","generative_ai","computer_vision","natural_language_processing"]},
{"id":"cybersecurity","name":"Cybersecurity & Information Security","subcategories":["security_audits","penetration_testing","managed_security","identity_access_management"]},
{"id":"telecommunications","name":"Telecommunications & Connectivity","subcategories":["internet_service_providers","mobile_networks","fibre_connectivity","satellite_communications"]},
{"id":"networking_and_iot","name":"Networking & Internet of Things","subcategories":["network_equipment","iot_platforms","industrial_iot","connected_devices"]},
{"id":"data_and_analytics","name":"Data Engineering & Analytics","subcategories":["data_warehousing","business_intelligence","data_science","data_governance"]},
{"id":"hardware_and_electronics","name":"Hardware & Electronics","subcategories":["computer_hardware","semiconductors","embedded_systems","electronics_manufacturing"]},
{"id":"it_consulting_and_managed_services","name":"IT Consulting & Managed Services","subcategories":["it_strategy","managed_it_services","systems_integration","technical_support"]},
{"id":"saas_and_platforms","name":"SaaS & Digital Platforms","subcategories":["business_saas","developer_platforms","api_services","workflow_automation"]},
{"id":"digital_identity_and_trust","name":"Digital Identity & Trust Services","subcategories":["digital_identity","electronic_signatures","certificate_services","access_management"]},
{"id":"telecom_equipment_and_services","name":"Telecom Equipment & Services","subcategories":["telecom_infrastructure","tower_services","network_maintenance","telecom_billing"]}]
def list_categories():
    return [dict(x, subcategories=list(x["subcategories"])) for x in CATEGORIES]
def get_category(category_id: str):
    for x in CATEGORIES:
        if x["id"] == category_id: return dict(x, subcategories=list(x["subcategories"]))
    return None
