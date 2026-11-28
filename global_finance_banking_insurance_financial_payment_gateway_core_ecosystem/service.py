"""Application-facing read-only service for finance ecosystem metadata."""
from .catalog import FINANCE_ECOSYSTEM_CATALOG
from .domain_catalog import finance_domain_summary
from .product_catalog import finance_packages_summary
class FinanceCoreEcosystemService:
    def status(self) -> dict:
        domains = finance_domain_summary()
        packages = finance_packages_summary()
        return {"success": True, "ecosystem_id": FINANCE_ECOSYSTEM_CATALOG["ecosystem_id"],
        "name": FINANCE_ECOSYSTEM_CATALOG["name"], "status": "CORE_CATALOG_AVAILABLE",
        "domain_count": domains["domain_count"], "package_count": packages["package_count"],
        "provider_connections_verified": 0, "transaction_execution_enabled": False}
    def overview(self) -> dict: return {**self.status(), "domains": finance_domain_summary()["domains"]}
