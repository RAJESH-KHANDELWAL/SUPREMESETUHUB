"""Storage boundary for GLOBAL CORE ECOSYSTEM referral workflows.

Business rules stay in CORE/ENGINE; persistence is delegated to the DATABASE layer
through the established central DatabaseService.
"""
from __future__ import annotations

from typing import Any

from backend.database.referral_repository import ReferralRepository


class ReferralStore:
    NAME = "GLOBAL_CORE_REFERRAL_STORAGE"

    def __init__(self, repository: ReferralRepository | None = None) -> None:
        self.repository = repository or ReferralRepository()

    def create_person(self, data: dict[str, Any]) -> dict[str, Any]:
        return self.repository.create_person(data)

    def get_person(self, person_id: str) -> dict[str, Any] | None:
        return self.repository.get_person(person_id)

    def list_people(self, response_stage: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        return self.repository.list_people(response_stage, limit)

    def update_person_stage(self, person_id: str, stage: str, next_follow_up_at: str | None = None) -> dict[str, Any] | None:
        return self.repository.update_person_stage(person_id, stage, next_follow_up_at)

    def create_referral_link(self, data: dict[str, Any]) -> dict[str, Any]:
        return self.repository.create_referral_link(data)

    def get_referral_link(self, referral_id: str) -> dict[str, Any] | None:
        return self.repository.get_referral_link(referral_id)

    def list_referral_links(self, platform: str | None = None, active_only: bool = False) -> list[dict[str, Any]]:
        return self.repository.list_referral_links(platform, active_only)

    def record_event(self, person_id: str | None, referral_id: str | None, event_type: str, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.repository.record_event(person_id, referral_id, event_type, metadata)

    def list_events(self, person_id: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        return self.repository.list_events(person_id, limit)

    def create_commission(self, data: dict[str, Any]) -> dict[str, Any]:
        return self.repository.create_commission(data)

    def get_commission(self, commission_id: str) -> dict[str, Any] | None:
        return self.repository.get_commission(commission_id)

    def update_commission_status(self, commission_id: str, status: str) -> dict[str, Any] | None:
        return self.repository.update_commission_status(commission_id, status)

    def summary_counts(self) -> dict[str, int]:
        return self.repository.summary_counts()

    def list_commissions(self, status: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        return self.repository.list_commissions(status, limit)

    def status(self) -> dict[str, object]:
        result = self.repository.initialize()
        return {"success": True, "storage": self.NAME, "status": "READY", **result}
