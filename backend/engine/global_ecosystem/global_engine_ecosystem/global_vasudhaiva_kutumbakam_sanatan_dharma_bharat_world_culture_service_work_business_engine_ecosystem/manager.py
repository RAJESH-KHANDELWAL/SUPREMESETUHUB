"""ENGINE orchestration for culture-service-work-business discovery."""
from __future__ import annotations

from typing import Any

from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.service import (
    GlobalBadaBusinessCulturalServiceWorkBusinessCore,
)
from .discovery import search_catalogue


class GlobalCultureServiceWorkBusinessEngine:
    def __init__(
        self,
        core: GlobalBadaBusinessCulturalServiceWorkBusinessCore | None = None,
    ) -> None:
        self.core = core or GlobalBadaBusinessCulturalServiceWorkBusinessCore()

    def status(self) -> dict[str, Any]:
        return {
            "component": "ENGINE",
            "status": "READY",
            "capabilities": [
                "CATALOGUE_DISCOVERY",
                "DOMAIN_FILTERING",
                "RELEVANCE_RANKING",
            ],
            "live_marketplace": False,
        }

    def catalogue(self, domain: str | None = None) -> list[dict[str, Any]]:
        return self.core.catalogue(domain)

    def _searchable_catalogue(self) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for capability in self.core.catalogue():
            for domain in capability.get("domains", []):
                records.append(
                    {
                        "id": capability["id"],
                        "name": capability["name"],
                        "description": capability.get("description", capability["name"]),
                        "domain": domain,
                        "keywords": capability.get("keywords", []),
                        "work_types": capability.get("work", []),
                        "business_types": capability.get("business", []),
                    }
                )
        return records

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        matches = search_catalogue(self._searchable_catalogue(), query, domain)
        return {
            "query": query.strip(),
            "domain": domain.upper() if domain else None,
            "count": len(matches),
            "results": matches,
            "classification_only": True,
            "live_providers": False,
            "live_jobs_or_gigs": False,
        }
