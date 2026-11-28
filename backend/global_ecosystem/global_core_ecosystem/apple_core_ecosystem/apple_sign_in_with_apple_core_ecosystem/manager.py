"""Canonical manager for APPLE_SIGN_IN_WITH_APPLE_CORE_ECOSYSTEM metadata."""
from __future__ import annotations
from typing import Any
from .service import AppleSignInWithAppleCoreService
class AppleSignInWithAppleCoreManager:
    def __init__(self) -> None: self._service = AppleSignInWithAppleCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def capabilities(self) -> dict[str, Any]: return self._service.capabilities()
    def authorize_capability(self, capability: str, context: Any = None) -> dict[str, Any]:
        return self._service.authorize_capability(capability, context)
def get_manager() -> AppleSignInWithAppleCoreManager: return AppleSignInWithAppleCoreManager()
__all__ = ["AppleSignInWithAppleCoreManager", "get_manager"]
