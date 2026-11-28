"""Canonical manager for the Twilio Core Ecosystem."""
from __future__ import annotations
from typing import Any
from .orchestrator import TwilioCoreOrchestrator
from .service import TwilioCoreService

class TwilioCoreManager:
    NAME = "TWILIO CORE ECOSYSTEM"
    ECOSYSTEM_ID = "TWILIO-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self._service = TwilioCoreService()
        self._orchestrator = TwilioCoreOrchestrator()

    def status(self) -> dict[str, Any]:
        return self._service.status()

    def health(self) -> dict[str, Any]:
        return self._orchestrator.health()

    def inventory(self) -> dict[str, Any]:
        return self._service.inventory()

    def list_products(self, *, enabled_only: bool = False) -> list[dict[str, Any]]:
        return self._orchestrator.products(enabled_only=enabled_only)

    def dependency_map(self) -> dict[str, Any]:
        return self._orchestrator.dependency_map()

    def authorize_metadata_capability(self, capability: str, context) -> dict:
        return self._service.authorize_metadata_capability(capability, context)

def get_manager() -> TwilioCoreManager:
    return TwilioCoreManager()

__all__ = ["TwilioCoreManager", "get_manager"]
