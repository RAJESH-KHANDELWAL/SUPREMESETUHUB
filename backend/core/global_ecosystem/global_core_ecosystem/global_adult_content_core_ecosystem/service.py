"""Public read-only service facade."""

from __future__ import annotations

from .catalog import get_catalog
from .policy import evaluate_content_metadata
from .taxonomy import get_orientation


class GlobalAdultContentCoreService:
    def describe(self) -> dict:
        return get_catalog()

    def orientation(self, value: str) -> dict | None:
        return get_orientation(value)

    def evaluate_policy(self, evidence):
        return evaluate_content_metadata(evidence)

    def readiness(self) -> dict:
        return {
            "status": "CORE_CATALOG_ONLY",
            "taxonomy_available": True,
            "live_age_assurance_verified": False,
            "consent_verification_verified": False,
            "moderation_execution_enabled": False,
            "media_execution_enabled": False,
        }
