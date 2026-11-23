"""Stable public manager matching the Google Core control-plane pattern."""
from __future__ import annotations
from typing import Any
from .domain_runtime import FinanceServiceWorkBusinessDomainManager
from .orchestrator import FinanceServiceWorkBusinessOrchestrator
from .service import FinanceServiceWorkBusinessService

class FinanceServiceWorkBusinessManager:
    NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY SERVICE WORK BUSINESS CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = FinanceServiceWorkBusinessOrchestrator()
        self._service = FinanceServiceWorkBusinessService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def catalog(self) -> dict[str, Any]:
        return self._orchestrator.catalog()

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def get_domain_manager(self, domain_id: str) -> FinanceServiceWorkBusinessDomainManager:
        return FinanceServiceWorkBusinessDomainManager(domain_id)

    def list_packages(self, *, business_domain_id: str | None = None) -> dict[str, Any]:
        return self._orchestrator.packages(business_domain_id=business_domain_id)

    def get_package(self, package_name: str) -> dict[str, Any] | None:
        return self._orchestrator.get_package(package_name)

    def list_offerings(self) -> dict[str, Any]:
        return self.list_packages()

    def get_offering(self, package_name: str) -> dict[str, Any] | None:
        return self.get_package(package_name)

    def search(self, keyword: str) -> dict[str, Any]:
        return self._orchestrator.search(keyword)

    def classify(self, domain_id: str, classification_type: str, **kwargs: Any) -> dict[str, Any]:
        return self._service.classify(domain_id, classification_type, **kwargs)

    def validate(self) -> dict[str, Any]:
        return self._service.validate()

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

def get_manager() -> FinanceServiceWorkBusinessManager:
    return FinanceServiceWorkBusinessManager()

__all__ = ["FinanceServiceWorkBusinessManager", "get_manager"]
