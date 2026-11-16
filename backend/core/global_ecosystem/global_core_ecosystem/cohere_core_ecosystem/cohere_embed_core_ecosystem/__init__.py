"""Public contract exports for Cohere Embed CORE."""
from .contracts import EmbedRequest, validate_request
from .service import EmbedCoreService

__all__ = ["EmbedRequest", "validate_request", "EmbedCoreService"]
