"""Catalog metadata for Microsoft Phi Model Family; this is a model-family record, not an API integration."""

PROVIDER = {
    "id": "phi_models",
    "name": "Microsoft Phi Model Family",
    "vendor": "Microsoft",
    "category": "open_model_family",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Phi model weights","Small language models"],
    "integration_status": "catalog_only",
    "notes": "Model family; hosting and inference depend on the selected runtime or cloud provider.",
}
