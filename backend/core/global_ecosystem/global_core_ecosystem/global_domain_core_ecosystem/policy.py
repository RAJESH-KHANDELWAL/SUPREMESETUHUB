"""Domain Core policy boundaries."""
CORE_POLICY = {"api_transport_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY","live_connection_claim_requires_smoke_test":True,"write_actions_require_explicit_authorization":True,"tenant_context_required_for_tenant_data":True,"provider_catalog_is_not_live_integration":True}
def get_policy(): return dict(CORE_POLICY)
