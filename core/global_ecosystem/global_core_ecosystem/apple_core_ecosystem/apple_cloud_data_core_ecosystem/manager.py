"""Domain manager for Apple CLOUD DATA metadata."""
from __future__ import annotations
from typing import Any
from ..domain_runtime import AppleCoreDomainManager
class AppleCloudDataCoreManager:
    DOMAIN_ID = "CLOUD_DATA"
    def __init__(self) -> None: self._runtime = AppleCoreDomainManager(self.DOMAIN_ID)
    def status(self) -> dict[str, Any]: return self._runtime.status()
    def list_offerings(self) -> dict[str, Any]: return self._runtime.list_offerings()
    def get_offering(self, offering_id: str) -> dict[str, Any] | None: return self._runtime.get_offering(offering_id)
def get_manager() -> AppleCloudDataCoreManager: return AppleCloudDataCoreManager()
__all__ = ["AppleCloudDataCoreManager", "get_manager"]
