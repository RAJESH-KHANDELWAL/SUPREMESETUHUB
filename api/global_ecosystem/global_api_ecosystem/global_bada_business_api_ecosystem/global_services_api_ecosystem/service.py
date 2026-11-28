"""Service functions for GLOBAL SERVICES API ECOSYSTEM."""
from __future__ import annotations
from ..services_platforms_integrations_business_api_ecosystem.service import DomainService

class GlobalServicesAPIService:
    ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-SERVICES-API"
    def __init__(self):
        self.domain = DomainService()

    def status(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID,
                "ecosystem": "GLOBAL SERVICES API ECOSYSTEM",
                "status": "CATALOG_FACADE_READY",
                "canonical_domain": self.domain.get_status()}

    def categories(self, query: str | None = None):
        items = self.domain.list_categories(query)
        return {"success": True, "count": len(items),
                "categories": [self._record(item) for item in items],
                "classification": "taxonomy_only"}

    def category(self, category_id: str):
        item = self.domain.get_category(category_id)
        return self._record(item) if item is not None else None

    def search(self, query: str):
        return [self._record(item) for item in self.domain.search(query)]

    @staticmethod
    def _record(item):
        from dataclasses import asdict, is_dataclass
        return asdict(item) if is_dataclass(item) else dict(item)
