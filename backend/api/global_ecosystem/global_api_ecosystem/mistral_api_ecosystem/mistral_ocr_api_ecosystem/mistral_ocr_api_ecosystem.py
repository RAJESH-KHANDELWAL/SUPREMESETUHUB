"""OCR family metadata; operation-level calls require separate implementation and tests."""
SERVICE_FAMILY = {
    "provider_id": "mistral",
    "provider_name": "MISTRAL AI",
    "family_id": "OCR",
    "family_name": "OCR",
    "api_area": "POST /v1/ocr",
    "purpose": "Extract text and structured content from supported documents and images.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "implementation_status": "CATALOG_AND_SETUP_SCAFFOLD",
    "family_live_connection_verified": False,
}
