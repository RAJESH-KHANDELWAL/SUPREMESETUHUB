"""Canonical manager for APPLE APP STORE CONNECT CORE ECOSYSTEM metadata."""
from __future__ import annotations
from typing import Any
from .service import AppleAppStoreConnectCoreService
class AppleAppStoreConnectCoreManager:
    def __init__(self) -> None: self._service = AppleAppStoreConnectCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def capabilities(self) -> dict[str, Any]: return self._service.capabilities()
    def authorize_capability(self, capability: str, context: Any = None) -> dict[str, Any]:
        return self._service.authorize_capability(capability, context)
def get_manager() -> AppleAppStoreConnectCoreManager: return AppleAppStoreConnectCoreManager()
__all__ = ["AppleAppStoreConnectCoreManager", "get_manager"]
