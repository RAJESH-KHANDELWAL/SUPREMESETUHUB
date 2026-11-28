"""Dependency contracts shared by API, CORE and ENGINE layers."""
from __future__ import annotations

from typing import Any, Protocol


class CulturalKnowledgeSearch(Protocol):
    """Minimal CORE capability required by the cultural knowledge ENGINE."""

    def search(self, query: str) -> list[dict[str, Any]]:
        """Return foundational cultural knowledge matches."""
        ...
