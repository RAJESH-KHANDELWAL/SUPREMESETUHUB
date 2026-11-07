"""Batch family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "BATCH",
    "family_name": "Batch",
    "api_area": "/v1/batch",
    "purpose": "Submit and inspect asynchronous batch processing jobs.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
