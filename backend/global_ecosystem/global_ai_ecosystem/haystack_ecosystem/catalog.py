"""Catalog metadata for Haystack; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "haystack",
    "name": "Haystack",
    "vendor": "deepset",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["RAG pipelines","Search and document processing"],
    "integration_status": "catalog_only",
    "notes": "Pipeline and retrieval framework; not a model provider.",
}
