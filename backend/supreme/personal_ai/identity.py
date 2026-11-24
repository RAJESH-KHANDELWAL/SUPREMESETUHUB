from __future__ import annotations

from typing import Any


class SupremeIdentity:
    """
    SUPREME PERSONAL AI identity layer.

    This layer defines the owner-controlled identity and
    operating context of SUPREME.
    """

    NAME = "SUPREME"
    TYPE = "PERSONAL_AI"
    VERSION = "1.0.0"

    OWNER_ROLE = "OWNER"

    BRAND = "👑 DR RAJESH KHANDELWAL IBC 👑"

    MODE = "OWNER_PERSONAL_AI"

    def context(self) -> dict[str, Any]:
        return {
            "name": self.NAME,
            "type": self.TYPE,
            "version": self.VERSION,
            "owner_role": self.OWNER_ROLE,
            "brand": self.BRAND,
            "mode": self.MODE,
            "status": "READY",
        }

    def is_owner_mode(self, actor_role: str) -> bool:
        return actor_role.strip().upper() == self.OWNER_ROLE
