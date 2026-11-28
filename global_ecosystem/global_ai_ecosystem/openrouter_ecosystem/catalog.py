"""Machine-readable catalog entry for OpenRouter."""

PROVIDER = {
    "id": "openrouter",
    "name": "OpenRouter",
    "vendor": "OpenRouter",
    "category": "model_router",
    "api_endpoint": "https://openrouter.ai/api/v1",
    "credential_env": "OPENROUTER_API_KEY",
    "models_or_services": ["Unified model routing","Provider fallback","Usage routing"],
    "integration_status": "scaffold",
    "notes": "Model gateway/router, not a foundation-model developer.",
}
