"""Canonical security-domain catalog with root-level package integrity checks."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_DATA = json.loads((_ROOT / "catalog.json").read_text(encoding="utf-8"))

def _load_domains():
    loaded, seen_ids, seen_folders = [], set(), set()
    for item in _DATA.get("domains", []):
        domain_id = str(item.get("id", "")).strip().upper()
        folder = str(item.get("folder", "")).strip()
        if not domain_id or not folder:
            raise ValueError("SECURITY_DOMAIN_ID_AND_FOLDER_REQUIRED")
        if domain_id in seen_ids or folder in seen_folders:
            raise ValueError("DUPLICATE_SECURITY_DOMAIN_ID_OR_FOLDER")
        if not folder.endswith("_core_ecosystem"):
            raise ValueError(f"SECURITY_DOMAIN_CORE_ECOSYSTEM_SUFFIX_REQUIRED: {domain_id}")
        package = (_ROOT / folder).resolve()
        if package.parent != _ROOT:
            raise ValueError("SECURITY_DOMAIN_PACKAGE_MUST_BE_DIRECT_CHILD_OF_ECOSYSTEM_ROOT")
        manifest_path, init_path = package / "domain_manifest.json", package / "__init__.py"
        if not package.is_dir() or not manifest_path.is_file() or not init_path.is_file():
            raise ValueError(f"SECURITY_DOMAIN_PACKAGE_INCOMPLETE: {domain_id}")
        package_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if package_manifest.get("domain_id") != domain_id:
            raise ValueError(f"SECURITY_DOMAIN_MANIFEST_ID_MISMATCH: {domain_id}")
        if package_manifest.get("parent_id") != _DATA.get("ecosystem_id"):
            raise ValueError(f"SECURITY_DOMAIN_PARENT_MISMATCH: {domain_id}")
        if package_manifest.get("status") != "CORE_CATALOG_ONLY":
            raise ValueError(f"SECURITY_DOMAIN_STATUS_INVALID: {domain_id}")
        loaded.append({**item, "status": "CORE_CATALOG_ONLY"})
        seen_ids.add(domain_id); seen_folders.add(folder)
    return tuple(loaded)

SECURITY_DOMAINS = _load_domains()
def get_domains():
    return deepcopy(list(SECURITY_DOMAINS))
def get_domain(domain_id: str):
    needle = domain_id.strip().upper()
    for item in SECURITY_DOMAINS:
        if item["id"] == needle:
            return deepcopy(item)
    return None
def domain_summary():
    return {"domain_count": len(SECURITY_DOMAINS), "coverage_exhaustive": False}
