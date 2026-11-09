"""FIM Completions family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "FIM_COMPLETIONS",
    "family_name": "FIM Completions",
    "api_area": "POST /v1/fim/completions",
    "purpose": "Fill-in-the-middle completions for code and text.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
