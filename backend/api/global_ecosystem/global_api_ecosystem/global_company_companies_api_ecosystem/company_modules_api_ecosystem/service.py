"""Service layer for company-specific module discovery."""
from .catalog import get_catalog_entry, get_catalog_metadata, list_catalog, search_catalog


class CompanyModulesService:
    ECOSYSTEM_ID = "global-company-companies"

    def get_status(self):
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            **get_catalog_metadata(),
        }

    def list_modules(self):
        items = list_catalog()
        return {
            "success": True,
            "count": len(items),
            "catalog_status": "module_index_only",
            "modules": items,
        }

    def search_modules(self, query: str):
        items = search_catalog(query)
        return {
            "success": True,
            "count": len(items),
            "query": query.strip(),
            "catalog_status": "module_index_only",
            "modules": items,
        }

    def get_module(self, company_id: str):
        return get_catalog_entry(company_id)
