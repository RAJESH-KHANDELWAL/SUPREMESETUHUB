"""Public read-only WEB CORE service; no provider requests or persistence."""
from __future__ import annotations
from .catalog import get_catalog
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME
from .orchestrator import WebCoreOrchestrator

class WebCoreEcosystemService:
    def __init__(self):
        self.orchestrator = WebCoreOrchestrator()
    def status(self) -> dict:
        catalog = get_catalog()
        return {"success": True, "layer": "CORE", "ecosystem_id": ECOSYSTEM_ID,
                "ecosystem": ECOSYSTEM_NAME, "status": "CORE_CATALOG_ONLY",
                "provider_count": catalog["provider_count"],
                "product_family_count": catalog["product_family_count"],
                "domain_count": catalog["domain_count"],
                "live_connection_verified": False, "remote_operations_enabled": False,
                "api_calls_performed": 0, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"}
    def catalog(self) -> dict: return self.orchestrator.catalog()
    def health(self) -> dict: return self.orchestrator.health()
    def dependency_map(self) -> dict: return self.orchestrator.dependency_map()
