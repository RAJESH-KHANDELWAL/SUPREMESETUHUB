"""Canonical read-only manager."""
from typing import Any
from .orchestrator import GlobalKamasutraCoreOrchestrator
from .service import GlobalKamasutraCoreService
from .domain_catalog import get_domain, list_domains
from .catalog import list_products
class GlobalKamasutraCoreManager:
    NAME = "GLOBAL KAMASUTRA RELATIONSHIP INTIMACY SEXUAL HEALTH AND ADULT WELLNESS CORE ECOSYSTEM"
    def __init__(self) -> None:
        self._orchestrator = GlobalKamasutraCoreOrchestrator()
        self._service = GlobalKamasutraCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_domains(self) -> list[dict[str, Any]]: return list_domains()
    def get_domain(self, domain_id: str) -> dict[str, Any] | None: return get_domain(domain_id)
    def list_products(self, *, enabled_only: bool = False) -> list[dict[str, Any]]: return list_products(enabled_only=enabled_only)
    def inventory(self) -> dict[str, Any]: return self._orchestrator.inventory()
def get_manager() -> GlobalKamasutraCoreManager: return GlobalKamasutraCoreManager()
__all__ = ["GlobalKamasutraCoreManager", "get_manager"]
