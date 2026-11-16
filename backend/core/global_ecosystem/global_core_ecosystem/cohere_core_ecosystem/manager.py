"""Stable public manager facade for Cohere CORE."""
from __future__ import annotations

from .contracts import CapabilityRequest, CoreResult, TenantContext
from .service import CohereCoreService


class CohereCoreManager:
    def __init__(self) -> None:
        self.service = CohereCoreService()

    def list_capabilities(self):
        return self.service.capabilities()

    def validate(self, request: CapabilityRequest) -> CoreResult:
        return self.service.validate(request)

    def status(self):
        return self.service.status()

    def authorize_capability(self, capability: str, context: TenantContext | None) -> dict:
        return self.service.authorize_capability(capability, context)

    def authorize_operation(self, operation: str, *, explicitly_authorized: bool = False) -> None:
        self.service.authorize_operation(operation, explicitly_authorized=explicitly_authorized)
