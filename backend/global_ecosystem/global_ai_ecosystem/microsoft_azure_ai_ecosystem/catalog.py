"""Machine-readable catalog entry for Microsoft Azure AI."""

PROVIDER = {
    "id": "microsoft_azure_ai",
    "name": "Microsoft Azure AI",
    "vendor": "Microsoft",
    "category": "ai_provider",
    "api_endpoint": None,
    "credential_env": "AZURE_AI_ENDPOINT",
    "models_or_services": ["azure-openai-deployment","azure-ai-model-deployment"],
    "integration_status": "scaffold",
    "notes": "Azure endpoints and deployments are resource-specific.",
}
