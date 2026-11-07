"""Fine-tuning family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "FINE_TUNING",
    "family_name": "Fine-tuning",
    "api_area": "/v1/fine_tuning",
    "purpose": "Manage supported fine-tuning jobs and related resources.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
