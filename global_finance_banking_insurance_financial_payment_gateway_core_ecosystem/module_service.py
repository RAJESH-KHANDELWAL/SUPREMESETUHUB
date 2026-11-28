"""Package-scoped read-only metadata service."""
from .orchestrator import FinanceCoreOrchestrator
class FinancePackageService:
    def __init__(self, orchestrator: FinanceCoreOrchestrator | None = None) -> None:
        self._orchestrator = orchestrator or FinanceCoreOrchestrator()
    def describe(self, package_name: str) -> dict | None: return self._orchestrator.get_package(package_name)
    def list_for_domain(self, domain_id: str) -> dict:
        return self._orchestrator.list_packages(domain_id=domain_id)
__all__ = ["FinancePackageService"]
