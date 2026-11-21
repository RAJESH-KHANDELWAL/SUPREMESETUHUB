"""Validated read-only access to the canonical server CORE domain registry."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parent
_REGISTRY_PATH = _ROOT / "domain_registry.json"


def load_domain_registry() -> dict[str, Any]:
    data = json.loads(_REGISTRY_PATH.read_text(encoding="utf-8"))
    domains = data.get("domains", [])
    if data.get("domain_count") != len(domains):
        raise ValueError("SERVER_DOMAIN_COUNT_MISMATCH")
    ids = [row.get("domain_id") for row in domains]
    directories = [row.get("directory") for row in domains]
    if len(ids) != len(set(ids)):
        raise ValueError("SERVER_DOMAIN_ID_DUPLICATE")
    if len(directories) != len(set(directories)):
        raise ValueError("SERVER_DOMAIN_DIRECTORY_DUPLICATE")
    for row in domains:
        name = row.get("directory", "")
        if not name.startswith("server_") or not name.endswith("_core_ecosystem"):
            raise ValueError(f"SERVER_DOMAIN_DIRECTORY_INVALID: {name}")
        directory = _ROOT / name
        if not directory.is_dir():
            raise FileNotFoundError(f"SERVER_DOMAIN_DIRECTORY_MISSING: {name}")
        manifest = directory / "domain_manifest.json"
        if not manifest.is_file():
            raise FileNotFoundError(f"SERVER_DOMAIN_MANIFEST_MISSING: {name}")
    return data


def get_domain(domain_id: str) -> dict[str, Any] | None:
    key = str(domain_id).strip().upper()
    return next(
        (row for row in load_domain_registry()["domains"] if row["domain_id"] == key),
        None,
    )


__all__ = ["load_domain_registry", "get_domain"]
