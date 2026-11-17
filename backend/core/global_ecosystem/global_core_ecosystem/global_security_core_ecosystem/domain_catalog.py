"""Canonical security-domain catalog with package-manifest integrity checks."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
_DATA = json.loads((_ROOT / "catalog.json").read_text(encoding="utf-8"))

def _load_domains():
    loaded = []
    seen_ids = set()
    seen_folders = set()
    for item in _DATA.get("domains", []):
        domain_id = str(item.get("id", "")).strip().upper()
        folder = str(item.get("folder", "")).strip()
        if not domain_id or not folder:
            raise ValueError("SECURITY_DOMAIN_ID_AND_FOLDER_REQUIRED")
        if domain_id in seen_ids or folder in seen_folders:
            raise ValueError("DUPLICATE_SECURITY_DOMAIN_ID_OR_FOLDER")
        package = (_ROOT / "domains" / folder).resolve()
        if _ROOT not in package.parents:
            raise ValueError("SECURITY_DOMAIN_PACKAGE_PATH_INVALID")
        manifest_path = package / "domain_manifest.json"
        init_path = package / "__init__.py"
        if not package.is_dir() or not manifest_path.is_file() or not init_path.is_file():
            raise ValueError(f"SECURITY_DOMAIN_PACKAGE_INCOMPLETE: {domain_id}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("domain_id") != domain_id:
            raise ValueError(f"SECURITY_DOMAIN_MANIFEST_ID_MISMATCH: {domain_id}")
        if manifest.get("parent_id") != _DATA.get("ecosystem_id"):
            raise ValueError(f"SECURITY_DOMAIN_PARENT_MISMATCH: {domain_id}")
        if manifest.get("status") != "CORE_CATALOG_ONLY":
            raise ValueError(f"SECURITY_DOMAIN_STATUS_INVALID: {domain_id}")
        loaded.append({**item, "status": "CORE_CATALOG_ONLY"})
        seen_ids.add(domain_id)
        seen_folders.add(folder)
    return tuple(loaded)

SECURITY_DOMAINS = _load_domains()

def get_domains():
    """Return a defensive copy of all registered security-domain metadata."""
    return deepcopy(list(SECURITY_DOMAINS))

def get_domain(domain_id: str):
    """Look up one domain by its stable ID."""
    needle = domain_id.strip().upper()
    for item in SECURITY_DOMAINS:
        if item["id"] == needle:
            return deepcopy(item)
    return None

def domain_summary():
    return {"domain_count": len(SECURITY_DOMAINS), "coverage_exhaustive": False}
