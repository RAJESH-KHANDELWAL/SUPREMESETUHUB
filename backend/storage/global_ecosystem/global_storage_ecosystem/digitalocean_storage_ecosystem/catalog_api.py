"""Read-only catalog interface; performs no DigitalOcean API calls."""
from __future__ import annotations
from typing import Any
from .ecosystem_taxonomy import list_ecosystems, find_ecosystem
from .ecosystem_service import EcosystemService

class DigitalOceanStorageCatalog:
    """Expose taxonomy metadata without moving or modifying user data."""
    def __init__(self) -> None:
        self._service = EcosystemService()
    def health(self) -> dict[str, Any]:
        return self._service.health()
    def list(self, group: str | None = None) -> list[dict[str, str]]:
        rows = list_ecosystems()
        if group is None:
            return rows
        key = group.strip().casefold()
        return [row for row in rows if key in row["group"].casefold()]
    def get(self, name_or_category: str) -> dict[str, str] | None:
        return find_ecosystem(name_or_category)
