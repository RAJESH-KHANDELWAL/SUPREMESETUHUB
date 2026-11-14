"""Small in-memory metadata registry; not a provider runtime."""
from __future__ import annotations

from typing import Any


class InfrastructureCatalogRegistry:
    """Register and retrieve catalog metadata without external side effects."""

    def __init__(self) -> None:
        self._records: dict[str, dict[str, Any]] = {}

    def register(self, record: dict[str, Any]) -> dict[str, Any]:
        record_id = str(record.get("id", "")).strip()
        if not record_id:
            raise ValueError("Catalog record requires a non-empty id.")
        if record_id in self._records:
            raise ValueError(f"Catalog record already exists: {record_id}")
        stored = dict(record)
        self._records[record_id] = stored
        return dict(stored)

    def get(self, record_id: str) -> dict[str, Any] | None:
        record = self._records.get(record_id)
        return dict(record) if record is not None else None

    def list_all(self) -> list[dict[str, Any]]:
        return [dict(item) for item in self._records.values()]
