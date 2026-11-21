"""Central manager for GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM.

Coordinates taxonomy, relationship metadata contracts, evidence policy, and
read-only discovery. It does not persist records or verify external claims.
"""
from __future__ import annotations

from typing import Any

from .catalog import ROOT_ID, ROOT, get_catalog, list_categories, RELATIONSHIP_TYPES
from .registry import EntityRelationshipRegistry
from .policy import RelationshipPolicy, RelationshipPolicyError

NAME = "GLOBAL ENTITY RELATIONSHIPS CORE ECOSYSTEM"
MASTER_CATALOG_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_ID = "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468
MASTER_CATALOG_CURRENT_UNIQUE_ENTRIES = 246
MASTER_CATALOG_REMAINING_UNIQUE_ENTRIES = 2222


class GlobalEntityRelationshipsCoreManager:
    """Stable read-only entry point for entity-relationship taxonomy metadata."""

    NAME = NAME
    ECOSYSTEM_ID = ROOT_ID

    def __init__(self) -> None:
        self._registry = EntityRelationshipRegistry(get_catalog())

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": ROOT_ID,
            "name": NAME,
            "provider": "global_entity_relationships",
            "status": "CORE_CATALOG_ONLY",
            "root": dict(ROOT),
            "category_count": len(list_categories()),
            "registry_record_count": self._registry.count(),
            "relationship_type_count": len(RELATIONSHIP_TYPES),
            "live_connection_verified": False,
            "api_calls_performed": 0,
            "persistence_enabled": False,
            "master_catalog_reference": self.master_catalog_reference(),
            "architecture": {
                "catalog": "catalog.py",
                "registry": "registry.py",
                "policy": "policy.py",
                "contracts": "models.py",
                "manager": "manager.py",
                "service": "service.py",
                "orchestrator": "orchestrator.py",
            },
        }

    def health(self) -> dict[str, Any]:
        records = self._registry.list()
        unique_ids = len({item["ecosystem_id"] for item in records})
        return {
            "success": unique_ids == len(records) and ROOT_ID in {item["ecosystem_id"] for item in records},
            "ecosystem_id": ROOT_ID,
            "status": "CORE_CATALOG_AVAILABLE",
            "registry_record_count": len(records),
            "category_count": len(list_categories()),
            "relationship_type_count": len(RELATIONSHIP_TYPES),
            "duplicate_ids": len(records) - unique_ids,
            "live_connections_verified": 0,
            "api_calls_performed": 0,
            "persistence_enabled": False,
            "warning": "Taxonomy and policy availability do not verify live relationships, ownership, affiliation, consent, licensing, or external connectivity.",
        }

    def list_categories(self) -> dict[str, Any]:
        categories = self._registry.list()[1:]
        return {"success": True, "count": len(categories), "categories": categories}

    def list_category_inventory(self) -> list[dict[str, Any]]:
        return self._registry.list()[1:]

    def get_category(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self._registry.get(ecosystem_id)

    def relationship_types(self) -> dict[str, Any]:
        return {"success": True, "count": len(RELATIONSHIP_TYPES), "types": list(RELATIONSHIP_TYPES)}

    def get_relationship_type(self, relationship_type: str) -> dict[str, Any] | None:
        key = str(relationship_type).strip().casefold()
        return next(({"name": value} for value in RELATIONSHIP_TYPES if value.casefold() == key), None)

    def tree(self) -> dict[str, Any]:
        records = self._registry.list()
        nodes = {item["ecosystem_id"]: {**item, "children": []} for item in records}
        for item in records:
            parent = item.get("parent_id")
            if parent in nodes:
                nodes[parent]["children"].append(nodes[item["ecosystem_id"]])
        return {"success": ROOT_ID in nodes, "tree": nodes.get(ROOT_ID)}

    def dependency_map(self) -> dict[str, Any]:
        return {
            "success": True,
            "edges": [
                {"component": component, "relationship": "USES_READ_ONLY_METADATA"}
                for component in ("catalog.py", "registry.py", "policy.py", "models.py")
            ],
            "external_api_dependencies": [],
            "persistence_dependencies": [],
        }

    def validate_relationship(self, record: dict[str, Any]) -> dict[str, Any]:
        try:
            RelationshipPolicy.validate(record)
        except RelationshipPolicyError as exc:
            return {"success": False, "valid": False, "error": str(exc)}
        return {"success": True, "valid": True, "live_relationship_verified": False}

    def master_catalog_reference(self) -> dict[str, Any]:
        return {
            "catalog_id": MASTER_CATALOG_ID,
            "target_unique_entries": MASTER_CATALOG_TARGET_UNIQUE_ENTRIES,
            "current_unique_entries": MASTER_CATALOG_CURRENT_UNIQUE_ENTRIES,
            "remaining_unique_entries": MASTER_CATALOG_REMAINING_UNIQUE_ENTRIES,
            "source_path": MASTER_CATALOG_PATH,
            "owner_layer": "GLOBAL_ENGINE_ECOSYSTEM",
            "access_mode": "READ_ONLY_REFERENCE",
            "catalog_loaded": False,
            "catalog_copied": False,
            "catalog_mutated": False,
            "note": "The 2468 master catalog is referenced as a planning taxonomy only. Entries are not copied, fabricated, or mutated by this CORE ecosystem.",
        }


_manager: GlobalEntityRelationshipsCoreManager | None = None


def get_manager() -> GlobalEntityRelationshipsCoreManager:
    """Return the canonical manager instance."""
    global _manager
    if _manager is None:
        _manager = GlobalEntityRelationshipsCoreManager()
    return _manager


__all__ = ["GlobalEntityRelationshipsCoreManager", "get_manager"]
