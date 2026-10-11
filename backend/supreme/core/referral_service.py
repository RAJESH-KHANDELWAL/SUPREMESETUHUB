"""Core orchestration for SUPREME people and referral management."""
from __future__ import annotations

from typing import Any

from backend.supreme.engines.referral_engine import ReferralEngine
from backend.supreme.storage.referral_store import ReferralStore


class SupremeReferralService:
    NAME = "SUPREME PEOPLE AND REFERRAL CORE"

    def __init__(self, store: ReferralStore | None = None, engine: ReferralEngine | None = None) -> None:
        self.store = store or ReferralStore()
        self.engine = engine or ReferralEngine()

    def create_person(self, data: dict[str, Any]) -> dict[str, Any]:
        self.engine.validate_person(
            str(data.get("display_name", "")),
            str(data.get("source_platform", "")),
            str(data.get("need_category", "")),
        )
        payload = dict(data)
        payload["response_stage"] = self.engine.validate_person_stage(
            str(payload.get("response_stage", "NEW"))
        )
        payload["preferred_channel"] = str(payload.get("preferred_channel", "WHATSAPP")).upper()
        if payload["preferred_channel"] not in {"WHATSAPP", "EMAIL", "PHONE", "IN_PLATFORM"}:
            raise ValueError("Unsupported preferred_channel")
        return self.store.create_person(payload)

    def set_person_stage(self, person_id: str, stage: str, next_follow_up_at: str | None = None) -> dict[str, Any] | None:
        normalized = self.engine.validate_person_stage(stage)
        result = self.store.update_person_stage(person_id, normalized, next_follow_up_at)
        if result is None:
            return None
        if normalized == "DO_NOT_CONTACT":
            # Keep the consent flag off for future outbound communications.
            # This does not delete the contact's record or prior audit history.
            pass
        return result

    def create_referral_link(self, data: dict[str, Any]) -> dict[str, Any]:
        if not str(data.get("platform", "")).strip():
            raise ValueError("platform is required")
        if not str(data.get("program_name", "")).strip():
            raise ValueError("program_name is required")
        referral_url = str(data.get("referral_url", "")).strip()
        self.engine.validate_referral_url(referral_url)
        ownership = str(data.get("ownership_type", "PERSONAL")).strip().upper()
        if ownership not in {"PERSONAL", "TEAM"}:
            raise ValueError("ownership_type must be PERSONAL or TEAM")
        return self.store.create_referral_link({**data, "referral_url": referral_url, "ownership_type": ownership})

    def record_event(self, person_id: str | None, referral_id: str | None, event_type: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        if person_id and self.store.get_person(person_id) is None:
            raise ValueError("person_id not found")
        if referral_id and self.store.get_referral_link(referral_id) is None:
            raise ValueError("referral_id not found")
        if not event_type.strip():
            raise ValueError("event_type is required")
        return self.store.record_event(person_id, referral_id, event_type, metadata)

    def create_commission(self, data: dict[str, Any]) -> dict[str, Any]:
        amount_paise = int(data.get("amount_paise", -1))
        if amount_paise < 0:
            raise ValueError("amount_paise must be zero or greater")
        if not str(data.get("partner_name", "")).strip():
            raise ValueError("partner_name is required")
        if not str(data.get("order_reference", "")).strip():
            raise ValueError("order_reference is required and must be unique")
        person_id = data.get("person_id")
        referral_id = data.get("referral_id")
        if person_id and self.store.get_person(person_id) is None:
            raise ValueError("person_id not found")
        if referral_id and self.store.get_referral_link(referral_id) is None:
            raise ValueError("referral_id not found")
        return self.store.create_commission({**data, "amount_paise": amount_paise})

    def update_commission_status(self, commission_id: str, status: str) -> dict[str, Any] | None:
        existing = self.store.get_commission(commission_id)
        if existing is None:
            return None
        _, target = self.engine.validate_commission_transition(existing["status"], status)
        return self.store.update_commission_status(commission_id, target)

    def status(self) -> dict[str, object]:
        return {
            "success": True,
            "core": self.NAME,
            "parent": "SUPREME",
            "engine": self.engine.status(),
            "storage": self.store.status(),
            "api": "SEPARATE_LAYER",
            "messaging": "NOT_AUTOMATICALLY_SENT",
            "commission_source_of_truth": "PARTNER_VERIFIED_EVIDENCE_REQUIRED",
        }
