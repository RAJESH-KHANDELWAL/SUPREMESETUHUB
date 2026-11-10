"""Machine-readable catalog entry for OpenAI ChatGPT."""

PROVIDER = {
    "id": "openai_chatgpt",
    "name": "OpenAI ChatGPT",
    "vendor": "OpenAI",
    "category": "ai_provider",
    "api_endpoint": "https://api.openai.com/v1",
    "credential_env": "OPENAI_API_KEY",
    "models_or_services": ["gpt-6","gpt-5.6","gpt-5.5"],
    "integration_status": "scaffold",
    "notes": "OpenAI API adapter boundary; ChatGPT consumer product access is not the same as API access.",
}
