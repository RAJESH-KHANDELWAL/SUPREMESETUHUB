"""Machine-readable catalog entry for Microsoft Azure AI."""

PROVIDER = {
    "id": "microsoft_azure_ai",
    "name": "Microsoft Azure AI",
    "vendor": "Microsoft",
    "category": "ai_provider",
    "api_endpoint": None,
    "credential_env": "AZURE_OPENAI_API_KEY",
    "models_or_services": ["azure-openai-deployment","azure-ai-model-deployment"],
    "integration_status": "scaffold",
    "notes": "Azure OpenAI adapter requires AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY and AZURE_OPENAI_DEPLOYMENT; resource endpoints are deployment-specific.",
}
