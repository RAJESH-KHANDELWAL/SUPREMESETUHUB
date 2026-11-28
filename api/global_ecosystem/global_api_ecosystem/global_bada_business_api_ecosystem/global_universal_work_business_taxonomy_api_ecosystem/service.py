"""Service layer for the India + Global work/business taxonomy."""
from .catalog import get_facets, get_sector, list_sectors, search_sectors, validate_catalogue

class UniversalWorkBusinessTaxonomyService:
    ECOSYSTEM_ID = "global-bada-business-universal-work-business-taxonomy"
    VERSION = "1.0.0"

    def get_status(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "version": self.VERSION, "status": "taxonomy_catalog_available", **validate_catalogue()}

    def list_sectors(self, include_adult=False):
        items = list_sectors(include_adult)
        return {"success": True, "count": len(items), "coverage_scope": ["india", "global"], "classification": "taxonomy_only", "sectors": items}

    def get_sector(self, sector_id, include_adult=False):
        return get_sector(sector_id, include_adult)

    def search(self, query, include_adult=False):
        return search_sectors(query, include_adult)

    def get_facets(self):
        return get_facets()

    def integrity(self):
        return validate_catalogue()
