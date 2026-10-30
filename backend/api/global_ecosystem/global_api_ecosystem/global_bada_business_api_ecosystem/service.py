from datetime import datetime, timezone

from .business_catalog import BUSINESS_CATEGORIES
from .business_dimensions import BUSINESS_DIMENSIONS, get_business_dimension


class BusinessEcosystemService:
    ECOSYSTEM_ID = "global-bada-business"
    ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS API ECOSYSTEM"
    VERSION = "2.1.0"

    MODULES = [
        {"id": "businesses", "name": "BUSINESSES", "description": "Business profiles and organisations across all sectors"},
        {"id": "companies", "name": "COMPANIES", "description": "Company information, structures and management"},
        {"id": "entrepreneurs", "name": "ENTREPRENEURS", "description": "Entrepreneurs, founders and initiatives"},
        {"id": "services", "name": "BUSINESS SERVICES", "description": "Professional, local, digital and enterprise services"},
        {"id": "products", "name": "PRODUCTS & COMMERCE", "description": "Physical goods, digital products, catalogues and commerce models"},
        {"id": "marketplaces", "name": "MARKETPLACES & DISTRIBUTION", "description": "Retail, wholesale, marketplaces, distributors and trade channels"},
        {"id": "operations", "name": "BUSINESS OPERATIONS", "description": "Finance, HR, sales, procurement, supply chain and operations"},
        {"id": "partnerships", "name": "PARTNERSHIPS", "description": "Business partnerships, joint ventures and collaboration"},
        {"id": "opportunities", "name": "BUSINESS OPPORTUNITIES", "description": "Business opportunities, markets and collaboration"},
        {"id": "funding-investment", "name": "FUNDING & INVESTMENT", "description": "Business finance, funding pathways and investment classifications"},
        {"id": "franchising-licensing", "name": "FRANCHISING & LICENSING", "description": "Franchise, distribution, intellectual property and licensing models"},
        {"id": "trade-global", "name": "GLOBAL TRADE", "description": "Import, export, cross-border commerce and international expansion"},
        {"id": "compliance-risk", "name": "COMPLIANCE & RISK", "description": "Business registration references, licensing, legal compliance and risk"},
        {"id": "online-businesses", "name": "ONLINE BUSINESSES", "description": "Digital-first and internet-enabled business models"},
        {"id": "offline-businesses", "name": "OFFLINE BUSINESSES", "description": "Physical-location and in-person business models"},
        {"id": "hybrid-businesses", "name": "HYBRID BUSINESSES", "description": "Businesses operating across physical and digital channels"},
        {"id": "adult-industry", "name": "ADULT INDUSTRY BUSINESSES (18+)", "description": "Age-restricted lawful adult-industry business categories; separate safeguards required"},
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
            "dimension_count": len(BUSINESS_DIMENSIONS),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def list_modules(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(self.MODULES), "modules": self.MODULES}

    def get_module(self, module_id: str):
        return next((item for item in self.MODULES if item["id"] == module_id), None)

    def list_dimensions(self):
        result = list(BUSINESS_DIMENSIONS)
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(result), "dimensions": result}

    def get_dimension(self, dimension_id: str):
        return get_business_dimension(dimension_id)

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
