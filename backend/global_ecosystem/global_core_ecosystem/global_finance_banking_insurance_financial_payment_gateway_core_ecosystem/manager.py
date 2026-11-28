"""Stable public manager for Global Finance Core metadata."""
from .domain_runtime import FinanceCoreDomainManager
from .orchestrator import FinanceCoreOrchestrator
from .service import FinanceCoreEcosystemService
class FinanceCoreManager:
    NAME = "GLOBAL FINANCE BANKING INSURANCE FINANCIAL PAYMENT GATEWAY CORE ECOSYSTEM"
    ECOSYSTEM_ID = "GLOBAL-FINANCE-BANKING-INSURANCE-FINANCIAL-PAYMENT-GATEWAY-CORE-ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = FinanceCoreOrchestrator()
        self._service = FinanceCoreEcosystemService()
    def status(self) -> dict: return self._service.status()
    def health(self) -> dict:
        return {"success": True, "status": "HEALTHY_CATALOGUE", "catalogue_readable": True,
        "provider_connections_verified": 0, "transaction_execution_enabled": False}
    def list_domains(self) -> dict: return self._orchestrator.domains()
    def list_packages(self, *, domain_id: str | None = None) -> dict:
        return self._orchestrator.list_packages(domain_id=domain_id)
    def get_package(self, package_name: str) -> dict | None: return self._orchestrator.get_package(package_name)
    def get_domain_manager(self, domain_id: str) -> FinanceCoreDomainManager:
        return FinanceCoreDomainManager(domain_id)
def get_manager() -> FinanceCoreManager: return FinanceCoreManager()
__all__ = ["FinanceCoreManager", "get_manager"]
