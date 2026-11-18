"""CORE orchestration for the GLOBAL BADA BUSINESS affiliate domain.

CORE owns validation and business workflow. It delegates persistence to the
DATABASE repository and does not call affiliate-provider APIs directly.
"""
from __future__ import annotations

from typing import Any

from .policies import (
    SUPPORTED_COMMISSION_TYPES,
    SUPPORTED_EVENT_TYPES,
    SUPPORTED_PROGRAM_STATUSES,
    SUPPORTED_VERIFICATION_STATUSES,
    validate_affiliate_disclosure,
    validate_http_url,
    validate_program_activation,
)

PLATFORM_IDS = frozenset({"I-DIGITALPRENEUR", "LEADSGURU", "MILLIONAIRE-TRACK"})


class AffiliateMarketingCoreService:
    """Coordinate program registration, referral creation and event capture."""

    def __init__(self, repository: Any):
        if repository is None:
            raise ValueError("AFFILIATE_MARKETING_REPOSITORY_REQUIRED")
        self.repository = repository

    @staticmethod
    def _required(value: str, field_name: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name}_REQUIRED")
        return value.strip()

    def register_program(
        self,
        *,
        program_id: str,
        platform_id: str,
        program_name: str,
        region: str = "GLOBAL",
        commission_type: str = "UNSPECIFIED",
        commission_rate: float = 0,
        currency: str = "USD",
        terms_url: str | None = None,
        verification_status: str = "UNVERIFIED",
        program_status: str = "PENDING_VERIFICATION",
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        program_id = self._required(program_id, "PROGRAM_ID")
        platform_id = self._required(platform_id, "PLATFORM_ID").upper()
        program_name = self._required(program_name, "PROGRAM_NAME")
        commission_type = commission_type.upper()
        verification_status = verification_status.upper()
        program_status = program_status.upper()
        currency = self._required(currency, "CURRENCY").upper()
        if platform_id not in PLATFORM_IDS:
            raise ValueError("AFFILIATE_PLATFORM_NOT_SUPPORTED")
        if commission_type not in SUPPORTED_COMMISSION_TYPES:
            raise ValueError("AFFILIATE_COMMISSION_TYPE_INVALID")
        if verification_status not in SUPPORTED_VERIFICATION_STATUSES:
            raise ValueError("AFFILIATE_VERIFICATION_STATUS_INVALID")
        if program_status not in SUPPORTED_PROGRAM_STATUSES:
            raise ValueError("AFFILIATE_PROGRAM_STATUS_INVALID")
        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("CURRENCY_MUST_BE_THREE_LETTERS")
        try:
            rate = float(commission_rate)
        except (TypeError, ValueError) as exc:
            raise ValueError("COMMISSION_RATE_MUST_BE_NUMERIC") from exc
        if rate < 0:
            raise ValueError("COMMISSION_RATE_CANNOT_BE_NEGATIVE")
        if terms_url:
            terms_url = validate_http_url(terms_url, "TERMS_URL")
        validate_program_activation(program_status, verification_status, terms_url)
        return self.repository.upsert_program(
            program_id=program_id,
            platform_id=platform_id,
            program_name=program_name,
            region=self._required(region, "REGION").upper(),
            commission_type=commission_type,
            commission_rate=rate,
            currency=currency,
            terms_url=terms_url,
            verification_status=verification_status,
            program_status=program_status,
            metadata=metadata or {},
        )

    def catalog(self, platform_id: str | None = None) -> list[dict[str, Any]]:
        normalized = platform_id.strip().upper() if platform_id else None
        if normalized and normalized not in PLATFORM_IDS:
            raise ValueError("AFFILIATE_PLATFORM_NOT_SUPPORTED")
        return self.repository.list_programs(normalized)

    def create_referral(
        self,
        *,
        owner_user_id: str,
        program_id: str,
        referral_code: str,
        destination_url: str,
        disclosure_text: str,
    ) -> dict[str, Any]:
        owner_user_id = self._required(owner_user_id, "OWNER_USER_ID")
        program_id = self._required(program_id, "PROGRAM_ID")
        referral_code = self._required(referral_code, "REFERRAL_CODE")
        destination_url = validate_http_url(destination_url, "DESTINATION_URL")
        disclosure_text = validate_affiliate_disclosure(disclosure_text)
        program = self.repository.get_program(program_id)
        if program is None:
            raise ValueError("AFFILIATE_PROGRAM_NOT_FOUND")
        if program["program_status"] != "ACTIVE":
            raise ValueError("AFFILIATE_PROGRAM_NOT_ACTIVE")
        return self.repository.create_referral(
            owner_user_id=owner_user_id,
            program_id=program_id,
            referral_code=referral_code,
            destination_url=destination_url,
            disclosure_text=disclosure_text,
        )

    def record_event(
        self,
        *,
        referral_id: str,
        source_event_id: str,
        event_type: str,
        amount_minor: int = 0,
        commission_minor: int = 0,
        currency: str,
        event_status: str = "PENDING",
        occurred_at: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        referral_id = self._required(referral_id, "REFERRAL_ID")
        source_event_id = self._required(source_event_id, "SOURCE_EVENT_ID")
        event_type = self._required(event_type, "EVENT_TYPE").upper()
        currency = self._required(currency, "CURRENCY").upper()
        event_status = self._required(event_status, "EVENT_STATUS").upper()
        if event_type not in SUPPORTED_EVENT_TYPES:
            raise ValueError("AFFILIATE_EVENT_TYPE_INVALID")
        if event_status not in {"PENDING", "APPROVED", "REJECTED", "PAID"}:
            raise ValueError("AFFILIATE_EVENT_STATUS_INVALID")
        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("CURRENCY_MUST_BE_THREE_LETTERS")
        for name, value in (("AMOUNT_MINOR", amount_minor), ("COMMISSION_MINOR", commission_minor)):
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"{name}_MUST_BE_A_NON_NEGATIVE_INTEGER")
        referral = self.repository.get_referral(referral_id)
        if referral is None:
            raise ValueError("AFFILIATE_REFERRAL_NOT_FOUND")
        if referral["referral_status"] != "ACTIVE":
            raise ValueError("AFFILIATE_REFERRAL_NOT_ACTIVE")
        if currency != referral["currency"]:
            raise ValueError("AFFILIATE_EVENT_CURRENCY_MISMATCH")
        return self.repository.record_event(
            referral_id=referral_id,
            source_event_id=source_event_id,
            event_type=event_type,
            amount_minor=amount_minor,
            commission_minor=commission_minor,
            currency=currency,
            event_status=event_status,
            occurred_at=occurred_at,
            metadata=metadata or {},
        )


__all__ = ["AffiliateMarketingCoreService", "PLATFORM_IDS"]
