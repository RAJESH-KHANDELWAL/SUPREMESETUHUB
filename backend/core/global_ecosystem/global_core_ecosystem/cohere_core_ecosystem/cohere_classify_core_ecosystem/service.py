"""Capability-specific CORE validation entry point."""
from .contracts import ClassifyRequest, validate_request

class ClassifyCoreService:
    capability = "classify"

    def validate(self, request: ClassifyRequest) -> bool:
        return validate_request(request)
