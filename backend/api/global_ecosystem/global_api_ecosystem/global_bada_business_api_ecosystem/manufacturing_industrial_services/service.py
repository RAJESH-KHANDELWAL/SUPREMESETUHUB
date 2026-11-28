"""Business logic for the manufacturing and factory-services taxonomy."""
from .catalog import (
    get_business_domain, get_category, list_business_domains, list_categories,
    validate_catalog,
)

class ManufacturingService:
    DOMAIN_ID = "manufacturing_industrial_services"

    def list_categories(self, query: str | None = None):
        items = list_categories()
        if query:
            needle = query.strip().casefold()
            items = [
                item for item in items
                if needle in item["id"].casefold()
                or needle in item["name"].casefold()
                or any(needle in sub.replace("_", " ").casefold() for sub in item["subcategories"])
            ]
        return items

    def get_category(self, category_id: str):
        return get_category(category_id)

    def list_business_domains(self, query: str | None = None, category_id: str | None = None):
        items = list_business_domains()
        if category_id:
            items = [item for item in items if item["category_id"] == category_id]
        if query:
            needle = query.strip().casefold()
            items = [
                item for item in items
                if needle in item["id"].casefold()
                or needle in item["name"].casefold()
                or needle in item["description"].casefold()
            ]
        return items

    def get_business_domain(self, domain_id: str):
        return get_business_domain(domain_id)

    def get_status(self):
        report = validate_catalog()
        return {
            "success": report["structurally_valid"],
            "domain_id": self.DOMAIN_ID,
            "status": "taxonomy_scaffold",
            "category_count": report["category_count"],
            "business_domain_count": report["business_domain_count"],
            "coverage": ["india", "global"],
            "channels": ["online", "offline", "hybrid"],
            "structurally_valid": report["structurally_valid"],
            "note": "Taxonomy only; no factory audit, supplier verification, certification, licence check, live production data or compliance approval is implied.",
        }

    def get_integrity(self):
        return validate_catalog()
