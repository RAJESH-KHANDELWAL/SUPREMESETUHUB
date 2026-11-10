"""Catalog metadata for CrewAI; framework metadata is not a hosted model API."""

PROVIDER = {
    "id": "crewai",
    "name": "CrewAI",
    "vendor": "CrewAI",
    "category": "agent_framework",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Multi-agent orchestration","Role-based agent teams"],
    "integration_status": "catalog_only",
    "notes": "Agent orchestration framework; agents and tool permissions require application-level governance.",
}
