"""Catalog metadata for FLUX Model Family; this is a model-family record, not an API integration."""

PROVIDER = {
    "id": "flux_models",
    "name": "FLUX Model Family",
    "vendor": "Black Forest Labs",
    "category": "model_family",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["FLUX image models","Image generation variants"],
    "integration_status": "catalog_only",
    "notes": "Model family; distinguish model weights, hosted API products and their separate licences.",
}
