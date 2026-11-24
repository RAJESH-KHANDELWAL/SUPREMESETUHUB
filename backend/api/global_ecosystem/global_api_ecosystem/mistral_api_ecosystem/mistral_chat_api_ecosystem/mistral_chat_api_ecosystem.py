"""Chat Completions family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "CHAT",
    "family_name": "Chat Completions",
    "api_area": "POST /v1/chat/completions",
    "purpose": "Conversational and text-generation requests.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
