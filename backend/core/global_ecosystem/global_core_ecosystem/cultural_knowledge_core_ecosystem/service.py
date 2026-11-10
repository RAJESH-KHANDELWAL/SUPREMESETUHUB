"""CORE contracts and governance facade for the cultural knowledge domain."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import (
    ECOSYSTEM, get_complete_knowledge, search_knowledge, assess_publication,
)

class CulturalKnowledgeCoreService:
    """Owns domain-level policy; deliberately contains no transport or persistence code."""
    ecosystem_id = ECOSYSTEM["id"]

    def describe(self) -> dict[str, Any]:
        return {"ecosystem_id": self.ecosystem_id, "name": ECOSYSTEM["name"],
                "pillars": list(ECOSYSTEM["pillars"]),
                "domains": list(ECOSYSTEM["cultural_domains"])}

    def knowledge(self) -> dict[str, Any]:
        return get_complete_knowledge()

    def search(self, query: str) -> list[dict[str, Any]]:
        return [dict(item) for item in search_knowledge(query)]

    def publication_decision(self, resource: Any) -> Any:
        return assess_publication(resource)
