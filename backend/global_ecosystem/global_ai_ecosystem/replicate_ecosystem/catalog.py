"""Machine-readable catalog entry for Replicate."""

PROVIDER = {
    "id": "replicate",
    "name": "Replicate",
    "vendor": "Replicate",
    "category": "model_platform",
    "api_endpoint": "https://api.replicate.com/v1",
    "credential_env": "REPLICATE_API_TOKEN",
    "models_or_services": ["Hosted model predictions", "Model deployments"],
    "integration_status": "scaffold",
    "notes": "Model hosting and execution platform; not a single model provider.",
}
