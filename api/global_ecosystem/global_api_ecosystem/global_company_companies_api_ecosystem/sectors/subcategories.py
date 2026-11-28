"""Stable Company sector identifiers."""
from .catalog import SECTORS
SUBCATEGORY_IDS=tuple(x.sector_id for x in SECTORS)
def list_subcategories(): return [{"id":x.sector_id,"name":x.name,"domain_id":"company_sectors"} for x in SECTORS]
