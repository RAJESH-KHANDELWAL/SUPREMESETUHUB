"""Machine-readable catalog entry for LiteLLM."""

PROVIDER = {
    "id": "litellm",
    "name": "LiteLLM",
    "vendor": "BerriAI",
    "category": "model_router",
    "api_endpoint": "http://localhost:4000",
    "credential_env": "LITELLM_MASTER_KEY",
    "models_or_services": ["Unified model gateway","Routing","Budgets and rate limits"],
    "integration_status": "scaffold",
    "notes": "Model gateway and routing layer; not a foundation-model provider.",
}
