"""Package-scoped read-only service for finance commercial classifications."""
from .orchestrator import FinanceServiceWorkBusinessOrchestrator

class FinanceBusinessPackageService:
    def __init__(self, orchestrator: FinanceServiceWorkBusinessOrchestrator | None = None) -> None:
        self._orchestrator = orchestrator or FinanceServiceWorkBusinessOrchestrator()

    def describe(self, package_name: str) -> dict | None:
        return self._orchestrator.get_package(package_name)

    def list_for_domain(self, domain_id: str) -> dict:
        return self._orchestrator.list_packages(business_domain_id=domain_id)

__all__ = ["FinanceBusinessPackageService"]
