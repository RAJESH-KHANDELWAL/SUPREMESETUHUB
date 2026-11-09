"""Provider-neutral CLOUD orchestration facade with explicit adapter injection."""
from __future__ import annotations
from typing import Any
from .catalog import get_cloud_catalog
from .models import CloudOperationRequest, CloudOperationResult
from .adapters import CloudAdapterRegistry

class GlobalCloudEcosystemService:
    def __init__(self, adapters: tuple[Any, ...] = ()) -> None:
        self.adapters = CloudAdapterRegistry()
        for adapter in adapters:
            self.adapters.register(adapter)

    def catalog(self) -> dict[str, Any]:
        return get_cloud_catalog()

    def provider_status(self) -> list[dict[str, Any]]:
        catalog = self.catalog()
        configured = set(self.adapters.list_ids())
        for item in catalog["providers"]:
            item["status"] = "adapter_injected" if item["provider_id"] in configured else "not_configured"
        return catalog["providers"]

    def execute(self, request: CloudOperationRequest) -> CloudOperationResult:
        adapter = self.adapters.get(request.provider_id)
        executor = getattr(adapter, "execute", None)
        if not callable(executor):
            raise RuntimeError(f"CLOUD_ADAPTER_EXECUTION_UNAVAILABLE:{request.provider_id}")
        result = executor(request)
        if not isinstance(result, CloudOperationResult):
            raise TypeError("CLOUD_ADAPTER_MUST_RETURN_CloudOperationResult")
        return result

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem": "GLOBAL_CLOUD_ECOSYSTEM",
            "layer": "CLOUD",
            "status": "FOUNDATION_READY",
            "configured_adapters": list(self.adapters.list_ids()),
            "provider_count": len(self.catalog()["providers"]),
            "live_provider_connectivity_verified": False,
        }
