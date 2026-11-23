"""Typed identity model for the iDigitalPreneur CORE ecosystem."""
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class IDigitalPreneurIdentity:
    platform_id: str = "I-DIGITALPRENEUR"
    platform_name: str = "iDigitalPreneur"
    layer: str = "CORE"
    ecosystem_id: str = "I-DIGITALPRENEUR-CORE-ECOSYSTEM"
    parent_ecosystem_id: str = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"
    verification_status: str = "UNVERIFIED"
    program_terms_verified: bool = False
    live_connection_verified: bool = False
    payout_execution_enabled: bool = False

__all__ = ["IDigitalPreneurIdentity"]
