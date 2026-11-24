"""Canonical domain-facing CORE facade; no HTTP, SQL or cloud dependencies."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import ECOSYSTEM, CULTURAL_DOMAINS, get_complete_knowledge, search_knowledge, assess_publication

class GlobalCulturalCore:
    ecosystem_id = ECOSYSTEM["id"]

    def describe(self) -> dict[str, Any]:
        return {"id": self.ecosystem_id, "name": ECOSYSTEM["name"],
                "pillars": list(ECOSYSTEM.get("pillars", ())),
                "domain_ids": list(CULTURAL_DOMAINS),
                "purpose": "Preserve, research, teach and connect living cultural knowledge."}

    def domains(self) -> list[dict[str, Any]]:
        return [{"id": key, "name": getattr(value, "DOMAIN_NAME", key.replace("_", " ").title()),
                 "description": getattr(value, "DOMAIN_DESCRIPTION", "")}
                for key, value in CULTURAL_DOMAINS.items()]

    def knowledge(self) -> dict[str, Any]:
        return get_complete_knowledge()

    def search_foundation(self, query: str) -> list[dict[str, Any]]:
        needle = str(query or "").strip()
        if not needle:
            raise ValueError("CULTURAL_QUERY_REQUIRED")
        return [dict(row) for row in search_knowledge(needle)]

    def publication_review(self, resource: Any) -> Any:
        return assess_publication(resource)
