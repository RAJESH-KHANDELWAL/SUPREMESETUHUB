"""Normalized errors for Adobe API transport."""
from __future__ import annotations

class AdobeApiError(RuntimeError):
    """Base error with safe, non-secret diagnostic metadata."""
    def __init__(self, message: str, *, status_code: int | None = None, retryable: bool = False) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.retryable = retryable

class AdobeAuthenticationError(AdobeApiError):
    """Authentication or authorization failed; never include token values."""

class AdobeRateLimitError(AdobeApiError):
    """Provider throttled the request."""

class AdobeTransportError(AdobeApiError):
    """Network, timeout, or upstream server failure."""

class AdobeResponseError(AdobeApiError):
    """Unexpected or non-successful API response."""
