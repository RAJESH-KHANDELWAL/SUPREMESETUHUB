"""Business-company domain service backed by the canonical Global Company taxonomy."""
from __future__ import annotations
from .catalog import DOMAIN_ID, get_category, list_categories

class DomainService:
    def list_categories(self, query: str | None = None):
        items = list_categories()
        if query:
            term = query.strip().casefold()
            items = [item for item in items if term in item.id.casefold() or term in item.name.casefold()]
        return items

    def get_category(self, category_id: str):
        return get_category(category_id)

    def search(self, query: str):
        return self.list_categories(query)

    def get_status(self):
        return {"success": True, "domain_id": DOMAIN_ID, "status": "taxonomy_scaffold", "category_count": len(list_categories()), "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"]}
