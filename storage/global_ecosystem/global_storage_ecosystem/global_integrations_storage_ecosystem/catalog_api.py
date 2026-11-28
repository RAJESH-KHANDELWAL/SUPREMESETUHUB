"""Read-only catalog facade; this module performs no provider API calls."""
from __future__ import annotations
from .ecosystem_taxonomy import find_ecosystem, list_ecosystems
from .ecosystem_service import EcosystemService

class GlobalIntegrationsStorageCatalog:
    def __init__(self) -> None:
        self._service = EcosystemService()
    def health(self) -> dict:
        return self._service.health()
    def list(self, group: str | None = None) -> list[dict[str, str]]:
        rows = list_ecosystems()
        if group is None:
            return rows
        key = group.strip().casefold()
        return [row for row in rows if key in row.get("category", "").casefold()]
    def get(self, name_or_category: str) -> dict[str, str] | None:
        return find_ecosystem(name_or_category)
