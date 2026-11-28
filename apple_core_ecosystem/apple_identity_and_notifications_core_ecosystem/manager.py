"""Domain manager for Apple IDENTITY AND NOTIFICATIONS metadata."""
from __future__ import annotations
from typing import Any
from ..domain_runtime import AppleCoreDomainManager
class AppleIdentityAndNotificationsCoreManager:
    DOMAIN_ID = "IDENTITY_AND_NOTIFICATIONS"
    def __init__(self) -> None: self._runtime = AppleCoreDomainManager(self.DOMAIN_ID)
    def status(self) -> dict[str, Any]: return self._runtime.status()
    def list_offerings(self) -> dict[str, Any]: return self._runtime.list_offerings()
    def get_offering(self, offering_id: str) -> dict[str, Any] | None: return self._runtime.get_offering(offering_id)
def get_manager() -> AppleIdentityAndNotificationsCoreManager: return AppleIdentityAndNotificationsCoreManager()
__all__ = ["AppleIdentityAndNotificationsCoreManager", "get_manager"]
