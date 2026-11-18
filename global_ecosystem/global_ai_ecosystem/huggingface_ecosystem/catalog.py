"""Machine-readable catalog entry for Hugging Face."""
PROVIDER = {
    "id": "huggingface", "name": "Hugging Face", "vendor": "Hugging Face",
    "category": "ai_provider", "api_endpoint": "https://router.huggingface.co",
    "credential_env": "HF_TOKEN", "models_or_services": ["hosted-models", "inference-endpoints"],
    "integration_status": "scaffold",
    "notes": "Hosted inference and dedicated endpoints; availability depends on provider and model licence.",
}
