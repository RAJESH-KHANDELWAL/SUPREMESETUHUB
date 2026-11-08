"""Application service for intelligence on existing Business records."""
from __future__ import annotations

from typing import Any

from backend.businesses.controller import BusinessController
from backend.businesses.intelligence import BusinessAssessment, BusinessIntelligence
from backend.businesses.model import Business
from backend.businesses.recommendations import BusinessActionPlanner


BIG_BUSINESS_TYPES = {"LARGE_BUSINESS", "ENTERPRISE"}


class BigBusinessIntelligenceService:
    """Runs deterministic intelligence over canonical, repository-backed records.

    Authentication and owner checks belong to the API layer. This service does
    not create a second repository and does not execute external AI providers.
    """

    def __init__(
        self,
        controller: BusinessController | None = None,
        intelligence: BusinessIntelligence | None = None,
        planner: BusinessActionPlanner | None = None,
    ) -> None:
        self.controller = controller or BusinessController()
        self.intelligence = intelligence or BusinessIntelligence()
        self.planner = planner or BusinessActionPlanner()

    @staticmethod
    def _require_big_business(business: Business) -> None:
        if str(business.business_type or "").strip().upper() not in BIG_BUSINESS_TYPES:
            raise LookupError(f"Big Business not found: {business.business_id}")

    def health(self) -> dict[str, Any]:
        return {
            "component": "BIG_BUSINESSES_INTELLIGENCE",
            "status": "READY",
            "business_domain": "backend.businesses",
            "persistence": "EXISTING_BUSINESS_PROFILES_REPOSITORY",
            "intelligence": "DETERMINISTIC_EXPLAINABLE_RULE_ENGINE",
            "external_ai_execution": "DELEGATED_TO_GLOBAL_AI_ECOSYSTEM",
            "live_market_data": False,
        }

    def assess(self, business_id: str) -> BusinessAssessment:
        business = self.controller.get(business_id)
        if business is None:
            raise LookupError(f"Business not found: {business_id}")
        self._require_big_business(business)
        return self.intelligence.assess(business)

    def action_plan(self, business_id: str) -> dict[str, Any]:
        return self.planner.build(self.assess(business_id))

    def compare(self, business_ids: list[str]) -> list[dict[str, Any]]:
        if not business_ids:
            raise ValueError("business_ids must contain at least one id")
        if len(set(business_ids)) != len(business_ids):
            raise ValueError("business_ids must not contain duplicates")
        profiles = []
        for business_id in business_ids:
            business = self.controller.get(business_id)
            if business is None:
                raise LookupError(f"Business not found: {business_id}")
            self._require_big_business(business)
            profiles.append(business)
        return self.intelligence.compare(profiles)
