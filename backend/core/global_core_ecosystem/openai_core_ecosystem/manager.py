"""Canonical manager for the OpenAI Core Ecosystem."""
from __future__ import annotations

from typing import Any

from .domain_runtime import OpenAICoreDomainManager
from .orchestrator import OpenAICoreOrchestrator
from .service import OpenAICoreEcosystemService


class OpenAICoreManager:
    """Stable application entry point for OpenAI Core metadata."""

    NAME = "OPENAI CORE ECOSYSTEM"
    ECOSYSTEM_ID = "OPENAI-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = OpenAICoreOrchestrator()
        self._service = OpenAICoreEcosystemService()

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

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return self._orchestrator.domain_inventory()

    def list_offerings(self) -> dict[str, Any]:
        return self._orchestrator.offerings()

    def get_offering(self, product_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_offering(product_id)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def get_domain_manager(self, domain_id: str) -> OpenAICoreDomainManager:
        return OpenAICoreDomainManager(domain_id)


def get_manager() -> OpenAICoreManager:
    """Return the canonical OpenAI Core manager."""
    return OpenAICoreManager()


__all__ = ["OpenAICoreManager", "get_manager"]
