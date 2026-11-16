"""Embeddings family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "EMBEDDINGS",
    "family_name": "Embeddings",
    "api_area": "POST /v1/embeddings",
    "purpose": "Generate text embeddings using an enabled embedding model.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
