"""CORE facade for canonical event snapshots."""
from __future__ import annotations
from typing import Any
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessEventsCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def list(self) -> dict[str, Any]:
        records = self.adapter.events()
        return {"success": True, "count": len(records), "events": list(records)}
