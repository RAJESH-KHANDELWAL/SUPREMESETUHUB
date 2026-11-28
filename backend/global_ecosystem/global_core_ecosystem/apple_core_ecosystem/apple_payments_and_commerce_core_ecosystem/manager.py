"""Domain manager for Apple PAYMENTS AND COMMERCE metadata."""
from __future__ import annotations
from typing import Any
from ..domain_runtime import AppleCoreDomainManager
class ApplePaymentsAndCommerceCoreManager:
    DOMAIN_ID = "PAYMENTS_AND_COMMERCE"
    def __init__(self) -> None: self._runtime = AppleCoreDomainManager(self.DOMAIN_ID)
    def status(self) -> dict[str, Any]: return self._runtime.status()
    def list_offerings(self) -> dict[str, Any]: return self._runtime.list_offerings()
    def get_offering(self, offering_id: str) -> dict[str, Any] | None: return self._runtime.get_offering(offering_id)
def get_manager() -> ApplePaymentsAndCommerceCoreManager: return ApplePaymentsAndCommerceCoreManager()
__all__ = ["ApplePaymentsAndCommerceCoreManager", "get_manager"]
