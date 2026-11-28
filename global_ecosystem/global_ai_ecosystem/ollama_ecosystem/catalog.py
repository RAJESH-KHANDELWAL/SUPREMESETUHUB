"""Machine-readable catalog entry for Ollama."""

PROVIDER = {
    "id": "ollama",
    "name": "Ollama",
    "vendor": "Ollama",
    "category": "local_model_runtime",
    "api_endpoint": "http://localhost:11434",
    "credential_env": "OLLAMA_HOST",
    "models_or_services": ["Local model runtime","Local model API"],
    "integration_status": "scaffold",
    "notes": "Local model runtime; normally uses a local host endpoint and does not require a cloud API key.",
}
