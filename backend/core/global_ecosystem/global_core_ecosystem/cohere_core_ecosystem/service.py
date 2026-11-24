"""Shared Cohere CORE validation and capability registry."""
from .contracts import CapabilityRequest, CoreResult
from .policies import ensure_operation_allowed
from .capabilities.catalog import CAPABILITIES

class CohereCoreService:
    def capabilities(self):
        return dict(CAPABILITIES)

    def validate(self, request: CapabilityRequest) -> CoreResult:
        capability = request.capability.strip().lower()
        if capability not in CAPABILITIES:
            return CoreResult(False, capability, errors=("Unsupported Cohere capability",), status="rejected")
        if not isinstance(request.inputs, dict) and not hasattr(request.inputs, "items"):
            return CoreResult(False, capability, errors=("inputs must be a mapping",), status="rejected")
        return CoreResult(True, capability, data={"model": request.model, "input_keys": tuple(request.inputs.keys())})

    def authorize_operation(self, operation: str) -> None:
        ensure_operation_allowed(operation)
