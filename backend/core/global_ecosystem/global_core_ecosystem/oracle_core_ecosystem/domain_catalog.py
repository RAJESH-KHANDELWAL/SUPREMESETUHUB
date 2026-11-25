"""Oracle capability domains derived from product ownership."""
from .product_catalog import list_products

_DOMAIN_NAMES = {
"AI_AND_MACHINE_LEARNING": "AI and machine learning",
"DATABASES": "Databases and data platforms",
"STORAGE": "Storage and backup",
"COMPUTE": "Compute and infrastructure",
"ENTERPRISE_APPLICATIONS": "Enterprise applications",
"IDENTITY_SECURITY": "Identity, security and governance",
"NETWORKING": "Networking and edge",
"OBSERVABILITY": "Observability and operations",
}

def list_domains() -> list[dict]:
    products = list_products()
    result = []
    for domain_id, name in _DOMAIN_NAMES.items():
        ids = [p["product_id"] for p in products if p["domain_id"] == domain_id]
        result.append({"domain_id": domain_id, "name": name, "product_ids": ids, "product_count": len(ids)})
    return result
