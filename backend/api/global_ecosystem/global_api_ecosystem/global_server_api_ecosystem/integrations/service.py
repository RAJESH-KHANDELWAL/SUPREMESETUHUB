"""Cross-layer integration catalog for GLOBAL SERVER API."""
INTEGRATIONS = (
    {"integration_id":"server_api_to_core","name":"SERVER API to CORE contracts","status":"implemented","direction":"API_TO_CORE","purpose":"Validate provider-neutral server identity payloads"},
    {"integration_id":"server_api_to_engine","name":"SERVER API to ENGINE execution","status":"boundary_defined","direction":"API_TO_ENGINE","purpose":"Invoke explicitly configured provider adapters through ENGINE"},
    {"integration_id":"server_to_database","name":"SERVER inventory to DATABASE","status":"boundary_defined","direction":"SERVER_TO_DATABASE","purpose":"Persist server inventory through DATABASE-owned repositories"},
    {"integration_id":"server_to_storage","name":"SERVER artifacts to STORAGE","status":"boundary_defined","direction":"SERVER_TO_STORAGE","purpose":"Store backup and artifact metadata through STORAGE-owned adapters"},
)

def list_entries():
    return [dict(item) for item in INTEGRATIONS]
