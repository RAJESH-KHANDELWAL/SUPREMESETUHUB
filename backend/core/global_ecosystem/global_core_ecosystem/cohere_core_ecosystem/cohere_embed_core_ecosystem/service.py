"""Capability-specific CORE validation entry point."""
from .contracts import EmbedRequest, validate_request

class EmbedCoreService:
    capability = "embed"

    def validate(self, request: EmbedRequest) -> bool:
        return validate_request(request)
