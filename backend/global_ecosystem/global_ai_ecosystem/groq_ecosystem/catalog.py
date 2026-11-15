"""Machine-readable catalog entry for Groq."""

PROVIDER = {
    "id": "groq",
    "name": "Groq",
    "vendor": "Groq",
    "category": "inference_provider",
    "api_endpoint": "https://api.groq.com/openai/v1",
    "credential_env": "GROQ_API_KEY",
    "models_or_services": ["Hosted inference","OpenAI-compatible chat API"],
    "integration_status": "scaffold",
    "notes": "Inference platform; hosted models and identifiers are account/catalog dependent.",
}
