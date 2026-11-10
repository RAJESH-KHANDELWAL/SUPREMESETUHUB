"""Retrieval-grounded AI context builder; provider invocation is deliberately external."""
from __future__ import annotations
from typing import Any
from .policy import CULTURAL_ANSWER_POLICY

class GlobalCulturalAI:
    def __init__(self, engine: Any) -> None:
        self.engine = engine

    def status(self) -> dict[str, Any]:
        return {"component": "GLOBAL_CULTURAL_AI", "status": "CONTEXT_BUILDER_READY",
                "llm_provider_invoked": False, "provider": "NOT_CONFIGURED"}

    def build_context(self, question: str, domain: str | None = None) -> dict[str, Any]:
        question = str(question or "").strip()
        if not question:
            raise ValueError("CULTURAL_AI_QUESTION_REQUIRED")
        retrieval = self.engine.search(question, domain)
        return {"ecosystem": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_SANATAN_DHARMA_BHARAT_WORLD_CULTURE",
                "question": question, "domain": domain, "retrieval": retrieval,
                "answer_policy": list(CULTURAL_ANSWER_POLICY),
                "provider_invocation": "NOT_PERFORMED",
                "instruction": "Use retrieved evidence only for supported claims; state when evidence is absent."}
