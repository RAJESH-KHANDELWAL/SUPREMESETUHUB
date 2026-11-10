"""Executable ENGINE entrypoint registered by the global engine catalog."""
from __future__ import annotations
from typing import Any
from .manager import GlobalCulturalEngine

class CulturalKnowledgeEngine:
    def __init__(self, manager: GlobalCulturalEngine | None = None) -> None:
        self.manager = manager or GlobalCulturalEngine()

    def execute(self, operation: str, payload: dict[str, Any]) -> dict[str, Any]:
        if operation == "SEARCH":
            return self.manager.search(str(payload.get("query", "")), payload.get("domain"))
        if operation == "STATUS":
            return self.manager.status()
        raise ValueError(f"UNSUPPORTED_CULTURAL_ENGINE_OPERATION:{operation}")

def create_engine() -> CulturalKnowledgeEngine:
    return CulturalKnowledgeEngine()
