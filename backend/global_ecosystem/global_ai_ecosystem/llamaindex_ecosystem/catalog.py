"""Catalog metadata for LlamaIndex; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "llamaindex",
    "name": "LlamaIndex",
    "vendor": "LlamaIndex",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Data framework","Retrieval-augmented generation","Agent workflows"],
    "integration_status": "catalog_only",
    "notes": "Data and context framework; model and storage backends are separately configured.",
}
