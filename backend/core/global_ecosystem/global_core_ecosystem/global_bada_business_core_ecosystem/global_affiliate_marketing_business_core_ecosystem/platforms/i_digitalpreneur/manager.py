"""Manager for the iDigitalPreneur-specific affiliate CORE ecosystem."""
from __future__ import annotations

from typing import Any

from .models import IDigitalPreneurIdentity
from .policies import PLATFORM_ID, validate_platform_id

class IDigitalPreneurCoreManager:
    ECOSYSTEM_ID = "I-DIGITALPRENEUR-CORE-ECOSYSTEM"
    PARENT_ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self.identity = IDigitalPreneurIdentity()

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "parent_ecosystem_id": self.PARENT_ECOSYSTEM_ID,
            "platform_id": self.identity.platform_id,
            "platform_name": self.identity.platform_name,
            "layer": "CORE",
            "status": "IDENTITY_READY_TERMS_UNVERIFIED",
            "verification_status": "UNVERIFIED",
            "program_terms_verified": False,
            "live_connection_verified": False,
            "payout_execution_enabled": False,
        }

    def get_identity(self, platform_id: str = PLATFORM_ID) -> IDigitalPreneurIdentity:
        validate_platform_id(platform_id)
        return self.identity

    def supports(self, platform_id: str) -> bool:
        try:
            validate_platform_id(platform_id)
        except ValueError:
            return False
        return True

def get_manager() -> IDigitalPreneurCoreManager:
    return IDigitalPreneurCoreManager()

__all__ = ["IDigitalPreneurCoreManager", "get_manager"]
