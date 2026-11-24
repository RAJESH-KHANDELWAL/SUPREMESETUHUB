"""Business logic for Finance, Banking & Insurance."""
from __future__ import annotations
from .catalog import get_category, list_categories

class FinanceService:
    DOMAIN_ID = "finance_banking_insurance"

    def list_categories(self, *, query: str | None = None) -> list[dict[str, object]]:
        items = list_categories()
        if query:
            term = query.strip().casefold()
            items = [item for item in items if term in str(item["id"]).casefold() or term in str(item["name"]).casefold() or any(term in value.replace("_", " ").casefold() for value in item["subcategories"])]
        return items

    def get_category(self, category_id: str) -> dict[str, object] | None:
        return get_category(category_id)

    def get_status(self) -> dict[str, object]:
        return {"success": True, "domain_id": self.DOMAIN_ID, "status": "taxonomy_scaffold", "category_count": len(list_categories()), "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "note": "Taxonomy scaffold only; no live provider verification, transaction processing or regulatory approval is implied."}
