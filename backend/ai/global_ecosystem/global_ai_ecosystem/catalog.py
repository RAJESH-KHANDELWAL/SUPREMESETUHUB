"""Unified read-only GLOBAL AI ECOSYSTEM catalog."""
from __future__ import annotations

from typing import Any

from .agents import AGENT_COMPONENTS
from .global_ai_agents.catalog import AGENT_CATALOG
from .bada_business_ai_ecosystem.catalog import AI_CAPABILITIES, AI_ECOSYSTEM_PROFILE
from .bada_business_ai_ecosystem.agents import BADA_BUSINESS_AGENTS
from .bada_business_ai_ecosystem.workflows import BADA_BUSINESS_WORKFLOWS
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
    "agent_profiles": tuple(AGENT_CATALOG.values()),
    "workflows": WORKFLOWS,
    "knowledge": KNOWLEDGE_COMPONENTS,
    "infrastructure": INFRASTRUCTURE,
    "governance": GOVERNANCE_CONTROLS,
    "integrations": INTEGRATIONS,
    "business_ai_ecosystems": (AI_ECOSYSTEM_PROFILE,),
    "business_ai_capabilities": AI_CAPABILITIES,
    "business_ai_agents": BADA_BUSINESS_AGENTS,
    "business_ai_workflows": BADA_BUSINESS_WORKFLOWS,
}


def get_catalog() -> dict[str, list[dict[str, Any]]]:
    return {
        category: [
            record.to_dict() if hasattr(record, "to_dict") else dict(record)
            for record in records
        ]
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
