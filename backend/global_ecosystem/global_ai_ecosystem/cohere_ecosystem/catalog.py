"""Machine-readable catalog entry for Cohere."""
PROVIDER = {
    "id": "cohere",
    "name": "Cohere",
    "vendor": "Cohere",
    "category": "ai_provider",
    "api_endpoint": "https://api.cohere.com",
    "credential_env": "COHERE_API_KEY",
    "models_or_services": ["command","embed"],
    "integration_status": "scaffold",
    "notes": "Cohere generation and embedding adapter boundary.",
}
