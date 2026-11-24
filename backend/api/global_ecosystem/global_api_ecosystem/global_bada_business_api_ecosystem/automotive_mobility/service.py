from .catalog import list_categories, get_category, list_business_domains, get_business_domain


class AutomotiveMobilityService:
    DOMAIN_ID = "automotive_mobility"

    def list_categories(self, query=None):
        items = list_categories()
        if query:
            q = query.strip().casefold()
            items = [
                item for item in items
                if q in item["id"].casefold()
                or q in item["name"].casefold()
                or any(q in value.replace("_", " ").casefold() for value in item["subcategories"])
            ]
        return items

    def get_category(self, category_id):
        return get_category(category_id)

    def list_business_domains(self, query=None):
        items = list_business_domains()
        if query:
            q = query.strip().casefold()
            items = [item for item in items if q in item["id"].casefold() or q in item["name"].casefold()]
        return items

    def get_business_domain(self, domain_id):
        return get_business_domain(domain_id)

    def get_status(self):
        return {
            "success": True,
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "business_domain_count": len(list_business_domains()),
            "category_count": len(list_categories()),
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "note": "Taxonomy only; no live provider verification, licensing, endorsement or quality certification is implied.",
        }
