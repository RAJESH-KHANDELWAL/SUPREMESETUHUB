"""Stable service facade for classify CORE validation."""
from ..contracts import ClassifyRequest, validate_request

class CapabilityCoreService:
    capability = "classify"

    def validate(self, request: ClassifyRequest) -> bool:
        return validate_request(request)
