"""Security and layer-ownership policy; no transport operations execute in Core."""
CORE_POLICY = {"catalogue_only_by_default": True, "provider_api_calls_in_core": False, "route_execution_in_core": False, "booking_dispatch_in_core": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY", "live_connection_requires_smoke_test": True}
