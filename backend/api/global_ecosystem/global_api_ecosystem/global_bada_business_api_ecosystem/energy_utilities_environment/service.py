"""Business logic for Energy, Utilities & Environment taxonomy."""
from .catalog import (
    list_categories, get_category, list_business_domains, get_business_domain,
)

class EnergyEnvironmentService:
    DOMAIN_ID = "energy_utilities_environment"

    def list_categories(self, query: str | None = None):
        items = list_categories()
        if query:
            q = query.strip().casefold()
            items = [
                x for x in items
                if q in x["id"].casefold() or q in x["name"].casefold()
                or any(q in s.replace("_", " ").casefold() for s in x["subcategories"])
            ]
        return items

    def get_category(self, category_id: str):
        return get_category(category_id)

    def list_business_domains(self, query: str | None = None, category_id: str | None = None):
        items = list_business_domains()
        if category_id:
            items = [x for x in items if x["category_id"] == category_id]
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold()]
        return items

    def get_business_domain(self, domain_id: str):
        return get_business_domain(domain_id)

    def get_status(self):
        categories = list_categories()
        domains = list_business_domains()
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "category_count": len(categories),
            "business_domain_count": len(domains),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Taxonomy scaffold only; no live provider verification, official affiliation, licensing, or service quality certification is implied.",
        }
