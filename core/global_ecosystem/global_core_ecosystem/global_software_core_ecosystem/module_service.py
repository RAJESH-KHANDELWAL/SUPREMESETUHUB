"""Shared read-only service for provider-specific software Core packages."""
from __future__ import annotations
from typing import Any
from .catalog import get_software_core_catalog
from .policy import SoftwareCorePolicy
class SoftwareProviderCoreService:
    PROVIDER_ID=""
    def __init__(self):
        if not self.PROVIDER_ID: raise NotImplementedError("PROVIDER_ID_REQUIRED")
        self._provider=next((p for p in get_software_core_catalog()["providers"] if p["provider"]==self.PROVIDER_ID),None)
        if self._provider is None: raise LookupError(f"SOFTWARE_PROVIDER_NOT_REGISTERED: {self.PROVIDER_ID}")
    def status(self) -> dict[str, Any]:
        return {"success":True,**SoftwareCorePolicy.safe_provider_summary(self._provider),"core_layer":"GLOBAL_SOFTWARE_CORE","api_transport_in_core":False,"live_connection_verified":False}
    def capabilities(self) -> dict[str, Any]:
        values=self._provider.get("capabilities",[])
        return {"success":True,"provider":self.PROVIDER_ID,"count":len(values),"capabilities":[{"name":v,"authorization_class":SoftwareCorePolicy.classify_capability(v)} for v in values]}
