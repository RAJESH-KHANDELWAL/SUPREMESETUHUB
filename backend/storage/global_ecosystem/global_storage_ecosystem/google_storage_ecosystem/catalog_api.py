"""Provider-neutral read API for Google's storage taxonomy."""
from __future__ import annotations
from typing import Any
from .ecosystem_taxonomy import list_ecosystems, find_ecosystem
from .ecosystem_service import EcosystemService

class GoogleStorageCatalog:
    """Catalog interface only; no provider API or file operations are performed."""
    def __init__(self) -> None:
        self._service = EcosystemService()

    def health(self) -> dict[str, Any]:
        return self._service.health()

    def list(self, *, group: str | None = None) -> list[dict[str, Any]]:
        rows = list_ecosystems()
        if group is None:
            return rows
        needle = group.strip().casefold()
        return [row for row in rows if needle in row["category"].casefold()]

    def get(self, name_or_id: str) -> dict[str, Any] | None:
        return find_ecosystem(name_or_id)
