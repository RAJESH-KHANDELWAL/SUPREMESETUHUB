"""Business logic for Agriculture, Food & Natural Resources."""
from __future__ import annotations

from .catalog import get_agriculture_category, list_agriculture_categories

class AgricultureFoodService:
    DOMAIN_ID = "agriculture_food_natural_resources"

    def list_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        items = list_agriculture_categories()
        if query:
            term = query.strip().casefold()
            items = [
                item for item in items
                if term in str(item["id"]).casefold()
                or term in str(item["name"]).casefold()
                or any(term in value.replace("_", " ").casefold() for value in item["subcategories"])
            ]
        return items

    def get_category(self, category_id: str) -> dict[str, object] | None:
        return get_agriculture_category(category_id)

    def get_status(self) -> dict[str, object]:
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "category_count": len(list_agriculture_categories()),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Category taxonomy only; no live market data or provider integration is implied.",
        }
