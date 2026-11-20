"""Read-only service facade for relationship taxonomy discovery."""
from .manager import get_manager
class EntityRelationshipCoreService:
    def status(self): return get_manager().status()
    def list_categories(self): return get_manager().list_categories()
    def get_category(self,ecosystem_id): return get_manager().get_category(ecosystem_id)
    def relationship_types(self): return get_manager().relationship_types()
    def master_catalog_reference(self): return get_manager().master_catalog_reference()
