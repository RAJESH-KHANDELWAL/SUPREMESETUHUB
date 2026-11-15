"""Machine-readable catalog entry for Cerebras."""

PROVIDER = {
    "id": "cerebras",
    "name": "Cerebras",
    "vendor": "Cerebras",
    "category": "inference_provider",
    "api_endpoint": "https://api.cerebras.ai/v1",
    "credential_env": "CEREBRAS_API_KEY",
    "models_or_services": ["Cloud inference API"],
    "integration_status": "scaffold",
    "notes": "Hosted inference platform; check current model catalog and limits.",
}
