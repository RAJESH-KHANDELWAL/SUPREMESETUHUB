"""Read-only facade for canonical provider and referral destinations."""
from __future__ import annotations
from typing import Any
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessLinksCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def list(self) -> dict[str, Any]:
        records = self.adapter.links()
        return {"success": True, "count": len(records), "links": records}
    def extract_referral_code(self, url: str) -> dict[str, Any]:
        return {"success": True, "referral_code": self.adapter.referral_code(url)}
