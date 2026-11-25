"""Canonical manager for APPLE_PAY_CORE_ECOSYSTEM metadata."""
from __future__ import annotations
from typing import Any
from .service import AppleApplePayCoreService
class AppleApplePayCoreManager:
    def __init__(self) -> None: self._service = AppleApplePayCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def capabilities(self) -> dict[str, Any]: return self._service.capabilities()
    def authorize_capability(self, capability: str, context: Any = None) -> dict[str, Any]:
        return self._service.authorize_capability(capability, context)
def get_manager() -> AppleApplePayCoreManager: return AppleApplePayCoreManager()
__all__ = ["AppleApplePayCoreManager", "get_manager"]
