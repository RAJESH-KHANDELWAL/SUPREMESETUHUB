"""Read-only orchestrator for finance catalogue and domain discovery."""
from .catalog import FINANCE_ECOSYSTEM_CATALOG
from .domain_catalog import DOMAIN_DEFINITIONS, DOMAIN_PACKAGES, finance_domain_summary
from .product_catalog import FINANCE_PACKAGES
class FinanceCoreOrchestrator:
    def status(self) -> dict:
        return {"success": True, "ecosystem_id": FINANCE_ECOSYSTEM_CATALOG["ecosystem_id"],
        "name": FINANCE_ECOSYSTEM_CATALOG["name"], "status": "CORE_CATALOG_AVAILABLE",
        "domain_count": len(DOMAIN_DEFINITIONS), "package_count": len(FINANCE_PACKAGES),
        "provider_connections_verified": 0, "transaction_execution_enabled": False}
    def domains(self) -> dict: return finance_domain_summary()
    def list_packages(self, *, domain_id: str | None = None) -> dict:
        if domain_id is not None and domain_id not in DOMAIN_PACKAGES:
            return {"success": False, "count": 0, "packages": [], "errors": ["UNKNOWN_DOMAIN"]}
        items = [dict(x) for x in FINANCE_PACKAGES if domain_id is None or x["domain_id"] == domain_id]
        return {"success": True, "count": len(items), "packages": items}
    def get_package(self, package_name: str) -> dict | None:
        needle = package_name.strip().casefold()
        if not needle: return None
        return next((dict(x) for x in FINANCE_PACKAGES if x["package_name"].casefold() == needle
                     or x["package_id"].casefold() == needle), None)
    def dependency_map(self) -> dict:
        return {"catalog":"catalog.py","domain_catalog":"domain_catalog.py","product_catalog":"product_catalog.py",
        "domain_runtime":"domain_runtime.py","orchestrator":"orchestrator.py","manager":"manager.py",
        "service":"service.py","external_integrations":"backend/api and provider integration layers",
        "secret_storage":"external secret manager only"}
