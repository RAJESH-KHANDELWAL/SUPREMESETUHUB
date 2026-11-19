"""Catalog metadata for Microsoft AutoGen; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "autogen",
    "name": "Microsoft AutoGen",
    "vendor": "Microsoft",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Multi-agent conversation","Agent application framework"],
    "integration_status": "catalog_only",
    "notes": "Agent framework; check current project package and API version before implementation.",
}
