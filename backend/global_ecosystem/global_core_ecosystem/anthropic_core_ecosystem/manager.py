"""Canonical manager entry point for Anthropic Core Ecosystem."""
from __future__ import annotations

from typing import Any

from .orchestrator import AnthropicCoreOrchestrator
from .domain_runtime import AnthropicCoreDomainManager
from .service import AnthropicCoreEcosystemService


class AnthropicCoreManager:
    NAME = "ANTHROPIC CORE ECOSYSTEM"
    ECOSYSTEM_ID = "ANTHROPIC-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._orchestrator = AnthropicCoreOrchestrator()
        self._service = AnthropicCoreEcosystemService()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def list_products(self, *, enabled_only: bool = False) -> dict[str, Any]:
        return self._orchestrator.list_products(enabled_only=enabled_only)

    def get_product(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._orchestrator.get_product(ecosystem_id)

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

    def get_domain_manager(self, domain_id: str) -> AnthropicCoreDomainManager:
        return AnthropicCoreDomainManager(domain_id)


def get_manager() -> AnthropicCoreManager:
    return AnthropicCoreManager()


__all__ = ["AnthropicCoreManager", "get_manager"]
