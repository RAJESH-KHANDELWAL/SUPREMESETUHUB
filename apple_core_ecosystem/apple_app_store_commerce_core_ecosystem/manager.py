"""Domain manager for Apple APP STORE COMMERCE metadata."""
from __future__ import annotations
from typing import Any
from ..domain_runtime import AppleCoreDomainManager
class AppleAppStoreCommerceCoreManager:
    DOMAIN_ID = "APP_STORE_COMMERCE"
    def __init__(self) -> None: self._runtime = AppleCoreDomainManager(self.DOMAIN_ID)
    def status(self) -> dict[str, Any]: return self._runtime.status()
    def list_offerings(self) -> dict[str, Any]: return self._runtime.list_offerings()
    def get_offering(self, offering_id: str) -> dict[str, Any] | None: return self._runtime.get_offering(offering_id)
def get_manager() -> AppleAppStoreCommerceCoreManager: return AppleAppStoreCommerceCoreManager()
__all__ = ["AppleAppStoreCommerceCoreManager", "get_manager"]
