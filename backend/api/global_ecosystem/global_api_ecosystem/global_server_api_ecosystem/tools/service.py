"""API-facing catalog for SERVER ecosystem tools."""
TOOLS = (
    {"tool_id":"server_inventory","name":"Server Inventory","status":"available","purpose":"Read locally registered server metadata"},
    {"tool_id":"provider_catalog","name":"Provider Catalog","status":"available","purpose":"Discover server provider metadata"},
    {"tool_id":"server_health_metadata","name":"Server Health Metadata","status":"catalog_only","purpose":"Expose health fields when a configured adapter reports them"},
    {"tool_id":"server_lifecycle_metadata","name":"Server Lifecycle Metadata","status":"available","purpose":"Read and update local inventory lifecycle flags"},
)

def list_entries():
    return [dict(item) for item in TOOLS]
