"""Company sector taxonomy service."""
from .catalog import get_sector,list_sectors,search_sectors,validate_sector_catalog
class SectorService:
 def list_sectors(self,query=None): return search_sectors(query) if query else list_sectors()
 def get_sector(self,sector_id): return get_sector(sector_id)
 def get_status(self): return validate_sector_catalog()
