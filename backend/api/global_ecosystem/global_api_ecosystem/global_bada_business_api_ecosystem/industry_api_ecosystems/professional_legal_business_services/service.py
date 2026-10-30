"""Business logic for Professional, Legal & Business Services taxonomy."""
from .catalog import list_categories, get_category

class ProfessionalServicesService:
    DOMAIN_ID = "professional_legal_business_services"
    def list_categories(self, query: str | None = None):
        items = list_categories()
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in s.replace("_", " ").casefold() for s in x["subcategories"])]
        return items
    def get_category(self, category_id: str):
        return get_category(category_id)
    def get_status(self):
        return {"success": True, "domain_id": self.DOMAIN_ID, "status": "taxonomy_scaffold", "category_count": len(list_categories()), "coverage": ["india", "global"], "channels": ["online", "offline", "hybrid"], "note": "Taxonomy scaffold only; no live provider verification, official affiliation, licensing, or service quality certification is implied."}
