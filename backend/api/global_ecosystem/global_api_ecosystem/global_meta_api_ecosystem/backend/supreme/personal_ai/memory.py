from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class SupremeMemory:
    """
    SUPREME PERSONAL AI memory layer.

    This is the first memory abstraction.
    Later, it can be connected to the existing database/storage
    foundation for persistent memory.
    """

    def __init__(self) -> None:
        self._records: list[dict[str, Any]] = []

    def remember(
        self,
        content: str,
        category: str = "general",
    ) -> dict[str, Any]:
        content = content.strip()

        if not content:
            raise ValueError("MEMORY_CONTENT_REQUIRED")

        category = category.strip().lower() or "general"

        record = {
            "id": f"memory-{len(self._records) + 1}",
            "content": content,
            "category": category,
            "created_at": datetime.now(
                timezone.utc
            ).isoformat(),
        }

        self._records.append(record)

        return record

    def list(
        self,
        category: str | None = None,
    ) -> list[dict[str, Any]]:
        if not category:
            return list(self._records)

        wanted = category.strip().lower()

        return [
            record
            for record in self._records
            if record["category"] == wanted
        ]

    def get(
        self,
        memory_id: str,
    ) -> dict[str, Any] | None:
        for record in self._records:
            if record["id"] == memory_id:
                return record

        return None

    def delete(
        self,
        memory_id: str,
    ) -> bool:
        for index, record in enumerate(self._records):
            if record["id"] == memory_id:
                del self._records[index]
                return True

        return False

    def clear(self) -> int:
        count = len(self._records)

        self._records.clear()

        return count

    def count(self) -> int:
        return len(self._records)
