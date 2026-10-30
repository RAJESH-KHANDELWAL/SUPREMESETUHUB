"""Read-only service layer for the industry taxonomy registry."""
from __future__ import annotations

from .registry import get_industry_ecosystem, list_industry_ecosystems


class IndustryEcosystemService:
    """Query curated industry domains; this is not a provider directory."""

    ECOSYSTEM_ID = "global_bada_business_api_ecosystem"

    def list_industries(
        self,
        *,
        channel: str | None = None,
        coverage: str | None = None,
        include_adult: bool = False,
        query: str | None = None,
    ) -> list[dict[str, object]]:
        industries = list_industry_ecosystems(include_adult=include_adult)
        if channel:
            industries = [item for item in industries if channel in item["channels"]]
        if coverage:
            industries = [item for item in industries if coverage in item["coverage"]]
        if query:
            term = query.strip().casefold()
            industries = [
                item for item in industries
                if term in str(item["id"]).casefold()
                or term in str(item["name"]).casefold()
            ]
        return [dict(item) for item in industries]

    def get_industry(
        self, industry_id: str, *, include_adult: bool = False
    ) -> dict[str, object] | None:
        item = get_industry_ecosystem(industry_id, include_adult=include_adult)
        return dict(item) if item is not None else None

    def get_status(self) -> dict[str, object]:
        visible = self.list_industries()
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "status": "taxonomy_scaffold",
            "industry_count": len(visible),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Catalog taxonomy only; provider integrations are not implied.",
        }
