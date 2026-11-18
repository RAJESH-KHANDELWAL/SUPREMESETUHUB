"""CORE facade for canonical Bada Business course records."""
from __future__ import annotations
from typing import Any
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessCoursesCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def list(self) -> dict[str, Any]:
        records = self.adapter.courses()
        return {"success": True, "count": len(records), "courses": list(records)}
    def get(self, course_id: str) -> dict[str, Any]:
        record = self.adapter.course(course_id)
        return {"success": record is not None, "course": record}
