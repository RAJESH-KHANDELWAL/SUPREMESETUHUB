"""GLOBAL ENGINE ECOSYSTEM catalog, discovery, and hierarchy manager.

The ENGINE manager owns its catalog data and discovers ENGINE modules from this
package only. It does not import sibling API, CORE, DATABASE, STORAGE, or SERVER
implementations.
"""
from __future__ import annotations

from copy import deepcopy
import json
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
_MASTER_CATALOG_PATH = Path(__file__).resolve().parents[3] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_TARGET_UNIQUE_ENTRIES = 2468


def get_master_catalog() -> dict[str, Any]:
    """Load the Bharat-to-global master planning catalog from the backend root."""
    if not _MASTER_CATALOG_PATH.is_file():
        raise FileNotFoundError(f"Master ecosystem catalog not found: {_MASTER_CATALOG_PATH}")
    with _MASTER_CATALOG_PATH.open("r", encoding="utf-8") as stream:
        catalog = json.load(stream)
    if catalog.get("catalogue_id") != "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM":
        raise ValueError("Unexpected master ecosystem catalog identity")
    return catalog


def _summarize_master_catalog(catalog: dict[str, Any]) -> dict[str, Any]:
    """Validate catalog structure and return counts derived from its actual entries."""
    if catalog.get("catalogue_id") != "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM":
        raise ValueError("Unexpected master ecosystem catalog identity")

    sections = []
    source_count = 0
    unique_count = 0
    cross_reference_count = 0
    capability_level_count = 0
    seen_ids: set[str] = set()
    seen_section_ids: set[str] = set()
    seen_names: set[str] = set()
    canonical_ids: set[str] = set()
    pending_references: list[tuple[str, str]] = []

    raw_sections = catalog.get("sections")
    if not isinstance(raw_sections, list) or not raw_sections:
        raise ValueError("Master catalog must contain a non-empty sections list")

    for expected_number, section in enumerate(raw_sections, start=1):
        section_id = str(section.get("section_id", "")).strip()
        if not section_id or section_id in seen_section_ids:
            raise ValueError(f"Missing or duplicate section_id: {section_id!r}")
        seen_section_ids.add(section_id)
        if section.get("section_number") != expected_number:
            raise ValueError(f"Section numbering must be contiguous at {section_id}")

        entries = section.get("entries")
        if not isinstance(entries, list):
            raise ValueError(f"Section entries must be a list: {section_id}")

        section_unique = 0
        section_cross_references = 0
        for expected_position, entry in enumerate(entries, start=1):
            if not isinstance(entry, dict):
                raise ValueError(f"Catalog entry must be an object in {section_id}")
            entry_id = str(entry.get("entry_id", "")).strip()
            name = str(entry.get("name", "")).strip()
            kind = str(entry.get("entry_kind", "")).strip()
            if not entry_id or entry_id in seen_ids:
                raise ValueError(f"Missing or duplicate master catalog entry_id: {entry_id!r}")
            if not name or not kind:
                raise ValueError(f"Entry requires name and entry_kind: {entry_id}")
            if entry.get("position") != expected_position:
                raise ValueError(f"Entry positions must be contiguous in {section_id}: {entry_id}")
            seen_ids.add(entry_id)
            source_count += 1

            if kind == "cross_reference":
                canonical_id = str(entry.get("canonical_entry_id", "")).strip()
                if not canonical_id:
                    raise ValueError(f"Cross-reference requires canonical_entry_id: {entry_id}")
                pending_references.append((entry_id, canonical_id))
                section_cross_references += 1
                cross_reference_count += 1
                continue

            normalized_name = " ".join(name.casefold().split())
            if normalized_name in seen_names:
                raise ValueError(f"Duplicate unique catalog entry name: {name!r}")
            seen_names.add(normalized_name)
            canonical_ids.add(entry_id)
            section_unique += 1
            unique_count += 1
            if kind == "capability_level":
                capability_level_count += 1

        sections.append({
            "section_number": section.get("section_number"),
            "section_id": section_id,
            "title": section.get("title"),
            "source_entry_count": len(entries),
            "unique_entry_count": section_unique,
            "cross_reference_count": section_cross_references,
        })

    for entry_id, canonical_id in pending_references:
        if canonical_id not in canonical_ids:
            raise ValueError(
                f"Cross-reference {entry_id} points to missing/non-canonical entry {canonical_id}"
            )

    expansion = catalog.get("expansion", {})
    counts = catalog.get("counts", {})
    target = int(expansion.get("target_unique_entries", 0))
    if target != MASTER_CATALOG_TARGET_UNIQUE_ENTRIES:
        raise ValueError(
            f"Catalog target must be {MASTER_CATALOG_TARGET_UNIQUE_ENTRIES}, got {target}"
        )

    actual_counts = {
        "section_count": len(sections),
        "source_numbered_entries": source_count,
        "unique_catalogue_entries": unique_count,
        "cross_reference_entries": cross_reference_count,
        "capability_levels": capability_level_count,
    }
    for key, actual in actual_counts.items():
        if counts.get(key) != actual:
            raise ValueError(
                f"Catalog counts.{key} mismatch: declared={counts.get(key)!r}, actual={actual}"
            )

    remaining = max(target - unique_count, 0)
    if expansion.get("current_unique_entries") != unique_count:
        raise ValueError(
            "Catalog expansion.current_unique_entries mismatch: "
            f"declared={expansion.get('current_unique_entries')!r}, actual={unique_count}"
        )
    if expansion.get("remaining_unique_entries") != remaining:
        raise ValueError(
            "Catalog expansion.remaining_unique_entries mismatch: "
            f"declared={expansion.get('remaining_unique_entries')!r}, actual={remaining}"
        )
    if unique_count > target:
        raise ValueError(f"Catalog has {unique_count} unique entries; target is exactly {target}")

    return {
        "success": True,
        "catalogue_id": catalog["catalogue_id"],
        "title": catalog.get("title"),
        "section_count": len(sections),
        "source_numbered_entry_count": source_count,
        "unique_entry_count": unique_count,
        "cross_reference_count": cross_reference_count,
        "capability_level_count": capability_level_count,
        "target_unique_entry_count": target,
        "remaining_unique_entries": remaining,
        "target_reached": unique_count == target,
        "expansion_status": "TARGET_REACHED" if unique_count == target else "FOUNDATION_CATALOG_ONLY",
        "sections": sections,
    }


def get_master_catalog_summary() -> dict[str, Any]:
    """Return validated counts; reject stale metadata and duplicate catalog records."""
    return _summarize_master_catalog(get_master_catalog())

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
        from .registry import GlobalEcosystemRegistry

        self.registry = GlobalEcosystemRegistry()
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

    def master_catalog(self) -> dict[str, Any]:
        """Return the complete planning catalog; this does not imply implementation."""
        return get_master_catalog()

    def master_catalog_summary(self) -> dict[str, Any]:
        """Return exact counts from the structured master planning catalog."""
        return get_master_catalog_summary()

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)
        master_summary = get_master_catalog_summary()
        return {
            "success": root is not None,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "version": self.VERSION,
            "status": "OPERATIONAL" if root else "NOT_INITIALIZED",
            "ecosystem_count": self.registry.count(),
            "master_catalog": master_summary,
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
    "EcosystemIdentity",
    "utc_now",
    "ROOT_ID",
    "ROOT",
    "CATEGORIES",
    "PROVIDER_ECOSYSTEMS",
    "get_catalog",
    "get_category_catalog",
    "get_provider_catalog",
    "get_master_catalog",
    "get_master_catalog_summary",
    "GlobalEcosystemManager",
    "EcosystemManager",
]
