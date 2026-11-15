"""Machine-readable catalog entry for Fireworks AI."""

PROVIDER = {
    "id": "fireworks_ai",
    "name": "Fireworks AI",
    "vendor": "Fireworks AI",
    "category": "inference_provider",
    "api_endpoint": "https://api.fireworks.ai/inference/v1",
    "credential_env": "FIREWORKS_API_KEY",
    "models_or_services": ["Model inference","Fine-tuning services"],
    "integration_status": "scaffold",
    "notes": "Hosted inference platform; endpoints and model IDs are account/catalog dependent.",
}
