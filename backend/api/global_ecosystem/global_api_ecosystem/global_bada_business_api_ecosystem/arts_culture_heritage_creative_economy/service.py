from .catalog import get_category, list_categories


class ArtsCultureHeritageService:
    DOMAIN_ID = "arts_culture_heritage_creative_economy"

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
            "focus": ["arts", "culture", "heritage", "creative_economy"],
            "note": "Taxonomy only; no institution, collection, event, artisan, heritage condition or funding verification is implied.",
        }
