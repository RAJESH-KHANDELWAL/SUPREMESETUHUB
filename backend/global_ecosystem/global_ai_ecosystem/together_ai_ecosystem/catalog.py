"""Machine-readable catalog entry for Together AI."""

PROVIDER = {
    "id": "together_ai",
    "name": "Together AI",
    "vendor": "Together AI",
    "category": "inference_provider",
    "api_endpoint": "https://api.together.xyz/v1",
    "credential_env": "TOGETHER_API_KEY",
    "models_or_services": ["Serverless inference","Dedicated inference"],
    "integration_status": "scaffold",
    "notes": "Hosted inference platform for supported open models.",
}
