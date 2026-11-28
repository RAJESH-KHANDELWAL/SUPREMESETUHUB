"""Atlassian storage catalog; no live provider connection is implied."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

PACKAGE_ID = "atlassian_storage_ecosystem"
MANIFEST_PATH = Path(__file__).with_name("ecosystem_manifest.json")
CHILD_ECOSYSTEMS = (
    "atlassian_jira_storage_ecosystem",
    "atlassian_confluence_storage_ecosystem",
    "atlassian_bitbucket_storage_ecosystem",
    "atlassian_trello_storage_ecosystem",
    "atlassian_jira_service_management_storage_ecosystem",
    "atlassian_jira_product_discovery_storage_ecosystem",
    "atlassian_compass_storage_ecosystem",
    "atlassian_bamboo_storage_ecosystem",
)
GEOGRAPHIC_SCOPES = ("BHARAT", "REGIONAL", "GLOBAL")
MATURITY_LEVELS = ("NORMAL", "PROFESSIONAL", "ADVANCED", "ENTERPRISE", "SUPREME")


def load_manifest() -> dict[str, Any]:
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("ecosystem_id") != "ATLASSIAN_STORAGE_ECOSYSTEM":
        raise ValueError("INVALID_ATLASSIAN_STORAGE_MANIFEST")
    actual = [item.get("package") for item in data.get("product_catalog", [])]
    if actual != list(CHILD_ECOSYSTEMS):
        raise ValueError("ATLASSIAN_PRODUCT_CATALOG_MISMATCH")
    return data


def describe() -> dict[str, Any]:
    manifest = load_manifest()
    return {"ecosystem_id": manifest["ecosystem_id"], "provider": "ATLASSIAN",
            "child_count": len(CHILD_ECOSYSTEMS), "child_ecosystems": list(CHILD_ECOSYSTEMS),
            "implementation_state": manifest["implementation_state"],
            "connection_state": manifest["external_connection_state"],
            "external_connections_verified": False, "taxonomy_only": True}


__all__ = ["CHILD_ECOSYSTEMS", "GEOGRAPHIC_SCOPES", "MATURITY_LEVELS", "describe", "load_manifest"]
