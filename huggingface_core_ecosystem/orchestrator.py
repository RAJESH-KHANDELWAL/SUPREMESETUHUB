"""Read-only discovery, dependency and health orchestration."""
from .catalog import get_catalog
from .product_catalog import get_product, list_products
from .domain_catalog import get_domain, list_domains
class HuggingFaceCoreOrchestrator:
    def catalog(self) -> dict: return get_catalog()
    def products(self) -> list[dict]: return list_products()
    def product(self, product_id: str) -> dict | None: return get_product(product_id)
    def domains(self) -> list[dict]: return list_domains()
    def domain(self, domain_id: str) -> dict | None: return get_domain(domain_id)
    def dependency_map(self) -> dict:
        return {"success": True, "provider_id": "huggingface",
                "dependencies": [{"layer": "API", "path": "backend/api/global_ecosystem/global_api_ecosystem/huggingface_api_ecosystem"},
                                 {"layer": "ENGINE", "path": "backend/engine/global_ecosystem/global_engine_ecosystem/huggingface_engine_ecosystem"},
                                 {"layer": "RUNTIME", "path": "backend/global_ecosystem/global_ai_ecosystem/huggingface_ecosystem"}],
                "product_api_mappings": [{"product_id": p["product_id"], "api_module": p["api_module"]} for p in self.products()],
                "remote_operations_enabled": False}
    def health(self) -> dict:
        c = get_catalog()
        return {"success": True, "ecosystem_id": c["ecosystem_id"], "status": "HEALTHY",
                "product_count": c["product_count"], "domain_count": c["domain_count"],
                "live_connection_verified": False, "remote_operations_enabled": False}
