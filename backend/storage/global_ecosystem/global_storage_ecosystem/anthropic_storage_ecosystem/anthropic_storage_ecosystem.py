"""Anthropic Storage Ecosystem catalog; taxonomy only, no live API claim."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

PACKAGE_ID = "anthropic_storage_ecosystem"
MANIFEST_PATH = Path(__file__).with_name("ecosystem_manifest.json")
CHILD_ECOSYSTEMS = (
    "anthropic_claude_storage_ecosystem",
    "anthropic_claude_projects_storage_ecosystem",
    "anthropic_claude_artifacts_storage_ecosystem",
    "anthropic_claude_files_storage_ecosystem",
    "anthropic_claude_knowledge_storage_ecosystem",
    "anthropic_claude_connectors_storage_ecosystem",
    "anthropic_claude_enterprise_storage_ecosystem",
    "anthropic_claude_code_storage_ecosystem",
)
GEOGRAPHIC_SCOPES = ("BHARAT", "REGIONAL", "GLOBAL")
MATURITY_LEVELS = ("NORMAL", "PROFESSIONAL", "ADVANCED", "ENTERPRISE", "SUPREME")


def load_manifest() -> dict[str, Any]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("ecosystem_id") != "ANTHROPIC_STORAGE_ECOSYSTEM":
        raise ValueError("INVALID_ANTHROPIC_STORAGE_MANIFEST")
    if tuple(data.get("child_storage_ecosystems", ())) != CHILD_ECOSYSTEMS:
        raise ValueError("ANTHROPIC_CHILD_CATALOG_MISMATCH")
    return data


def describe() -> dict[str, Any]:
    manifest = load_manifest()
    return {
        "ecosystem_id": manifest["ecosystem_id"],
        "child_count": len(CHILD_ECOSYSTEMS),
        "child_ecosystems": list(CHILD_ECOSYSTEMS),
        "implementation_state": manifest["implementation_state"],
        "connection_state": manifest["external_connection_state"],
        "external_connections_verified": False,
        "taxonomy_only": True,
    }


__all__ = ["CHILD_ECOSYSTEMS", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS", "describe", "load_manifest"]
