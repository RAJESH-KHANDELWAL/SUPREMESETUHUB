"""Service layer for business_companies_trade; no live listings are implied."""
from .catalog import list_categories, get_category, search_categories, get_catalogue_metadata

class DomainService:
    DOMAIN_ID = "business_companies_trade"

    def list_categories(self, query: str | None = None):
        return search_categories(query) if query else list_categories()

    def get_category(self, category_id: str):
        return get_category(category_id)

    def search(self, query: str):
        return search_categories(query)

    def get_status(self):
        return {"success": True, **get_catalogue_metadata()}
