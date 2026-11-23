"""Security and layer-ownership policy for transport business Core."""
CORE_POLICY = {"catalogue_only_by_default": True, "provider_api_calls_in_core": False, "dispatch_or_fulfilment_execution_in_core": False, "booking_or_payment_execution_in_core": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY", "live_connection_requires_smoke_test": True}
