"""Curated Oracle product inventory; presence is not connectivity."""
from copy import deepcopy

_ROWS = [
("oracle-ai-services","Oracle AI Services","AI services and managed AI capabilities","AI_AND_MACHINE_LEARNING"),
("oracle-autonomous-database","Oracle Autonomous Database","Autonomous relational database capabilities","DATABASES"),
("oracle-base-database","Oracle Base Database","Base database services and deployment metadata","DATABASES"),
("oracle-block-volumes","Oracle Block Volumes","Block storage and attachment capabilities","STORAGE"),
("oracle-compute","Oracle Compute","Compute service and shape metadata","COMPUTE"),
("oracle-compute-instances","Oracle Compute Instances","Virtual machine lifecycle metadata","COMPUTE"),
("oracle-data-science","Oracle Data Science","Data science projects, models and workspaces","AI_AND_MACHINE_LEARNING"),
("oracle-database-tools","Oracle Database Tools","Database development and administration tools","DATABASES"),
("oracle-enterprise-applications","Oracle Enterprise Applications","Enterprise application service families","ENTERPRISE_APPLICATIONS"),
("oracle-fusion-cloud-applications","Oracle Fusion Cloud Applications","Fusion business application suites","ENTERPRISE_APPLICATIONS"),
("oracle-generative-ai","Oracle Generative AI","Generative AI model service metadata","AI_AND_MACHINE_LEARNING"),
("oracle-identity","Oracle Identity","Identity, access and federation capabilities","IDENTITY_SECURITY"),
("oracle-mysql-heatwave","MySQL HeatWave","MySQL database and analytics capabilities","DATABASES"),
("oracle-networking","Oracle Networking","Connectivity, routing and network metadata","NETWORKING"),
("oracle-object-storage","Oracle Object Storage","Object storage and lifecycle capabilities","STORAGE"),
("oracle-observability","Oracle Observability","Monitoring, logging and tracing metadata","OBSERVABILITY"),
("oracle-virtual-cloud-networks","Oracle Virtual Cloud Networks","VCN, subnet, gateway and security metadata","NETWORKING"),
]

def list_products(*, enabled_only: bool = False) -> list[dict]:
    items = [{
        "product_id": pid, "name": name, "purpose": purpose, "domain_id": domain,
        "provider_id": "oracle", "status": "CATALOG_ONLY", "enabled": True,
        "live_connection_verified": False, "api_calls_performed": 0,
    } for pid, name, purpose, domain in _ROWS]
    if enabled_only:
        items = [item for item in items if item["enabled"]]
    return deepcopy(items)

def get_product(product_id: str) -> dict | None:
    return next((item for item in list_products() if item["product_id"] == product_id), None)
