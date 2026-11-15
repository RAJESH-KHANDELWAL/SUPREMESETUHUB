"""Machine-readable catalog entry for Meta AI."""

PROVIDER = {
    "id": "meta_ai",
    "name": "Meta AI",
    "vendor": "Meta",
    "category": "ai_provider",
    "api_endpoint": None,
    "credential_env": "META_AI_ACCESS_TOKEN",
    "models_or_services": ["llama"],
    "integration_status": "scaffold",
    "notes": "Use an explicitly configured authorized hosting provider for Llama inference; Meta AI consumer app is not a public general API.",
}
