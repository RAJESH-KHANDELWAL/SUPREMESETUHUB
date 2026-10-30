from datetime import datetime, timezone

from .business_catalog import BUSINESS_CATEGORIES


class BusinessEcosystemService:
    ECOSYSTEM_ID = "global-bada-business"
    ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS API ECOSYSTEM"
    VERSION = "2.0.0"

    MODULES = [
        {"id": "businesses", "name": "BUSINESSES", "description": "Business profiles and organisations across all sectors"},
        {"id": "companies", "name": "COMPANIES", "description": "Company information, structures and management"},
        {"id": "entrepreneurs", "name": "ENTREPRENEURS", "description": "Entrepreneurs, founders and initiatives"},
        {"id": "services", "name": "BUSINESS SERVICES", "description": "Professional, local, digital and enterprise services"},
        {"id": "partnerships", "name": "PARTNERSHIPS", "description": "Business partnerships and collaboration"},
        {"id": "opportunities", "name": "BUSINESS OPPORTUNITIES", "description": "Business opportunities, markets and collaboration"},
        {"id": "online-businesses", "name": "ONLINE BUSINESSES", "description": "Digital-first and internet-enabled business models"},
        {"id": "offline-businesses", "name": "OFFLINE BUSINESSES", "description": "Physical-location and in-person business models"},
        {"id": "hybrid-businesses", "name": "HYBRID BUSINESSES", "description": "Businesses operating across physical and digital channels"},
        {"id": "adult-industry", "name": "ADULT INDUSTRY BUSINESSES (18+)", "description": "Age-restricted adult-industry business categories and providers"},
    ]

    def get_status(self):
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "ecosystem_name": self.ECOSYSTEM_NAME,
            "version": self.VERSION,
            "status": "catalog_available",
            "module_count": len(self.MODULES),
            "category_count": len(BUSINESS_CATEGORIES),
            "adult_category_count": sum(1 for item in BUSINESS_CATEGORIES if item.get("adult_only")),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list_modules(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(self.MODULES), "modules": self.MODULES}

    def get_module(self, module_id: str):
        return next((item for item in self.MODULES if item["id"] == module_id), None)

    def list_categories(self, channel: str | None = None, include_adult: bool = False):
        allowed_channels = {"online", "offline", "hybrid"}
        if channel is not None and channel not in allowed_channels:
            raise ValueError("channel must be online, offline, or hybrid")
        results = []
        for item in BUSINESS_CATEGORIES:
            if item.get("adult_only") and not include_adult:
                continue
            if channel and channel not in item["modes"]:
                continue
            results.append(item)
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(results), "categories": results}

    def get_category(self, category_id: str, include_adult: bool = False):
        for item in BUSINESS_CATEGORIES:
            if item["id"] == category_id and (include_adult or not item.get("adult_only")):
                return item
        return None

    def search_categories(self, query: str, include_adult: bool = False):
        needle = query.strip().casefold()
        if not needle:
            return []
        results = []
        for item in BUSINESS_CATEGORIES:
            if item.get("adult_only") and not include_adult:
                continue
            searchable = " ".join([item["id"], item["name"], *item["subcategories"]]).casefold()
            if needle in searchable:
                results.append(item)
        return results
