"""Capability-specific CORE validation entry point."""
from .contracts import TokenizeRequest, validate_request

class TokenizeCoreService:
    capability = "tokenize"
    def validate(self, request: TokenizeRequest) -> bool:
        return validate_request(request)
