"""Discovery and health orchestration for relationship CORE metadata."""
from __future__ import annotations
from typing import Any
from .manager import get_manager

class GlobalEntityRelationshipsCoreOrchestrator:
    """Coordinate metadata discovery without persistence or external requests."""
    def catalog(self) -> dict[str, Any]: return get_manager().tree()
    def categories(self) -> dict[str, Any]: return get_manager().list_categories()
    def relationship_types(self) -> dict[str, Any]: return get_manager().relationship_types()
    def health(self) -> dict[str, Any]: return get_manager().health()
    def dependency_map(self) -> dict[str, Any]: return get_manager().dependency_map()
