"""Canonical manager for APPLE_APP_STORE_SERVER_CORE_ECOSYSTEM metadata."""
from __future__ import annotations
from typing import Any
from .service import AppleAppStoreServerCoreService
class AppleAppStoreServerCoreManager:
    def __init__(self) -> None: self._service = AppleAppStoreServerCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def capabilities(self) -> dict[str, Any]: return self._service.capabilities()
    def authorize_capability(self, capability: str, context: Any = None) -> dict[str, Any]:
        return self._service.authorize_capability(capability, context)
def get_manager() -> AppleAppStoreServerCoreManager: return AppleAppStoreServerCoreManager()
__all__ = ["AppleAppStoreServerCoreManager", "get_manager"]
