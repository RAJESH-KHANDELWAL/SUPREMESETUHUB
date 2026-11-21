"""Read-only service facade for GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM."""
from __future__ import annotations

from typing import Any

from .manager import get_manager


class EntityRelationshipCoreService:
    """Application-facing facade; no persistence or external API calls."""

    def status(self) -> dict[str, Any]:
        return get_manager().status()

    def health(self) -> dict[str, Any]:
        return get_manager().health()

    def list_categories(self) -> dict[str, Any]:
        return get_manager().list_categories()

    def list_category_inventory(self) -> list[dict[str, Any]]:
        return get_manager().list_category_inventory()

    def get_category(self, ecosystem_id: str) -> dict[str, Any] | None:
        return get_manager().get_category(ecosystem_id)

    def relationship_types(self) -> dict[str, Any]:
        return get_manager().relationship_types()

    def get_relationship_type(self, relationship_type: str) -> dict[str, Any] | None:
        return get_manager().get_relationship_type(relationship_type)

    def tree(self) -> dict[str, Any]:
        return get_manager().tree()

    def dependency_map(self) -> dict[str, Any]:
        return get_manager().dependency_map()

    def validate_relationship(self, record: dict[str, Any]) -> dict[str, Any]:
        return get_manager().validate_relationship(record)

    def master_catalog_reference(self) -> dict[str, Any]:
        return get_manager().master_catalog_reference()
