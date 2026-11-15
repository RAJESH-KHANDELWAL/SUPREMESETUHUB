"""DigiLocker application ecosystem package."""
from __future__ import annotations
from collections.abc import Callable, Mapping
from typing import Any

PROVIDER = {
    "id": "digilocker",
    "name": "DigiLocker",
    "origin": "india",
    "scope": "Digital documents and public-service application ecosystem",
    "integration_status": "catalog_only",
    "live_connection_verified": False,
}

class DigilockerAppAdapter:
    """Explicit integration boundary; no undocumented endpoint is called."""
    provider = PROVIDER
    def __init__(self, handler: Callable[[str, Mapping[str, Any]], Any] | None = None):
        self._handler = handler
    @property
    def configured(self) -> bool:
        return self._handler is not None
    def execute(self, operation: str, payload: Mapping[str, Any] | None = None) -> Any:
        if not operation or not operation.strip():
            raise ValueError("operation must be a non-empty string")
        if self._handler is None:
            raise RuntimeError("DigiLocker is catalog-only until an official, tested handler is configured")
        return self._handler(operation, payload or {})

__all__ = ["PROVIDER", "DigilockerAppAdapter"]
