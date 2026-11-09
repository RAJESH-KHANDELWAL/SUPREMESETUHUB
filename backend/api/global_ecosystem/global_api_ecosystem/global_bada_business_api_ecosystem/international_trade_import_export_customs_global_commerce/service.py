from .catalog import get_category, list_categories


class InternationalTradeService:
    DOMAIN_ID = "international_trade_import_export_customs_global_commerce"

    def list_categories(self, query: str | None = None, channel: str | None = None):
        items = list_categories()
        if channel:
            items = [item for item in items if channel in item["channels"]]
        if query:
            term = query.strip().casefold()
            items = [
                item for item in items
                if term in item["id"].casefold()
                or term in item["name"].casefold()
                or any(term in sub.replace("_", " ").casefold() for sub in item["subcategories"])
            ]
        return items

    def get_category(self, category_id: str):
        return get_category(category_id)

    def get_status(self):
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "category_count": len(list_categories()),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "focus": ["international_trade", "import_export", "customs", "global_commerce"],
            "note": "Taxonomy only; no customs authority connection, legal classification ruling, broker credential, tariff calculation or provider verification is implied.",
        }
