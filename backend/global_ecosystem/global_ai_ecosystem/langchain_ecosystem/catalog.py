"""Catalog metadata for LangChain; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "langchain",
    "name": "LangChain",
    "vendor": "LangChain",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["LLM application framework","Tool and retrieval integrations"],
    "integration_status": "catalog_only",
    "notes": "Application and agent framework; it orchestrates model providers rather than replacing them.",
}
