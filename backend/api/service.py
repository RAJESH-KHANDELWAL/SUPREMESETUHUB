"""MAIN BASE FOUNDATION API module status service.

This service reports the core API layer's configured state. The actual HTTP
routes and request middleware live in the FastAPI application module.
"""

from __future__ import annotations

from backend.api.model import APIInfo


class APIService:
    def __init__(self) -> None:
        self.info = APIInfo(
            api_name="MAIN BASE FOUNDATION API",
            version="1.0",
            status="Available",
        )

    def initialize(self) -> dict:
        """Return stable startup metadata for the API core module."""
        return {
            **self.info.__dict__,
            "transport": "FastAPI",
            "private_routes": "AUTHENTICATION_REQUIRED",
        }

    def status(self) -> dict:
        """Return the API module status."""
        return self.initialize()

    def health(self) -> dict:
        """Return module-level health; this is not an external uptime probe."""
        return {
            "module": "API",
            "healthy": True,
            "status": self.info.status,
            "note": "Module readiness only; use the deployed /health endpoint for runtime health.",
        }
