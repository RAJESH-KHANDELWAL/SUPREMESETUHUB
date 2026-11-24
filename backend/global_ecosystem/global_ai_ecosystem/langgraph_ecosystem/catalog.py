"""Catalog metadata for LangGraph; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "langgraph",
    "name": "LangGraph",
    "vendor": "LangChain",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Stateful agent orchestration","Graph-based workflows"],
    "integration_status": "catalog_only",
    "notes": "Agent orchestration framework; bounded state and explicit tool permissions remain application responsibilities.",
}
