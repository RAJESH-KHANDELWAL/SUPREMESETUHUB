"""Compatibility service backed by the canonical finance ecosystem."""
from . import DOMAIN_ID
from .catalog import list_categories, get_category, search_categories, get_catalogue_metadata
class DomainService:
    DOMAIN_ID = "finance_banking_insurance"
    def list_categories(self, query: str | None = None, include_restricted: bool = False):
        return search_categories(query, include_restricted) if query else list_categories(include_restricted)
    def get_category(self, category_id: str, include_restricted: bool = False):
        return get_category(category_id, include_restricted)
    def search(self, query: str, include_restricted: bool = False):
        return search_categories(query, include_restricted)
    def get_status(self):
        return {"success": True, **get_catalogue_metadata()}
