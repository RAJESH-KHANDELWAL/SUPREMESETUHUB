"""Canonical manager for Hugging Face provider CORE."""
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME
from .catalog import get_catalog
from .domain_catalog import get_domain
from .module_service import HuggingFaceProductCoreService
from .orchestrator import HuggingFaceCoreOrchestrator
from .service import HuggingFaceCoreEcosystemService

class HuggingFaceCoreManager:
    NAME = ECOSYSTEM_NAME
    ECOSYSTEM_ID = ECOSYSTEM_ID
    def __init__(self) -> None:
        self._orchestrator = HuggingFaceCoreOrchestrator()
        self._service = HuggingFaceCoreEcosystemService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def catalog(self) -> dict[str, Any]: return self._orchestrator.catalog()
    def list_products(self) -> list[dict[str, Any]]: return self._orchestrator.products()
    def get_product(self, product_id: str) -> dict[str, Any] | None: return self._orchestrator.product(product_id)
    def list_domains(self) -> list[dict[str, Any]]: return self._orchestrator.domains()
    def get_domain(self, domain_id: str) -> dict[str, Any] | None: return get_domain(domain_id)
    def get_product_manager(self, product_id: str) -> HuggingFaceProductCoreService:
        return HuggingFaceProductCoreService(product_id)
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()

def get_manager() -> HuggingFaceCoreManager:
    return HuggingFaceCoreManager()
__all__ = ["HuggingFaceCoreManager", "get_manager"]
