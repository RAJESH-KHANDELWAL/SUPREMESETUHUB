"""API-safe catalog for configured server integration adapters."""
INTEGRATIONS = (
    {"integration_id":"server_inventory_to_core","name":"SERVER API to CORE contracts","status":"implemented","direction":"API_TO_CORE","purpose":"Validate provider-neutral server identities"},
    {"integration_id":"server_api_to_engine","name":"SERVER API to ENGINE execution","status":"boundary_defined","direction":"API_TO_ENGINE","purpose":"Request authorized provider operations through engine adapters"},
    {"integration_id":"server_to_database","name":"SERVER inventory to DATABASE","status":"boundary_defined","direction":"SERVER_TO_DATABASE","purpose":"Persist inventory records through DATABASE-owned repositories"},
    {"integration_id":"server_to_storage","name":"SERVER artifacts to STORAGE","status":"boundary_defined","direction":"SERVER_TO_STORAGE","purpose":"Store backups and artifacts through STORAGE-owned adapters"},
)

def list_entries():
    return [dict(item) for item in INTEGRATIONS]
