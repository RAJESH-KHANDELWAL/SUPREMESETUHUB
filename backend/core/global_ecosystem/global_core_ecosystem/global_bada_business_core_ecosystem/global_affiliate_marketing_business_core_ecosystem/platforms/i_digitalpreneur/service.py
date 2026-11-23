"""Repository-injected iDigitalPreneur CORE adapter.

All platform-specific operations are constrained to I-DIGITALPRENEUR and
reuse the parent affiliate CORE contracts. No provider API is called here.
"""
from __future__ import annotations

from typing import Any

from ...service import AffiliateMarketingCoreService
from .policies import PLATFORM_ID, validate_platform_id

class IDigitalPreneurCoreService:
    def __init__(self, repository: Any) -> None:
        self._service = AffiliateMarketingCoreService(repository)
        self.repository = repository

    def register_program(self, **record: Any) -> dict[str, Any]:
        supplied = record.pop("platform_id", PLATFORM_ID)
        validate_platform_id(supplied)
        return self._service.register_program(platform_id=PLATFORM_ID, **record)

    def catalog(self) -> list[dict[str, Any]]:
        return self._service.catalog(PLATFORM_ID)

    def _require_platform_program(self, program_id: str) -> dict[str, Any]:
        program = self.repository.get_program(program_id)
        if program is None:
            raise ValueError("AFFILIATE_PROGRAM_NOT_FOUND")
        validate_platform_id(program.get("platform_id", ""))
        return program

    def create_referral(self, **record: Any) -> dict[str, Any]:
        program_id = record.get("program_id", "")
        self._require_platform_program(program_id)
        return self._service.create_referral(**record)

    def record_event(self, **record: Any) -> dict[str, Any]:
        referral_id = record.get("referral_id", "")
        referral = self.repository.get_referral(referral_id)
        if referral is None:
            raise ValueError("AFFILIATE_REFERRAL_NOT_FOUND")
        self._require_platform_program(referral.get("program_id", ""))
        return self._service.record_event(**record)

__all__ = ["IDigitalPreneurCoreService"]
