"""Machine-readable catalog entry for OpenAI's API ecosystem."""

PROVIDER = {
    "id": "openai_chatgpt",
    "name": "OpenAI / ChatGPT ecosystem",
    "vendor": "OpenAI",
    "category": "ai_provider",
    "api_endpoint": "https://api.openai.com/v1",
    "credential_env": "OPENAI_API_KEY",
    "models_or_services": [
        "Responses API", "Chat Completions API", "Embeddings API",
        "Images API", "Audio API", "Realtime API", "Moderation API",
    ],
    "integration_status": "scaffold",
    "notes": "This package targets OpenAI developer APIs. A ChatGPT consumer subscription does not itself provide API credentials or API billing.",
}
