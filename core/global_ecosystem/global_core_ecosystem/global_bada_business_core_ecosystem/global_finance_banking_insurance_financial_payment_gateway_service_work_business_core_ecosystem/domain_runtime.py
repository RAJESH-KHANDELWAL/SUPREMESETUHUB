"""Read-only runtime for a registered finance service/work/business domain."""
from .domain_catalog import get_domain
from .product_catalog import list_packages

class FinanceServiceWorkBusinessDomainManager:
    def __init__(self, domain_id: str) -> None:
        item = get_domain(domain_id)
        if item is None:
            raise ValueError(f"UNKNOWN_FINANCE_BUSINESS_DOMAIN: {domain_id}")
        self.domain_id = item["domain_id"]

    def status(self) -> dict:
        item = get_domain(self.domain_id)
        packages = list_packages(business_domain_id=self.domain_id)
        return {
            "success": True,
            "domain_id": self.domain_id,
            "name": item["name"],
            "canonical_domain_id": item["core_domain_id"],
            "status": "BUSINESS_CLASSIFICATION_AVAILABLE",
            "package_count": len(packages),
            "service_work_business_capabilities": list(item["service_work_business_capabilities"]),
            "execution_enabled": False,
        }

    def list_packages(self) -> dict:
        items = list_packages(business_domain_id=self.domain_id)
        return {"success": True, "business_domain_id": self.domain_id, "count": len(items), "packages": items}

__all__ = ["FinanceServiceWorkBusinessDomainManager"]
