"""Corporate-group taxonomy service; no live relationship data is implied."""
from .catalog import list_categories,get_category,search_categories,get_catalogue_metadata
class DomainService:
 DOMAIN_ID="corporate_groups"
 def list_categories(self,query=None): return search_categories(query) if query else list_categories()
 def get_category(self,category_id): return get_category(category_id)
 def search(self,query): return search_categories(query)
 def get_status(self): return {"success":True,**get_catalogue_metadata()}
