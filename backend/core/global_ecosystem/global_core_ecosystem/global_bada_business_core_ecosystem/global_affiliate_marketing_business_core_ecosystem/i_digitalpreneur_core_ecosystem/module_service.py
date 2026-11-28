"""Read-only discovery facade for the iDigitalPreneur CORE identity."""
from __future__ import annotations

from typing import Any

from .manager import IDigitalPreneurCoreManager


class IDigitalPreneurModuleService:
    def __init__(self) -> None:
        self.manager = IDigitalPreneurCoreManager()

    def status(self) -> dict[str, Any]:
        return self.manager.status()

    def identity(self) -> dict[str, Any]:
        identity = self.manager.get_identity()
        return {
            "platform_id": identity.platform_id,
            "platform_name": identity.platform_name,
            "layer": identity.layer,
            "ecosystem_id": identity.ecosystem_id,
            "parent_ecosystem_id": identity.parent_ecosystem_id,
            "verification_status": identity.verification_status,
            "program_terms_verified": identity.program_terms_verified,
            "live_connection_verified": identity.live_connection_verified,
        }


__all__ = ["IDigitalPreneurModuleService"]
