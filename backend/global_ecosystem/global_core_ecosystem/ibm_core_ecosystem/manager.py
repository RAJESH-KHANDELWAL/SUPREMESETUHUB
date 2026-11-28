"""Canonical IBM Core manager matching the Google Core manager contract."""
from __future__ import annotations
from typing import Any
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME
from .catalog import get_catalog
from .domain_catalog import get_domain
from .domain_runtime import IBMCoreDomainManager
from .module_service import IBMProductCoreService
from .orchestrator import IBMCoreOrchestrator
from .service import IBMCoreEcosystemService
class IBMCoreManager:
    NAME=ECOSYSTEM_NAME
    ECOSYSTEM_ID=ECOSYSTEM_ID
    def __init__(self) -> None:
        self._orchestrator=IBMCoreOrchestrator()
        self._service=IBMCoreEcosystemService()
    def status(self) -> dict[str,Any]: return self._service.status()
    def health(self) -> dict[str,Any]: return self._orchestrator.health()
    def catalog(self) -> dict[str,Any]: return self._orchestrator.catalog()
    def list_products(self) -> list[dict[str,Any]]: return self._orchestrator.products()
    def get_product(self,product_id: str) -> dict[str,Any] | None: return self._orchestrator.product(product_id)
    def list_domains(self) -> list[dict[str,Any]]: return self._orchestrator.domains()
    def get_domain(self,domain_id: str) -> dict[str,Any] | None: return get_domain(domain_id)
    def get_product_manager(self,product_id: str) -> IBMProductCoreService: return IBMProductCoreService(product_id)
    def get_domain_manager(self,domain_id: str) -> IBMCoreDomainManager: return IBMCoreDomainManager(domain_id)
    def dependency_map(self) -> dict[str,Any]: return self._orchestrator.dependency_map()
def get_manager() -> IBMCoreManager: return IBMCoreManager()
__all__=["IBMCoreManager","get_manager"]
