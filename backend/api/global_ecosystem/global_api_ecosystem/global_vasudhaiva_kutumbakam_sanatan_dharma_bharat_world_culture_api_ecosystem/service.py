"""Application service joining cultural API use-cases to CORE, ENGINE and AI."""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem.service import GlobalCulturalCore
from backend.engine.global_ecosystem.global_engine_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_engine_ecosystem.manager import GlobalCulturalEngine
from backend.ai.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ai_ecosystem.assistant import GlobalCulturalAI

class GlobalCulturalAPIService:
    def __init__(self) -> None:
        self.core = GlobalCulturalCore()
        self.engine = GlobalCulturalEngine(self.core)
        self.ai = GlobalCulturalAI(self.engine)

    def status(self) -> dict[str, Any]:
        return {"ecosystem": self.core.describe(), "engine": self.engine.status(),
                "ai": self.ai.status(), "api": "READY",
                "database": "AVAILABLE_ON_DEMAND", "storage": "LOCAL_ADAPTER",
                "cloud": "ADAPTER_REQUIRED"}

    def knowledge(self) -> dict[str, Any]:
        return self.core.knowledge()

    def domains(self) -> list[dict[str, Any]]:
        return self.core.domains()

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        return self.engine.search(query, domain)

    def ai_context(self, query: str, domain: str | None = None) -> dict[str, Any]:
        return self.ai.build_context(query, domain)
