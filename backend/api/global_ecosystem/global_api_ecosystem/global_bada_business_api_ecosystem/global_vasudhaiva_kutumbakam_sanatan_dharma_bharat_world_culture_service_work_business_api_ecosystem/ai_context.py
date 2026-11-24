"""AI context orchestration; inference policy/provider remains in AI layer."""
from __future__ import annotations

from typing import Any


class CultureServiceWorkBusinessAIContext:
    def __init__(self, ai: Any) -> None:
        self.ai = ai

    def build(self, question: str, domain: str | None = None) -> dict[str, Any]:
        normalized = str(question or "").strip()
        if not normalized:
            raise ValueError("AI_QUESTION_REQUIRED")
        return self.ai.build_context(normalized, domain)
