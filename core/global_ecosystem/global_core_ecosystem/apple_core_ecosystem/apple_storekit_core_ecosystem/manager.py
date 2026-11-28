"""Canonical manager for APPLE_STOREKIT_CORE_ECOSYSTEM metadata."""
from __future__ import annotations
from typing import Any
from .service import AppleStorekitCoreService
class AppleStorekitCoreManager:
    def __init__(self) -> None: self._service = AppleStorekitCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def capabilities(self) -> dict[str, Any]: return self._service.capabilities()
    def authorize_capability(self, capability: str, context: Any = None) -> dict[str, Any]:
        return self._service.authorize_capability(capability, context)
def get_manager() -> AppleStorekitCoreManager: return AppleStorekitCoreManager()
__all__ = ["AppleStorekitCoreManager", "get_manager"]
