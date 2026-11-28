"""Read-only referral metadata utilities; no commission or conversion claims."""
from __future__ import annotations
from ..resource_adapter import BadaBusinessResourceAdapter

class BadaBusinessReferralsCoreService:
    def __init__(self, adapter: BadaBusinessResourceAdapter | None = None) -> None:
        self.adapter = adapter or BadaBusinessResourceAdapter()
    def extract_code(self, url: str) -> dict[str, object]:
        return {"success": True, "referral_code": self.adapter.referral_code(url)}
