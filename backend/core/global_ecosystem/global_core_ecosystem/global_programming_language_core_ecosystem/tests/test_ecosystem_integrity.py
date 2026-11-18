"""Repository-level integrity checks for the Global Programming Language CORE ecosystem."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PATH = (
    "backend/core/global_ecosystem/global_core_ecosystem/"
    "global_programming_language_core_ecosystem"
)
EXPECTED_SHARED_SUPPORT = {
    "compatibility",
    "configuration",
    "contracts",
    "documentation",
    "events",
    "exceptions",
    "orchestration",
    "security",
    "testing",
    "utilities",
    "validation",
}


def _json(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_manifest_identity_and_canonical_location():
    manifest = _json("ecosystem_manifest.json")
    assert manifest["ecosystem_id"] == "GLOBAL-PROGRAMMING-LANGUAGE-CORE-ECOSYSTEM"
    assert manifest["parent_id"] == "GLOBAL-CORE-ECOSYSTEM"
    assert manifest["layer"] == "CORE"
    assert manifest["status"] == "CORE_CATALOG_ONLY"
    assert manifest["canonical_path"] == EXPECTED_PATH
    assert manifest["division"]["id"] == "PROGRAMMING"
    assert manifest["division"]["folder"] == ROOT.name


def test_manifest_catalog_and_domain_directories_are_consistent():
    manifest = _json("ecosystem_manifest.json")
    catalog = _json("catalog.json")
    domains = catalog["domains"]
    ids = [item["id"] for item in domains]
    folders = [item["folder"] for item in domains]

    assert catalog["division"] == "PROGRAMMING"
    assert manifest["domain_count"] == len(domains)
    assert len(ids) == len(set(ids))
    assert len(folders) == len(set(folders))

    for item in domains:
        folder = item["folder"]
        assert item["id"].strip()
        assert item["name"].strip()
        assert item["scope"].strip()
        assert folder == Path(folder).name
        assert folder == folder.lower()
        assert "/" not in folder and "\\" not in folder
        assert folder.endswith("_core_ecosystem")
        assert (ROOT / folder).is_dir()


def test_language_catalog_count_matches_manifest_and_is_metadata_only():
    from backend.core.global_ecosystem.global_core_ecosystem.global_programming_language_core_ecosystem.language_catalog import (
        LANGUAGE_RECORDS,
    )

    manifest = _json("ecosystem_manifest.json")
    assert manifest["language_record_count"] == len(LANGUAGE_RECORDS)
    assert manifest["language_coverage_exhaustive"] is False
    assert all(record.get("support_status") == "METADATA_ONLY" for record in LANGUAGE_RECORDS)


def test_shared_support_areas_exist_and_match_manifest():
    manifest = _json("ecosystem_manifest.json")
    shared_root = ROOT / "shared_support"
    actual = {path.name for path in shared_root.iterdir() if path.is_dir()}
    expected = set(manifest["shared_support_areas"])
    assert actual == EXPECTED_SHARED_SUPPORT
    assert expected == EXPECTED_SHARED_SUPPORT


def test_core_runtime_and_external_integration_boundaries_remain_closed():
    manifest = _json("ecosystem_manifest.json")
    security = manifest["security"]
    assert manifest["api_calls_performed"] == 0
    assert manifest["runtime_execution_verified"] is False
    assert manifest["compiler_execution_verified"] is False
    assert manifest["credential_storage"] == "EXTERNAL_SECRET_STORE_ONLY"
    assert security["untrusted_code_execution_in_core"] is False
    assert security["sandbox_required_for_execution"] is True
    assert set(manifest["layer_boundaries"]) == {
        "core", "api", "storage", "database", "runtime", "application"
    }
