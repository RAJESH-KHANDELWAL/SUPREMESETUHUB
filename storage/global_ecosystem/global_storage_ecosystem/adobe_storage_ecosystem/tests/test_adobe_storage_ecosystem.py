"""Offline validation for the Adobe Storage Ecosystem catalog."""
from pathlib import Path
import json

from ..adobe_storage_ecosystem import ADOBE_STORAGE_ECOSYSTEM, list_adobe_storage_ecosystems

PACKAGE = Path(__file__).resolve().parents[1]


def test_catalog_children_have_unique_ids_and_folders():
    children = list_adobe_storage_ecosystems()
    assert children
    assert len({item["id"] for item in children}) == len(children)
    assert len({item["folder"] for item in children}) == len(children)
    for item in children:
        assert item["folder"].startswith("adobe_")
        assert item["folder"].endswith("_storage_ecosystem")
        assert (PACKAGE / item["folder"] / "README.md").is_file()


def test_catalog_does_not_claim_live_connection():
    assert ADOBE_STORAGE_ECOSYSTEM["live_connection_verified"] is False
    assert all(item["status"] == "CATALOG_SCAFFOLD" for item in ADOBE_STORAGE_ECOSYSTEM["children"])


def test_manifest_matches_catalog():
    manifest = json.loads((PACKAGE / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    folders = [item["folder"] for item in list_adobe_storage_ecosystems()]
    assert manifest["child_ecosystems"] == folders
    assert manifest["external_connection_state"] == "NOT_CONFIGURED"
