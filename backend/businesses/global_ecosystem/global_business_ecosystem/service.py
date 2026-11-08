"""Public orchestration service for the Global Business Ecosystem."""
from __future__ import annotations

from typing import Any

from backend.businesses.controller import BusinessController
from .intelligence import BusinessAssessment, BusinessIntelligence
from .providers import ProviderRegistry
from .recommendations import BusinessActionPlanner


class GlobalBusinessEcosystemService:
    """Composes the existing Business domain with explainable AI-style tooling.

    Persistence and ownership remain in the established Business modules and
    API authorization layer. This service does not create a second database.
    """

    def __init__(
        self,
        controller: BusinessController | None = None,
        intelligence: BusinessIntelligence | None = None,
        planner: BusinessActionPlanner | None = None,
        providers: ProviderRegistry | None = None,
    ) -> None:
        self.controller = controller or BusinessController()
        self.intelligence = intelligence or BusinessIntelligence()
        self.planner = planner or BusinessActionPlanner()
        self.providers = providers or ProviderRegistry()

    def health(self) -> dict[str, Any]:
        return {
            "component": "GLOBAL_BUSINESS_ECOSYSTEM",
            "status": "READY",
            "business_domain": "backend.businesses",
            "persistence": "EXISTING_BUSINESS_PROFILES_REPOSITORY",
            "intelligence": "DETERMINISTIC_EXPLAINABLE_RULE_ENGINE",
            "external_ai": "NOT_CONFIGURED",
            "live_market_data": False,
        }

    def assess(self, business_id: str) -> BusinessAssessment:
        business = self.controller.get(business_id)
        if business is None:
            raise LookupError(f"Business not found: {business_id}")
        return self.intelligence.assess(business)

    def action_plan(self, business_id: str) -> dict[str, Any]:
        return self.planner.build(self.assess(business_id))

    def compare(self, business_ids: list[str]) -> list[dict[str, Any]]:
        if len(set(business_ids)) != len(business_ids):
            raise ValueError("business_ids must not contain duplicates")
        profiles = []
        for business_id in business_ids:
            business = self.controller.get(business_id)
            if business is None:
                raise LookupError(f"Business not found: {business_id}")
            profiles.append(business)
        return self.intelligence.compare(profiles)

    def provider_capabilities(self) -> list[dict[str, Any]]:
        return self.providers.capabilities()
