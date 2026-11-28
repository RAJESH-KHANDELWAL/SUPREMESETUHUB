"""Read-only service facade for workforce category discovery."""
from .catalog import get_category, search_roles
class WorkBusinessDirectory:
    def get(self, category_id: str):
        return get_category(category_id)
    def search(self, query: str):
        return search_roles(query)
