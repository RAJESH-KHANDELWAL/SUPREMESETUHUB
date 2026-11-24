"""Oracle product/domain discovery and registry health."""
from .constants import ECOSYSTEM_ID
from .product_catalog import get_product, list_products
from .domain_catalog import list_domains

class OracleCoreOrchestrator:
    def list_products(self, *, enabled_only: bool = False) -> dict:
        items = list_products(enabled_only=enabled_only)
        return {"items": items, "count": len(items)}

    def get_product(self, product_id: str) -> dict | None:
        return get_product(product_id)

    def domains(self) -> dict:
        items = list_domains()
        return {"items": items, "count": len(items)}

    def health(self) -> dict:
        products = list_products()
        return {"ecosystem_id": ECOSYSTEM_ID, "status": "HEALTHY_METADATA_REGISTRY",
                "product_count": len(products), "domain_count": len(list_domains()),
                "live_connections_verified": 0, "catalog_only_products": len(products)}

    def dependency_map(self) -> dict:
        from .constants import API_ECOSYSTEM_REF, ENGINE_ECOSYSTEM_REF
        return {"api": API_ECOSYSTEM_REF, "engine": ENGINE_ECOSYSTEM_REF,
                "ownership": "references_only_no_runtime_calls"}
