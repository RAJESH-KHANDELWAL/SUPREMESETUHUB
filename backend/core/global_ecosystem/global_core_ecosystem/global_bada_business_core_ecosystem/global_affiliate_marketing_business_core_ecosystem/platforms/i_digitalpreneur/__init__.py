"""Isolated iDigitalPreneur CORE adapter over the affiliate business domain.

This module owns platform identity and enforces that all program operations
remain scoped to iDigitalPreneur. It does not verify external terms or connect
to provider APIs.
"""
from __future__ import annotations

from typing import Any

from ...models import AffiliatePlatformIdentity
from ...service import AffiliateMarketingCoreService
from ...policies import (
    validate_http_url,
    validate_program_activation,
)

PLATFORM_ID = "I-DIGITALPRENEUR"
PLATFORM_NAME = "iDigitalPreneur"
LAYER = "CORE"
ECOSYSTEM_ID = "I-DIGITALPRENEUR-CORE-ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM"


def validate_platform_program(
    *,
    platform_id: str,
    program_status: str,
    verification_status: str,
    terms_url: str | None,
) -> bool:
    """Validate program policy while rejecting cross-platform identities."""
    if not isinstance(platform_id, str) or platform_id.strip().upper() != PLATFORM_ID:
        raise ValueError("PLATFORM_ID_MISMATCH")
    status = str(program_status).strip().upper()
    verification = str(verification_status).strip().upper()
    if terms_url:
        validate_http_url(terms_url, "TERMS_URL")
    validate_program_activation(status, verification, terms_url)
    return True


class IDigitalPreneurCoreManager:
    """Expose the platform's isolated, explicitly unverified CORE status."""

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "platform_id": PLATFORM_ID,
            "platform_name": PLATFORM_NAME,
            "layer": LAYER,
            "program_terms_verified": False,
            "live_connection_verified": False,
            "status": "IDENTITY_REGISTERED_PENDING_VERIFICATION",
        }


class IDigitalPreneurModuleService:
    """Read-only identity adapter for the canonical affiliate platform catalog."""

    def identity(self) -> dict[str, Any]:
        return {
            "ecosystem_id": ECOSYSTEM_ID,
            "platform_id": PLATFORM_ID,
            "platform_name": PLATFORM_NAME,
            "parent_ecosystem_id": PARENT_ECOSYSTEM_ID,
            "layer": LAYER,
            "read_only": True,
            "program_terms_verified": False,
            "live_connection_verified": False,
        }

    def get(self) -> AffiliatePlatformIdentity:
        from ...catalog import get_platform

        record = get_platform(PLATFORM_ID)
        if record is None:
            raise LookupError("IDIGITALPRENEUR_PLATFORM_NOT_REGISTERED")
        return AffiliatePlatformIdentity.from_record(record)


class IDigitalPreneurCoreService:
    """Force every program operation through the iDigitalPreneur identity."""

    def __init__(self, repository: Any):
        self._service = AffiliateMarketingCoreService(repository)

    def register_program(self, *, program_id: str, program_name: str, **kwargs: Any) -> dict[str, Any]:
        return self._service.register_program(
            program_id=program_id,
            platform_id=PLATFORM_ID,
            program_name=program_name,
            **kwargs,
        )

    def catalog(self) -> list[dict[str, Any]]:
        return self._service.catalog(platform_id=PLATFORM_ID)

    def create_referral(self, **kwargs: Any) -> dict[str, Any]:
        program_id = kwargs.get("program_id")
        if not isinstance(program_id, str) or not program_id.strip():
            raise ValueError("PROGRAM_ID_REQUIRED")
        # Prevent referrals from being created against another platform's program.
        program = self._service.repository.get_program(program_id.strip())
        if program is None:
            raise ValueError("AFFILIATE_PROGRAM_NOT_FOUND")
        if str(program.get("platform_id", "")).strip().upper() != PLATFORM_ID:
            raise ValueError("PLATFORM_ID_MISMATCH")
        return self._service.create_referral(**kwargs)


__all__ = [
    "PLATFORM_ID",
    "PLATFORM_NAME",
    "LAYER",
    "ECOSYSTEM_ID",
    "IDigitalPreneurCoreManager",
    "IDigitalPreneurCoreService",
    "IDigitalPreneurModuleService",
    "validate_platform_program",
]
