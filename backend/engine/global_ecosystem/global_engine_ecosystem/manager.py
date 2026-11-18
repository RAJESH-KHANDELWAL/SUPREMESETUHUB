"""GLOBAL ENGINE ECOSYSTEM catalog, discovery, and hierarchy manager.

The ENGINE manager owns its catalog data and discovers ENGINE modules from this
package only. It does not import sibling API, CORE, DATABASE, STORAGE, or SERVER
implementations.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any



def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class EcosystemIdentity:
    ecosystem_id: str
    name: str
    ecosystem_type: str = "GENERAL"
    repository_ref: str | None = None
    status: str = "REGISTERED"
    enabled: bool = True
    capabilities: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    message: str | None = None
    parent_id: str | None = None
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "ecosystem_id": self.ecosystem_id, "name": self.name,
            "ecosystem_type": self.ecosystem_type, "repository_ref": self.repository_ref,
            "status": self.status, "enabled": self.enabled,
            "capabilities": list(self.capabilities), "metadata": dict(self.metadata),
            "message": self.message, "parent_id": self.parent_id,
            "created_at": self.created_at, "updated_at": self.updated_at,
        }


ROOT_ID = "GLOBAL-ENGINE-ECOSYSTEM"
ROOT: dict[str, Any] = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL ENGINE ECOSYSTEM",
    "ecosystem_type": "ENGINE_LAYER",
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": ["EXECUTION", "PROCESSING", "ORCHESTRATION"],
    "parent_id": None,
    "metadata": {"owner_layer": "ENGINE"},
}

_PACKAGE_ROOT = Path(__file__).resolve().parent


def _discover() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Discover provider groups and executable engine modules owned by ENGINE."""
    categories: list[dict[str, Any]] = []
    providers: list[dict[str, Any]] = []
    for directory in sorted(_PACKAGE_ROOT.iterdir(), key=lambda item: item.name):
        if not directory.is_dir() or directory.name.startswith("_"):
            continue
        if not directory.name.endswith("_engine_ecosystem"):
            continue
        category_id = directory.name.removesuffix("_engine_ecosystem").upper().replace("_", "-")
        modules = sorted(directory.rglob("engine.py"))
        categories.append({
            "ecosystem_id": f"{category_id}-ENGINE-ECOSYSTEM",
            "name": directory.name.replace("_", " ").upper(),
            "ecosystem_type": "ENGINE_CATEGORY",
            "parent_id": ROOT_ID,
            "module_count": len(modules),
            "status": "DISCOVERED" if modules else "CATALOG_ONLY",
            "capabilities": ["ENGINE_MODULE_DISCOVERY"],
        })
        for module in modules:
            relative = module.parent.relative_to(_PACKAGE_ROOT).as_posix()
            module_id = relative.upper().replace("/", "-").replace("_", "-")
            providers.append({
                "ecosystem_id": module_id,
                "name": relative.replace("/", " ").replace("_", " ").upper(),
                "ecosystem_type": "ENGINE_MODULE",
                "parent_id": f"{category_id}-ENGINE-ECOSYSTEM",
                "module": f"{__package__}." + relative.replace("/", "."),
                "entrypoint": "engine.py",
                "status": "DISCOVERED",
                "capabilities": ["ENGINE_EXECUTION_MODULE"],
            })
    return categories, providers


def get_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the ENGINE root and discovered modules."""
    categories, providers = _discover()
    return [deepcopy(ROOT), *deepcopy(categories), *deepcopy(providers)]


def get_category_catalog() -> list[dict[str, Any]]:
    """Return the discovered ENGINE category catalog."""
    categories, _ = _discover()
    return deepcopy(categories)


def get_provider_catalog() -> list[dict[str, Any]]:
    """Return discovered executable ENGINE modules (not external providers)."""
    _, providers = _discover()
    return deepcopy(providers)


CATEGORIES, PROVIDER_ECOSYSTEMS = _discover()


class GlobalEcosystemManager:
    """Manage the independent GLOBAL ENGINE ECOSYSTEM registry."""

    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL ENGINE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        self.name, self.version = self.ROOT_NAME, self.VERSION
        from .registry import GlobalEcosystemRegistry\n\n        self.registry = GlobalEcosystemRegistry()
        # Module counts belong to the ENGINE manager, not the shared identity model.
        self.module_counts: dict[str, int] = {}
        self.module_references: dict[str, str] = {}
        self.module_entrypoints: dict[str, str] = {}
        for record in get_catalog():
            item = dict(record)
            module_count = item.pop("module_count", None)
            module_reference = item.pop("module", None)
            module_entrypoint = item.pop("entrypoint", None)
            ecosystem_id = item["ecosystem_id"]
            if module_count is not None:
                self.module_counts[ecosystem_id] = int(module_count)
            if module_reference is not None:
                self.module_references[ecosystem_id] = str(module_reference)
            if module_entrypoint is not None:
                self.module_entrypoints[ecosystem_id] = str(module_entrypoint)
            self.registry.register(EcosystemIdentity(**item))

    def register(self, ecosystem: dict[str, Any] | EcosystemIdentity) -> dict[str, Any]:
        module_count = None
        module_reference = None
        module_entrypoint = None
        if isinstance(ecosystem, dict):
            ecosystem = dict(ecosystem)
            module_count = ecosystem.pop("module_count", None)
            module_reference = ecosystem.pop("module", None)
            module_entrypoint = ecosystem.pop("entrypoint", None)
        identity = ecosystem if isinstance(ecosystem, EcosystemIdentity) else EcosystemIdentity(
            ecosystem_id=str(ecosystem.get("ecosystem_id", "")).strip(),
            name=str(ecosystem.get("name", "")).strip(),
            ecosystem_type=str(ecosystem.get("ecosystem_type", "GENERAL")).strip(),
            repository_ref=ecosystem.get("repository_ref"),
            status=str(ecosystem.get("status", "REGISTERED")),
            enabled=bool(ecosystem.get("enabled", True)),
            capabilities=list(ecosystem.get("capabilities", [])),
            metadata=dict(ecosystem.get("metadata", {})),
            message=ecosystem.get("message"),
            parent_id=ecosystem.get("parent_id") or self.ROOT_ID,
        )
        if self.registry.exists(identity.ecosystem_id):
            return {
                "success": False,
                "error": "ECOSYSTEM_ALREADY_EXISTS",
                "ecosystem_id": identity.ecosystem_id,
            }
        try:
            registered = self.registry.register(identity)
            if module_count is not None:
                self.module_counts[identity.ecosystem_id] = int(module_count)
            if module_reference is not None:
                self.module_references[identity.ecosystem_id] = str(module_reference)
            if module_entrypoint is not None:
                self.module_entrypoints[identity.ecosystem_id] = str(module_entrypoint)
            return {"success": True, "ecosystem": registered}
        except (ValueError, KeyError) as exc:
            return {"success": False, "error": "REGISTRATION_FAILED", "message": str(exc)}

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)
        return {
            "success": root is not None,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "version": self.VERSION,
            "status": "OPERATIONAL" if root else "NOT_INITIALIZED",
            "ecosystem_count": self.registry.count(),
            "category_module_counts": dict(self.module_counts),
            "total_engine_modules": sum(self.module_counts.values()),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    def health(self) -> dict[str, Any]:
        ready = self.registry.exists(self.ROOT_ID)
        return {
            "success": ready,
            "service": self.ROOT_NAME,
            "status": "HEALTHY" if ready else "DEGRADED",
            "registry_available": self.registry is not None,
            "ecosystem_count": self.registry.count(),
            "category_module_counts": dict(self.module_counts),
            "total_engine_modules": sum(self.module_counts.values()),
        }

    def list(self) -> dict[str, Any]:
        items = self.registry.list()
        return {"success": True, "count": len(items), "ecosystems": items}

    def names(self) -> dict[str, Any]:
        items = self.registry.names()
        return {"success": True, "count": len(items), "names": items}

    def get(self, ecosystem_id: str):
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self.registry.exists(ecosystem_id)

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()
        nodes = {record["ecosystem_id"]: {**record, "children": []} for record in records}
        for record in records:
            parent = record.get("parent_id")
            if parent in nodes:
                nodes[parent]["children"].append(nodes[record["ecosystem_id"]])
        root = nodes.get(self.ROOT_ID)
        return {"success": root is not None, "tree": root}

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()
        edges = [
            {
                "source": record["parent_id"],
                "target": record["ecosystem_id"],
                "relationship": "CONTAINS",
            }
            for record in records
            if record.get("parent_id")
        ]
        return {"success": True, "node_count": len(records), "edge_count": len(edges), "edges": edges}


EcosystemManager = GlobalEcosystemManager

__all__ = [
    "EcosystemIdentity",\n    "utc_now",\n    "ROOT_ID",\n    "ROOT",
    "CATEGORIES",
    "PROVIDER_ECOSYSTEMS",
    "get_catalog",
    "get_category_catalog",
    "get_provider_catalog",
    "GlobalEcosystemManager",
    "EcosystemManager",
]
