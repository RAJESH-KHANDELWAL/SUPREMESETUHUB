"""Service facade for the Global Business Ecosystem."""
from __future__ import annotations
from typing import Any
from .catalog import get_catalog
from .registry import get_business_ecosystem, list_business_ecosystems, search_business_ecosystems
from .adapters.bada_business import get_bada_business_connection

class GlobalBusinessEcosystemService:
    """Read-only business namespace discovery and connected-resource summary."""
    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def list_ecosystems(self, *, category: str | None = None) -> tuple[dict, ...]:
        return list_business_ecosystems(category=category)

    def get_ecosystem(self, ecosystem_id: str) -> dict | None:
        return get_business_ecosystem(ecosystem_id)

    def search(self, query: str) -> tuple[dict, ...]:
        return search_business_ecosystems(query)

    def bada_business_connection(self) -> dict[str, Any]:
        return get_bada_business_connection()

__all__ = ["GlobalBusinessEcosystemService"]
