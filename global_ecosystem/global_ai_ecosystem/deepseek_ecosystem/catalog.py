"""Machine-readable catalog entry for DeepSeek."""
PROVIDER = {
    "id": "deepseek",
    "name": "DeepSeek",
    "vendor": "DeepSeek",
    "category": "ai_provider",
    "api_endpoint": "https://api.deepseek.com",
    "credential_env": "DEEPSEEK_API_KEY",
    "models_or_services": ["deepseek-chat","deepseek-reasoner"],
    "integration_status": "scaffold",
    "notes": "DeepSeek API adapter boundary.",
}
