"""Unified read-only GLOBAL AI ECOSYSTEM catalog."""
from __future__ import annotations

from typing import Any

from .agents import AGENT_COMPONENTS
from .capabilities import CAPABILITIES
from .governance import GOVERNANCE_CONTROLS
from .infrastructure import INFRASTRUCTURE
from .integrations import INTEGRATIONS
from .knowledge import KNOWLEDGE_COMPONENTS
from .models import MODELS
from .providers import PROVIDERS
from .services import SERVICES
from .workflows import WORKFLOWS

CATALOG: dict[str, tuple] = {
    "providers": PROVIDERS,
    "models": MODELS,
    "capabilities": CAPABILITIES,
    "services": SERVICES,
    "agent_components": AGENT_COMPONENTS,
    "workflows": WORKFLOWS,
    "knowledge": KNOWLEDGE_COMPONENTS,
    "infrastructure": INFRASTRUCTURE,
    "governance": GOVERNANCE_CONTROLS,
    "integrations": INTEGRATIONS,
}


def get_catalog() -> dict[str, list[dict[str, Any]]]:
    return {
        category: [record.to_dict() for record in records]
        for category, records in CATALOG.items()
    }


def list_providers() -> list[dict[str, Any]]:
    return [record.to_dict() for record in PROVIDERS]


def get_provider(provider_id: str) -> dict[str, Any]:
    key = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider.id == key:
            return provider.to_dict()
    raise KeyError("AI_PROVIDER_NOT_FOUND")


def catalog_counts() -> dict[str, int]:
    return {category: len(records) for category, records in CATALOG.items()}
