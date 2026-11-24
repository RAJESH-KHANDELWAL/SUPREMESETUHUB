"""ENGINE orchestration for culture-service-work-business discovery."""
from __future__ import annotations

from typing import Any

from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem.service_work_business import list_capabilities
from .discovery import search_catalogue


class GlobalCultureServiceWorkBusinessEngine:
    """Searches domain-owned capability metadata without owning CORE logic."""

    def __init__(self, catalogue_provider: Any | None = None) -> None:
        self._catalogue_provider = catalogue_provider or list_capabilities

    def status(self) -> dict[str, Any]:
        return {
            "component": "ENGINE",
            "status": "READY",
            "capabilities": ["CATALOGUE_DISCOVERY", "DOMAIN_FILTERING", "RELEVANCE_RANKING"],
            "live_marketplace": False,
        }

    def catalogue(self, domain: str | None = None) -> list[dict[str, Any]]:
        return self._catalogue_provider(domain)

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        matches = search_catalogue(self.catalogue(), query, domain)
        return {
            "query": query.strip(),
            "domain": domain.upper() if domain else None,
            "count": len(matches),
            "results": matches,
            "classification_only": True,
            "live_providers": False,
            "live_jobs_or_gigs": False,
        }
