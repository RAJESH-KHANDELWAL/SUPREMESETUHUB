"""Public orchestration service for the Global Business Ecosystem."""
from __future__ import annotations

from typing import Any

from backend.businesses.controller import BusinessController
from .intelligence import BusinessAssessment, BusinessIntelligence
from .openai_provider import OpenAIBusinessAIProvider
from .providers import ProviderRegistry
from .recommendations import BusinessActionPlanner


class GlobalBusinessEcosystemService:
    """Composes Business domain intelligence with optional live LLM analysis.

    Persistence and ownership remain in the established Business modules and
    API authorization layer. This service does not create a second database.
    Callers must authorize business ownership before exposing any result.
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
        if providers is None:
            providers = ProviderRegistry()
            providers.register(OpenAIBusinessAIProvider())
        self.providers = providers

    @staticmethod
    def _context(business: Any) -> dict[str, Any]:
        if isinstance(business, dict):
            return dict(business)
        to_dict = getattr(business, "to_dict", None)
        if callable(to_dict):
            result = to_dict()
            if isinstance(result, dict):
                return result
        return {
            key: getattr(business, key)
            for key in OpenAIBusinessAIProvider.SAFE_CONTEXT_FIELDS
            if hasattr(business, key)
        }

    def health(self) -> dict[str, Any]:
        providers = self.provider_capabilities()
        openai = next((item for item in providers if item["provider_id"] == "openai"), None)
        return {
            "component": "GLOBAL_BUSINESS_ECOSYSTEM",
            "status": "READY",
            "business_domain": "backend.businesses",
            "persistence": "EXISTING_BUSINESS_PROFILES_REPOSITORY",
            "intelligence": "DETERMINISTIC_EXPLAINABLE_RULE_ENGINE",
            "external_ai": "CONFIGURED" if openai and openai["enabled"] else "NOT_CONFIGURED",
            "live_ai_verified": bool(openai and openai["live"]),
            "live_market_data": False,
        }

    def assess(self, business_id: str) -> BusinessAssessment:
        business = self.controller.get(business_id)
        if business is None:
            raise LookupError(f"Business not found: {business_id}")
        return self.intelligence.assess(business)

    def action_plan(self, business_id: str) -> dict[str, Any]:
        return self.planner.build(self.assess(business_id))

    def analyze_with_ai(self, business_id: str, task: str, provider_id: str = "openai") -> dict[str, Any]:
        """Run an LLM analysis for an existing business after caller authorization."""
        business = self.controller.get(business_id)
        if business is None:
            raise LookupError(f"Business not found: {business_id}")
        if not isinstance(task, str) or not task.strip():
            raise ValueError("BUSINESS_AI_TASK_REQUIRED")
        result = self.providers.analyze(
            provider_id,
            task=task,
            business_context=self._context(business),
        )
        return {
            "business_id": business_id,
            "analysis_type": "AI_BUSINESS_ANALYSIS",
            **result,
        }

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
