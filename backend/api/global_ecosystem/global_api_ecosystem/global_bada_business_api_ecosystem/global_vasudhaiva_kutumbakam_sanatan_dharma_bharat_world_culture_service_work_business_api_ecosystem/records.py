"""Record submission, validation and public retrieval operations."""
from __future__ import annotations

from typing import Any


class CultureServiceWorkBusinessRecords:
    """Keep record lifecycle rules in CORE and persistence in DATABASE."""

    PUBLIC_SUBMISSION_STATUSES = frozenset({"DRAFT", "SUBMITTED"})

    def __init__(self, core: Any, repository: Any) -> None:
        self.core = core
        self.repository = repository

    def validate(self, record: dict[str, Any]) -> list[str]:
        return self.core.validate(record)

    def can_publish(self, record: dict[str, Any]) -> bool:
        return self.core.can_publish(record)

    def submit(self, record: dict[str, Any]) -> dict[str, Any]:
        status = str(record.get("status", "DRAFT")).upper()
        if status not in self.PUBLIC_SUBMISSION_STATUSES:
            raise ValueError("PUBLIC_API_CANNOT_SET_MODERATION_STATUS")
        errors = self.validate(record)
        if errors:
            raise ValueError("RECORD_VALIDATION_FAILED:" + ",".join(errors))
        self.repository.save(record)
        return {
            "record_id": record["record_id"],
            "status": status,
            "publication_allowed": self.can_publish(record),
        }

    def get(self, record_id: str) -> dict[str, Any] | None:
        normalized = str(record_id or "").strip()
        if not normalized:
            raise ValueError("RECORD_ID_REQUIRED")
        return self.repository.get(normalized)

    def search(
        self, query: str = "", capability_id: str | None = None, limit: int = 50
    ) -> list[dict[str, Any]]:
        return self.repository.search(
            str(query or "").strip(),
            str(capability_id).strip() if capability_id is not None else None,
            limit,
        )
}
