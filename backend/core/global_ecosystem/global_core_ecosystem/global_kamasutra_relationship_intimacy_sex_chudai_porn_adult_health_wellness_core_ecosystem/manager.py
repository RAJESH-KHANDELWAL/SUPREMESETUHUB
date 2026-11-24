"""Canonical manager for the Global Kamasutra Core ecosystem."""
from __future__ import annotations

from typing import Any
from .orchestrator import GlobalKamasutraCoreOrchestrator
from .service import GlobalKamasutraCoreService
from .domain_runtime import get_domain_manager


class GlobalKamasutraCoreManager:
    NAME = "GLOBAL KAMASUTRA RELATIONSHIP INTIMACY SEXUAL HEALTH AND ADULT WELLNESS CORE ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = GlobalKamasutraCoreOrchestrator()
        self._service = GlobalKamasutraCoreService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_domains(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_domain(domain_id)

    def list_products(self, *, enabled_only: bool = False) -> list[dict[str, Any]]:
        from .catalog import list_products
        return list_products(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)

    def get_domain_manager(self, domain_id: str):
        return get_domain_manager(domain_id)

    def inventory(self) -> dict[str, Any]:
        return self._orchestrator.inventory()


def get_manager() -> GlobalKamasutraCoreManager:
    return GlobalKamasutraCoreManager()


__all__ = ["GlobalKamasutraCoreManager", "get_manager"]
