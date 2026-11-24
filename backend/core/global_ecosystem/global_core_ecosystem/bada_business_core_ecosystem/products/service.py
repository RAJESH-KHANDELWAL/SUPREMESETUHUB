"""Product discovery facade; empty until canonical product records are supplied."""
from __future__ import annotations
from typing import Any
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessProductsCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def list(self) -> dict[str, Any]:
        records = self.adapter.products()
        return {"success": True, "count": len(records), "products": records, "status": "NO_CANONICAL_PRODUCT_RECORDS_PUBLISHED" if not records else "CATALOG_ONLY"}
