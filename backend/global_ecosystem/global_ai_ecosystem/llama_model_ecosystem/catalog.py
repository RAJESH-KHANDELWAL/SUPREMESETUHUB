"""Catalog metadata for Meta Llama Model Family; this is a model-family record, not an API integration."""

PROVIDER = {
    "id": "llama_models",
    "name": "Meta Llama Model Family",
    "vendor": "Meta",
    "category": "open_model_family",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Llama model weights","Text and multimodal model variants"],
    "integration_status": "catalog_only",
    "notes": "Model family, not a separate hosted API provider; licensing and acceptable-use terms vary by release.",
}
