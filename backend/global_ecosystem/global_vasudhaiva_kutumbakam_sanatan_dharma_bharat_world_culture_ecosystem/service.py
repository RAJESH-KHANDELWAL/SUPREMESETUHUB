"""Read-only service boundary for the cultural knowledge domain package."""
from __future__ import annotations

from typing import Any

from . import get_complete_knowledge, search_knowledge


class CulturalKnowledgeDomainService:
    def knowledge(self) -> dict[str, Any]:
        return get_complete_knowledge()

    def search(self, query: str) -> list[dict[str, Any]]:
        return search_knowledge(query)


__all__ = ["CulturalKnowledgeDomainService"]
