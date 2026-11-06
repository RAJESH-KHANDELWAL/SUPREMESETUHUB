"""Industry taxonomy service."""
from .catalog import get_catalog_entry,get_catalog_metadata,list_catalog,search_catalog
class IndustryService:
 def list_industries(self,query=None): return search_catalog(query) if query else list_catalog()
 def get_industry(self,industry_id): return get_catalog_entry(industry_id)
 def get_status(self): return get_catalog_metadata()
