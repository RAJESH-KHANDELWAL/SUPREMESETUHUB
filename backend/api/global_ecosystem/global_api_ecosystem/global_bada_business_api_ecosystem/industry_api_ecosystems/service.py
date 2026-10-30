"""Business logic for the Industry API Ecosystems registry."""
from __future__ import annotations
from .registry import get_industry_ecosystem, list_industry_ecosystems

class IndustryEcosystemService:
    ECOSYSTEM_ID = "global_bada_business_api_ecosystem"

    def list_industries(self, *, channel: str | None = None, coverage: str | None = None,
                        include_adult: bool = False, query: str | None = None) -> list[dict[str, object]]:
        items = list_industry_ecosystems(include_adult=include_adult)
        if channel:
            items = [x for x in items if channel in x["channels"]]
        if coverage:
            items = [x for x in items if coverage in x["coverage"]]
        if query:
            term = query.strip().casefold()
            items = [x for x in items if term in str(x["id"]).casefold() or term in str(x["name"]).casefold()]
        return [dict(x) for x in items]

    def get_industry(self, industry_id: str, *, include_adult: bool = False) -> dict[str, object] | None:
        item = get_industry_ecosystem(industry_id, include_adult=include_adult)
        return dict(item) if item is not None else None

    def get_status(self) -> dict[str, object]:
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "status": "taxonomy_scaffold",
            "industry_count": len(self.list_industries()),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Taxonomy catalog only; third-party provider integrations are not implied.",
        }
