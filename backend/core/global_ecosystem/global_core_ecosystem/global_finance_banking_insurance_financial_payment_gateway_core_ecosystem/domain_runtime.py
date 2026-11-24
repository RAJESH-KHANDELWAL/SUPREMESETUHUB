"""Shared read-only runtime for finance domain discovery."""
from typing import Any
from .domain_catalog import DOMAIN_DEFINITIONS, DOMAIN_PACKAGES
class FinanceCoreDomainManager:
    def __init__(self, domain_id: str) -> None:
        if domain_id not in DOMAIN_DEFINITIONS: raise ValueError(f"UNKNOWN_FINANCE_CORE_DOMAIN: {domain_id}")
        self.domain_id = domain_id
    def status(self) -> dict[str, Any]:
        item = DOMAIN_DEFINITIONS[self.domain_id]
        return {"success": True, "domain_id": self.domain_id, "name": item["name"],
        "purpose": item["purpose"], "status": "CORE_DOMAIN_AVAILABLE",
        "package_count": len(DOMAIN_PACKAGES[self.domain_id]), "live_connections_verified": 0,
        "financial_transactions_performed": 0}
    def list_packages(self) -> dict[str, Any]:
        names = DOMAIN_PACKAGES[self.domain_id]
        return {"success": True, "domain_id": self.domain_id, "count": len(names), "packages": list(names)}
__all__ = ["FinanceCoreDomainManager"]
