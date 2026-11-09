"""API-facing catalog for server service categories."""
from backend.server.global_ecosystem.global_server_ecosystem import list_service_types

def list_entries():
    return [
        {
            "name": item["name"],
            "description": item.get("category", ""),
            "status": item.get("status", "catalog_only"),
            "service_type_id": item["service_type_id"],
            "capabilities": list(item.get("capabilities", [])),
        }
        for item in list_service_types()
    ]
