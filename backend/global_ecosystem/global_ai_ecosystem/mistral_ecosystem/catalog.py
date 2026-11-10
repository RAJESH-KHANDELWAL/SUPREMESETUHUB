"""Machine-readable catalog entry for Mistral AI."""
PROVIDER = {
    "id": "mistral",
    "name": "Mistral AI",
    "vendor": "Mistral AI",
    "category": "ai_provider",
    "api_endpoint": "https://api.mistral.ai/v1",
    "credential_env": "MISTRAL_API_KEY",
    "models_or_services": ["mistral-large","codestral"],
    "integration_status": "scaffold",
    "notes": "Mistral API adapter boundary.",
}
