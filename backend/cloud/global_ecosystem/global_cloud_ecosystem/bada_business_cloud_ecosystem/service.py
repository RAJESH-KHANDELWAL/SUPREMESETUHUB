"""Bada Business CLOUD domain service with fail-closed approval checks."""
from __future__ import annotations
from typing import Any
from .catalog import CLOUD_CAPABILITIES, get_bada_business_cloud_catalog
from .models import BadaBusinessCloudRequest, BadaBusinessCloudResult
from .policies import BADA_BUSINESS_CLOUD_POLICY
from .resource_adapter import GlobalCloudServiceAdapter

class BadaBusinessCloudService:
    def __init__(self, cloud_service: Any = None) -> None:
        self._adapter = GlobalCloudServiceAdapter(cloud_service) if cloud_service is not None else None

    def catalog(self) -> dict[str, Any]:
        return get_bada_business_cloud_catalog()

    def status(self) -> dict[str, Any]:
        return {
            "ecosystem": "BADA_BUSINESS_CLOUD_ECOSYSTEM",
            "layer": "CLOUD",
            "status": "CLOUD_INTEGRATION_FOUNDATION_READY",
            "shared_cloud_service_injected": self._adapter is not None,
            "provider_execution_enabled": self._adapter is not None,
            "credentials_configured": False,
        }

    def execute(self, request: BadaBusinessCloudRequest) -> BadaBusinessCloudResult:
        capability = next((item for item in CLOUD_CAPABILITIES if item["id"] == request.capability_id), None)
        if capability is None:
            raise KeyError(f"BADA_BUSINESS_CLOUD_CAPABILITY_NOT_FOUND:{request.capability_id}")
        if request.operation not in capability["operations"]:
            raise ValueError(f"OPERATION_NOT_ALLOWED_FOR_CAPABILITY:{request.operation}")
        if request.operation in BADA_BUSINESS_CLOUD_POLICY["approval_required_operations"] and not request.approved:
            return BadaBusinessCloudResult(
                request.capability_id, request.provider_id, request.operation,
                "pending_approval", {"approval_required": True},
            )
        if request.operation not in (
            BADA_BUSINESS_CLOUD_POLICY["read_only_operations"]
            + BADA_BUSINESS_CLOUD_POLICY["approval_required_operations"]
        ):
            raise ValueError(f"CLOUD_OPERATION_NOT_CLASSIFIED:{request.operation}")
        if self._adapter is None:
            raise RuntimeError("BADA_BUSINESS_CLOUD_ADAPTER_NOT_CONFIGURED")
        raw = self._adapter.execute(request)
        return BadaBusinessCloudResult(
            capability_id=request.capability_id,
            provider_id=request.provider_id,
            operation=request.operation,
            status=getattr(raw, "status", "completed"),
            details=dict(getattr(raw, "details", {}) or {}),
        )
