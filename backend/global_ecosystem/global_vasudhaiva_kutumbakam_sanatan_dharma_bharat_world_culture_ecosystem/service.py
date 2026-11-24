"""Domain-level facade for the global cultural knowledge ecosystem.

This module belongs to the cultural domain package, not the global CORE registry.
It exposes the domain's approved knowledge and publication-governance operations
to API and ENGINE composition roots without owning transport or persistence.
"""
from __future__ import annotations

from typing import Any

from . import ECOSYSTEM, assess_publication, get_complete_knowledge, search_knowledge


class CulturalKnowledgeDomainService:
    """Provides domain metadata, foundational knowledge, search and governance."""

    ecosystem_id = ECOSYSTEM["id"]

    def describe(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ecosystem_id,
            "name": ECOSYSTEM["name"],
            "pillars": list(ECOSYSTEM["pillars"]),
            "domains": list(ECOSYSTEM["cultural_domains"]),
        }

    def knowledge(self) -> dict[str, Any]:
        return get_complete_knowledge()

    def search(self, query: str) -> list[dict[str, Any]]:
        return [dict(item) for item in search_knowledge(query)]

    def publication_decision(self, resource: Any) -> Any:
        return assess_publication(resource)
