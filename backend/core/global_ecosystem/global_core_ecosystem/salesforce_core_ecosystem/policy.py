"""Core architectural boundaries and governance policy."""
CORE_POLICY={"catalog_only":True,"api_transport_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY","live_connection_claims_require_smoke_test":True,"tenant_identity_required_for_user_connections":True,"secret_values_must_not_be_returned":True}
def policy_snapshot(): return dict(CORE_POLICY)
