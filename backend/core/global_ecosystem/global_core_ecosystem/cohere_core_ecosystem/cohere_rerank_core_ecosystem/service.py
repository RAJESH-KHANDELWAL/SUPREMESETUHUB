"""Capability-specific CORE validation entry point."""
from .contracts import RerankRequest, validate_request

class RerankCoreService:
    capability = "rerank"
    def validate(self, request: RerankRequest) -> bool:
        return validate_request(request)
