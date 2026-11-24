"""Canonical Oracle Core manager; metadata only, no remote operations."""
from typing import Any
from .orchestrator import OracleCoreOrchestrator
from .service import OracleCoreEcosystemService
from .module_service import OracleProductCoreService

class OracleCoreManager:
    NAME = "ORACLE CORE ECOSYSTEM"
    ECOSYSTEM_ID = "ORACLE-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = OracleCoreOrchestrator()
        self._service = OracleCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(product_id)

    def list_domains(self) -> dict[str, Any]:
        return self._orchestrator.domains()

    def get_product_manager(self, product_id: str) -> OracleProductCoreService:
        return OracleProductCoreService(product_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

def get_manager() -> OracleCoreManager:
    return OracleCoreManager()

__all__ = ["OracleCoreManager", "get_manager"]
