from datetime import datetime, timezone

from .business_catalog import BUSINESS_CATEGORIES
from .global_world_business_map import GLOBAL_WORLD_BUSINESS_MAP
from .global_world_catalog import GLOBAL_WORLD_CATALOG
from .sectors import get_sector, get_sector_facets, list_sectors


class BusinessEcosystemService:
    ECOSYSTEM_ID = "global-bada-business"
    ECOSYSTEM_NAME = "GLOBAL BADA BUSINESS API ECOSYSTEM"
    VERSION = "2.2.0"

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
        from .domain_registry import DOMAIN_REGISTRY
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "ecosystem_name": self.ECOSYSTEM_NAME,
            "version": self.VERSION,
            "status": "catalog_available",
            "module_count": len(self.MODULES),
            "category_count": len(BUSINESS_CATEGORIES),
            "global_world_domain_count": len(GLOBAL_WORLD_CATALOG),
            "domain_package_count": len(DOMAIN_REGISTRY),
            "domain_subcategory_count": sum(item["subcategory_count"] for item in DOMAIN_REGISTRY),
            "domain_registry_status": "taxonomy_only",
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

    def list_global_world_map(self, include_adult: bool = False):
        results = [
            item for item in GLOBAL_WORLD_BUSINESS_MAP
            if include_adult or not item.get("adult_only")
        ]
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(results),
            "global_world_domains": results,
            "note": "Business-facing crosswalk only; people, jobs, households and relationship records remain in their owning ecosystems.",
        }

    def get_global_world_domain(self, domain_id: str, include_adult: bool = False):
        for item in GLOBAL_WORLD_BUSINESS_MAP:
            if item["world_domain_id"] != domain_id:
                continue
            if item.get("adult_only") and not include_adult:
                return None
            return item
        return None

    def list_global_world_catalog(self, include_adult: bool = False):
        results = [
            item for item in GLOBAL_WORLD_CATALOG
            if include_adult or not item.get("adult_only")
        ]
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(results),
            "global_world_domains": results,
            "source": "Global World A-Z taxonomy snapshot",
            "note": "Full domain and subgroup catalogue for business-facing discovery. Personal records remain in their owning ecosystems.",
        }

    def get_global_world_catalog_domain(self, domain_id: str, include_adult: bool = False):
        for item in GLOBAL_WORLD_CATALOG:
            if item["id"] == domain_id:
                if item.get("adult_only") and not include_adult:
                    return None
                return item
        return None

    def search_global_world_catalog(self, query: str, include_adult: bool = False):
        needle = query.strip().casefold()
        if not needle:
            return []
        results = []
        for item in GLOBAL_WORLD_CATALOG:
            if item.get("adult_only") and not include_adult:
                continue
            searchable = " ".join([item["id"], item["name"], *item["groups"]]).casefold()
            if needle in searchable:
                results.append(item)
        return results



    def list_work_business(self, channel=None, include_adult=False):
        sectors = list_sectors(channel=channel, include_adult=include_adult)
        return {
            "success": True, "ecosystem_id": self.ECOSYSTEM_ID, "count": len(sectors),
            "filters": {"delivery_mode": channel, "include_adult": include_adult},
            "facets": get_sector_facets(), "sectors": sectors, "classification": "taxonomy_only",
            "note": "Offline, online and hybrid work/business taxonomy. Work-mode, business-size, maturity, geography and audience values are discovery facets, not verified sector-specific availability. This is not a vacancy or live-provider feed.",
        }

    def get_work_business_sector(self, sector_id, include_adult=False):
        sector = get_sector(sector_id)
        if sector is None or (sector.get("adult_only") and not include_adult):
            return None
        return sector

    def get_taxonomy_integrity(self):
        """Return structural checks for the embedded business/world taxonomy."""
        category_ids = {item["id"] for item in BUSINESS_CATEGORIES}
        domain_ids = [item["id"] for item in GLOBAL_WORLD_CATALOG]
        map_ids = [item["world_domain_id"] for item in GLOBAL_WORLD_BUSINESS_MAP]
        broken_catalog_links = sorted({
            category_id
            for domain in GLOBAL_WORLD_CATALOG
            for category_id in domain.get("business_category_ids", [])
            if category_id not in category_ids
        })
        broken_map_links = sorted({
            category_id
            for domain in GLOBAL_WORLD_BUSINESS_MAP
            for category_id in domain.get("business_category_ids", [])
            if category_id not in category_ids
        })
        catalog_only_domains = sorted(set(domain_ids) - set(map_ids))
        map_only_domains = sorted(set(map_ids) - set(domain_ids))
        duplicate_catalog_ids = sorted({item for item in domain_ids if domain_ids.count(item) > 1})
        duplicate_map_ids = sorted({item for item in map_ids if map_ids.count(item) > 1})
        checks = {
            "unique_business_category_ids": len(category_ids) == len(BUSINESS_CATEGORIES),
            "unique_global_world_domain_ids": not duplicate_catalog_ids,
            "unique_crosswalk_domain_ids": not duplicate_map_ids,
            "catalog_category_links_valid": not broken_catalog_links,
            "crosswalk_category_links_valid": not broken_map_links,
            "catalog_and_crosswalk_domains_match": not catalog_only_domains and not map_only_domains,
        }
        return {
            "success": all(checks.values()),
            "ecosystem_id": self.ECOSYSTEM_ID,
            "version": self.VERSION,
            "counts": {
                "business_categories": len(BUSINESS_CATEGORIES),
                "global_world_domains": len(GLOBAL_WORLD_CATALOG),
                "crosswalk_domains": len(GLOBAL_WORLD_BUSINESS_MAP),
            },
            "checks": checks,
            "issues": {
                "broken_catalog_category_ids": broken_catalog_links,
                "broken_crosswalk_category_ids": broken_map_links,
                "catalog_only_domain_ids": catalog_only_domains,
                "crosswalk_only_domain_ids": map_only_domains,
                "duplicate_catalog_domain_ids": duplicate_catalog_ids,
                "duplicate_crosswalk_domain_ids": duplicate_map_ids,
            },
            "note": "Structural catalogue validation only; it does not verify provider existence, licensing, or jurisdictional legality.",
        }

    def list_domains(self, include_adult: bool = False):
        from .domain_registry import list_domains
        domains = list_domains(include_adult=include_adult)
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(domains),
            "registry_status": "taxonomy_only",
            "domains": domains,
        }

    def get_domain(self, domain_id: str, include_adult: bool = False):
        from .domain_registry import get_domain
        return get_domain(domain_id, include_adult=include_adult)

    def search_domains(self, query: str, include_adult: bool = False):
        from .domain_registry import search_domains
        return search_domains(query, include_adult=include_adult)

    def get_domain_registry_integrity(self):
        from .domain_registry import validate_domain_registry
        return validate_domain_registry()
