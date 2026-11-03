"""Service layer for the wellness and fitness taxonomy."""
from .catalog import get_category, list_categories

class WellnessFitnessService:
    DOMAIN_ID = "healthcare_wellness_fitness"

    def list_categories(self, query=None):
        items = list_categories()
        if query:
            term = query.strip().casefold()
            items = [item for item in items if term in item["id"].casefold() or term in item["name"].casefold() or any(term in sub.replace("_", " ").casefold() for sub in item["subcategories"])]
        return items

    def get_category(self, category_id):
        return get_category(category_id)

    def get_status(self):
        return {"success": True, "domain_id": self.DOMAIN_ID, "status": "taxonomy_scaffold", "category_count": len(list_categories()), "coverage": ["india", "global"]}
