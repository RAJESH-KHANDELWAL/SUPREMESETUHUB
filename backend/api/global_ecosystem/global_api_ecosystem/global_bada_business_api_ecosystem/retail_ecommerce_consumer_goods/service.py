"""Retail, e-commerce and consumer-goods taxonomy service."""
from .catalog import list_categories, get_category, list_business_domains, get_business_domain


class RetailService:
    DOMAIN_ID = "retail_ecommerce_consumer_goods"

    def list_categories(self, query: str | None = None):
        items = list_categories()
        if query:
            q = query.strip().casefold()
            items = [
                x for x in items
                if q in x["id"].casefold()
                or q in x["name"].casefold()
                or any(q in s.replace("_", " ").casefold() for s in x["subcategories"])
            ]
        return items

    def get_category(self, category_id: str):
        return get_category(category_id)

    def list_business_domains(self, query: str | None = None):
        items = list_business_domains()
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold()]
        return items

    def get_business_domain(self, domain_id: str):
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
            "note": "Taxonomy only; no live product inventory, seller verification, payments, repair authorization or fulfilment integrations are implied.",
        }
