"""Public catalogue and capability discovery operations for this API."""
from __future__ import annotations

from typing import Any


class CultureServiceWorkBusinessCatalogue:
    """Expose CORE/ENGINE catalogue operations without duplicating their policy."""

    def __init__(self, core: Any, engine: Any) -> None:
        self.core = core
        self.engine = engine

    def list(self, domain: str | None = None) -> list[dict[str, Any]]:
        return self.engine.catalogue(domain)

    def get(self, capability_id: str) -> dict[str, Any] | None:
        normalized = str(capability_id or "").strip()
        if not normalized:
            raise ValueError("CAPABILITY_ID_REQUIRED")
        return self.core.capability(normalized)

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        normalized = str(query or "").strip()
        if not normalized:
            raise ValueError("SEARCH_QUERY_REQUIRED")
        return self.engine.search(normalized, domain)
