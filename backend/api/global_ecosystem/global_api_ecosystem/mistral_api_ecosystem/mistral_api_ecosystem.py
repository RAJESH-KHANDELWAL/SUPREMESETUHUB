"""Central Mistral AI provider API ecosystem metadata."""
SERVICE_FAMILIES = ["CHAT", "MODELS", "EMBEDDINGS", "AGENTS", "OCR", "FINE_TUNING", "BATCH", "FIM_COMPLETIONS", "AUDIO"]
PROVIDER_API_ECOSYSTEM = {
    "provider_id": "mistral",
    "name": "MISTRAL AI API ECOSYSTEM",
    "vendor": "Mistral AI",
    "families": ["AI", "DEVELOPER"],
    "service_families": SERVICE_FAMILIES,
    "service_family_count": len(SERVICE_FAMILIES),
    "scope": "Mistral inference, model discovery, embeddings, agents, OCR, fine-tuning, batch, FIM completions and supported audio APIs.",
    "adapter_path": "backend/integrations/providers/mistral.py",
    "setup_guide": "backend/api/global_ecosystem/global_api_ecosystem/mistral_api_ecosystem/README.md",
    "required_configuration": ["MISTRAL_API_KEY"],
    "implementation_status": "LIVE_MODELS_ENDPOINT_VERIFICATION_IMPLEMENTED",
    "live_connection_verified": False,
}
