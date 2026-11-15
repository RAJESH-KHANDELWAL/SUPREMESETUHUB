"""Adapter boundary for the shared GLOBAL CLOUD service."""
from __future__ import annotations
from typing import Any
from .models import BadaBusinessCloudRequest

class GlobalCloudServiceAdapter:
    """Translate Bada Business cloud requests into the shared CLOUD contract."""
    def __init__(self, cloud_service: Any) -> None:
        if cloud_service is None:
            raise ValueError("GLOBAL_CLOUD_SERVICE_REQUIRED")
        self._cloud_service = cloud_service

    def execute(self, request: BadaBusinessCloudRequest) -> Any:
        # Lazy import keeps this package's contracts usable without provider SDKs.
        from ..models import CloudOperationRequest
        return self._cloud_service.execute(
            CloudOperationRequest(
                provider_id=request.provider_id,
                operation=request.operation,
                resource=request.resource,
                parameters=dict(request.parameters),
            )
        )
