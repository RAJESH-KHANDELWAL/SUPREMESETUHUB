"""Evidence-aware AI context builder for cultural knowledge.

This module prepares grounded context; it does not claim to call an LLM provider.
The platform AI engine can consume the returned context through its own adapter.
"""
from __future__ import annotations
from typing import Any
from backend.engine.global_ecosystem.global_engine_ecosystem.cultural_knowledge_engine_ecosystem.manager import CulturalKnowledgeEngineManager

class CulturalKnowledgeAssistant:
    def __init__(self, engine: CulturalKnowledgeEngineManager | None = None) -> None:
        self.engine = engine or CulturalKnowledgeEngineManager()

    def build_context(self, question: str, domain: str | None = None) -> dict[str, Any]:
        result = self.engine.search(question, domain=domain)
        return {
            "knowledge_domain": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE",
            "user_question": question,
            "retrieved_evidence": result,
            "answering_rules": [
                "Separate primary texts from later interpretation.",
                "Do not invent authors, dates, places, quotations or citations.",
                "State uncertainty and identify evidence gaps.",
                "Respect cultural context, community consent and intellectual property.",
            ],
            "provider_invocation": "NOT_PERFORMED",
        }
