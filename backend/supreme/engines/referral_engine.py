"""Business rules for SUPREME people, referral, follow-up and commission workflows.

This engine does not send messages, claim conversions, or infer a person's mindset.
It validates explicit user/customer states and enforces safe commission transitions.
"""
from __future__ import annotations

from urllib.parse import urlparse


class ReferralEngine:
    NAME = "SUPREME_REFERRAL_ENGINE"

    PERSON_STAGES = {
        "NEW",
        "INFORMATION_REQUESTED",
        "READY_NOW",
        "FOLLOW_UP",
        "LONG_TERM",
        "CONVERTED",
        "NOT_INTERESTED",
        "DO_NOT_CONTACT",
    }
    COMMISSION_STAGES = {"PENDING", "APPROVED", "PAID", "REJECTED", "REVERSED"}
    _COMMISSION_TRANSITIONS = {
        "PENDING": {"APPROVED", "REJECTED"},
        "APPROVED": {"PAID", "REVERSED"},
        "PAID": {"REVERSED"},
        "REJECTED": set(),
        "REVERSED": set(),
    }

    @staticmethod
    def normalize_stage(stage: str) -> str:
        normalized = " ".join(stage.strip().upper().replace("-", " ").split())
        return normalized.replace(" ", "_")

    def validate_person(self, display_name: str, source_platform: str, need_category: str) -> None:
        if not display_name.strip():
            raise ValueError("display_name is required")
        if not source_platform.strip():
            raise ValueError("source_platform is required")
        if not need_category.strip():
            raise ValueError("need_category is required")

    def validate_referral_url(self, referral_url: str) -> None:
        parsed = urlparse(referral_url.strip())
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("referral_url must be an absolute HTTPS URL")

    def validate_person_stage(self, stage: str) -> str:
        normalized = self.normalize_stage(stage)
        if normalized not in self.PERSON_STAGES:
            raise ValueError(f"Unsupported person stage: {normalized}")
        return normalized

    def validate_commission_transition(self, current: str, target: str) -> tuple[str, str]:
        current_stage = self.normalize_stage(current)
        target_stage = self.normalize_stage(target)
        if current_stage not in self.COMMISSION_STAGES:
            raise ValueError(f"Unsupported current commission stage: {current_stage}")
        if target_stage not in self.COMMISSION_STAGES:
            raise ValueError(f"Unsupported target commission stage: {target_stage}")
        if target_stage not in self._COMMISSION_TRANSITIONS[current_stage]:
            raise ValueError(f"Commission transition {current_stage} -> {target_stage} is not allowed")
        return current_stage, target_stage

    def status(self) -> dict[str, object]:
        return {
            "success": True,
            "engine": self.NAME,
            "person_stages": sorted(self.PERSON_STAGES),
            "commission_stages": sorted(self.COMMISSION_STAGES),
            "messaging": "NOT_SENT_BY_ENGINE",
        }
