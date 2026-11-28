"""Discovery and health orchestration for WEB CORE metadata only."""
from __future__ import annotations
from .catalog import get_catalog
from .domain_catalog import get_domain, list_domain_inventory
from .product_catalog import get_product_family, list_product_families
from .provider_catalog import get_provider, list_providers
from .constants import ECOSYSTEM_ID

class WebCoreOrchestrator:
    def catalog(self) -> dict: return get_catalog()
    def providers(self) -> list[dict]: return list_providers()
    def provider(self, provider_id: str) -> dict | None: return get_provider(provider_id)
    def domains(self) -> list[dict]: return list_domain_inventory()
    def domain(self, domain_id: str) -> dict | None: return get_domain(domain_id)
    def product_families(self) -> list[dict]: return list_product_families()
    def product_family(self, family_id: str) -> dict | None: return get_product_family(family_id)
    def dependency_map(self) -> dict:
        return {"success": True, "ecosystem_id": ECOSYSTEM_ID,
                "provider_edges": [{"provider_id": x["provider_id"], "relationship": "PROVIDER_METADATA_ONLY",
                                    "live_connection_verified": False} for x in self.providers()],
                "family_edges": [{"family_id": x["family_id"], "domain_ids": list(x["domain_ids"])}
                                 for x in self.product_families()],
                "remote_operations_enabled": False}
    def health(self) -> dict:
        catalog = get_catalog()
        return {"success": True, "ecosystem_id": ECOSYSTEM_ID, "status": "HEALTHY",
                "catalog_status": catalog["status"], "provider_count": catalog["provider_count"],
                "domain_count": catalog["domain_count"], "product_family_count": catalog["product_family_count"],
                "live_connection_verified": False, "remote_operations_enabled": False}
