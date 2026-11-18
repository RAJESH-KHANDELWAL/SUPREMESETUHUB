"""Machine-readable catalog entry for xAI Grok."""

PROVIDER = {
    "id": "xai_grok",
    "name": "xAI Grok",
    "vendor": "xAI",
    "category": "ai_provider",
    "api_endpoint": "https://api.x.ai/v1",
    "credential_env": "XAI_API_KEY",
    "models_or_services": ["Grok API","Chat completions","Tool calling"],
    "integration_status": "scaffold",
    "notes": "Hosted Grok model API; model availability depends on xAI account and current API catalog.",
}
