"""Domain service for family_relationships_community; catalogue only, no live listings."""
from .catalog import list_categories, get_category, search_categories, get_catalogue_metadata
class DomainService:
    DOMAIN_ID = "family_relationships_community"
    def list_categories(self, query: str | None = None):
        return search_categories(query) if query else list_categories()
    def get_category(self, category_id: str):
        return get_category(category_id)
    def search(self, query: str):
        return search_categories(query)
    def get_status(self):
        return {"success": True, **get_catalogue_metadata()}
